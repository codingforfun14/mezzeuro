from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import sys
INK='#1A1A1A'; CARTA='#FAF6E8'; ORO='#D4A017'
f=TTFont('/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf')
gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm
asc=f['OS/2'].sCapHeight
def run(text, x0, y0, size, track=-0.05):
    """returns list of (char, path_d, advance) ; baseline at y0, cap height top"""
    s=size/upm; x=x0; out=[]
    for ch in text:
        gn=cmap[ord(ch)]; g=gs[gn]
        pen=SVGPathPen(gs)
        tp=TransformPen(pen,(s,0,0,-s,x,y0))
        g.draw(tp)
        out.append((ch,pen.getCommands()))
        x+=g.width*s+track*size
    return out, x-track*size
def wordmark(colors, size=200, pad=0):
    cap=asc*size/upm
    parts,w=run('MEZZ€URO',pad,pad+cap,size)
    paths=[]
    for i,(ch,d) in enumerate(parts):
        c=colors['euro'] if ch=='€' else colors['letters']
        paths.append(f'<path d="{d}" fill="{c}"/>')
    return paths, w+pad, cap+2*pad
def svg(w,h,body,bg=None):
    b=f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" width="{w:.0f}" height="{h:.0f}">{b}{"".join(body)}</svg>'
out='/mnt/project-files/brandkit/logo/'
variants={
 'mezzeuro-logo-orizzontale':({'letters':INK,'euro':ORO},None),
 'mezzeuro-logo-negativo':({'letters':CARTA,'euro':ORO},INK),
 'mezzeuro-logo-mono-inchiostro':({'letters':INK,'euro':INK},None),
 'mezzeuro-logo-mono-carta':({'letters':CARTA,'euro':CARTA},INK),
}
for name,(cols,bg) in variants.items():
    pad=60 if bg else 0
    p,w,h=wordmark(cols,200,pad)
    open(out+name+'.svg','w').write(svg(w,h,p,bg))
# stacked
size=200; cap=asc*size/upm; gap=cap*0.32
a,w1=run('MEZZ',0,cap,size); b,w2=run('€URO',0,cap*2+gap,size)
body=[f'<path d="{d}" fill="{ORO if ch=="€" else INK}"/>' for ch,d in a+b]
open(out+'mezzeuro-logo-verticale.svg','w').write(svg(max(w1,w2),cap*2+gap,body))
# monogram M€ (avatar A)
S=1080
size=520; cap=asc*size/upm
parts,w=run('M€',0,0,size,-0.03)
x0=(S-w)/2; y0=(S+cap)/2
parts,w=run('M€',x0,y0,size,-0.03)
body=[f'<circle cx="{S/2}" cy="{S/2}" r="{S/2}" fill="{INK}"/>']+[f'<path d="{d}" fill="{ORO if ch=="€" else CARTA}"/>' for ch,d in parts]
open(out+'mezzeuro-avatar-monogramma.svg','w').write(svg(S,S,body))
# mezza moneta (avatar B / favicon)
def moneta(S, bg, ring, half, glyph, glyph_on_half):
    R=S*0.40; cx=cy=S/2
    size=S*0.50; cap=asc*size/upm
    from fontTools.pens.boundsPen import BoundsPen
    bp=BoundsPen(gs); gs[cmap[ord('€')]].draw(bp); xmin,ymin,xmax,ymax=bp.bounds
    sc=size/upm
    gx=cx-((xmin+xmax)/2)*sc; gy=cy+((ymin+ymax)/2)*sc
    parts,w=run('€',gx,gy,size)
    d=parts[0][1]
    body=[]
    if bg: body.append(f'<circle cx="{cx}" cy="{cy}" r="{S/2}" fill="{bg}"/>')
    body.append(f'<defs><clipPath id="L"><rect x="0" y="0" width="{cx}" height="{S}"/></clipPath><clipPath id="R"><rect x="{cx}" y="0" width="{cx}" height="{S}"/></clipPath></defs>')
    body.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{half}" clip-path="url(#L)"/>')
    body.append(f'<circle cx="{cx}" cy="{cy}" r="{R-S*0.012}" fill="none" stroke="{ring}" stroke-width="{S*0.024}"/>')
    body.append(f'<path d="{d}" fill="{glyph_on_half}" clip-path="url(#L)"/>')
    body.append(f'<path d="{d}" fill="{glyph}" clip-path="url(#R)"/>')
    return svg(S,S,body)
open(out+'mezzeuro-avatar-moneta.svg','w').write(moneta(1080,INK,ORO,ORO,ORO,INK))
open(out+'mezzeuro-simbolo-moneta.svg','w').write(moneta(1080,None,INK,ORO,INK,INK))
def fav(S):
    from fontTools.pens.boundsPen import BoundsPen
    bp=BoundsPen(gs); gs[cmap[ord('€')]].draw(bp); xmin,ymin,xmax,ymax=bp.bounds
    size=S*0.62; sc=size/upm
    parts,w=run('€',S/2-((xmin+xmax)/2)*sc,S/2+((ymin+ymax)/2)*sc,size)
    return svg(S,S,[f'<circle cx="{S/2}" cy="{S/2}" r="{S/2}" fill="{INK}"/>',f'<path d="{parts[0][1]}" fill="{ORO}"/>'])
open(out+'mezzeuro-favicon.svg','w').write(fav(64))
print('ok')
