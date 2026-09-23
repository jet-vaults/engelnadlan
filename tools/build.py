# -*- coding: utf-8 -*-
"""Static site generator for engelnadlan.co.il.

    python tools/build.py

Reads nothing but this file (all content lives here) and writes the HTML pages into wwwroot/.
Assets (css/js/img/fonts) are authored directly in wwwroot/assets and are not touched.
"""
import os, html
from PIL import Image

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "wwwroot")
IMG = os.path.join(OUT, "assets", "img")

# ---------------------------------------------------------------- settings
SITE_NAME = "אנגל נדל״ן"
SITE_URL = "https://engelnadlan.co.il"
PREVIEW = True                      # preview build => noindex everywhere
WEB3FORMS_KEY = "YOUR-WEB3FORMS-ACCESS-KEY"   # replace to activate the contact forms
PHONE = "03-6005955"
PHONE_TEL = "+97236005955"
FAX = "03-6005999"
EMAIL = "office@engelnadlan.co.il"
ADDRESS = "מרמורק 26, תל אביב"
YEAR = "2026"

STATUS = {
    "active":   "בביצוע",
    "permit":   "בהיתר בנייה · לקראת ביצוע",
    "planning": "לאחר החלטת ועדה · לקראת היתר",
    "done":     "אוכלס",
}

# ---------------------------------------------------------------- projects
PROJECTS = [
  dict(slug="ussishkin-46", title="אוסישקין 46", area="הצפון הישן", status="active",
       type="תמ״א 38/2 · הריסה ובנייה מחדש", bank="בנק הפועלים",
       short="קו ראשון לפארק הירקון, עם נוף למפגש נחל הירקון והים התיכון.",
       card="ussishkin-46-card", wide="ussishkin-46-wide",
       overview=[
         "פרויקט תמ״א 38/2 של הריסה ובנייה מחדש, בקו ראשון לפארק הירקון. הבניין החדש נהנה מנוף מרהיב על מפגש הימים של נחל הירקון והים התיכון, ומרפסת וחניה לכל דירה.",
         "הבניין מוגבה כ־1.5 מטר מעל גובה הרחוב לקבלת אור, אוויר ונוף, ומתוכנן עם לובאים בסטנדרט גבוה. הפרויקט נמצא כיום בביצוע בליווי בנקאי של בנק הפועלים.",
       ],
       specs=[("סוג הפרויקט","תמ״א 38/2 · הריסה ובנייה מחדש"),("סטטוס","בביצוע"),("ליווי בנקאי","בנק הפועלים"),("מיקום","רובע 3, הצפון הישן, תל אביב"),("לכל דירה","מרפסת וחניה"),("מפרט","לובאים בסטנדרט גבוה · הבניין מוגבה כ־1.5 מ׳ מעל הרחוב")],
       location=["קו ראשון לפארק הירקון, עם נוף לים","רובע 3 - הצפון הישן של תל אביב","בקרבת הים, נמל תל אביב, בתי קפה ומסעדות"],
       gallery=[("ussishkin-46-roof",16/9,"הדמיית קומת הגג","הדמיה · קומת הגג ונוף העיר","span"),
                ("ussishkin-46-living",16/9,"הדמיית סלון עם נוף לים","הדמיה · סלון",""),
                ("ussishkin-46-kitchen",16/9,"הדמיית מטבח","הדמיה · מטבח",""),
                ("ussishkin-46-bedroom",16/9,"הדמיית חדר שינה","הדמיה · חדר שינה",""),
                ("yarkon-panorama",2678/762,"נוף פנורמי לפארק הירקון ולים","הנוף מגובה הדירות · פארק הירקון והים","span")],
       units=[dict(name="מיני פנטהאוז", sub="דירת 4/5 חדרים · קומה 5",
                   rows=[("שטח עיקרי","126 מ״ר"),("מרפסת צפונית","24 מ״ר"),("כיווני אוויר","3"),("חזית","מלוא חזית הבניין לפארק ולים"),("תכנון","5 חדרים או 4 חדרים")])],
  ),
  dict(slug="prague-3", title="פראג 3", area="הצפון הישן", status="active",
       type="תמ״א 38/2 · הריסה ובנייה מחדש", bank="כלל",
       short="רחוב שקט בין דיזנגוף לבן־יהודה, חמש דקות הליכה לחוף הילטון.",
       card="prague-3-card", wide="prague-3-wide",
       overview=[
         "בניין בוטיק חדש ברחוב שקט בין דיזנגוף לבן־יהודה, במרחק חמש דקות הליכה מחוף הילטון. הפרויקט מוקם במסגרת תמ״א 38/2 - הריסה ובנייה מחדש - ומיועד ל־12 דיירים בלבד.",
         "לכל הדירות מרפסות וחניות. הפרויקט נמצא בביצוע בליווי בנקאי של חברת כלל.",
       ],
       specs=[("סוג הפרויקט","תמ״א 38/2 · הריסה ובנייה מחדש"),("סטטוס","בביצוע"),("ליווי בנקאי","כלל"),("מיקום","הצפון הישן, תל אביב"),("היקף","בניין בוטיק · 12 דיירים בלבד"),("לכל דירה","מרפסת וחניה")],
       location=["רחוב שקט בין דיזנגוף לבן־יהודה","5 דקות הליכה לחוף הילטון"],
       gallery=[], units=[],
  ),
  dict(slug="ussishkin-52", title="אוסישקין 52", area="הצפון הישן", status="permit",
       type="תמ״א 38/2 · הריסה ובנייה מחדש", bank=None,
       short="קו ראשון לפארק הירקון. בהיתר בנייה ולקראת תחילת ביצוע.",
       card="ussishkin-52-card", wide="ussishkin-52-wide",
       overview=[
         "פרויקט תמ״א 38/2 של הריסה ובנייה מחדש בקו ראשון לפארק הירקון, עם נוף על מפגש נחל הירקון והים התיכון. מרפסת וחניה לכל דירה.",
         "הפרויקט קיבל היתר בנייה ונמצא לקראת תחילת ביצוע.",
       ],
       specs=[("סוג הפרויקט","תמ״א 38/2 · הריסה ובנייה מחדש"),("סטטוס","היתר בנייה · לקראת ביצוע"),("מיקום","הצפון הישן, תל אביב"),("לכל דירה","מרפסת וחניה")],
       location=["קו ראשון לפארק הירקון","9 דקות הליכה לחוף הים","5 דקות הליכה לנמל תל אביב"],
       gallery=[("yarkon-aerial",1213/512,"מבט מהגג לפארק הירקון","נוף להמחשה מהגג העליון · פארק הירקון","span")],
       units=[dict(name="דירת 3 חדרים", sub="קומה 5",
                   rows=[("שטח עיקרי","60 מ״ר"),("מרפסת צפונית","13 מ״ר"),("כיווני אוויר","2 · צפון־מזרח, לכיוון פארק הירקון"),("חניה","חניה תת־קרקעית אחת")])],
  ),
  dict(slug="bartenura-3-5", title="עובדיה מברטנורה 3 ו־5", area="הצפון הישן", status="planning",
       type="תמ״א 38/2 · הריסה ובנייה מחדש · שני בניינים", bank=None,
       short="שני בניינים ברחוב שקט בין שדרות נורדאו לכיכר בזל.",
       card="bartenura-card", wide="bartenura-wide",
       overview=[
         "פרויקט תמ״א 38/2 של הריסה ובנייה מחדש לשני בניינים ברחוב שקט בין שדרות נורדאו לכיכר בזל, במרחק שמונה דקות הליכה מחוף מציצים. מרפסת וחניה לכל דירה.",
         "הפרויקט ממוקם בלב צפון תל אביב המבוקש - בסביבה שקטה, איכותית ופסטורלית, המשלבת חיי שכונה נעימים לצד נגישות עירונית מלאה: קרבה לצירי תנועה מרכזיים, מוסדות חינוך מובילים, בתי קפה, פארקים ומרכזי בילוי, והכול במרחק דקות מהים.",
         "הפרויקט נמצא לאחר החלטת ועדה ולקראת קבלת היתר בנייה.",
       ],
       specs=[("סוג הפרויקט","תמ״א 38/2 · הריסה ובנייה מחדש"),("היקף","שני בניינים"),("סטטוס","לאחר החלטת ועדה · לקראת היתר"),("מיקום","הצפון הישן, תל אביב"),("לכל דירה","מרפסת וחניה")],
       location=["בין שדרות נורדאו לכיכר בזל","8 דקות הליכה לחוף מציצים","קרבה לצירי תנועה, מוסדות חינוך, בתי קפה ופארקים"],
       gallery=[("bartenura-2",4/3,"הדמיית הבניין החדש","הדמיה · חזית הבניין","span")],
       units=[],
  ),
  dict(slug="berdichevsky-17", title="ברדיצ׳בסקי 17", area="לב העיר", status="done",
       type="תמ״א 38/1 · חיזוק ושיפוץ", bank=None,
       short="בניין בוטיק פינתי מול מלון ברדיצ׳בסקי, בכניסה משדרות רוטשילד.",
       card="berdichevsky-card", wide="berdichevsky-wide",
       overview=[
         "פרויקט תמ״א 38/1 של חיזוק ושיפוץ: בניין בוטיק פינתי של עשרה דיירים בלבד, בעיצוב מודרני, הממוקם מול מלון ברדיצ׳בסקי בלב תל אביב.",
         "הבניין יושב במרכז התרבות השוקק של העיר - כיכר הבימה, היכל התרבות והסינמטק במרחק הליכה - ברחוב חד־סטרי עם כניסה משדרות רוטשילד. הפרויקט הושלם ואוכלס.",
       ],
       specs=[("סוג הפרויקט","תמ״א 38/1 · חיזוק ושיפוץ"),("סטטוס","אוכלס"),("מיקום","לב העיר, תל אביב"),("היקף","בניין בוטיק פינתי · 10 דיירים")],
       location=["מול מלון ברדיצ׳בסקי","כיכר הבימה, היכל התרבות והסינמטק במרחק הליכה","רחוב חד־סטרי, כניסה משדרות רוטשילד"],
       gallery=[], units=[],
  ),
  dict(slug="marmorek-26", title="מרמורק 26", area="לב העיר", status="done",
       type="תמ״א 38/1 · חיזוק ושיפוץ", bank=None,
       short="בלב המרכז התרבותי של תל אביב, בין כיכר הבימה לשדרות רוטשילד.",
       card="marmorek-card", wide=None,
       overview=[
         "פרויקט תמ״א 38/1 של חיזוק ושיפוץ בלב תל אביב, במרכז התרבות השוקק של העיר: כיכר הבימה, היכל התרבות, הסינמטק ושדרות רוטשילד - ברחוב חד־סטרי עם שביל אופניים חדש.",
         "הפרויקט הושלם ואוכלס. בבניין שוכנים גם משרדי אנגל נדל״ן.",
       ],
       specs=[("סוג הפרויקט","תמ״א 38/1 · חיזוק ושיפוץ"),("סטטוס","אוכלס"),("מיקום","לב העיר, תל אביב")],
       location=["כיכר הבימה, היכל התרבות והסינמטק","שדרות רוטשילד","רחוב חד־סטרי עם שביל אופניים חדש"],
       gallery=[], units=[],
  ),
]
BY_SLUG = {p["slug"]: p for p in PROJECTS}

# ---------------------------------------------------------------- helpers
def esc(s): return html.escape(s, quote=True)

def dims(name, w):
    with Image.open(os.path.join(IMG, f"{name}-{w}.webp")) as im: return im.size

def widths_of(name):
    ws = sorted(int(f[len(name)+1:-5]) for f in os.listdir(IMG) if f.startswith(name + "-") and f.endswith(".webp") and f[len(name)+1:-5].isdigit())
    return ws

def pic(name, alt, sizes="100vw", eager=False, cls="", style=""):
    ws = widths_of(name)
    avif = ", ".join(f"/assets/img/{name}-{w}.avif {w}w" for w in ws)
    webp = ", ".join(f"/assets/img/{name}-{w}.webp {w}w" for w in ws)
    w, h = dims(name, ws[-1])
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (f'<picture{(" class=%s" % chr(34)+cls+chr(34)) if cls else ""}>'
            f'<source type="image/avif" srcset="{avif}" sizes="{sizes}">'
            f'<img src="/assets/img/{name}-{ws[-1]}.webp" srcset="{webp}" sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt)}" {load}{(" style=%s" % chr(34)+style+chr(34)) if style else ""}>'
            f'</picture>')

def preload(name, sizes, media=None):
    ws = widths_of(name)
    ss = ", ".join(f"/assets/img/{name}-{w}.avif {w}w" for w in ws)
    m = f' media="{media}"' if media else ""
    return f'<link rel="preload" as="image" fetchpriority="high" type="image/avif" imagesrcset="{ss}" imagesizes="{sizes}"{m}>'

ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M14 8H2M7 3 2 8l5 5"/></svg>'
MARK = '<svg viewBox="0 0 40 28" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M1 27V11h9v16"/><path d="M15 27V1h11v26"/><path d="M31 27V7h8v20"/></svg>'

NAV = [("/projects/","פרויקטים"),("/urban-renewal/","התחדשות עירונית"),("/about/","אודות"),("/contact/","צור קשר")]

def head(title, desc, path, extra=""):
    full = f"{title} | {SITE_NAME}" if path != "/" else title
    robots = '<meta name="robots" content="noindex, nofollow">' if PREVIEW else f'<link rel="canonical" href="{SITE_URL}{path}">'
    return f'''<!DOCTYPE html>
<html lang="he" dir="rtl" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
{robots}
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="he_IL">
<meta property="og:image" content="{SITE_URL}/assets/img/hero-wide-1200.webp">
<meta name="theme-color" content="#f6f7f9">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="preload" href="/assets/fonts/plex-hebrew-200-hebrew.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/plex-hebrew-400-hebrew.woff2" as="font" type="font/woff2" crossorigin>
{extra}
<link rel="stylesheet" href="/assets/css/site.css">
<script>document.documentElement.classList.remove('no-js')</script>
</head>
<body>
<a class="skip" href="#main">דילוג לתוכן</a>
'''

def header(active):
    links = "".join(f'<a href="{h}"{" aria-current=%spage%s" % (chr(34),chr(34)) if h == active else ""}>{t}</a>' for h, t in NAV)
    menu = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f'''<header class="header">
  <div class="wrap">
    <a class="brand" href="/"><img src="/assets/img/logo-black.png" width="453" height="324" alt="{SITE_NAME}"></a>
    <nav class="nav" aria-label="ניווט ראשי">{links}</nav>
    <div class="header__cta"><a class="header__phone" href="tel:{PHONE_TEL}">{PHONE}</a><a class="btn btn--solid" href="/urban-renewal/#feasibility">בדיקת היתכנות</a></div>
    <button class="burger" aria-label="תפריט" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="menu" id="menu">
  <ul>{menu}</ul>
  <div class="menu__foot"><a href="tel:{PHONE_TEL}" dir="ltr" style="text-align:end">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a><span class="muted">{ADDRESS}</span></div>
</div>
<main id="main">
'''

def footer():
    nav = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f'''</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <a class="brand" href="/"><img src="/assets/img/logo-white.png" width="453" height="324" alt="{SITE_NAME}" loading="lazy"></a>
        <p class="footer__tag">חברת בוטיק משפחתית לייזום וביצוע פרויקטים של תמ״א 38 - בתל אביב בלבד.</p>
      </div>
      <div><p class="footer__h">ניווט</p><ul>{nav}</ul></div>
      <div><p class="footer__h">יצירת קשר</p><ul>
        <li><a class="ltr" href="tel:{PHONE_TEL}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><span class="ltr">{FAX}</span> פקס</li>
        <li>{ADDRESS}</li></ul></div>
      <div><p class="footer__h">מידע</p><ul>
        <li><a href="/terms/">תנאי שימוש</a></li>
        <li><a href="/privacy/">מדיניות פרטיות</a></li>
        <li><a href="/accessibility/">הצהרת נגישות</a></li>
        <li><a href="/projects/">דירות למכירה</a></li></ul></div>
    </div>
    <div class="footer__bottom">
      <span>© {YEAR} כל הזכויות שמורות לאנגל נדל״ן</span>
      <span>התמונות והדמיות להמחשה בלבד. ט.ל.ח</span>
    </div>
  </div>
</footer>
<script src="/assets/js/site.js" defer></script>
<script src="/assets/js/a11y.js" defer></script>
</body>
</html>
'''

def card(p, sizes="(min-width:1000px) 30vw, (min-width:640px) 45vw, 92vw", d=0):
    return f'''<a class="card rv" data-d="{d}" data-status="{p['status']}" href="/projects/{p['slug']}/">
  <div class="card__media">{pic(p['card'], f"הדמיה - {p['title']}, תל אביב", sizes)}<span class="card__status" data-s="{p['status']}">{STATUS[p['status']]}</span></div>
  <div class="card__body">
    <span class="card__title">{p['title']}</span>
    <span class="card__arrow">{ARROW}</span>
    <span class="card__loc">{p['area']} · תל אביב</span>
    <span class="card__type">{p['type']}</span>
  </div>
</a>'''

def form(kind="contact", dark=False, project=None):
    subj_default = "בדיקת היתכנות להתחדשות עירונית" if kind == "feasibility" else ""
    subject_field = f'''<input type="hidden" name="subject" value="פנייה מהאתר - {SITE_NAME}">'''
    interest = f'''<div class="field"><label for="f-interest">מה מעניין אתכם?</label>
      <select id="f-interest" name="interest">
        <option{" selected" if kind=="feasibility" else ""}>בדיקת היתכנות להתחדשות עירונית בבניין שלי</option>
        <option{" selected" if kind=="buy" else ""}>רכישת דירה ישירות מהחברה</option>
        <option>אחר</option></select></div>'''
    proj = f'<input type="hidden" name="project" value="{esc(project)}">' if project else ""
    return f'''<form class="form" action="https://api.web3forms.com/submit" method="POST" novalidate>
  <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
  {subject_field}{proj}
  <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="form__row">
    <div class="field"><label for="f-name">שם מלא</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
    <div class="field"><label for="f-phone">טלפון</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
  </div>
  <div class="form__row">
    <div class="field"><label for="f-email">דוא״ל</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
    <div class="field"><label for="f-address">כתובת הבניין</label><input id="f-address" name="building" type="text" placeholder="רחוב ומספר, תל אביב"></div>
  </div>
  {interest}
  <div class="field"><label for="f-msg">הודעה</label><textarea id="f-msg" name="message" placeholder="ספרו לנו בקצרה על הבניין, מספר הדירות והדיירים, או כל שאלה אחרת"></textarea></div>
  <div class="form__foot">
    <button class="btn btn--solid" type="submit">שליחה {ARROW}</button>
    <span class="note">הפרטים ישמשו למענה לפנייתכם בלבד.</span>
  </div>
  <div class="form__msg" role="status" aria-live="polite"></div>
</form>'''

def cta_section():
    return f'''<section class="section section--dark cta grain">
  <div class="wrap">
    <div>
      <p class="eyebrow"><span class="num">06</span> נתחיל בשיחה</p>
      <h2 class="h-l">רוצים לבדוק היתכנות להתחדשות עירונית בבניין שלכם?</h2>
      <p class="lead" style="margin-top:20px">השאירו פרטים וצוות המומחים שלנו יבחן את הבניין ויחזור אליכם עם תשובה מפורטת האם קיימת היתכנות כלכלית לפרויקט - ללא כל עלות.</p>
      <div class="actions" style="margin-top:28px"><a class="btn btn--solid" href="/urban-renewal/#feasibility">השאירו פרטים {ARROW}</a><a class="btn btn--ghost" href="/projects/">דירות למכירה</a></div>
    </div>
    <div class="cta__contact">
      <span class="muted" style="color:var(--on-dark-2)">או פשוט התקשרו</span>
      <a class="big" href="tel:{PHONE_TEL}">{PHONE}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <span style="color:var(--on-dark-2)">{ADDRESS}</span>
    </div>
  </div>
</section>
'''

def write(path, content):
    fp = os.path.join(OUT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(OUT, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8", newline="\n") as f: f.write(content)
    print("wrote", os.path.relpath(fp, ROOT))

# ---------------------------------------------------------------- pages
def page_home():
    cards = "".join(card(p, d=i % 3) for i, p in enumerate(PROJECTS))
    hero_sizes_tall = "(min-width:1320px) 600px, (min-width:900px) 45vw, 0px"
    hero_sizes_wide = "(max-width:899px) 100vw, 0px"
    extra = preload("hero-tall", "45vw", "(min-width:900px)") + "\n" + preload("hero-wide", "100vw", "(max-width:899px)")
    h = head("אנגל נדל״ן | התחדשות עירונית בתל אביב · תמ״א 38", "אנגל נדל״ן היא חברת בוטיק משפחתית לייזום וביצוע פרויקטים של תמ״א 38 בתל אביב בלבד - מהבדיקה הראשונית ועד מסירת המפתח.", "/", extra)
    return h + header("/") + f'''
<section class="hero">
  <div class="wrap">
    <div class="hero__grid">
      <div class="hero__copy">
        <p class="eyebrow">התחדשות עירונית · תל אביב</p>
        <h1 class="h-xl">בונים מחדש את <span class="em">לב תל אביב.</span></h1>
        <p class="lead">אנגל נדל״ן היא חברת בוטיק משפחתית לייזום וביצוע פרויקטים של תמ״א 38 - בתל אביב בלבד. מהבדיקה הראשונית ועד מסירת המפתח, באחריות מלאה ובסטנדרט הגבוה בעיר.</p>
        <div class="actions"><a class="btn btn--solid" href="/urban-renewal/#feasibility">בדיקת היתכנות לבניין שלכם {ARROW}</a><a class="btn btn--ghost" href="/projects/">הפרויקטים שלנו</a></div>
      </div>
      <div class="hero__media">
        {pic("hero-tall", "הדמיית פרויקט פראג 3 - בניין בוטיק חדש בצפון הישן של תל אביב", hero_sizes_tall, eager=True, cls="tall")}
        {pic("hero-wide", "הדמיית פרויקט פראג 3 - בניין בוטיק חדש בצפון הישן של תל אביב", hero_sizes_wide, eager=True, cls="wide")}
        <div class="hero__cap">פראג 3 · הצפון הישן<b>בביצוע</b></div>
      </div>
    </div>
    <div class="facts">
      <ul>
        <li><b>תל אביב בלבד</b>עיר אחת. התמחות אחת.</li>
        <li><b>תמ״א 38</b>חיזוק ושיפוץ · הריסה ובנייה מחדש</li>
        <li><b>ליווי בנקאי</b>בנק הפועלים · כלל</li>
        <li><b>עשרות לקוחות</b>בחרו בנו כשותף אמין</li>
      </ul>
    </div>
  </div>
</section>

<section class="section" id="projects">
  <div class="wrap">
    <div class="section-head">
      <div class="rv"><p class="eyebrow"><span class="num">01</span> פרויקטים נבחרים</p><h2 class="h-l">מהצפון הישן ועד לב העיר</h2></div>
      <a class="link more rv" href="/projects/">לכל הפרויקטים {ARROW}</a>
    </div>
    <div class="grid grid--3">{cards}</div>
  </div>
</section>

<section class="section section--dark grain">
  <div class="wrap">
    <div class="split split--wide">
      <div class="rv">
        <p class="eyebrow"><span class="num">02</span> אודות החברה</p>
        <p class="statement">חברת בוטיק משפחתית. <span class="em">עיר אחת.</span> אחריות מלאה מהתכנון ועד המפתח.</p>
      </div>
      <div class="rv" data-d="1">
        <p class="lead" style="max-width:none">אנגל נדל״ן היא חברת בוטיק משפחתית העוסקת בבנייה ובייזום מזה שנים, ומורכבת מאנשי מקצוע איכותיים בתחומי הנדל״ן והבנייה. הניסיון המגוון של הצוות המוביל הוא היתרון שלנו - ושל הדיירים שלנו.</p>
        <p style="color:var(--on-dark-2)">אנחנו מנהלים את כל ההיבטים של כל פרויקט מראשיתו ועד השלמתו: מהתכנון ההנדסי, דרך המימון, המיסוי והליווי המשפטי, השיווק והמכירות - וכלה בניהול ובביצוע. אנגל נדל״ן פועלת רק בעיר תל אביב, ונבחרה כשותף אמין על ידי עשרות לקוחות למימוש פרויקטים בתחום התמ״א.</p>
        <ul class="tags" style="margin:26px 0 30px"><li>מהנדסים</li><li>אדריכלים</li><li>מנהלי פרויקטים</li><li>כלכלנים</li><li>עורכי דין</li><li>מנהלי שיווק</li></ul>
        <a class="btn btn--ghost" href="/about/">להכיר את החברה {ARROW}</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div class="rv"><p class="eyebrow"><span class="num">03</span> התחדשות עירונית</p><h2 class="h-l">שני מסלולים. סטנדרט אחד.</h2></div>
      <a class="link more rv" href="/urban-renewal/">על התהליך המלא {ARROW}</a>
    </div>
    <div class="tracks">
      <div class="track rv">
        <p class="track__k">תמ״א 38/2</p><h3>הריסה ובנייה מחדש</h3>
        <p>בניין חדש לחלוטין, ממרתפי החניה ועד הגג העליון - בעיצוב יוקרתי, במפרט עשיר ובסטנדרט בנייה גבוה.</p>
        <ul><li>דירות חדשות, פונקציונליות ושטופות אור, בשטח מקסימלי לפי הזכויות מעיריית תל אביב</li><li>בנייה ירוקה, בידוד אקוסטי ולובי מפואר עם מעלית במפרט גבוה</li><li>חניון פונקציונלי לכל הדירות - קונבנציונלי או רובוטי</li><li>פגישת תכנון אישית עם אדריכל לכל דייר</li></ul>
      </div>
      <div class="track rv" data-d="1">
        <p class="track__k">תמ״א 38/1</p><h3>חיזוק ושיפוץ בניין קיים</h3>
        <p>חיזוק המבנה מפני רעידות אדמה לפי התקנים המחמירים ביותר, יחד עם שדרוג מלא של הבניין והדירות.</p>
        <ul><li>הגדלת הדירות: מרפסות שמש, ממ״ד ושטחים נוספים</li><li>הוספת מעלית ושדרוג הלובי וחדר המדרגות</li><li>שיפוץ חיצוני ברמת גימור גבוהה והחלפת תשתיות: ביוב, חשמל, מים וגז</li><li>שבילי גישה וגינה מעוצבת עם מערכות השקיה מתקדמות</li></ul>
      </div>
    </div>
    <ol class="steps rv" style="margin-top:clamp(40px,5vw,72px)">
      <li><b>בדיקת היתכנות</b><p>בדיקה ראשונית של עמידה בתנאי התוכנית - ללא עלות.</p></li>
      <li><b>בדיקות ותכנון</b><p>בדיקות משפטיות ברשויות, תכנון הנדסי ואדריכלי ומינוי צוות היועצים.</p></li>
      <li><b>הסכמות דיירים</b><p>ליווי הדיירים, סיכום פרטי הפרויקט, המפרט ורמת הגימור.</p></li>
      <li><b>מימון וביצוע</b><p>ליווי בנקאי, ערבויות חוק מכר, מימון דיור זמני - וביצוע במעקב צמוד.</p></li>
      <li><b>מסירה ורישום</b><p>מסירת הדירות החדשות, הסדרת התקנות והרישום בטאבו.</p></li>
    </ol>
  </div>
</section>

<section class="section--stone">
  <div class="band">{pic("yarkon-panorama", "נוף פנורמי לפארק הירקון ולים התיכון מגובה הדירות באוסישקין", "100vw")}</div>
  <div class="wrap section">
    <div class="section-head">
      <div class="rv"><p class="eyebrow"><span class="num">04</span> תל אביב</p><h2 class="h-l">פועלים רק בתל אביב. ומכירים כל רחוב.</h2></div>
    </div>
    <div class="areas">
      <div class="area rv">
        <h3>הצפון הישן</h3>
        <p>בין פארק הירקון, הנמל והים: רחובות שקטים במרחק דקות הליכה מחוף הילטון, חוף מציצים וכיכר בזל.</p>
        <ul>
          <li><a href="/projects/ussishkin-46/">אוסישקין 46</a><span>{STATUS['active']}</span></li>
          <li><a href="/projects/ussishkin-52/">אוסישקין 52</a><span>היתר בנייה</span></li>
          <li><a href="/projects/prague-3/">פראג 3</a><span>{STATUS['active']}</span></li>
          <li><a href="/projects/bartenura-3-5/">עובדיה מברטנורה 3 ו־5</a><span>לקראת היתר</span></li>
        </ul>
      </div>
      <div class="area rv" data-d="1">
        <h3>לב העיר</h3>
        <p>המרכז התרבותי של תל אביב: כיכר הבימה, היכל התרבות, הסינמטק ושדרות רוטשילד.</p>
        <ul>
          <li><a href="/projects/berdichevsky-17/">ברדיצ׳בסקי 17</a><span>{STATUS['done']}</span></li>
          <li><a href="/projects/marmorek-26/">מרמורק 26</a><span>{STATUS['done']}</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div class="rv"><p class="eyebrow"><span class="num">05</span> למה אנגל נדל״ן</p><h2 class="h-l">שיטת עבודה של חברת בוטיק</h2></div></div>
    <ul class="why">
      <li class="rv"><svg class="ic" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M4 28h24M8 28V10l8-6 8 6v18M13 28v-8h6v8"/></svg><b>אחריות מלאה על הביצוע</b><p>מעקב צמוד על איכות הביצוע וקבלת אחריות מלאה על הנעשה בשטח - מהיום הראשון ועד המסירה.</p></li>
      <li class="rv" data-d="1"><svg class="ic" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.3"><circle cx="16" cy="16" r="12"/><path d="M16 8v8l5 3"/></svg><b>עמידה בלוחות זמנים</b><p>הקפדה יתרה על לוחות הזמנים ועל כל פרט ופרט, בכל שלב של הפרויקט.</p></li>
      <li class="rv" data-d="2"><svg class="ic" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M3 16s5-8 13-8 13 8 13 8-5 8-13 8S3 16 3 16Z"/><circle cx="16" cy="16" r="4"/></svg><b>שקיפות בכל שלב</b><p>תמיכה, נגישות ותחושת ביטחון לדיירים, עם עדכון שוטף לאורך כל הדרך.</p></li>
      <li class="rv" data-d="3"><svg class="ic" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M16 3 5 8v8c0 7 5 11 11 13 6-2 11-6 11-13V8L16 3Z"/><path d="m11 16 3 3 7-7"/></svg><b>ביטחון כלכלי לדיירים</b><p>ליווי בנקאי, ערבויות חוק מכר לדירות החדשות, מימון דיור זמני והובלות.</p></li>
    </ul>
  </div>
</section>
''' + cta_section() + footer()

def page_projects():
    cards = "".join(card(p, d=i % 3) for i, p in enumerate(PROJECTS))
    h = head("הפרויקטים", "פרויקטי תמ״א 38 של אנגל נדל״ן בתל אביב: אוסישקין 46 ו־52, פראג 3, עובדיה מברטנורה, ברדיצ׳בסקי 17 ומרמורק 26.", "/projects/")
    return h + header("/projects/") + f'''
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">הפרויקטים</p>
    <h1 class="h-xl">בניין אחד בכל פעם, ברחובות שאנחנו מכירים.</h1>
    <p class="lead">פרויקטים של תמ״א 38 - הריסה ובנייה מחדש וחיזוק ושיפוץ - בצפון הישן ובלב העיר של תל אביב. חלק מהדירות בפרויקטים שבביצוע נמכרות ישירות מהחברה, ללא עמלת תיווך.</p>
  </div>
</section>
<section class="section--tight" style="padding-top:0">
  <div class="wrap">
    <div class="filters" role="group" aria-label="סינון לפי סטטוס">
      <button type="button" data-filter="all" aria-pressed="true">הכול</button>
      <button type="button" data-filter="active" aria-pressed="false">בביצוע</button>
      <button type="button" data-filter="permit" aria-pressed="false">היתר בנייה</button>
      <button type="button" data-filter="planning" aria-pressed="false">בתכנון</button>
      <button type="button" data-filter="done" aria-pressed="false">אוכלס</button>
    </div>
    <div class="grid grid--3">{cards}</div>
    <p class="empty" hidden>אין פרויקטים בסטטוס הזה כרגע.</p>
    <p class="note" style="margin-top:36px">ועוד פרויקטים נבחרים בתל אביב. ההדמיות להמחשה בלבד. ט.ל.ח.</p>
  </div>
</section>
''' + cta_section() + footer()

def page_project(p, i):
    prev = PROJECTS[i - 1]; nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    hero_img = p["wide"] or p["card"]
    extra = preload(hero_img, "(min-width:1320px) 1208px, 92vw")
    h = head(f"{p['title']} - {p['type']}", f"{p['title']}, {p['area']} תל אביב. {p['short']}", f"/projects/{p['slug']}/", extra)
    specs = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in p["specs"])
    loc = "".join(f'<li><span class="n">0{n+1}</span><p>{t}</p></li>' for n, t in enumerate(p["location"]))
    gallery = ""
    if p["gallery"]:
        figs = "".join(f'<figure class="{cls}">{pic(name, alt, "(min-width:1320px) 1208px, 92vw" if cls else "(min-width:760px) 45vw, 92vw")}<figcaption>{cap}</figcaption></figure>' for name, r, alt, cap, cls in p["gallery"])
        gallery = f'''<section class="section--tight"><div class="wrap"><p class="eyebrow">גלריה</p><div class="gallery">{figs}</div><p class="note" style="margin-top:14px">ההדמיות להמחשה בלבד. ט.ל.ח.</p></div></section>'''
    units = ""
    if p["units"]:
        us = "".join(f'''<div class="unit rv"><h3>{u['name']}</h3><p class="sub">{u['sub']}</p><ul>{"".join(f"<li><span>{k}</span><span>{v}</span></li>" for k, v in u['rows'])}</ul></div>''' for u in p["units"])
        units = f'''<section class="section section--stone"><div class="wrap">
  <div class="section-head"><div class="rv"><p class="eyebrow">דירות למכירה</p><h2 class="h-l">ישירות מהחברה, ללא עמלת תיווך</h2></div><a class="link more rv" href="/contact/?project={p['slug']}">לתיאום פגישה {ARROW}</a></div>
  <div class="units">{us}</div>
</div></section>'''
    return h + header("/projects/") + f'''
<section class="proj-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="פירורי לחם"><a href="/">ראשי</a><span>/</span><a href="/projects/">פרויקטים</a><span>/</span><span>{p['title']}</span></nav>
    <div class="proj-hero__media">{pic(hero_img, f"הדמיה - {p['title']}, {p['area']} תל אביב", "(min-width:1320px) 1208px, 92vw", eager=True)}</div>
    <div class="proj-hero__head">
      <div><p class="eyebrow">{p['area']} · תל אביב</p><h1 class="h-xl">{p['title']}</h1></div>
      <span class="pill" data-s="{p['status']}">{STATUS[p['status']]}</span>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">על הפרויקט</p>
        <p class="lead" style="max-width:none">{p['overview'][0]}</p>
        {"".join(f"<p>{t}</p>" for t in p['overview'][1:])}
        <p class="eyebrow" style="margin-top:40px">מיקום</p>
        <ul class="list-hair">{loc}</ul>
      </div>
      <div class="split__sticky">
        <p class="eyebrow">פרטי הפרויקט</p>
        <dl class="specs">{specs}</dl>
        <div class="actions" style="margin-top:28px"><a class="btn btn--solid" href="/contact/?project={p['slug']}">לפרטים נוספים {ARROW}</a><a class="btn btn--ghost" href="tel:{PHONE_TEL}"><span dir="ltr">{PHONE}</span></a></div>
      </div>
    </div>
  </div>
</section>
{gallery}
{units}
<section class="section--tight"><div class="wrap">
  <nav class="proj-nav" aria-label="ניווט בין פרויקטים">
    <a href="/projects/{prev['slug']}/"><small>הפרויקט הקודם</small><b>{prev['title']}</b></a>
    <a class="next" href="/projects/{nxt['slug']}/"><small>הפרויקט הבא</small><b>{nxt['title']}</b></a>
  </nav>
</div></section>
''' + cta_section() + footer()

def page_urban():
    h = head("התחדשות עירונית · תמ״א 38 בתל אביב", "איך עובד פרויקט תמ״א 38 עם אנגל נדל״ן: הריסה ובנייה מחדש (38/2) או חיזוק ושיפוץ (38/1), ליווי הדיירים, צוות היועצים ובדיקת היתכנות ללא עלות.", "/urban-renewal/")
    return h + header("/urban-renewal/") + f'''
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">התחדשות עירונית</p>
    <h1 class="h-xl">הבניין שלכם יכול להיות הבניין הבא של תל אביב.</h1>
    <p class="lead">אנגל נדל״ן מתמחה בייזום ובמימוש פרויקטים של תמ״א 38 בתל אביב - החל מהבדיקה הראשונית של עמידה בתנאי התוכנית, דרך הבדיקות המשפטיות ברשויות והתכנון על כל היבטיו, וכלה בייזום, במימון ובביצוע.</p>
    <div class="actions" style="margin-top:30px"><a class="btn btn--solid" href="#feasibility">בדיקת היתכנות ללא עלות {ARROW}</a></div>
  </div>
</section>

<section class="section section--paper" style="border-top:1px solid var(--line)">
  <div class="wrap">
    <div class="section-head"><div class="rv"><p class="eyebrow"><span class="num">01</span> שני מסלולים</p><h2 class="h-l">הריסה ובנייה מחדש, או חיזוק ושיפוץ</h2></div></div>
    <div class="tracks">
      <div class="track rv">
        <p class="track__k">תמ״א 38/2</p><h3>הריסה ובנייה מחדש</h3>
        <p>בניית בניין חדש ממרתפי החניה ועד הגג העליון. הבניין מתוכנן בעיצוב יוקרתי, במפרט עשיר ובסטנדרט בנייה גבוה.</p>
        <ul>
          <li>דירות פונקציונליות ושטופות אור, בהתאם לתקני התכנון</li>
          <li>מיקסום שטח הדירות לפי מדידות וקבלת הזכויות המקסימליות מעיריית תל אביב</li>
          <li>בנייה ירוקה השומרת על הסביבה, חוסכת בחשבונות הצריכה ומבטיחה את עמידות הבניין לאורך שנים</li>
          <li>בידוד אקוסטי בין הדירות, המרחבים הציבוריים וחוץ המבנה</li>
          <li>לובי מפואר ויוקרתי, מעלית במפרט גבוה, טלוויזיה במעגל סגור ואינטרקום</li>
          <li>חניון פונקציונלי לכלל הדירות - קונבנציונלי או רובוטי</li>
          <li>פגישת ייעוץ עם אדריכל לכל דייר, לתכנון פנים הדירה וחלוקת החדרים</li>
          <li>הסדרת התקנות והרישום בטאבו בהתאם לשינויים החדשים</li>
        </ul>
      </div>
      <div class="track rv" data-d="1">
        <p class="track__k">תמ״א 38/1</p><h3>חיזוק ושיפוץ בניין קיים</h3>
        <p>חיזוק המבנה מפני רעידות אדמה בהתאם לתקנים המחמירים ביותר, יחד עם שדרוג מקיף של הבניין ושל הדירות.</p>
        <ul>
          <li>הגדלת שטח הדירות בתוספות בנייה: מרפסות שמש, ממ״ד ושטחים נוספים</li>
          <li>הוספת מעלית</li>
          <li>שדרוג הלובי וחדר המדרגות</li>
          <li>שיפוץ חיצוני ברמת גימור גבוהה ושדרוג מעטפת הבניין</li>
          <li>החלפת התשתיות החיצוניות: ביוב, חשמל, מים וגז</li>
          <li>שבילי גישה וגינה מעוצבת הכוללת מערכות השקיה מתקדמות</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--wide">
      <div class="rv"><p class="eyebrow"><span class="num">02</span> ליווי הדיירים</p><p class="statement">במהלך כל הפרויקט, הדיירים מקבלים <span class="em">תמיכה, ביטחון ושקיפות</span> - ועדכון בכל שלב ושלב.</p></div>
      <div class="rv" data-d="1">
        <ul class="list-hair">
          <li><span class="n">01</span><div><b>מימון דיור זמני</b><p>אנו מעניקים מימון לדיור זמני לאורך תקופת הבנייה.</p></div></li>
          <li><span class="n">02</span><div><b>ערבויות חוק מכר</b><p>ערבויות לדירות החדשות שייבנו, לביטחון מלא של הדיירים.</p></div></li>
          <li><span class="n">03</span><div><b>הובלות</b><p>הליווי כולל גם את הובלת תכולת הדירות.</p></div></li>
          <li><span class="n">04</span><div><b>פגישת תכנון עם אדריכל</b><p>כל דייר מקבל פגישת ייעוץ אישית לתכנון פנים הדירה וחלוקת החדרים.</p></div></li>
          <li><span class="n">05</span><div><b>מפרט גבוה, מקיף ויוקרתי</b><p>אנו מציעים לדיירים מפרט גבוה, ומסכמים מול הדיירים את פרטי הפרויקט, רמת הגימור והתכנון ההנדסי־אדריכלי.</p></div></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--dark grain">
  <div class="wrap">
    <div class="section-head"><div class="rv"><p class="eyebrow"><span class="num">03</span> התהליך</p><h2 class="h-l">מבדיקה ראשונית ועד רישום בטאבו</h2></div></div>
    <ol class="steps rv">
      <li><b>בדיקת היתכנות</b><p>בדיקה ראשונית של עמידת הבניין בתנאי התוכנית והיתכנות כלכלית - ללא כל עלות.</p></li>
      <li><b>בדיקות ותכנון</b><p>בדיקות משפטיות ברשויות, תכנון הנדסי ואדריכלי ומינוי צוות היועצים.</p></li>
      <li><b>הסכמות דיירים</b><p>ליווי הדיירים וסיכום פרטי הפרויקט: המפרט, רמת הגימור והתכנון שניתן ליישם.</p></li>
      <li><b>מימון וביצוע</b><p>ליווי בנקאי, ערבויות חוק מכר ומימון דיור זמני - וביצוע במעקב צמוד על האיכות ועל לוחות הזמנים.</p></li>
      <li><b>מסירה ורישום</b><p>מסירת הדירות החדשות והסדרת התקנות והרישום בטאבו.</p></li>
    </ol>
    <div class="rv" style="margin-top:clamp(40px,5vw,72px)">
      <p class="eyebrow">צוות היועצים בכל פרויקט</p>
      <ul class="tags"><li>אדריכל</li><li>מהנדס קונסטרוקציה</li><li>אינסטלציה</li><li>חשמל</li><li>בטיחות</li><li>מעליות</li><li>הידרולוג</li><li>יועץ נגישות</li><li>יועץ הג״א</li><li>יועץ אקוסטיקה</li><li>יועץ בנייה ירוקה</li><li>יועץ קרקע וביסוס</li><li>יועץ תנועה</li><li>אגרונום</li><li>יועץ מס</li></ul>
    </div>
  </div>
</section>

<section class="section" id="feasibility">
  <div class="wrap">
    <div class="split">
      <div class="split__sticky">
        <p class="eyebrow"><span class="num">04</span> בדיקת היתכנות</p>
        <h2 class="h-l">השאירו פרטים על הבניין שלכם</h2>
        <p class="lead" style="margin-top:20px">נציג החברה ייצור עמכם קשר לקבלת פרטים ראשוניים. צוות המומחים שלנו יבחן את הבניין ויחזור אליכם עם תשובה מפורטת האם קיימת היתכנות כלכלית לפרויקט - ללא כל עלות.</p>
        <p class="note">מעדיפים לדבר? <a href="tel:{PHONE_TEL}" dir="ltr" style="font-weight:600">{PHONE}</a></p>
      </div>
      <div>{form("feasibility")}</div>
    </div>
  </div>
</section>
''' + footer()

def page_about():
    h = head("אודות", "אנגל נדל״ן היא חברת בוטיק משפחתית לבנייה ולייזום, הפועלת רק בתל אביב ומנהלת פרויקטים של תמ״א 38 מראשיתם ועד השלמתם.", "/about/")
    return h + header("/about/") + f'''
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">אודות</p>
    <h1 class="h-xl">חברת בוטיק משפחתית שבונה מחדש את תל אביב.</h1>
    <p class="lead">אנגל נדל״ן עוסקת בבנייה ובייזום מזה שנים, ומורכבת מאנשי מקצוע איכותיים בתחומי הנדל״ן והבנייה: מהנדסים, אדריכלים, מנהלי פרויקטים, כלכלנים, עורכי דין ומנהלי שיווק.</p>
  </div>
</section>
<section class="section--tight" style="padding-top:0">
  <div class="wrap"><figure class="fig" style="aspect-ratio:21/9">{pic("berdichevsky-wide", "הדמיית ברדיצ׳בסקי 17 - בניין בוטיק פינתי בלב תל אביב", "(min-width:1320px) 1208px, 92vw", eager=True)}<figcaption>ברדיצ׳בסקי 17 · תמ״א 38/1 · אוכלס</figcaption></figure></div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--wide">
      <div class="rv"><p class="eyebrow"><span class="num">01</span> מי אנחנו</p><p class="statement">הניסיון המגוון של הצוות המוביל הוא <span class="em">יתרון איכותי</span> בענף - ואנחנו מביאים אותו לכל בניין.</p></div>
      <div class="rv" data-d="1">
        <p>חברתנו מנוסה בניהול כלל ההיבטים הכרוכים בכל פרויקט, מראשיתו ועד השלמתו: החל משלב התכנון ההנדסי, דרך שלבי המימון, המיסוי והליווי המשפטי, השיווק והמכירות - וכלה בניהול ובביצוע.</p>
        <p>שיטת העבודה הייחודית שלנו מבטיחה מעקב צמוד על איכות הביצוע, קבלת אחריות מלאה על הנעשה בשטח והקפדה יתרה על עמידה בלוחות הזמנים ועל כל פרט ופרט. כך אנחנו מבצעים מגוון פרויקטים בסטנדרטים הגבוהים ביותר בעיר תל אביב.</p>
        <p>אנגל נדל״ן פועלת רק בעיר תל אביב, ונבחרה כשותף אמין על ידי עשרות לקוחות מתל אביב למימוש פרויקטים בתחום התמ״א.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--dark grain">
  <div class="wrap">
    <div class="section-head"><div class="rv"><p class="eyebrow"><span class="num">02</span> הערכים שלנו</p><h2 class="h-l">מה שמנחה אותנו בכל פרויקט</h2></div></div>
    <ul class="list-hair rv">
      <li><span class="n">01</span><div><b>עיר אחת, התמחות אחת</b><p>אנגל נדל״ן פועלת רק בעיר תל אביב, ונבחרה כשותף אמין על ידי עשרות לקוחות מהעיר למימוש פרויקטים בתחום התמ״א.</p></div></li>
      <li><span class="n">02</span><div><b>אחריות מלאה</b><p>מהתכנון ועד המפתח, האחריות על הנעשה בשטח היא שלנו - עם מעקב צמוד על איכות הביצוע ועל לוחות הזמנים.</p></div></li>
      <li><span class="n">03</span><div><b>שקיפות ונגישות</b><p>הדיירים מקבלים תמיכה, תחושת ביטחון ועדכון שוטף בכל שלב ושלב של הפרויקט.</p></div></li>
      <li><span class="n">04</span><div><b>סטנדרט של בוטיק</b><p>מפרט גבוה, מקיף ויוקרתי, בנייני בוטיק, ופגישת ייעוץ אישית עם אדריכל לכל דייר לתכנון פנים הדירה.</p></div></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <figure class="fig rv" style="aspect-ratio:3/2">{pic("interior-living", "הדמיית סלון בדירה חדשה", "(min-width:900px) 45vw, 92vw")}<figcaption>הדמיה · דירה חדשה בסטנדרט בוטיק</figcaption></figure>
      <div class="rv" data-d="1">
        <p class="eyebrow"><span class="num">03</span> הצוות</p>
        <h2 class="h-m">אנשי מקצוע איכותיים בתחומי הנדל״ן והבנייה</h2>
        <p style="margin-top:18px">בכל פרויקט אנחנו ממנים יועצים מובילים בתחומם - אדריכל, מהנדס קונסטרוקציה, יועצי אינסטלציה, חשמל, בטיחות, מעליות, אקוסטיקה, בנייה ירוקה, קרקע וביסוס, תנועה, נגישות והג״א, הידרולוג, אגרונום ויועץ מס - וכל יועץ נוסף שיידרש.</p>
        <ul class="tags" style="margin:22px 0 30px"><li>מהנדסים</li><li>אדריכלים</li><li>מנהלי פרויקטים</li><li>כלכלנים</li><li>עורכי דין</li><li>מנהלי שיווק</li></ul>
        <div class="actions"><a class="btn btn--solid" href="/projects/">לפרויקטים שלנו {ARROW}</a><a class="btn btn--ghost" href="/contact/">דברו איתנו</a></div>
      </div>
    </div>
  </div>
</section>
''' + cta_section() + footer()

def page_contact():
    h = head("צור קשר", "מעוניינים בפרויקט התחדשות עירונית לבניין שלכם או ברכישת דירה ישירות מהחברה? השאירו פרטים או התקשרו: 03-6005955.", "/contact/")
    return h + header("/contact/") + f'''
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">צור קשר</p>
    <h1 class="h-xl">צרו איתנו קשר</h1>
    <p class="lead">מעוניינים בביצוע פרויקט התחדשות עירונית, או ברכישת דירה ישירות מהחברה וללא עמלת תיווך? השאירו פרטים ואנו נחזור אליכם בהקדם.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="split">
      <div>
        <ul class="contact-list">
          <li><small>טלפון המשרד</small><a class="ltr" href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><small>דוא״ל</small><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><small>פקס</small><span class="ltr">{FAX}</span></li>
          <li><small>כתובת</small><span>{ADDRESS}</span></li>
        </ul>
        <p class="note" style="margin-top:28px">אנגל נדל״ן פועלת בתל אביב בלבד.</p>
      </div>
      <div>{form("contact")}</div>
    </div>
  </div>
</section>
''' + footer()

TERMS = [
 ("כללי", ["השימוש באתר מהווה הסכמה מצד המשתמש לכל תנאי השימוש, לרבות מדיניות הפרטיות.", "החברה שומרת לעצמה את הזכות לעדכן ולשנות את תנאי השימוש בכל עת, ולמשתמש לא תהיה כל טענה או דרישה בגין שינויים אלה."]),
 ("שימוש באתר", ["האתר מספק מידע ושירותים הקשורים לנדל״ן, ובפרט לפרויקטים של התחדשות עירונית.", "המשתמש מתחייב לעשות שימוש הוגן, חוקי וסביר באתר ולא לבצע כל פעולה שעלולה לפגוע בפעילות האתר או במשתמשים אחרים.", "החברה רשאית למנוע גישה לאתר לכל משתמש שיפר תנאים אלה או יבצע שימוש בלתי ראוי באתר."]),
 ("תוכן ומידע באתר", ["התכנים באתר ניתנים כמידע כללי בלבד ואינם מהווים ייעוץ משפטי, פיננסי או נדל״ני.", "החברה אינה מתחייבת לכך שהתוכן באתר יהיה מדויק, שלם או עדכני.", "כל הסתמכות על התכנים המופיעים באתר נעשית באחריותו הבלעדית של המשתמש."]),
 ("קישורים לאתרים חיצוניים", ["האתר עשוי לכלול קישורים לאתרים חיצוניים שאינם בשליטת החברה.", "החברה אינה אחראית לתוכן, למדיניות הפרטיות או לנכונות המידע המצוי באתרים חיצוניים אלה."]),
 ("פרטיות ואבטחת מידע", ["החברה מתחייבת לשמור על פרטיות המשתמשים בהתאם למדיניות הפרטיות שלה.", "המשתמש מסכים לכך שהחברה תעשה שימוש במידע אישי שהוא מוסר בהתאם למדיניות הפרטיות.", "למרות מאמצי החברה לאבטח את האתר, אין החברה יכולה להבטיח הגנה מוחלטת מפני חדירות בלתי מורשות."]),
 ("קניין רוחני", ["כל זכויות הקניין הרוחני באתר, לרבות טקסטים, תמונות, עיצוב, קוד תוכנה וסימני מסחר, שייכות לחברה או לצדדים שלישיים שהעניקו לה רישיון שימוש.", "אין להעתיק, לשכפל, להפיץ, לשדר או לפרסם את תכני האתר ללא אישור מראש ובכתב מהחברה."]),
 ("אחריות והגבלת אחריות", ["השימוש באתר נעשה באחריות המשתמש בלבד.", "החברה אינה אחראית לכל נזק ישיר או עקיף שייגרם כתוצאה משימוש או הסתמכות על המידע והשירותים באתר.", "החברה אינה מתחייבת שהאתר יהיה פעיל בכל עת ללא הפרעות או תקלות טכניות."]),
 ("שיפוי", ["המשתמש מתחייב לשפות את החברה בגין כל נזק, הפסד או הוצאה שייגרמו לה עקב הפרת תנאים אלה על ידי המשתמש."]),
 ("הדין החל וסמכות שיפוט", ["על השימוש באתר יחולו אך ורק דיני מדינת ישראל.", "סמכות השיפוט הבלעדית בכל הנוגע לתנאים אלה ולשימוש באתר תהיה לבתי המשפט המוסמכים בתל אביב־יפו."]),
]

def page_terms():
    h = head("תנאי שימוש", "תנאי השימוש באתר אנגל נדל״ן.", "/terms/")
    body = "".join(f"<h2>{i+1}. {t}</h2>" + "".join(f"<p>{i+1}.{j+1}. {s}</p>" for j, s in enumerate(ps)) for i, (t, ps) in enumerate(TERMS))
    return h + header("") + f'''
<section class="page-head"><div class="wrap"><p class="eyebrow">משפטי</p><h1 class="h-xl">תנאי שימוש</h1><p class="lead">ברוכים הבאים לאתר אנגל נדל״ן (להלן: ״האתר״). השימוש באתר כפוף לתנאים ולהוראות המפורטים להלן. אנא קראו תנאים אלה בעיון, שכן השימוש באתר מעיד על הסכמתכם להם.</p></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="prose">{body}<p style="margin-top:2em">לשאלות בנוגע לתנאי השימוש ניתן לפנות אלינו בכתובת <a href="mailto:{EMAIL}" style="font-weight:600">{EMAIL}</a>.</p></div></div></section>
''' + footer()

def page_privacy():
    h = head("מדיניות פרטיות", "מדיניות הפרטיות של אתר אנגל נדל״ן.", "/privacy/")
    return h + header("") + f'''
<section class="page-head"><div class="wrap"><p class="eyebrow">משפטי</p><h1 class="h-xl">מדיניות פרטיות</h1><p class="lead">אנו מחויבים לשמור על פרטיות המשתמשים ולנהל את המידע האישי בהתאם להוראות הדין. מדיניות זו מפרטת כיצד אנו אוספים, משתמשים ושומרים על המידע שלכם בעת השימוש באתר.</p></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="prose">
<h2>איסוף מידע</h2>
<p>אנו עשויים לאסוף מידע אישי שאתם מוסרים לנו, כולל אך לא רק: שם מלא, כתובת דוא״ל, מספר טלפון ומידע שנשלח דרך טפסים באתר.</p>
<p>בנוסף, אנו עשויים לאסוף מידע טכני בעת השימוש באתר, כגון כתובת IP, סוג הדפדפן ומערכת ההפעלה, וזמני גישה ופעילות באתר.</p>
<h2>שימוש במידע</h2>
<ul><li>אספקת שירותים ומענה לפניות המשתמשים.</li><li>שליחת עדכונים, מידע פרסומי והודעות חשובות (בכפוף להסכמת המשתמש).</li><li>שיפור חוויית המשתמש והתאמת האתר לצרכים האישיים.</li><li>עמידה בהוראות החוק ורשויות האכיפה במקרה הצורך.</li></ul>
<h2>מסירת מידע לצדדים שלישיים</h2>
<p>אנו לא נמסור מידע אישי לצדדים שלישיים, למעט במקרים הבאים:</p>
<ul><li>כאשר הדבר נדרש לצורך אספקת השירותים או ניהול האתר (כגון ספקי אחסון וניתוח נתונים).</li><li>על פי דרישת רשות מוסמכת או על פי הוראות החוק.</li><li>במקרה של מיזוג, רכישה או העברת פעילות האתר לצד שלישי.</li></ul>
<h2>אבטחת מידע</h2>
<p>אנו נוקטים באמצעים טכנולוגיים וארגוניים מתאימים כדי להגן על המידע האישי של המשתמשים מפני גישה בלתי מורשית, שינוי, חשיפה או השמדה. למרות מאמצינו, אין אנו יכולים להבטיח אבטחה מוחלטת של הנתונים, והשימוש באתר הוא על אחריות המשתמש.</p>
<h2>עוגיות (Cookies) וטכנולוגיות מעקב</h2>
<p>אנו עשויים להשתמש בעוגיות ובטכנולוגיות דומות כדי לשפר את חוויית המשתמש, לנתח את השימוש באתר ולהתאים תכנים ופרסומות. ניתן לנהל את העדפות העוגיות באמצעות הגדרות הדפדפן ולחסום אותן, אך הדבר עלול להשפיע על חוויית השימוש באתר.</p>
<h2>זכויות המשתמש</h2>
<p>המשתמש רשאי לבקש לעיין, לתקן או למחוק את המידע האישי שנאסף עליו, בהתאם להוראות החוק. לבקשות בנושא פרטיות ניתן לפנות אלינו בכתובת <a href="mailto:{EMAIL}" style="font-weight:600">{EMAIL}</a>.</p>
<h2>שינויים במדיניות הפרטיות</h2>
<p>החברה רשאית לעדכן מדיניות זו מעת לעת. עדכונים מהותיים יפורסמו באתר, והמשך השימוש באתר לאחר עדכון המדיניות מהווה הסכמה לתנאים החדשים.</p>
</div></div></section>
''' + footer()

def page_accessibility():
    h = head("הצהרת נגישות", "הצהרת הנגישות של אתר אנגל נדל״ן: התאמות הנגישות שבוצעו, תפריט הנגישות ודרכי פנייה.", "/accessibility/")
    return h + header("") + f'''
<section class="page-head"><div class="wrap"><p class="eyebrow">נגישות</p><h1 class="h-xl">הצהרת נגישות</h1><p class="lead">אנו באנגל נדל״ן משקיעים ככל שניתן על מנת לספק לכל לקוחותינו שירות שוויוני ונגיש, בכדי לאפשר חוויית גלישה נוחה לכלל האוכלוסייה, לרבות אנשים עם מוגבלויות, בהתאם לחוק שוויון זכויות לאנשים עם מוגבלות.</p></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="prose">
<p>באתר זה בוצעו התאמות נגישות על פי דרישות תקנות שוויון זכויות לאנשים עם מוגבלות (התאמות נגישות לשירות), התשע״ג-2013, בצורה קפדנית ככל שניתן.</p>
<p>התאמות הנגישות בוצעו על פי המלצות התקן הישראלי (ת״י 5568) לנגישות תכנים באינטרנט ברמת AA ומסמך WCAG 2.0 הבינלאומי.</p>
<h2>מידע על נגישות האתר</h2>
<p>באתר מוטמע תפריט נגישות, הנפתח באמצעות כפתור הנגישות בתחתית המסך. התפריט כולל:</p>
<ul><li>הגדלת טקסט והקטנת טקסט</li><li>גווני אפור</li><li>ניגודיות גבוהה וניגודיות הפוכה</li><li>רקע בהיר</li><li>הדגשת קישורים</li><li>פונט קריא</li><li>איפוס ההגדרות</li></ul>
<p>בנוסף, האתר נבנה עם מבנה כותרות תקין, ניווט מלא באמצעות מקלדת, טקסט חלופי לתמונות, תמיכה בהעדפת הפחתת תנועה (Reduced Motion) ותגיות ARIA בתפריטים ובטפסים.</p>
<h2>פנייה בנושא נגישות</h2>
<p>אנו ממשיכים לפעול במאמץ לשפר את נגישות האתר כחלק ממחויבותנו לאפשר לכלל האוכלוסייה לקבל שירות שווה והוגן. במידה ונתקלתם בבעיה כלשהי בנושא הנגישות, נשמח שתעדכנו אותנו ואנו נעשה כל מאמץ למצוא עבורכם פתרון מתאים ולטפל בבעיה בהקדם האפשרי.</p>
<p>טלפון: <a href="tel:{PHONE_TEL}" dir="ltr" style="font-weight:600">{PHONE}</a><br>דוא״ל: <a href="mailto:{EMAIL}" style="font-weight:600">{EMAIL}</a></p>
<h2>פרסום הצהרת הנגישות</h2>
<p>הצהרת הנגישות עודכנה ביום 23.09.2026.</p>
</div></div></section>
''' + footer()

def page_404():
    h = head("הדף לא נמצא", "הדף שחיפשתם אינו קיים.", "/404.html")
    return h + header("") + f'''
<section class="page-head" style="min-height:50vh"><div class="wrap"><p class="eyebrow">404</p><h1 class="h-xl">הדף הזה עדיין לא נבנה.</h1><p class="lead">הדף שחיפשתם אינו קיים או שהועבר. אפשר לחזור לדף הבית או לעבור לפרויקטים.</p><div class="actions" style="margin-top:28px"><a class="btn btn--solid" href="/">לדף הבית {ARROW}</a><a class="btn btn--ghost" href="/projects/">הפרויקטים</a></div></div></section>
''' + footer()

FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" fill="#1a1917"/><g fill="none" stroke="#f4f1ea" stroke-width="2"><path d="M6 33V17h8v16"/><path d="M16 33V7h9v26"/><path d="M27 33V13h7v20"/></g></svg>'''

HEADERS = '''/*
  X-Robots-Tag: noindex
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN

/assets/*
  Cache-Control: public, max-age=31536000, immutable
'''

if __name__ == "__main__":
    write("/", page_home())
    write("/projects/", page_projects())
    for i, p in enumerate(PROJECTS): write(f"/projects/{p['slug']}/", page_project(p, i))
    write("/urban-renewal/", page_urban())
    write("/about/", page_about())
    write("/contact/", page_contact())
    write("/terms/", page_terms())
    write("/privacy/", page_privacy())
    write("/accessibility/", page_accessibility())
    write("404.html", page_404())
    write("_headers", HEADERS if PREVIEW else HEADERS.replace("  X-Robots-Tag: noindex\n", ""))
    write("robots.txt", "User-agent: *\nDisallow: /\n" if PREVIEW else f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
