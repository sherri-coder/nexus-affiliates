"""Regenerate public/sales-kit.html and public/nexus_affiliate_kit.zip.
Run after editing public/index.html or public/affiliate_sales_kit.md:
    pip install markdown && python3 build_sales_kit.py
"""
import re, zipfile, pathlib, markdown
root = pathlib.Path(__file__).parent
idx = (root/'public/index.html').read_text(encoding='utf-8')
css = re.search(r'<style>(.*?)</style>', idx, re.S).group(1)
md = (root/'public/affiliate_sales_kit.md').read_text(encoding='utf-8')
body = markdown.markdown(md, extensions=['tables'])
extra = """
.kit{max-width:860px;margin:0 auto;padding:9rem 1.5rem 5rem}
.kit h1{font:300 clamp(2.2rem,5vw,3.6rem)/1.15 'Cormorant Garamond',Georgia,serif;margin-bottom:1.5rem}
.kit h2{font:400 clamp(1.6rem,3vw,2.2rem)/1.2 'Cormorant Garamond',Georgia,serif;color:var(--gold);margin:3rem 0 1rem}
.kit p,.kit li{color:#c9c2b7;font-size:.95rem;margin:1rem 0}
.kit ul{padding-left:1.5rem}
.kit strong{color:var(--white);font-weight:600}
.kit a{color:var(--gold);overflow-wrap:anywhere}
.kit table{width:100%;border-collapse:collapse;margin:1.5rem 0}
.kit th,.kit td{border:1px solid var(--border);padding:.8rem 1rem;font-size:.85rem;text-align:left}
.kit th{color:var(--gold);font-weight:600}
.kit-actions{display:flex;gap:1rem;flex-wrap:wrap;margin:2rem 0}
.kit-wrap{overflow-x:auto}
"""
body = body.replace('<table>', '<div class="kit-wrap"><table>').replace('</table>', '</table></div>')
html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Nexus Affiliate Sales Kit | Elevate Ops 360</title><meta name="robots" content="noindex"><link rel="canonical" href="https://affiliates.elevateops360.com/sales-kit.html"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet"><style>{css}{extra}</style></head><body><a class="skip" href="#main">Skip to content</a>
<nav aria-label="Main navigation"><a class="nav-logo" href="https://nexus.elevateops360.com/">Nexus <span>·</span> Elevate Ops 360</a><ul class="nav-links"><li><a href="/">Affiliate Program</a></li><li><a href="/#apply">Apply</a></li><li><a class="nav-cta" href="https://calendly.com/sherriparsonsrealestate/nexus-onboarding-session">Book Onboarding</a></li></ul></nav>
<main id="main" class="kit">{body}
<div class="kit-actions"><a class="btn-primary" href="/#apply">Apply to Become an Affiliate</a><a class="btn-secondary" href="/">Back to the program</a><a class="btn-secondary" href="affiliate_sales_kit.md" download>Download as Markdown</a><a class="btn-secondary" href="nexus_affiliate_kit.zip" download>Download the kit (.zip)</a></div></main>
<footer class="site-footer"><div><a href="https://nexus.elevateops360.com/" class="nav-logo">Nexus <span>·</span> Elevate Ops 360</a><p>The AI operating layer for real estate.<br>Hampton Roads, Virginia.</p></div><div><p>Affiliate program preview · USD<br>No earnings are guaranteed.</p></div></footer></body></html>"""
(root/'public/sales-kit.html').write_text(html, encoding='utf-8')
with zipfile.ZipFile(root/'public/nexus_affiliate_kit.zip','w',zipfile.ZIP_DEFLATED) as z:
    for n in ['index.html','sales-kit.html','affiliate_sales_kit.md']:
        z.write(root/'public'/n, n)
print('built', [i.filename for i in zipfile.ZipFile(root/'public/nexus_affiliate_kit.zip').infolist()])
