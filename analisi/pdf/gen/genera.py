import sys
sys.path.insert(0, "/home/user/clauderesearch/analisi/pdf/gen")
from base import *
from cap_a import cover, cap00, cap01, cap02
from cap_b import cap03
from cap_c import cap04, cap05, cap06
from cap_d import cap07, cap08, cap09
from cap_e import cap10
from cap_f import cap11, cap12, cap13, cap14, cap15
from cap_g import cap16, appA, appB
html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>Kriné Labs · Piano di progetto</title>
<style>{HEAD_CSS}{EXTRA_CSS}</style>
</head>
<body>
{cover()}{cap00()}{cap01()}{cap02()}{cap03()}{cap04()}{cap05()}{cap06()}{cap07()}{cap08()}{cap09()}{cap10()}{cap11()}{cap12()}{cap13()}{cap14()}{cap15()}{cap16()}{appA()}{appB()}
</body>
</html>"""
open("/home/user/clauderesearch/analisi/pdf/report-piano.html", "w").write(html)
print("scritto", len(html))
