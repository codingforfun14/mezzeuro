// Converts text into SVG path data using CoreText (no third-party tools).
//
//   ctpaths --list [filter]                       list installed PostScript font names
//   ctpaths --axes <font.ttf>                     list a variable font's axes
//   ctpaths <font> <size> <text> [tracking]       JSON: metrics + one entry per glyph
//
// <font> is an installed PostScript name, or a font file with optional variation settings:
//   path/to/Font.ttf@wght=500,opsz=96
//
// Each glyph's "d" is in glyph-local coordinates: origin on the baseline, y pointing down (SVG).
// "x" is the glyph origin along the line (kerning and tracking applied).
import CoreGraphics
import CoreText
import Foundation

func fmt(_ v: CGFloat) -> String {
    var s = String(format: "%.2f", Double(v))
    while s.contains(".") && (s.hasSuffix("0") || s.hasSuffix(".")) { s.removeLast() }
    return s == "-0" ? "0" : s
}

func svgPath(_ path: CGPath) -> String {
    var d = ""
    path.applyWithBlock { ptr in
        let el = ptr.pointee
        let p = el.points
        func pt(_ i: Int) -> String { "\(fmt(p[i].x)) \(fmt(-p[i].y))" }
        switch el.type {
        case .moveToPoint: d += "M\(pt(0))"
        case .addLineToPoint: d += "L\(pt(0))"
        case .addQuadCurveToPoint: d += "Q\(pt(0)) \(pt(1))"
        case .addCurveToPoint: d += "C\(pt(0)) \(pt(1)) \(pt(2))"
        case .closeSubpath: d += "Z"
        @unknown default: break
        }
    }
    return d
}

func fileDescriptor(_ path: String) -> CTFontDescriptor? {
    let descs = CTFontManagerCreateFontDescriptorsFromURL(URL(fileURLWithPath: path) as CFURL) as? [CTFontDescriptor]
    return descs?.first
}

/// Installed PostScript name, or "file.ttf@tag=value,tag=value" for a (variable) font file.
func makeFont(_ spec: String, _ size: CGFloat) -> CTFont? {
    let parts = spec.split(separator: "@", maxSplits: 1).map(String.init)
    let base = parts[0]
    if base.lowercased().hasSuffix(".ttf") || base.lowercased().hasSuffix(".otf") {
        guard var desc = fileDescriptor(base) else { return nil }
        if parts.count > 1 {
            var axes: [NSNumber: NSNumber] = [:]
            for kv in parts[1].split(separator: ",") {
                let p = kv.split(separator: "=").map(String.init)
                guard p.count == 2, p[0].utf8.count == 4, let v = Double(p[1]) else { return nil }
                let tag = p[0].utf8.reduce(UInt32(0)) { ($0 << 8) | UInt32($1) }
                axes[NSNumber(value: tag)] = NSNumber(value: v)
            }
            desc = CTFontDescriptorCreateCopyWithAttributes(
                desc, [kCTFontVariationAttribute as String: axes] as CFDictionary)
        }
        return CTFontCreateWithFontDescriptor(desc, size, nil)
    }
    let f = CTFontCreateWithName(spec as CFString, size, nil)
    return (CTFontCopyPostScriptName(f) as String) == spec ? f : nil
}

let args = CommandLine.arguments
if args.count >= 2 && args[1] == "--list" {
    let names = (CTFontManagerCopyAvailablePostScriptNames() as? [String]) ?? []
    let filter = args.count >= 3 ? args[2].lowercased() : ""
    for n in names.sorted() where filter.isEmpty || n.lowercased().contains(filter) { print(n) }
    exit(0)
}
if args.count >= 3 && args[1] == "--axes" {
    guard let d = fileDescriptor(args[2]) else { print("cannot read \(args[2])"); exit(3) }
    let f = CTFontCreateWithFontDescriptor(d, 12, nil)
    for axis in (CTFontCopyVariationAxes(f) as? [[String: Any]]) ?? [] {
        let name = axis[kCTFontVariationAxisNameKey as String] ?? "?"
        let lo = axis[kCTFontVariationAxisMinimumValueKey as String] ?? "?"
        let hi = axis[kCTFontVariationAxisMaximumValueKey as String] ?? "?"
        let def = axis[kCTFontVariationAxisDefaultValueKey as String] ?? "?"
        print("\(name): \(lo)…\(hi) (default \(def))")
    }
    exit(0)
}
guard args.count >= 4, let sizeArg = Double(args[2]) else {
    FileHandle.standardError.write("usage: ctpaths <psname> <size> <text> [tracking] | --list [filter]\n".data(using: .utf8)!)
    exit(2)
}
let name = args[1]
let size = CGFloat(sizeArg)
let text = args[3]
let tracking = args.count >= 5 ? CGFloat(Double(args[4]) ?? 0) : 0

guard let font = makeFont(name, size) else {
    FileHandle.standardError.write("ctpaths: cannot load font \(name)\n".data(using: .utf8)!)
    exit(3)
}
let actual = CTFontCopyPostScriptName(font) as String
var attrs: [NSAttributedString.Key: Any] = [NSAttributedString.Key(kCTFontAttributeName as String): font]
if tracking != 0 { attrs[NSAttributedString.Key(kCTKernAttributeName as String)] = tracking }
let line = CTLineCreateWithAttributedString(NSAttributedString(string: text, attributes: attrs))
let ns = text as NSString

var glyphsOut: [[String: Any]] = []
for run in (CTLineGetGlyphRuns(line) as? [CTRun]) ?? [] {
    let n = CTRunGetGlyphCount(run)
    var glyphs = [CGGlyph](repeating: 0, count: n)
    var pos = [CGPoint](repeating: .zero, count: n)
    var adv = [CGSize](repeating: .zero, count: n)
    var idx = [CFIndex](repeating: 0, count: n)
    let all = CFRange(location: 0, length: 0)
    CTRunGetGlyphs(run, all, &glyphs)
    CTRunGetPositions(run, all, &pos)
    CTRunGetAdvances(run, all, &adv)
    CTRunGetStringIndices(run, all, &idx)
    let runAttrs = CTRunGetAttributes(run) as NSDictionary
    let runFont = runAttrs[kCTFontAttributeName as String] as! CTFont
    for i in 0..<n {
        var d = ""
        var bbox: [Double] = [0, 0, 0, 0]
        if let p = CTFontCreatePathForGlyph(runFont, glyphs[i], nil) {
            d = svgPath(p)
            let b = p.boundingBoxOfPath
            bbox = [Double(b.minX), Double(-b.maxY), Double(b.maxX), Double(-b.minY)]
        }
        glyphsOut.append([
            "ch": ns.substring(with: NSRange(location: idx[i], length: 1)),
            "x": Double(pos[i].x), "adv": Double(adv[i].width), "d": d, "bbox": bbox,
        ])
    }
}
let result: [String: Any] = [
    "font": actual, "size": Double(size),
    "ascent": Double(CTFontGetAscent(font)), "descent": Double(CTFontGetDescent(font)),
    "capHeight": Double(CTFontGetCapHeight(font)), "xHeight": Double(CTFontGetXHeight(font)),
    "width": Double(CTLineGetTypographicBounds(line, nil, nil, nil)), "glyphs": glyphsOut,
]
FileHandle.standardOutput.write(try! JSONSerialization.data(withJSONObject: result))
