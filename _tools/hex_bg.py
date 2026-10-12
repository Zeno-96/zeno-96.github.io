"""Generates img/hex-bg.svg, the metal hex background.

Run from the repo root:  python _tools/hex_bg.py [seed]
Change the seed to reshuffle which tiles are raised or shadowed.
"""
import math,random,sys
r=110; NC,NR=5,4; seed=int(sys.argv[1]) if len(sys.argv)>1 else 7
W=math.sqrt(3)*r; TW=NC*W; TH=NR*1.5*r; gap=r*0.075
random.seed(seed)
shade={(i,j):random.choice([-.5,-.3,0,0,.25,.4,.55,.7]) for i in range(NC) for j in range(NR)}
def hp(rad):
    pts=[(rad*math.cos(math.radians(60*k-90)), rad*math.sin(math.radians(60*k-90))) for k in range(6)]
    return "M"+"L".join(f"{x:.1f} {y:.1f}" for x,y in pts)+"Z"
cells=[]
for j in range(-1,NR+1):
    for i in range(-1,NC+1):
        cx=i*W+(j%2)*W/2; cy=j*1.5*r
        cells.append((cx,cy,shade[(i%NC,j%NR)]))
u=lambda ref,cx,cy,extra='': f'<use href="#{ref}" x="{cx:.1f}" y="{cy:.1f}"{extra}/>'
outl="".join(u('o',cx,cy) for cx,cy,_ in cells)
metal="".join(u('t',cx,cy) for cx,cy,_ in cells)
shad="".join(u('f',cx,cy,f' fill-opacity="{s}"') for cx,cy,s in cells if s>0)
lift="".join(u('t',cx,cy,f' fill-opacity="{-s}"') for cx,cy,s in cells if s<0)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{TW:.1f}" height="{TH:.1f}" viewBox="0 0 {TW:.1f} {TH:.1f}">
<defs>
<path id="o" d="{hp(r)}"/><path id="t" d="{hp(r-gap)}"/><path id="f" d="{hp(r*1.02)}"/>
<radialGradient id="m" cx=".5" cy=".42" r=".62"><stop offset="0" stop-color="#04070c"/><stop offset=".55" stop-color="#070d18"/><stop offset=".8" stop-color="#0c1828"/><stop offset=".93" stop-color="#14304c" stop-opacity=".85"/><stop offset="1" stop-color="#1d4a70" stop-opacity=".55"/></radialGradient>
<radialGradient id="s" cx=".5" cy=".5" r=".5"><stop offset=".5" stop-color="#01030a"/><stop offset="1" stop-color="#01030a" stop-opacity=".35"/></radialGradient><radialGradient id="l" cx=".5" cy=".3" r=".7"><stop offset="0" stop-color="#1e3556"/><stop offset=".8" stop-color="#132640" stop-opacity=".6"/><stop offset="1" stop-color="#1d4a70" stop-opacity="0"/></radialGradient>
<linearGradient id="b" x1=".2" y1="0" x2=".8" y2="1"><stop offset="0" stop-color="#7aa8d0" stop-opacity=".7"/><stop offset=".5" stop-color="#1d3350" stop-opacity=".3"/><stop offset="1" stop-color="#02050a" stop-opacity=".8"/></linearGradient>
<filter id="g1" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="{r*.12:.1f}"/></filter>
<filter id="g2" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="{r*.03:.1f}"/></filter>
</defs>
<rect width="100%" height="100%" fill="#050a14"/>
<g fill="none" stroke="#4f46e5" stroke-opacity=".5" stroke-width="{r*.3:.1f}" filter="url(#g1)">{outl}</g>
<g fill="none" stroke="#0ea5c6" stroke-opacity=".85" stroke-width="{r*.11:.1f}" filter="url(#g2)">{outl}</g>
<g fill="none" stroke="#38bdf8" stroke-width="{r*.025:.1f}">{outl}</g>
<g fill="url(#m)">{metal}</g>
<g fill="url(#l)">{lift}</g>
<g fill="none" stroke="url(#b)" stroke-width="{r*.035:.1f}">{metal}</g>
<g fill="url(#s)">{shad}</g>
</svg>'''
open('img/hex-bg.svg','w').write(svg); print(f'wrote img/hex-bg.svg ({len(svg)} bytes)')
