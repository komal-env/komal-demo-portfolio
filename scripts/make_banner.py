"""
Komal — self-hosted animated header banner (pink/lavender theme).
Structure adapted from the referral repo's banner: terminal-style greeting,
cycling role text, quote box, tech pills, about-me lines, stats row, and a
character illustration on the right, all as one hand-authored SVG with SMIL
animation (no external render service).
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
OUT = os.path.join(HERE, "..", "komal-banner.svg")

with open(os.path.join(ASSETS, "character.webp"), "rb") as f:
    CHAR_B64 = base64.b64encode(f.read()).decode()

W, H = 1280, 740

TECH_PILLS_ROW1 = [
    ("Python", "rgba(55,118,171,.14)", "#3776ab", "#1e4f78"),
    ("Java", "rgba(176,114,25,.14)", "#b07219", "#7a4f11"),
    ("C", "rgba(85,85,85,.12)", "#6e6e6e", "#3f3f3f"),
    ("NumPy", "rgba(77,171,247,.12)", "#4dabf7", "#1971c2"),
]
TECH_PILLS_ROW2 = [
    ("Pandas", "rgba(139,92,246,.14)", "#7c3aed", "#6639ba"),
    ("Scikit-Learn", "rgba(255,126,182,.10)", "#db2777", "#be3980"),
    ("Machine Learning", "rgba(192,38,211,.10)", "#c026d3", "#9333ea"),
]

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Komal Priya - Aspiring AI Engineer">
<title>Komal Priya — Aspiring AI Engineer</title>
<defs>
<style type="text/css"><![CDATA[
text{{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes popIn{{0%{{opacity:0;transform:translateY(14px) scale(.7)}}70%{{opacity:1;transform:translateY(-3px) scale(1.06)}}100%{{opacity:1;transform:translateY(0) scale(1)}}}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes floaty{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-9px)}}}}
@keyframes floaty2{{0%,100%{{transform:translateY(0) rotate(0deg)}}50%{{transform:translateY(-12px) rotate(6deg)}}}}
@keyframes heartBeat{{0%,100%{{transform:scale(1)}}12%{{transform:scale(1.25)}}24%{{transform:scale(1)}}36%{{transform:scale(1.18)}}48%{{transform:scale(1)}}}}
@keyframes neonFlicker{{0%{{opacity:0}}5%{{opacity:.7}}7%{{opacity:.1}}10%{{opacity:.9}}12%{{opacity:.3}}16%,100%{{opacity:1}}}}
@keyframes neonPulse{{0%,100%{{opacity:.55}}50%{{opacity:1}}}}
@keyframes twinkle{{0%,100%{{opacity:0;transform:scale(.4)}}50%{{opacity:1;transform:scale(1)}}}}
@keyframes rise{{0%{{transform:translateY(0);opacity:0}}12%{{opacity:.55}}88%{{opacity:.55}}100%{{transform:translateY(-46px);opacity:0}}}}
.ltr{{opacity:0;animation:popIn .5s cubic-bezier(.2,.8,.3,1.3) forwards;transform-box:fill-box;transform-origin:center bottom}}
.ii,.pill,.soc,.st,.cl{{opacity:0}}
.pill{{transition:transform .2s ease,filter .2s ease;transform-box:fill-box;transform-origin:center;cursor:pointer}}
.pill:hover{{transform:scale(1.08);filter:brightness(1.35)}}
.cur{{animation:blink 1s step-end infinite}}
.tw{{transform-box:fill-box;transform-origin:center;animation:twinkle 2.6s ease-in-out infinite}}
.hb{{transform-box:fill-box;transform-origin:center;animation:heartBeat 2.2s ease-in-out infinite}}
.fl{{animation:floaty 5s ease-in-out infinite}}
.fl2{{transform-box:fill-box;transform-origin:center;animation:floaty2 4.2s ease-in-out infinite}}
.neon-on{{animation:neonFlicker 2.4s ease 3.2s backwards}}
.np{{animation:neonPulse 2.6s ease-in-out infinite}}
.rp{{animation:rise linear infinite}}
.sep{{stroke:#eadef8;stroke-width:1;opacity:.7}}
.nm{{font-family:'Segoe Script','Brush Script MT',cursive;opacity:0;animation:popIn .6s cubic-bezier(.2,.8,.3,1.3) forwards}}
]]></style>

<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#ffffff"/><stop offset="55%" stop-color="#fdf8ff"/><stop offset="100%" stop-color="#fff6fc"/>
</linearGradient>
<linearGradient id="nameg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#db2777;#9333ea;#7c3aed;#db2777" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="55%"><animate attributeName="stop-color" values="#c026d3;#a78bfa;#db2777;#c026d3" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#7c3aed;#db2777;#9333ea;#7c3aed" dur="7s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="borderg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#db2777" stop-opacity=".55"/>
  <stop offset="50%" stop-color="#9333ea" stop-opacity=".5"/>
  <stop offset="100%" stop-color="#7c3aed" stop-opacity=".55"/>
</linearGradient>
<radialGradient id="orbP"><stop offset="0%" stop-color="#db2777" stop-opacity=".09"/><stop offset="100%" stop-color="#db2777" stop-opacity="0"/></radialGradient>
<radialGradient id="orbV"><stop offset="0%" stop-color="#7c3aed" stop-opacity=".10"/><stop offset="100%" stop-color="#7c3aed" stop-opacity="0"/></radialGradient>
<radialGradient id="orbB"><stop offset="0%" stop-color="#0284c7" stop-opacity=".07"/><stop offset="100%" stop-color="#0284c7" stop-opacity="0"/></radialGradient>
<radialGradient id="girlGlow"><stop offset="0%" stop-color="#9333ea" stop-opacity=".10"/><stop offset="100%" stop-color="#9333ea" stop-opacity="0"/></radialGradient>
<filter id="glow"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glowBig"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="dots" width="30" height="30" patternUnits="userSpaceOnUse"><circle cx="15" cy="15" r=".6" fill="rgba(147,51,234,.08)"/></pattern>

<clipPath id="cPrompt"><rect x="48" y="48" width="0" height="32"><animate attributeName="width" from="0" to="480" dur="1s" begin=".3s" fill="freeze"/></rect></clipPath>
<clipPath id="cHi"><rect x="48" y="86" width="0" height="42"><animate attributeName="width" from="0" to="200" dur=".5s" begin="1.2s" fill="freeze"/></rect></clipPath>
<clipPath id="q1"><rect x="76" y="258" width="0" height="46"><animate attributeName="width" from="0" to="300" dur=".7s" begin="3.4s" fill="freeze"/></rect></clipPath>
<clipPath id="q2"><rect x="76" y="284" width="0" height="46"><animate attributeName="width" from="0" to="300" dur=".6s" begin="4.2s" fill="freeze"/></rect></clipPath>
<clipPath id="r1"><rect x="48" y="200" width="0" height="36"><animate attributeName="width" values="0;0;340;340;0;0" keyTimes="0;.01;.07;.2;.24;1" dur="24s" repeatCount="indefinite" begin="1.9s"/></rect></clipPath>
<clipPath id="r2"><rect x="48" y="200" width="0" height="36"><animate attributeName="width" values="0;0;340;340;0;0" keyTimes="0;.26;.32;.45;.49;1" dur="24s" repeatCount="indefinite" begin="1.9s"/></rect></clipPath>
<clipPath id="r3"><rect x="48" y="200" width="0" height="36"><animate attributeName="width" values="0;0;340;340;0;0" keyTimes="0;.51;.57;.7;.74;1" dur="24s" repeatCount="indefinite" begin="1.9s"/></rect></clipPath>
<clipPath id="r4"><rect x="48" y="200" width="0" height="36"><animate attributeName="width" values="0;0;340;340;0;0" keyTimes="0;.76;.82;.95;.99;1" dur="24s" repeatCount="indefinite" begin="1.9s"/></rect></clipPath>
<linearGradient id="scanEdge" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#db2777" stop-opacity="0"/><stop offset="18%" stop-color="#db2777"/>
  <stop offset="50%" stop-color="#c026d3"/><stop offset="82%" stop-color="#9333ea"/>
  <stop offset="100%" stop-color="#9333ea" stop-opacity="0"/>
</linearGradient>
<linearGradient id="scanTrail" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#db2777" stop-opacity="0"/><stop offset="100%" stop-color="#db2777" stop-opacity=".13"/>
</linearGradient>
<clipPath id="girlReveal"><rect x="722" y="152" width="558" height="0">
  <animate attributeName="height" from="0" to="522" dur="1.8s" begin=".5s" fill="freeze"/>
</rect></clipPath>
<clipPath id="girlBox"><rect x="722" y="152" width="558" height="522"/></clipPath>
<clipPath id="bannerBox"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="22"/></clipPath>
</defs>

<!-- ================= BACKGROUND ================= -->
<rect width="{W}" height="{H}" rx="22" fill="url(#bg)"/>
<rect width="{W}" height="{H}" rx="22" fill="url(#dots)"/>
<circle cx="230" cy="220" r="260" fill="url(#orbP)"><animate attributeName="r" values="260;290;260" dur="6s" repeatCount="indefinite"/></circle>
<circle cx="1000" cy="520" r="300" fill="url(#orbV)"><animate attributeName="r" values="300;330;300" dur="7s" repeatCount="indefinite"/></circle>
<circle cx="700" cy="120" r="200" fill="url(#orbB)"><animate attributeName="r" values="200;225;200" dur="5.5s" repeatCount="indefinite"/></circle>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="22" fill="none" stroke="url(#borderg)" stroke-width="1.5"/>

<!-- rising particles -->
<circle class="rp" cx="140" cy="620" r="1.4" fill="#db2777" style="animation-duration:5s"/>
<circle class="rp" cx="420" cy="700" r="1.1" fill="#9333ea" style="animation-duration:6s;animation-delay:1s"/>
<circle class="rp" cx="620" cy="660" r="1.3" fill="#7c3aed" style="animation-duration:4.6s;animation-delay:2s"/>
<circle class="rp" cx="1180" cy="690" r="1.2" fill="#db2777" style="animation-duration:5.4s;animation-delay:.6s"/>
<circle class="rp" cx="1240" cy="360" r="1" fill="#9333ea" style="animation-duration:6.4s;animation-delay:1.6s"/>
<circle class="rp" cx="70" cy="420" r="1" fill="#c026d3" style="animation-duration:5.8s;animation-delay:2.4s"/>

<!-- sparkles -->
<g class="tw" style="animation-delay:.4s"><path d="M470 120l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="#d946ef"/></g>
<g class="tw" style="animation-delay:1.5s"><path d="M880 120l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#db2777"/></g>
<g class="tw" style="animation-delay:2.6s"><path d="M1245 250l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#9333ea"/></g>

<!-- ================= LEFT: CONTENT ================= -->
<text clip-path="url(#cPrompt)" x="48" y="69" font-size="14"><tspan fill="#1a7f37" font-weight="bold">komal@ai-engineer</tspan><tspan fill="#6e7781">:~$ </tspan><tspan fill="#1f2328">cat </tspan><tspan fill="#c026d3">README.md</tspan></text>
<rect x="454" y="56" width="8" height="16" fill="#1a7f37" opacity="0"><animate attributeName="opacity" values="1;0" dur="1s" repeatCount="indefinite" begin="1.35s"/></rect>

<text clip-path="url(#cHi)" x="48" y="114" font-size="24" font-weight="bold" fill="#1f2328">Hi, I'm 👋</text>

<!-- Name (styled cursive text, animated gradient + pop-in) -->
<text class="nm" x="46" y="180" font-size="58" font-weight="700" fill="url(#nameg)" filter="url(#glow)" style="animation-delay:1.5s">Komal Priya</text>
<g class="hb" style="animation-delay:3s"><path d="M470 150 c-5-11-21-9-21 4 0 9 12 16 21 22 9-6 21-13 21-22 0-13-16-15-21-4z" fill="#db2777" opacity=".95"/></g>

<!-- Cycling roles -->
<text clip-path="url(#r1)" x="48" y="225" font-size="17" fill="#c026d3" filter="url(#glow)">&lt; Aspiring AI Engineer /&gt;</text>
<text clip-path="url(#r2)" x="48" y="225" font-size="17" fill="#c026d3" filter="url(#glow)">&lt; Machine Learning Enthusiast /&gt;</text>
<text clip-path="url(#r3)" x="48" y="225" font-size="17" fill="#c026d3" filter="url(#glow)">&lt; Python • DSA Learner /&gt;</text>
<text clip-path="url(#r4)" x="48" y="225" font-size="17" fill="#c026d3" filter="url(#glow)">&lt; GenAI Explorer /&gt;</text>
<rect x="48" y="212" width="2.5" height="16" fill="#c026d3" opacity="0"><animate attributeName="opacity" values="1;0" dur=".8s" repeatCount="indefinite" begin="1.9s"/></rect>

<!-- Quote box -->
<g class="cl" style="animation:fadeIn .5s ease 3.2s forwards">
  <rect x="48" y="262" width="380" height="72" rx="8" fill="#faf5ff" stroke="#e6d5f7" stroke-width="1"/>
  <rect x="48" y="266" width="3.5" height="64" rx="1.5" fill="#db2777"/>
</g>
<text clip-path="url(#q1)" x="76" y="292" font-size="15" fill="#1f2328">I don't just study AI,</text>
<text clip-path="url(#q2)" x="76" y="318" font-size="15"><tspan fill="#1f2328">I </tspan><tspan fill="#db2777" font-weight="bold">build</tspan><tspan fill="#1f2328"> with it.</tspan></text>
<g class="tw" style="animation-delay:.9s"><path d="M400 288l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#d946ef"/></g>

<!-- Tech I Know -->
<text class="ii" x="48" y="374" font-size="15" fill="#9333ea" font-weight="bold" style="animation:fadeIn .4s ease 4.6s forwards">🧩 Tech I Know</text>
'''

x = 48
delay = 4.8
for label, fillrgba, stroke, textcol in TECH_PILLS_ROW1:
    width = 44 + len(label) * 10
    svg += (f'<g class="pill" style="animation:fadeIn .3s ease {delay:.1f}s forwards">'
            f'<rect x="{x}" y="388" width="{width}" height="26" rx="13" fill="{fillrgba}" stroke="{stroke}" stroke-width="1"/>'
            f'<text x="{x+width/2:.0f}" y="405" text-anchor="middle" font-size="12" fill="{textcol}" font-weight="bold">{label}</text></g>\n')
    x += width + 12
    delay += 0.1

x = 48
delay = 5.2
for label, fillrgba, stroke, textcol in TECH_PILLS_ROW2:
    width = 44 + len(label) * 10
    svg += (f'<g class="pill" style="animation:fadeIn .3s ease {delay:.1f}s forwards">'
            f'<rect x="{x}" y="422" width="{width}" height="26" rx="13" fill="{fillrgba}" stroke="{stroke}" stroke-width="1"/>'
            f'<text x="{x+width/2:.0f}" y="439" text-anchor="middle" font-size="12" fill="{textcol}" font-weight="bold">{label}</text></g>\n')
    x += width + 12
    delay += 0.1

svg += f'''
<!-- About Me -->
<text class="ii" x="48" y="490" font-size="15" fill="#db2777" font-weight="bold" style="animation:fadeIn .4s ease 5.6s forwards">💗 About Me</text>
<text class="ii" x="48" y="516" font-size="13.5" style="animation:fadeIn .4s ease 5.8s forwards"><tspan fill="#1a7f37">&gt;_ </tspan><tspan fill="#424a53">I build practical solutions with Python and data-driven thinking.</tspan></text>
<text class="ii" x="48" y="540" font-size="13.5" style="animation:fadeIn .4s ease 6s forwards"><tspan fill="#b45309">💡 </tspan><tspan fill="#424a53">Always learning, always experimenting.</tspan></text>
<text class="ii" x="48" y="564" font-size="13.5" style="animation:fadeIn .4s ease 6.2s forwards"><tspan fill="#db2777">🚀 </tspan><tspan fill="#424a53">Turning coursework into real-world AI projects.</tspan></text>

<!-- Stats card -->
<g class="st" style="animation:fadeIn .5s ease 6.4s forwards">
  <rect x="48" y="586" width="560" height="66" rx="12" fill="#faf5ff" stroke="#e6d5f7" stroke-width="1"/>
  <line x1="188" y1="598" x2="188" y2="640" class="sep"/>
  <line x1="328" y1="598" x2="328" y2="640" class="sep"/>
  <line x1="468" y1="598" x2="468" y2="640" class="sep"/>
  <text x="118" y="612" text-anchor="middle" font-size="11.5" fill="#6e7781">📦 Repos</text>
  <text x="258" y="612" text-anchor="middle" font-size="11.5" fill="#6e7781">💻 Commits</text>
  <text x="398" y="612" text-anchor="middle" font-size="11.5" fill="#6e7781">⭐ Stars</text>
  <text x="538" y="612" text-anchor="middle" font-size="11.5" fill="#6e7781">👥 Followers</text>
</g>
<text class="st" x="118" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#db2777" filter="url(#glow)" style="animation:fadeIn .4s ease 6.6s forwards">6+</text>
<text class="st" x="258" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#c026d3" filter="url(#glow)" style="animation:fadeIn .4s ease 6.75s forwards">300+</text>
<text class="st" x="398" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#b45309" filter="url(#glow)" style="animation:fadeIn .4s ease 6.9s forwards">10+</text>
<text class="st" x="538" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#9333ea" filter="url(#glow)" style="animation:fadeIn .4s ease 7.05s forwards">15+</text>

<!-- ================= RIGHT: ILLUSTRATION ================= -->
<circle cx="1000" cy="440" r="270" fill="url(#girlGlow)"><animate attributeName="r" values="270;292;270" dur="5s" repeatCount="indefinite"/></circle>
<g class="fl">
  <g clip-path="url(#girlReveal)"><image x="722" y="152" width="558" height="522" href="data:image/webp;base64,{CHAR_B64}" preserveAspectRatio="xMidYMid slice"/></g>
  <g clip-path="url(#girlBox)">
    <rect x="722" y="150" width="558" height="4" fill="url(#scanEdge)" filter="url(#glow)" opacity="0">
      <animate attributeName="opacity" values="0;.95;.95;0" keyTimes="0;.04;.9;1" dur="2s" begin=".5s" fill="freeze"/>
      <animate attributeName="y" from="150" to="672" dur="1.8s" begin=".5s" fill="freeze"/>
    </rect>
  </g>
</g>

<!-- buildFuture() code card -->
<g class="cl" style="animation:fadeIn .5s ease 1.4s forwards">
  <rect x="552" y="40" width="286" height="212" rx="12" fill="#ffffff" fill-opacity=".94" stroke="#e6d5f7" stroke-width="1.2"/>
  <rect x="552" y="40" width="286" height="28" rx="12" fill="#f3ebfb"/>
  <rect x="552" y="56" width="286" height="12" fill="#f3ebfb"/>
  <circle cx="572" cy="54" r="4.5" fill="#ff5f57"/><circle cx="588" cy="54" r="4.5" fill="#febc2e"/><circle cx="604" cy="54" r="4.5" fill="#28c840"/>
  <text x="695" y="58" text-anchor="middle" font-size="11" fill="#6e7781">buildFuture.py</text>
</g>
<g font-size="12.5">
  <text class="cl" x="568" y="90" style="animation:fadeIn .3s ease 1.8s forwards"><tspan fill="#c026d3">def</tspan><tspan fill="#0969da"> build_future</tspan><tspan fill="#1f2328">():</tspan></text>
  <text class="cl" x="582" y="110" style="animation:fadeIn .3s ease 2.1s forwards"><tspan fill="#c026d3">return</tspan><tspan fill="#1f2328"> {{</tspan></text>
  <text class="cl" x="596" y="130" style="animation:fadeIn .3s ease 2.4s forwards"><tspan fill="#b45309">"learn"</tspan><tspan fill="#1f2328">: </tspan><tspan fill="#1a7f37">True</tspan><tspan fill="#1f2328">,</tspan></text>
  <text class="cl" x="596" y="150" style="animation:fadeIn .3s ease 2.7s forwards"><tspan fill="#b45309">"code"</tspan><tspan fill="#1f2328">: </tspan><tspan fill="#1a7f37">True</tspan><tspan fill="#1f2328">,</tspan></text>
  <text class="cl" x="596" y="168" style="animation:fadeIn .3s ease 2.95s forwards"><tspan fill="#b45309">"grow"</tspan><tspan fill="#1f2328">: </tspan><tspan fill="#1a7f37">True</tspan><tspan fill="#1f2328">,</tspan></text>
  <text class="cl" x="582" y="186" style="animation:fadeIn .3s ease 3.2s forwards"><tspan fill="#1f2328">}}</tspan></text>
  <text class="cl" x="568" y="204" style="animation:fadeIn .3s ease 3.45s forwards"><tspan fill="#6e7781"># always in progress</tspan></text>
</g>

<!-- Neon sign -->
<g class="neon-on">
  <rect x="1012" y="42" width="238" height="128" rx="14" fill="none" stroke="#c026d3" stroke-width="1.5" opacity=".5" filter="url(#glow)"/>
  <text class="np" x="1131" y="86" text-anchor="middle" font-size="30" font-weight="bold" fill="#db2777" filter="url(#glowBig)" style="animation-delay:.2s">&lt;/&gt;</text>
  <text class="np" x="1131" y="118" text-anchor="middle" font-size="19" font-weight="bold" fill="#c026d3" filter="url(#glow)" letter-spacing="2">KEEP LEARNING</text>
  <text class="np" x="1131" y="146" text-anchor="middle" font-size="19" font-weight="bold" fill="#9333ea" filter="url(#glow)" letter-spacing="1.5" style="animation-delay:1.3s">KEEP BUILDING</text>
</g>

<!-- Pixel heart -->
<g class="fl2" style="animation-delay:.7s">
  <g transform="translate(600,300)" opacity="0">
    <animate attributeName="opacity" from="0" to=".95" dur=".6s" begin="4.4s" fill="freeze"/>
    <g fill="#9333ea"><rect x="6" y="0" width="6" height="6"/><rect x="18" y="0" width="6" height="6"/><rect x="0" y="6" width="30" height="6"/><rect x="3" y="12" width="24" height="6"/><rect x="9" y="18" width="12" height="6"/><rect x="12" y="24" width="6" height="4"/></g>
  </g>
</g>
<g class="hb" style="animation-delay:1.4s"><path d="M1236 320 c-4-9-17-7-17 3 0 7 10 13 17 18 7-5 17-11 17-18 0-10-13-12-17-3z" fill="#db2777" opacity=".85" filter="url(#glow)"/></g>

<!-- ================= FOOTER ================= -->
<line x1="48" y1="676" x2="1232" y2="676" class="sep" stroke-dasharray="1184" stroke-dashoffset="1184">
  <animate attributeName="stroke-dashoffset" from="1184" to="0" dur=".7s" begin="7.2s" fill="freeze"/>
</line>
<g class="soc" style="animation:fadeIn .5s ease 7.4s forwards">
  <g transform="translate(48,692) scale(.8)"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" fill="#30363d"/></g>
  <text x="74" y="707" font-size="12.5" fill="#30363d">komal-env</text>
  <g transform="translate(190,693) scale(.8)"><rect x="1" y="3" width="22" height="17" rx="3.5" fill="none" stroke="#db2777" stroke-width="2"/><path d="M2.5 5.5 12 13l9.5-7.5" fill="none" stroke="#db2777" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>
  <text x="216" y="707" font-size="12.5" fill="#30363d">komalraj2318@gmail.com</text>
  <g transform="translate(452,692) scale(.8)"><rect width="24" height="24" rx="5" fill="none" stroke="#0a66c2" stroke-width="2"/><rect x="4" y="9" width="4" height="11" fill="#0a66c2"/><circle cx="6" cy="4.5" r="2.3" fill="#0a66c2"/><path d="M11 9h4v2.2c.7-1.4 2-2.6 4.2-2.6 4.4 0 5 2.7 5 6.3V20h-4v-4.5c0-1.1 0-2.5-1.6-2.5s-1.9 1.2-1.9 2.4V20h-4z" fill="#0a66c2"/></g>
  <text x="480" y="707" font-size="12.5" fill="#30363d">komal-env</text>
</g>
<text class="soc" x="1232" y="707" text-anchor="end" font-size="13" style="animation:fadeIn .5s ease 7.6s forwards"><tspan fill="#6e7781">“</tspan><tspan fill="#d946ef">Code is my craft, curiosity is my compass.</tspan><tspan fill="#6e7781">” </tspan><tspan fill="#db2777">❤</tspan></text>
<text class="soc" x="700" y="707" font-size="11.5" style="animation:fadeIn .5s ease 7.5s forwards"><tspan fill="#28c840">●</tspan><tspan fill="#6e7781"> open to collaborate</tspan></text>

<!-- full-banner scanner -->
<g clip-path="url(#bannerBox)" opacity="0">
  <animate attributeName="opacity" from="0" to="1" dur=".6s" begin="3s" fill="freeze"/>
  <g>
    <animateTransform attributeName="transform" type="translate" values="0,-40;0,780" dur="3.5s" begin="3s" repeatCount="indefinite"/>
    <rect x="0" y="-34" width="{W}" height="34" fill="url(#scanTrail)"/>
    <rect x="0" y="0" width="{W}" height="2.6" fill="url(#scanEdge)" opacity=".6" filter="url(#glow)"/>
  </g>
</g>
</svg>
'''

with open(OUT, "w") as f:
    f.write(svg)
print("wrote", OUT, len(svg), "bytes;", W, "x", H)
