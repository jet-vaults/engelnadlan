# -*- coding: utf-8 -*-
"""Static site generator for engelnadlan.co.il (Hebrew at /, English at /en/).

    python tools/build.py

All copy lives in this file: the T dictionary (per-language UI strings), C (page copy),
PROJECTS (per-project data with he/en fields), TERMS / PRIVACY / A11Y (legal pages).
Assets under wwwroot/assets are authored directly and are not touched by the build.
"""
import os, html
from PIL import Image

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "wwwroot")
IMG = os.path.join(OUT, "assets", "img")

# ---------------------------------------------------------------- settings
SITE_URL = "https://engelnadlan.co.il"
PREVIEW = False                     # True => noindex + robots Disallow (preview); False => indexable + canonical + sitemap
WEB3FORMS_KEY = "YOUR-WEB3FORMS-ACCESS-KEY"   # replace to activate the contact forms
PHONE = "03-6005955"
PHONE_TEL = "+97236005955"
FAX = "03-6005999"
EMAIL = "office@engelnadlan.co.il"
YEAR = "2026"
A11Y_DATE = "23.09.2026"

LANGS = {
    "he": dict(dir="rtl", prefix="", other="en", locale="he_IL", site="אנגל נדל״ן", address="מרמורק 26, תל אביב"),
    "en": dict(dir="ltr", prefix="/en", other="he", locale="en_US", site="Engel Real Estate", address="26 Marmorek St., Tel Aviv"),
}

STATUS = {
    "he": {"active": "בביצוע", "permit": "בהיתר בנייה · לקראת ביצוע", "planning": "לאחר החלטת ועדה · לקראת היתר", "done": "אוכלס"},
    "en": {"active": "Under construction", "permit": "Building permit · pre-construction", "planning": "Committee approved · pending permit", "done": "Completed & occupied"},
}

# ---------------------------------------------------------------- UI strings
T = {
 "he": dict(
  nav=[("/projects/","פרויקטים"),("/urban-renewal/","התחדשות עירונית"),("/about/","אודות"),("/contact/","צור קשר")],
  skip="דילוג לתוכן", menu="תפריט", nav_label="ניווט ראשי", feas="בדיקת היתכנות", lang="EN", lang_label="English",
  tagline="חברת בוטיק משפחתית לייזום וביצוע פרויקטים של תמ״א 38 - בתל אביב בלבד.",
  f_nav="ניווט", f_contact="יצירת קשר", f_info="מידע", fax="פקס", terms="תנאי שימוש", privacy="מדיניות פרטיות",
  a11y="הצהרת נגישות", forsale="דירות למכירה",
  copyright="© {y} כל הזכויות שמורות לאנגל נדל״ן", disclaimer="התמונות והדמיות להמחשה בלבד. ט.ל.ח",
  credit="זכויות העיצוב שמורות ל", credit_name="איינשטיין אתרים",
  tlv="תל אביב", crumbs_home="ראשי", crumbs_projects="פרויקטים",
  f_name="שם מלא", f_phone="טלפון", f_email="דוא״ל", f_building="כתובת הבניין", f_building_ph="רחוב ומספר, תל אביב",
  f_interest="מה מעניין אתכם?", f_opt1="בדיקת היתכנות להתחדשות עירונית בבניין שלי", f_opt2="רכישת דירה ישירות מהחברה", f_opt3="אחר",
  f_msg="הודעה", f_msg_ph="ספרו לנו בקצרה על הבניין, מספר הדירות והדיירים, או כל שאלה אחרת",
  f_send="שליחה", f_note="הפרטים ישמשו למענה לפנייתכם בלבד.", f_subject="פנייה מהאתר - אנגל נדל״ן",
  cta_eyebrow="נתחיל בשיחה", cta_h="רוצים לבדוק היתכנות להתחדשות עירונית בבניין שלכם?",
  cta_p="השאירו פרטים וצוות המומחים שלנו יבחן את הבניין ויחזור אליכם עם תשובה מפורטת האם קיימת היתכנות כלכלית לפרויקט - ללא כל עלות.",
  cta_btn="השאירו פרטים", cta_btn2="דירות למכירה", cta_or="או פשוט התקשרו",
  card_alt="הדמיה - {t}, תל אביב",
 ),
 "en": dict(
  nav=[("/projects/","Projects"),("/urban-renewal/","Urban Renewal"),("/about/","About"),("/contact/","Contact")],
  skip="Skip to content", menu="Menu", nav_label="Main navigation", feas="Feasibility check", lang="עב", lang_label="עברית",
  tagline="A family-run boutique developer of TAMA 38 projects - in Tel Aviv only.",
  f_nav="Navigation", f_contact="Contact", f_info="Information", fax="Fax", terms="Terms of Use", privacy="Privacy Policy",
  a11y="Accessibility Statement", forsale="Apartments for sale",
  copyright="© {y} Engel Real Estate. All rights reserved.", disclaimer="Images and renderings are for illustration only. E&OE",
  credit="Design by ", credit_name="Einstein Web",
  tlv="Tel Aviv", crumbs_home="Home", crumbs_projects="Projects",
  f_name="Full name", f_phone="Phone", f_email="Email", f_building="Building address", f_building_ph="Street and number, Tel Aviv",
  f_interest="What are you interested in?", f_opt1="A feasibility check for urban renewal in my building", f_opt2="Buying an apartment directly from the developer", f_opt3="Other",
  f_msg="Message", f_msg_ph="Tell us briefly about the building, the number of apartments and owners, or anything else",
  f_send="Send", f_note="Your details are used only to respond to your enquiry.", f_subject="Website enquiry - Engel Real Estate",
  cta_eyebrow="Let's talk", cta_h="Want to check whether your building qualifies for urban renewal?",
  cta_p="Leave your details and our team of experts will assess the building and come back to you with a detailed answer on whether the project is economically feasible - at no cost.",
  cta_btn="Leave your details", cta_btn2="Apartments for sale", cta_or="Or simply call",
  card_alt="Rendering - {t}, Tel Aviv",
 ),
}

# ---------------------------------------------------------------- projects
def L2(he, en): return {"he": he, "en": en}

PROJECTS = [
  dict(slug="ussishkin-46", status="active", card="ussishkin-46-card", wide="ussishkin-46-wide",
       title=L2("אוסישקין 46", "Ussishkin 46"), area=L2("הצפון הישן", "The Old North"),
       type=L2("תמ״א 38/2 · הריסה ובנייה מחדש", "TAMA 38/2 · demolition & rebuild"),
       short=L2("קו ראשון לפארק הירקון, עם נוף למפגש נחל הירקון והים התיכון.", "First line to Yarkon Park, overlooking the meeting of the Yarkon River and the Mediterranean."),
       overview=L2([
         "פרויקט תמ״א 38/2 של הריסה ובנייה מחדש, בקו ראשון לפארק הירקון. הבניין החדש נהנה מנוף מרהיב על מפגש הימים של נחל הירקון והים התיכון, ומרפסת וחניה לכל דירה.",
         "הבניין מוגבה כ-1.5 מטר מעל גובה הרחוב לקבלת אור, אוויר ונוף, ומתוכנן עם לובאים בסטנדרט גבוה. הפרויקט נמצא כיום בביצוע בליווי בנקאי של בנק הפועלים.",
       ],[
         "A TAMA 38/2 demolition-and-rebuild project on the first line to Yarkon Park. The new building enjoys a spectacular view of the meeting of the Yarkon River and the blue Mediterranean, with a balcony and parking for every apartment.",
         "The building is raised about 1.5 m above street level for light, air and views, and is designed with high-specification lobbies. The project is currently under construction with bank financing from Bank Hapoalim.",
       ]),
       specs=L2([("סוג הפרויקט","תמ״א 38/2 · הריסה ובנייה מחדש"),("סטטוס","בביצוע"),("ליווי בנקאי","בנק הפועלים"),("מיקום","רובע 3, הצפון הישן, תל אביב"),("לכל דירה","מרפסת וחניה"),("מפרט","לובאים בסטנדרט גבוה · הבניין מוגבה כ-1.5 מ׳ מעל הרחוב")],
               [("Project type","TAMA 38/2 · demolition & rebuild"),("Status","Under construction"),("Bank financing","Bank Hapoalim"),("Location","District 3, the Old North, Tel Aviv"),("Every apartment","Balcony and parking"),("Specification","High-spec lobbies · building raised ~1.5 m above the street")]),
       location=L2(["קו ראשון לפארק הירקון, עם נוף לים","רובע 3 - הצפון הישן של תל אביב","בקרבת הים, נמל תל אביב, בתי קפה ומסעדות"],
                   ["First line to Yarkon Park, with sea views","District 3 - Tel Aviv's Old North","Close to the sea, Tel Aviv Port, cafés and restaurants"]),
       gallery=[("ussishkin-46-roof", L2("הדמיית קומת הגג","Rendering of the roof level"), L2("הדמיה · קומת הגג ונוף העיר","Rendering · roof level and city view"), "span"),
                ("ussishkin-46-living", L2("הדמיית סלון עם נוף לים","Rendering of a living room with sea view"), L2("הדמיה · סלון","Rendering · living room"), ""),
                ("ussishkin-46-kitchen", L2("הדמיית מטבח","Rendering of a kitchen"), L2("הדמיה · מטבח","Rendering · kitchen"), ""),
                ("ussishkin-46-bedroom", L2("הדמיית חדר שינה","Rendering of a bedroom"), L2("הדמיה · חדר שינה","Rendering · bedroom"), ""),
                ("yarkon-panorama", L2("נוף פנורמי לפארק הירקון ולים","Panoramic view of Yarkon Park and the sea"), L2("הנוף מגובה הדירות · פארק הירקון והים","The view from apartment height · Yarkon Park and the sea"), "span")],
       units=[dict(name=L2("מיני פנטהאוז","Mini penthouse"), sub=L2("דירת 4/5 חדרים · קומה 5","4/5-room apartment · 5th floor"),
                   rows=L2([("שטח עיקרי","126 מ״ר"),("מרפסת צפונית","24 מ״ר"),("כיווני אוויר","3"),("חזית","מלוא חזית הבניין לפארק ולים"),("תכנון","5 חדרים או 4 חדרים")],
                           [("Main area","126 sqm"),("North balcony","24 sqm"),("Exposures","3"),("Frontage","Full building frontage to the park and sea"),("Layout","5 rooms or 4 rooms")]))],
       plans=[("ussishkin-46-plan-5r", L2("תכנון 5 חדרים","5-room layout")), ("ussishkin-46-plan-4r", L2("תכנון 4 חדרים","4-room layout"))],
       plan_pdf="/assets/files/ussishkin-46-plan.pdf",
       extras=[dict(title=L2("עיצוב הלובאים בסטנדרט גבוה","Lobby design at a high standard"),
                    imgs=[("ussishkin-46-lobby-1", L2("קונספט עיצוב הלובי - אוסישקין 46","Lobby design concept - Ussishkin 46")),
                          ("ussishkin-46-lobby-2", L2("לוח חומרים לעיצוב הלובי","Lobby materials board")),
                          ("ussishkin-46-lobby-3", L2("פרטי גמר וחומרים ללובי","Lobby finishes and materials")) ])],
  ),
  dict(slug="prague-3", status="active", card="prague-3-card", wide="prague-3-wide",
       title=L2("פראג 3", "Prague 3"), area=L2("הצפון הישן", "The Old North"),
       type=L2("תמ״א 38/2 · הריסה ובנייה מחדש", "TAMA 38/2 · demolition & rebuild"),
       short=L2("רחוב שקט בין דיזנגוף לבן-יהודה, חמש דקות הליכה לחוף הילטון.", "A quiet street between Dizengoff and Ben Yehuda, a five-minute walk to Hilton Beach."),
       overview=L2([
         "בניין בוטיק חדש ברחוב שקט בין דיזנגוף לבן-יהודה, במרחק חמש דקות הליכה מחוף הילטון. הפרויקט מוקם במסגרת תמ״א 38/2 - הריסה ובנייה מחדש - ומיועד ל-12 דיירים בלבד.",
         "לכל הדירות מרפסות וחניות. הפרויקט נמצא בביצוע בליווי בנקאי של חברת כלל.",
       ],[
         "A new boutique building on a quiet street between Dizengoff and Ben Yehuda, a five-minute walk from Hilton Beach. The project is built under TAMA 38/2 - demolition and rebuild - for only 12 residents.",
         "All apartments have balconies and parking. The project is under construction with bank financing from Clal.",
       ]),
       specs=L2([("סוג הפרויקט","תמ״א 38/2 · הריסה ובנייה מחדש"),("סטטוס","בביצוע"),("ליווי בנקאי","כלל"),("מיקום","הצפון הישן, תל אביב"),("היקף","בניין בוטיק · 12 דיירים בלבד"),("לכל דירה","מרפסת וחניה")],
               [("Project type","TAMA 38/2 · demolition & rebuild"),("Status","Under construction"),("Bank financing","Clal"),("Location","The Old North, Tel Aviv"),("Scale","Boutique building · only 12 residents"),("Every apartment","Balcony and parking")]),
       location=L2(["רחוב שקט בין דיזנגוף לבן-יהודה","5 דקות הליכה לחוף הילטון"],["A quiet street between Dizengoff and Ben Yehuda","5-minute walk to Hilton Beach"]),
       gallery=[], units=[],
  ),
  dict(slug="ussishkin-52", status="permit", card="ussishkin-52-card", wide="ussishkin-52-wide",
       title=L2("אוסישקין 52", "Ussishkin 52"), area=L2("הצפון הישן", "The Old North"),
       type=L2("תמ״א 38/2 · הריסה ובנייה מחדש", "TAMA 38/2 · demolition & rebuild"),
       short=L2("קו ראשון לפארק הירקון. בהיתר בנייה ולקראת תחילת ביצוע.", "First line to Yarkon Park. Building permit granted, construction starting soon."),
       overview=L2([
         "פרויקט תמ״א 38/2 של הריסה ובנייה מחדש בקו ראשון לפארק הירקון, עם נוף על מפגש נחל הירקון והים התיכון. מרפסת וחניה לכל דירה.",
         "הפרויקט קיבל היתר בנייה ונמצא לקראת תחילת ביצוע.",
       ],[
         "A TAMA 38/2 demolition-and-rebuild project on the first line to Yarkon Park, overlooking the meeting of the Yarkon River and the Mediterranean. Balcony and parking for every apartment.",
         "The project has received its building permit and is about to start construction.",
       ]),
       specs=L2([("סוג הפרויקט","תמ״א 38/2 · הריסה ובנייה מחדש"),("סטטוס","היתר בנייה · לקראת ביצוע"),("מיקום","הצפון הישן, תל אביב"),("לכל דירה","מרפסת וחניה")],
               [("Project type","TAMA 38/2 · demolition & rebuild"),("Status","Building permit · pre-construction"),("Location","The Old North, Tel Aviv"),("Every apartment","Balcony and parking")]),
       location=L2(["קו ראשון לפארק הירקון","9 דקות הליכה לחוף הים","5 דקות הליכה לנמל תל אביב"],["First line to Yarkon Park","9-minute walk to the beach","5-minute walk to Tel Aviv Port"]),
       gallery=[("yarkon-aerial", L2("מבט מהגג לפארק הירקון","View from the roof over Yarkon Park"), L2("נוף להמחשה מהגג העליון · פארק הירקון","Illustrative view from the top roof · Yarkon Park"), "span")],
       units=[dict(name=L2("דירת 3 חדרים","3-room apartment"), sub=L2("קומה 5","5th floor"),
                   rows=L2([("שטח עיקרי","60 מ״ר"),("מרפסת צפונית","13 מ״ר"),("כיווני אוויר","2 · צפון-מזרח, לכיוון פארק הירקון"),("חניה","חניה תת-קרקעית אחת")],
                           [("Main area","60 sqm"),("North balcony","13 sqm"),("Exposures","2 · north-east, towards Yarkon Park"),("Parking","One underground space")]))],
  ),
  dict(slug="bartenura-3-5", status="planning", card="bartenura-card", wide="bartenura-wide",
       title=L2("עובדיה מברטנורה 3 ו-5", "Ovadia MiBartenura 3 & 5"), area=L2("הצפון הישן", "The Old North"),
       type=L2("תמ״א 38/2 · הריסה ובנייה מחדש · שני בניינים", "TAMA 38/2 · demolition & rebuild · two buildings"),
       short=L2("שני בניינים ברחוב שקט בין שדרות נורדאו לכיכר בזל.", "Two buildings on a quiet street between Nordau Boulevard and Basel Square."),
       overview=L2([
         "פרויקט תמ״א 38/2 של הריסה ובנייה מחדש לשני בניינים ברחוב שקט בין שדרות נורדאו לכיכר בזל, במרחק שמונה דקות הליכה מחוף מציצים. מרפסת וחניה לכל דירה.",
         "הפרויקט ממוקם בלב צפון תל אביב המבוקש - בסביבה שקטה, איכותית ופסטורלית, המשלבת חיי שכונה נעימים לצד נגישות עירונית מלאה: קרבה לצירי תנועה מרכזיים, מוסדות חינוך מובילים, בתי קפה, פארקים ומרכזי בילוי, והכול במרחק דקות מהים.",
         "הפרויקט נמצא לאחר החלטת ועדה ולקראת קבלת היתר בנייה.",
       ],[
         "A TAMA 38/2 demolition-and-rebuild project for two buildings on a quiet street between Nordau Boulevard and Basel Square, an eight-minute walk from Metzitzim Beach. Balcony and parking for every apartment.",
         "The project sits in the heart of sought-after north Tel Aviv - a quiet, high-quality, pastoral setting that combines pleasant neighbourhood life with full urban accessibility: close to main roads, leading schools, cafés, parks and leisure, all minutes from the sea.",
         "The project has passed the planning committee and is awaiting its building permit.",
       ]),
       specs=L2([("סוג הפרויקט","תמ״א 38/2 · הריסה ובנייה מחדש"),("היקף","שני בניינים"),("סטטוס","לאחר החלטת ועדה · לקראת היתר"),("מיקום","הצפון הישן, תל אביב"),("לכל דירה","מרפסת וחניה")],
               [("Project type","TAMA 38/2 · demolition & rebuild"),("Scale","Two buildings"),("Status","Committee approved · pending permit"),("Location","The Old North, Tel Aviv"),("Every apartment","Balcony and parking")]),
       location=L2(["בין שדרות נורדאו לכיכר בזל","8 דקות הליכה לחוף מציצים","קרבה לצירי תנועה, מוסדות חינוך, בתי קפה ופארקים"],
                   ["Between Nordau Boulevard and Basel Square","8-minute walk to Metzitzim Beach","Close to main roads, schools, cafés and parks"]),
       gallery=[("bartenura-2", L2("הדמיית הבניין החדש","Rendering of the new building"), L2("הדמיה · חזית הבניין","Rendering · building façade"), "span")],
       units=[dict(name=L2("עובדיה מברטנורה 3","Ovadia MiBartenura 3"), sub=L2("דירות לשיווק","Apartments for marketing"), rows=L2([],[])),
              dict(name=L2("עובדיה מברטנורה 5","Ovadia MiBartenura 5"), sub=L2("דירות לשיווק","Apartments for marketing"), rows=L2([],[]))],
       units_note=L2("פרטי הדירות והמפרט יימסרו בפנייה למשרד.","Apartment details and specification are available on request."),
  ),
  dict(slug="berdichevsky-17", status="done", card="berdichevsky-card", wide="berdichevsky-wide",
       title=L2("ברדיצ׳בסקי 17", "Berdichevsky 17"), area=L2("לב העיר", "City Center"),
       type=L2("תמ״א 38/1 · חיזוק ושיפוץ", "TAMA 38/1 · strengthening & renovation"),
       short=L2("בניין בוטיק פינתי מול מלון ברדיצ׳בסקי, בכניסה משדרות רוטשילד.", "A corner boutique building opposite the Berdichevsky Hotel, entered from Rothschild Boulevard."),
       overview=L2([
         "פרויקט תמ״א 38/1 של חיזוק ושיפוץ: בניין בוטיק פינתי של עשרה דיירים בלבד, בעיצוב מודרני, הממוקם מול מלון ברדיצ׳בסקי בלב תל אביב.",
         "הבניין יושב במרכז התרבות השוקק של העיר - כיכר הבימה, היכל התרבות והסינמטק במרחק הליכה - ברחוב חד-סטרי עם כניסה משדרות רוטשילד. הפרויקט הושלם ואוכלס.",
       ],[
         "A TAMA 38/1 strengthening-and-renovation project: a corner boutique building of only ten residents, with a modern design, located opposite the Berdichevsky Hotel in the heart of Tel Aviv.",
         "The building sits in the city's bustling cultural centre - Habima Square, the Culture Hall and the Cinematheque within walking distance - on a one-way street entered from Rothschild Boulevard. The project is completed and occupied.",
       ]),
       specs=L2([("סוג הפרויקט","תמ״א 38/1 · חיזוק ושיפוץ"),("סטטוס","אוכלס"),("מיקום","לב העיר, תל אביב"),("היקף","בניין בוטיק פינתי · 10 דיירים")],
               [("Project type","TAMA 38/1 · strengthening & renovation"),("Status","Completed & occupied"),("Location","City center, Tel Aviv"),("Scale","Corner boutique building · 10 residents")]),
       location=L2(["מול מלון ברדיצ׳בסקי","כיכר הבימה, היכל התרבות והסינמטק במרחק הליכה","רחוב חד-סטרי, כניסה משדרות רוטשילד"],
                   ["Opposite the Berdichevsky Hotel","Habima Square, the Culture Hall and the Cinematheque within walking distance","One-way street, entered from Rothschild Boulevard"]),
       gallery=[], units=[],
  ),
  dict(slug="marmorek-26", status="done", card="marmorek-card", wide=None,
       title=L2("מרמורק 26", "Marmorek 26"), area=L2("לב העיר", "City Center"),
       type=L2("תמ״א 38/1 · חיזוק ושיפוץ", "TAMA 38/1 · strengthening & renovation"),
       short=L2("בלב המרכז התרבותי של תל אביב, בין כיכר הבימה לשדרות רוטשילד.", "In the heart of Tel Aviv's cultural centre, between Habima Square and Rothschild Boulevard."),
       overview=L2([
         "פרויקט תמ״א 38/1 של חיזוק ושיפוץ בלב תל אביב, במרכז התרבות השוקק של העיר: כיכר הבימה, היכל התרבות, הסינמטק ושדרות רוטשילד - ברחוב חד-סטרי עם שביל אופניים חדש.",
         "הפרויקט הושלם ואוכלס. בבניין שוכנים גם משרדי אנגל נדל״ן.",
       ],[
         "A TAMA 38/1 strengthening-and-renovation project in the heart of Tel Aviv, in the city's bustling cultural centre: Habima Square, the Culture Hall, the Cinematheque and Rothschild Boulevard - on a one-way street with a new bike lane.",
         "The project is completed and occupied. The building is also home to the Engel Real Estate offices.",
       ]),
       specs=L2([("סוג הפרויקט","תמ״א 38/1 · חיזוק ושיפוץ"),("סטטוס","אוכלס"),("מיקום","לב העיר, תל אביב")],
               [("Project type","TAMA 38/1 · strengthening & renovation"),("Status","Completed & occupied"),("Location","City center, Tel Aviv")]),
       location=L2(["כיכר הבימה, היכל התרבות והסינמטק","שדרות רוטשילד","רחוב חד-סטרי עם שביל אופניים חדש"],
                   ["Habima Square, the Culture Hall and the Cinematheque","Rothschild Boulevard","One-way street with a new bike lane"]),
       gallery=[], units=[],
  ),
]
BY_SLUG = {p["slug"]: p for p in PROJECTS}

# ---------------------------------------------------------------- helpers
def esc(s): return html.escape(s, quote=True)

def dims(name, w):
    with Image.open(os.path.join(IMG, f"{name}-{w}.webp")) as im: return im.size

def widths_of(name):
    return sorted(int(f[len(name)+1:-5]) for f in os.listdir(IMG) if f.startswith(name + "-") and f.endswith(".webp") and f[len(name)+1:-5].isdigit())

def pic(name, alt, sizes="100vw", eager=False, cls=""):
    ws = widths_of(name)
    avif = ", ".join(f"/assets/img/{name}-{w}.avif {w}w" for w in ws)
    webp = ", ".join(f"/assets/img/{name}-{w}.webp {w}w" for w in ws)
    w, h = dims(name, ws[-1])
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<picture{c}><source type="image/avif" srcset="{avif}" sizes="{sizes}">'
            f'<img src="/assets/img/{name}-{ws[-1]}.webp" srcset="{webp}" sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt)}" {load}></picture>')

def preload(name, sizes, media=None):
    ws = widths_of(name)
    ss = ", ".join(f"/assets/img/{name}-{w}.avif {w}w" for w in ws)
    m = f' media="{media}"' if media else ""
    return f'<link rel="preload" as="image" fetchpriority="high" type="image/avif" imagesrcset="{ss}" imagesizes="{sizes}"{m}>'

ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M14 8H2M7 3 2 8l5 5"/></svg>'

def head(L, title, desc, path, extra=""):
    lg = LANGS[L]; t = T[L]
    full = f"{title} | {lg['site']}" if path != "/" else title
    robots = '<meta name="robots" content="noindex, nofollow">' if PREVIEW else f'<link rel="canonical" href="{SITE_URL}{lg["prefix"]}{path}">'
    sub = "hebrew" if L == "he" else "latin"
    return f'''<!DOCTYPE html>
<html lang="{L}" dir="{lg['dir']}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
{robots}
<link rel="alternate" hreflang="he" href="{SITE_URL}{path}">
<link rel="alternate" hreflang="en" href="{SITE_URL}/en{path}">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}{path}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{lg['locale']}">
<meta property="og:image" content="{SITE_URL}/assets/img/hero-wide-1200.webp">
<meta name="theme-color" content="#f6f7f9">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="preload" href="/assets/fonts/plex-hebrew-200-{sub}.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/plex-hebrew-400-{sub}.woff2" as="font" type="font/woff2" crossorigin>
{extra}
<link rel="stylesheet" href="/assets/css/site.css">
<script>document.documentElement.classList.remove('no-js')</script>
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>
'''

def header(L, active, path):
    lg = LANGS[L]; t = T[L]; P = lg["prefix"]; OP = LANGS[lg["other"]]["prefix"]
    links = "".join(f'<a href="{P}{h}"{" aria-current=%spage%s" % (chr(34),chr(34)) if h == active else ""}>{n}</a>' for h, n in t["nav"])
    menu = "".join(f'<li><a href="{P}{h}">{n}</a></li>' for h, n in t["nav"])
    lang = f'<a class="lang" href="{OP}{path}" lang="{lg["other"]}" hreflang="{lg["other"]}" aria-label="{t["lang_label"]}">{t["lang"]}</a>'
    phone_style = ' style="text-align:end"' if L == "he" else ""
    return f'''<header class="header">
  <div class="wrap">
    <a class="brand" href="{P}/"><img src="/assets/img/logo-black.png" width="453" height="355" alt="{lg['site']}"></a>
    <nav class="nav" aria-label="{t['nav_label']}">{links}</nav>
    <div class="header__cta">{lang}<a class="header__phone" href="tel:{PHONE_TEL}">{PHONE}</a><a class="btn btn--solid" href="{P}/urban-renewal/#feasibility">{t['feas']}</a></div>
    <button class="burger" aria-label="{t['menu']}" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="menu" id="menu">
  <ul>{menu}</ul>
  <div class="menu__foot">{lang}<a href="tel:{PHONE_TEL}" dir="ltr"{phone_style}>{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a><span class="muted">{lg['address']}</span></div>
</div>
<main id="main">
'''

def footer(L):
    lg = LANGS[L]; t = T[L]; P = lg["prefix"]
    nav = "".join(f'<li><a href="{P}{h}">{n}</a></li>' for h, n in t["nav"])
    fax = f'<li><span class="ltr">{FAX}</span> {t["fax"]}</li>' if L == "he" else f'<li>{t["fax"]} <span class="ltr">{FAX}</span></li>'
    return f'''</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <a class="brand" href="{P}/"><img src="/assets/img/logo-white.png" width="453" height="355" alt="{lg['site']}" loading="lazy"></a>
        <p class="footer__tag">{t['tagline']}</p>
      </div>
      <div><p class="footer__h">{t['f_nav']}</p><ul>{nav}</ul></div>
      <div><p class="footer__h">{t['f_contact']}</p><ul>
        <li><a class="ltr" href="tel:{PHONE_TEL}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        {fax}
        <li>{lg['address']}</li></ul></div>
      <div><p class="footer__h">{t['f_info']}</p><ul>
        <li><a href="{P}/terms/">{t['terms']}</a></li>
        <li><a href="{P}/privacy/">{t['privacy']}</a></li>
        <li><a href="{P}/accessibility/">{t['a11y']}</a></li>
        <li><a href="{P}/projects/">{t['forsale']}</a></li></ul></div>
    </div>
    <div class="footer__bottom">
      <span>{t['copyright'].format(y=YEAR)}</span>
      <span>{t['disclaimer']}</span>
      <span>{t['credit']}<a href="https://einstein-web.co.il" target="_blank" rel="noopener">{t['credit_name']}</a></span>
    </div>
  </div>
</footer>
<script src="/assets/js/site.js" defer></script>
<script src="/assets/js/a11y.js" defer></script>
</body>
</html>
'''

def card(L, p, sizes="(min-width:1000px) 30vw, (min-width:640px) 45vw, 92vw", d=0):
    P = LANGS[L]["prefix"]; t = T[L]
    return f'''<a class="card rv" data-d="{d}" data-status="{p['status']}" href="{P}/projects/{p['slug']}/">
  <div class="card__media">{pic(p['card'], t['card_alt'].format(t=p['title'][L]), sizes)}<span class="card__status" data-s="{p['status']}">{STATUS[L][p['status']]}</span></div>
  <div class="card__body">
    <span class="card__title">{p['title'][L]}</span>
    <span class="card__arrow">{ARROW}</span>
    <span class="card__loc">{p['area'][L]} · {t['tlv']}</span>
    <span class="card__type">{p['type'][L]}</span>
  </div>
</a>'''

def form(L, kind="contact"):
    t = T[L]
    return f'''<form class="form" action="https://api.web3forms.com/submit" method="POST" novalidate>
  <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
  <input type="hidden" name="subject" value="{t['f_subject']}">
  <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="form__row">
    <div class="field"><label for="f-name">{t['f_name']}</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
    <div class="field"><label for="f-phone">{t['f_phone']}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
  </div>
  <div class="form__row">
    <div class="field"><label for="f-email">{t['f_email']}</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
    <div class="field"><label for="f-address">{t['f_building']}</label><input id="f-address" name="building" type="text" placeholder="{t['f_building_ph']}"></div>
  </div>
  <div class="field"><label for="f-interest">{t['f_interest']}</label>
      <select id="f-interest" name="interest">
        <option{" selected" if kind=="feasibility" else ""}>{t['f_opt1']}</option>
        <option>{t['f_opt2']}</option>
        <option>{t['f_opt3']}</option></select></div>
  <div class="field"><label for="f-msg">{t['f_msg']}</label><textarea id="f-msg" name="message" placeholder="{t['f_msg_ph']}"></textarea></div>
  <div class="form__foot">
    <button class="btn btn--solid" type="submit">{t['f_send']} {ARROW}</button>
    <span class="note">{t['f_note']}</span>
  </div>
  <div class="form__msg" role="status" aria-live="polite"></div>
</form>'''

def cta_section(L):
    t = T[L]; lg = LANGS[L]; P = lg["prefix"]
    return f'''<section class="section section--dark cta grain">
  <div class="wrap">
    <div>
      <p class="eyebrow"><span class="num">06</span> {t['cta_eyebrow']}</p>
      <h2 class="h-l">{t['cta_h']}</h2>
      <p class="lead" style="margin-top:20px">{t['cta_p']}</p>
      <div class="actions" style="margin-top:28px"><a class="btn btn--solid" href="{P}/urban-renewal/#feasibility">{t['cta_btn']} {ARROW}</a><a class="btn btn--ghost" href="{P}/projects/">{t['cta_btn2']}</a></div>
    </div>
    <div class="cta__contact">
      <span class="muted" style="color:var(--on-dark-2)">{t['cta_or']}</span>
      <a class="big" href="tel:{PHONE_TEL}">{PHONE}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <span style="color:var(--on-dark-2)">{lg['address']}</span>
    </div>
  </div>
</section>
'''

def write(L, path, content):
    P = LANGS[L]["prefix"]
    fp = os.path.join(OUT, (P + path).strip("/"), "index.html") if path.endswith("/") else os.path.join(OUT, (P + "/" + path).strip("/"))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8", newline="\n") as f: f.write(content)
    print("wrote", os.path.relpath(fp, ROOT))

# ---------------------------------------------------------------- page copy
C = {
 "he": dict(
  home_title="אנגל נדל״ן | התחדשות עירונית בתל אביב · תמ״א 38",
  home_desc="אנגל נדל״ן היא חברת בוטיק משפחתית לייזום וביצוע פרויקטים של תמ״א 38 בתל אביב בלבד - מהבדיקה הראשונית ועד מסירת המפתח.",
  hero_eyebrow="התחדשות עירונית · תל אביב", hero_h='בונים מחדש את <span class="em">לב תל אביב.</span>',
  hero_lead="אנגל נדל״ן היא חברת בוטיק משפחתית לייזום וביצוע פרויקטים של תמ״א 38 - בתל אביב בלבד. מהבדיקה הראשונית ועד מסירת המפתח, באחריות מלאה ובסטנדרט הגבוה בעיר.",
  hero_btn1="בדיקת היתכנות לבניין שלכם", hero_btn2="הפרויקטים שלנו",
  hero_alt="הדמיית פרויקט פראג 3 - בניין בוטיק חדש בצפון הישן של תל אביב", hero_cap="פראג 3 · הצפון הישן", hero_cap_b="בביצוע",
  facts=[("תל אביב בלבד","עיר אחת. התמחות אחת."),("תמ״א 38","חיזוק ושיפוץ · הריסה ובנייה מחדש"),("ליווי בנקאי","בנק הפועלים · כלל"),("עשרות לקוחות","בחרו בנו כשותף אמין")],
  s1_eyebrow="פרויקטים נבחרים", s1_h="מהצפון הישן ועד לב העיר", s1_more="לכל הפרויקטים",
  s2_eyebrow="אודות החברה", s2_statement='חברת בוטיק משפחתית. <span class="em">עיר אחת.</span> אחריות מלאה מהתכנון ועד המפתח.',
  s2_lead="אנגל נדל״ן היא חברת בוטיק משפחתית העוסקת בבנייה ובייזום מזה שנים, ומורכבת מאנשי מקצוע איכותיים בתחומי הנדל״ן והבנייה. הניסיון המגוון של הצוות המוביל הוא היתרון שלנו - ושל הדיירים שלנו.",
  s2_p="אנחנו מנהלים את כל ההיבטים של כל פרויקט מראשיתו ועד השלמתו: מהתכנון ההנדסי, דרך המימון, המיסוי והליווי המשפטי, השיווק והמכירות - וכלה בניהול ובביצוע. אנגל נדל״ן פועלת רק בעיר תל אביב, ונבחרה כשותף אמין על ידי עשרות לקוחות למימוש פרויקטים בתחום התמ״א.",
  disciplines=["מהנדסים","אדריכלים","מנהלי פרויקטים","כלכלנים","עורכי דין","מנהלי שיווק"], s2_btn="להכיר את החברה",
  s3_eyebrow="התחדשות עירונית", s3_h="שני מסלולים. סטנדרט אחד.", s3_more="על התהליך המלא",
  t2_k="תמ״א 38/2", t2_h="הריסה ובנייה מחדש", t2_p="בניין חדש לחלוטין, ממרתפי החניה ועד הגג העליון - בעיצוב יוקרתי, במפרט עשיר ובסטנדרט בנייה גבוה.",
  t2_home=["דירות חדשות, פונקציונליות ושטופות אור, בשטח מקסימלי לפי הזכויות מעיריית תל אביב","בנייה ירוקה, בידוד אקוסטי ולובי מפואר עם מעלית במפרט גבוה","חניון פונקציונלי לכל הדירות - קונבנציונלי או רובוטי","פגישת תכנון אישית עם אדריכל לכל דייר"],
  t1_k="תמ״א 38/1", t1_h="חיזוק ושיפוץ בניין קיים", t1_p="חיזוק המבנה מפני רעידות אדמה לפי התקנים המחמירים ביותר, יחד עם שדרוג מלא של הבניין והדירות.",
  t1_home=["הגדלת הדירות: מרפסות שמש, ממ״ד ושטחים נוספים","הוספת מעלית ושדרוג הלובי וחדר המדרגות","שיפוץ חיצוני ברמת גימור גבוהה והחלפת תשתיות: ביוב, חשמל, מים וגז","שבילי גישה וגינה מעוצבת עם מערכות השקיה מתקדמות"],
  steps=[("בדיקת היתכנות","בדיקה ראשונית של עמידה בתנאי התוכנית - ללא עלות."),("בדיקות ותכנון","בדיקות משפטיות ברשויות, תכנון הנדסי ואדריכלי ומינוי צוות היועצים."),("הסכמות דיירים","ליווי הדיירים, סיכום פרטי הפרויקט, המפרט ורמת הגימור."),("מימון וביצוע","ליווי בנקאי, ערבויות חוק מכר, מימון דיור זמני - וביצוע במעקב צמוד."),("מסירה ורישום","מסירת הדירות החדשות, הסדרת התקנות והרישום בטאבו.")],
  band_alt="נוף פנורמי לפארק הירקון ולים התיכון מגובה הדירות באוסישקין",
  s4_eyebrow="תל אביב", s4_h="פועלים רק בתל אביב. ומכירים כל רחוב.",
  area1_h="הצפון הישן", area1_p="בין פארק הירקון, הנמל והים: רחובות שקטים במרחק דקות הליכה מחוף הילטון, חוף מציצים וכיכר בזל.",
  area2_h="לב העיר", area2_p="המרכז התרבותי של תל אביב: כיכר הבימה, היכל התרבות, הסינמטק ושדרות רוטשילד.",
  area_status={"ussishkin-52":"היתר בנייה","bartenura-3-5":"לקראת היתר"},
  s5_eyebrow="למה אנגל נדל״ן", s5_h="שיטת עבודה של חברת בוטיק",
  why=[("אחריות מלאה על הביצוע","מעקב צמוד על איכות הביצוע וקבלת אחריות מלאה על הנעשה בשטח - מהיום הראשון ועד המסירה."),("עמידה בלוחות זמנים","הקפדה יתרה על לוחות הזמנים ועל כל פרט ופרט, בכל שלב של הפרויקט."),("שקיפות בכל שלב","תמיכה, נגישות ותחושת ביטחון לדיירים, עם עדכון שוטף לאורך כל הדרך."),("ביטחון כלכלי לדיירים","ליווי בנקאי, ערבויות חוק מכר לדירות החדשות, מימון דיור זמני והובלות.")],
  pl_title="הפרויקטים", pl_desc="פרויקטי תמ״א 38 של אנגל נדל״ן בתל אביב: אוסישקין 46 ו-52, פראג 3, עובדיה מברטנורה, ברדיצ׳בסקי 17 ומרמורק 26.",
  pl_eyebrow="הפרויקטים", pl_h="בניין אחד בכל פעם, ברחובות שאנחנו מכירים.",
  pl_lead="פרויקטים של תמ״א 38 - הריסה ובנייה מחדש וחיזוק ושיפוץ - בצפון הישן ובלב העיר של תל אביב. חלק מהדירות בפרויקטים שבביצוע נמכרות ישירות מהחברה, ללא עמלת תיווך.",
  filters=[("all","הכול"),("active","בביצוע"),("permit","היתר בנייה"),("planning","בתכנון"),("done","אוכלס")], filter_label="סינון לפי סטטוס",
  pl_empty="אין פרויקטים בסטטוס הזה כרגע.", pl_note="ועוד פרויקטים נבחרים בתל אביב. ההדמיות להמחשה בלבד. ט.ל.ח.",
  pp_about="על הפרויקט", pp_loc="מיקום", pp_specs="פרטי הפרויקט", pp_more="לפרטים נוספים", pp_gallery="גלריה", pp_gallery_note="ההדמיות להמחשה בלבד. ט.ל.ח.",
  pp_units_eyebrow="דירות למכירה", pp_units_h="ישירות מהחברה, ללא עמלת תיווך", pp_units_more="לתיאום פגישה", pp_plans="תכניות הדירה", pp_plan_pdf="להורדת התכנית (PDF)", pp_prev="הפרויקט הקודם", pp_next="הפרויקט הבא", pp_nav_label="ניווט בין פרויקטים", crumbs_label="פירורי לחם",
  ur_title="התחדשות עירונית · תמ״א 38 בתל אביב", ur_desc="איך עובד פרויקט תמ״א 38 עם אנגל נדל״ן: הריסה ובנייה מחדש (38/2) או חיזוק ושיפוץ (38/1), ליווי הדיירים, צוות היועצים ובדיקת היתכנות ללא עלות.",
  ur_eyebrow="התחדשות עירונית", ur_h="הבניין שלכם יכול להיות הבניין הבא של תל אביב.",
  ur_lead="אנגל נדל״ן מתמחה בייזום ובמימוש פרויקטים של תמ״א 38 בתל אביב - החל מהבדיקה הראשונית של עמידה בתנאי התוכנית, דרך הבדיקות המשפטיות ברשויות והתכנון על כל היבטיו, וכלה בייזום, במימון ובביצוע.",
  ur_btn="בדיקת היתכנות ללא עלות", ur1_eyebrow="שני מסלולים", ur1_h="הריסה ובנייה מחדש, או חיזוק ושיפוץ",
  t2_p_full="בניית בניין חדש ממרתפי החניה ועד הגג העליון. הבניין מתוכנן בעיצוב יוקרתי, במפרט עשיר ובסטנדרט בנייה גבוה.",
  t2_full=["דירות פונקציונליות ושטופות אור, בהתאם לתקני התכנון","מיקסום שטח הדירות לפי מדידות וקבלת הזכויות המקסימליות מעיריית תל אביב","בנייה ירוקה השומרת על הסביבה, חוסכת בחשבונות הצריכה ומבטיחה את עמידות הבניין לאורך שנים","בידוד אקוסטי בין הדירות, המרחבים הציבוריים וחוץ המבנה","לובי מפואר ויוקרתי, מעלית במפרט גבוה, טלוויזיה במעגל סגור ואינטרקום","חניון פונקציונלי לכלל הדירות - קונבנציונלי או רובוטי","פגישת ייעוץ עם אדריכל לכל דייר, לתכנון פנים הדירה וחלוקת החדרים","הסדרת התקנות והרישום בטאבו בהתאם לשינויים החדשים"],
  t1_p_full="חיזוק המבנה מפני רעידות אדמה בהתאם לתקנים המחמירים ביותר, יחד עם שדרוג מקיף של הבניין ושל הדירות.",
  t1_full=["הגדלת שטח הדירות בתוספות בנייה: מרפסות שמש, ממ״ד ושטחים נוספים","הוספת מעלית","שדרוג הלובי וחדר המדרגות","שיפוץ חיצוני ברמת גימור גבוהה ושדרוג מעטפת הבניין","החלפת התשתיות החיצוניות: ביוב, חשמל, מים וגז","שבילי גישה וגינה מעוצבת הכוללת מערכות השקיה מתקדמות"],
  ur2_eyebrow="ליווי הדיירים", ur2_statement='במהלך כל הפרויקט, הדיירים מקבלים <span class="em">תמיכה, ביטחון ושקיפות</span> - ועדכון בכל שלב ושלב.',
  support=[("מימון דיור זמני","אנו מעניקים מימון לדיור זמני לאורך תקופת הבנייה."),("ערבויות חוק מכר","ערבויות חוק מכר לדירות החדשות שייבנו."),("הובלות","הליווי כולל גם את הובלת תכולת הדירות."),("פגישת תכנון עם אדריכל","כל דייר מקבל פגישת ייעוץ אישית לתכנון פנים הדירה וחלוקת החדרים."),("מפרט גבוה, מקיף ויוקרתי","אנו מציעים לדיירים מפרט גבוה, ומסכמים מול הדיירים את פרטי הפרויקט, רמת הגימור והתכנון ההנדסי-אדריכלי.")],
  ur3_eyebrow="התהליך", ur3_h="מבדיקה ראשונית ועד רישום בטאבו",
  steps_full=[("בדיקת היתכנות","בדיקה ראשונית של עמידת הבניין בתנאי התוכנית והיתכנות כלכלית - ללא כל עלות."),("בדיקות ותכנון","בדיקות משפטיות ברשויות, תכנון הנדסי ואדריכלי ומינוי צוות היועצים."),("הסכמות דיירים","ליווי הדיירים וסיכום פרטי הפרויקט: המפרט, רמת הגימור והתכנון שניתן ליישם."),("מימון וביצוע","ליווי בנקאי, ערבויות חוק מכר ומימון דיור זמני - וביצוע במעקב צמוד על האיכות ועל לוחות הזמנים."),("מסירה ורישום","מסירת הדירות החדשות והסדרת התקנות והרישום בטאבו.")],
  consultants_h="צוות היועצים בכל פרויקט",
  consultants=["אדריכל","מהנדס קונסטרוקציה","אינסטלציה","חשמל","בטיחות","מעליות","הידרולוג","יועץ נגישות","יועץ הג״א","יועץ אקוסטיקה","יועץ בנייה ירוקה","יועץ קרקע וביסוס","יועץ תנועה","אגרונום","יועץ מס"],
  ur4_eyebrow="בדיקת היתכנות", ur4_h="השאירו פרטים על הבניין שלכם",
  ur4_lead="נציג החברה ייצור עמכם קשר לקבלת פרטים ראשוניים. צוות המומחים שלנו יבחן את הבניין ויחזור אליכם עם תשובה מפורטת האם קיימת היתכנות כלכלית לפרויקט - ללא כל עלות.",
  ur4_call="מעדיפים לדבר?",
  ab_title="אודות", ab_desc="אנגל נדל״ן היא חברת בוטיק משפחתית לבנייה ולייזום, הפועלת רק בתל אביב ומנהלת פרויקטים של תמ״א 38 מראשיתם ועד השלמתם.",
  ab_eyebrow="אודות", ab_h="חברת בוטיק משפחתית שבונה מחדש את תל אביב.",
  ab_lead="אנגל נדל״ן עוסקת בבנייה ובייזום מזה שנים, ומורכבת מאנשי מקצוע איכותיים בתחומי הנדל״ן והבנייה: מהנדסים, אדריכלים, מנהלי פרויקטים, כלכלנים, עורכי דין ומנהלי שיווק.",
  ab_img_alt="הדמיית קומת הגג באוסישקין 46 עם נוף לתל אביב", ab_img_cap="אוסישקין 46 · תמ״א 38/2 · בביצוע",
  ab1_eyebrow="מי אנחנו", ab1_statement='הניסיון המגוון של הצוות המוביל הוא <span class="em">יתרון איכותי</span> בענף - ואנחנו מביאים אותו לכל בניין.',
  ab1_ps=["חברתנו מנוסה בניהול כלל ההיבטים הכרוכים בכל פרויקט, מראשיתו ועד השלמתו: החל משלב התכנון ההנדסי, דרך שלבי המימון, המיסוי והליווי המשפטי, השיווק והמכירות - וכלה בניהול ובביצוע.","שיטת העבודה הייחודית שלנו מבטיחה מעקב צמוד על איכות הביצוע, קבלת אחריות מלאה על הנעשה בשטח והקפדה יתרה על עמידה בלוחות הזמנים ועל כל פרט ופרט. כך אנחנו מבצעים מגוון פרויקטים בסטנדרטים הגבוהים ביותר בעיר תל אביב.","אנגל נדל״ן פועלת רק בעיר תל אביב, ונבחרה כשותף אמין על ידי עשרות לקוחות מתל אביב למימוש פרויקטים בתחום התמ״א."],
  ab2_eyebrow="הערכים שלנו", ab2_h="מה שמנחה אותנו בכל פרויקט",
  values=[("עיר אחת, התמחות אחת","אנגל נדל״ן פועלת רק בעיר תל אביב, ונבחרה כשותף אמין על ידי עשרות לקוחות מהעיר למימוש פרויקטים בתחום התמ״א."),("אחריות מלאה","מהתכנון ועד המפתח, האחריות על הנעשה בשטח היא שלנו - עם מעקב צמוד על איכות הביצוע ועל לוחות הזמנים."),("שקיפות ונגישות","הדיירים מקבלים תמיכה, תחושת ביטחון ועדכון שוטף בכל שלב ושלב של הפרויקט."),("סטנדרט של בוטיק","מפרט גבוה, מקיף ויוקרתי, בנייני בוטיק, ופגישת ייעוץ אישית עם אדריכל לכל דייר לתכנון פנים הדירה.")],
  ab3_img_alt="הדמיית סלון בדירה חדשה", ab3_img_cap="הדמיה · דירה חדשה בסטנדרט בוטיק", ab3_eyebrow="הצוות", ab3_h="אנשי מקצוע איכותיים בתחומי הנדל״ן והבנייה",
  ab3_p="בכל פרויקט אנחנו ממנים יועצים מובילים בתחומם - אדריכל, מהנדס קונסטרוקציה, יועצי אינסטלציה, חשמל, בטיחות, מעליות, אקוסטיקה, בנייה ירוקה, קרקע וביסוס, תנועה, נגישות והג״א, הידרולוג, אגרונום ויועץ מס - וכל יועץ נוסף שיידרש.",
  ab3_btn1="לפרויקטים שלנו", ab3_btn2="דברו איתנו",
  ct_title="צור קשר", ct_desc="מעוניינים בפרויקט התחדשות עירונית לבניין שלכם או ברכישת דירה ישירות מהחברה? השאירו פרטים או התקשרו: 03-6005955.",
  ct_eyebrow="צור קשר", ct_h="צרו איתנו קשר",
  ct_lead="מעוניינים בביצוע פרויקט התחדשות עירונית, או ברכישת דירה ישירות מהחברה וללא עמלת תיווך? השאירו פרטים ואנו נחזור אליכם בהקדם.",
  ct_phone="טלפון המשרד", ct_email="דוא״ל", ct_fax="פקס", ct_address="כתובת", ct_note="אנגל נדל״ן פועלת בתל אביב בלבד.",
  legal_eyebrow="משפטי", terms_h="תנאי שימוש", terms_desc="תנאי השימוש באתר אנגל נדל״ן.",
  terms_lead="ברוכים הבאים לאתר אנגל נדל״ן (להלן: ״האתר״). השימוש באתר כפוף לתנאים ולהוראות המפורטים להלן. אנא קראו תנאים אלה בעיון, שכן השימוש באתר מעיד על הסכמתכם להם.",
  terms_contact="לשאלות בנוגע לתנאי השימוש ניתן לפנות אלינו בכתובת",
  privacy_h="מדיניות פרטיות", privacy_desc="מדיניות הפרטיות של אתר אנגל נדל״ן.",
  privacy_lead="אנו מחויבים לשמור על פרטיות המשתמשים ולנהל את המידע האישי בהתאם להוראות הדין. מדיניות זו מפרטת כיצד אנו אוספים, משתמשים ושומרים על המידע שלכם בעת השימוש באתר.",
  a11y_h="הצהרת נגישות", a11y_desc="הצהרת הנגישות של אתר אנגל נדל״ן: התאמות הנגישות שבוצעו, תפריט הנגישות ודרכי פנייה.", a11y_eyebrow="נגישות",
  nf_title="הדף לא נמצא", nf_desc="הדף שחיפשתם אינו קיים.", nf_h="הדף הזה עדיין לא נבנה.", nf_p="הדף שחיפשתם אינו קיים או שהועבר. אפשר לחזור לדף הבית או לעבור לפרויקטים.", nf_btn1="לדף הבית", nf_btn2="הפרויקטים",
 ),
 "en": dict(
  home_title="Engel Real Estate | Urban Renewal in Tel Aviv · TAMA 38",
  home_desc="Engel Real Estate is a family-run boutique developer of TAMA 38 projects in Tel Aviv only - from the first feasibility check to handing over the keys.",
  hero_eyebrow="Urban renewal · Tel Aviv", hero_h='Rebuilding the <span class="em">heart of Tel Aviv.</span>',
  hero_lead="Engel Real Estate is a family-run boutique developer of TAMA 38 projects - in Tel Aviv only. From the first feasibility check to handing over the keys, with full responsibility and the highest standards in the city.",
  hero_btn1="Check your building's feasibility", hero_btn2="Our projects",
  hero_alt="Rendering of the Prague 3 project - a new boutique building in Tel Aviv's Old North", hero_cap="Prague 3 · The Old North", hero_cap_b="Under construction",
  facts=[("Tel Aviv only","One city. One specialty."),("TAMA 38","Strengthening & renovation · demolition & rebuild"),("Bank financing","Bank Hapoalim · Clal"),("Dozens of clients","chose us as a trusted partner")],
  s1_eyebrow="Selected projects", s1_h="From the Old North to the city center", s1_more="All projects",
  s2_eyebrow="About the company", s2_statement='A family-run boutique firm. <span class="em">One city.</span> Full responsibility from planning to keys.',
  s2_lead="Engel Real Estate is a family-run boutique company that has been engaged in construction and development for years, made up of quality professionals in real estate and construction. The diverse experience of our leading team is our advantage - and our residents'.",
  s2_p="We manage every aspect of each project from inception to completion: engineering design, financing, taxation and legal support, marketing and sales - through to management and execution. Engel Real Estate operates only in the city of Tel Aviv, and has been chosen as a trusted partner by dozens of clients for TAMA 38 projects.",
  disciplines=["Engineers","Architects","Project managers","Economists","Lawyers","Marketing managers"], s2_btn="Get to know us",
  s3_eyebrow="Urban renewal", s3_h="Two tracks. One standard.", s3_more="The full process",
  t2_k="TAMA 38/2", t2_h="Demolition & rebuild", t2_p="A completely new building, from the parking basements to the top roof - luxurious design, rich specification and a high construction standard.",
  t2_home=["New, functional, light-filled apartments at the maximum area allowed by the Tel Aviv municipality's rights","Green building, acoustic insulation and a grand lobby with a high-spec elevator","A functional parking garage for all apartments - conventional or robotic","A personal design meeting with an architect for every resident"],
  t1_k="TAMA 38/1", t1_h="Strengthening & renovation", t1_p="Seismic strengthening of the building to the strictest standards, together with a full upgrade of the building and its apartments.",
  t1_home=["Larger apartments: sun balconies, safe rooms and additional areas","A new elevator and an upgraded lobby and stairwell","High-finish exterior renovation and new infrastructure: sewage, electricity, water and gas","Access paths and a designed garden with advanced irrigation"],
  steps=[("Feasibility check","An initial check that the building meets the plan's conditions - at no cost."),("Due diligence & planning","Legal checks with the authorities, engineering and architectural design, and appointing the consultant team."),("Resident agreements","Guiding the residents and finalising the project details, specification and finish level."),("Financing & construction","Bank financing, sale-law guarantees, temporary housing financing - and closely supervised construction."),("Handover & registration","Delivering the new apartments, regularising the bylaws and registering in the Land Registry.")],
  band_alt="Panoramic view of Yarkon Park and the Mediterranean from apartment height on Ussishkin",
  s4_eyebrow="Tel Aviv", s4_h="We work only in Tel Aviv. And we know every street.",
  area1_h="The Old North", area1_p="Between Yarkon Park, the port and the sea: quiet streets minutes on foot from Hilton Beach, Metzitzim Beach and Basel Square.",
  area2_h="City Center", area2_p="Tel Aviv's cultural centre: Habima Square, the Culture Hall, the Cinematheque and Rothschild Boulevard.",
  area_status={"ussishkin-52":"Building permit","bartenura-3-5":"Pending permit"},
  s5_eyebrow="Why Engel Real Estate", s5_h="The working method of a boutique firm",
  why=[("Full responsibility for execution","Close supervision of construction quality and full responsibility for what happens on site - from day one to handover."),("Meeting schedules","Strict adherence to timelines and to every single detail, at every stage of the project."),("Transparency at every stage","Support, accessibility and peace of mind for residents, with regular updates all the way through."),("Financial security for residents","Bank financing, sale-law guarantees for the new apartments, temporary housing financing and moving.")],
  pl_title="Projects", pl_desc="Engel Real Estate's TAMA 38 projects in Tel Aviv: Ussishkin 46 and 52, Prague 3, Ovadia MiBartenura, Berdichevsky 17 and Marmorek 26.",
  pl_eyebrow="Projects", pl_h="One building at a time, on streets we know.",
  pl_lead="TAMA 38 projects - demolition and rebuild, strengthening and renovation - in Tel Aviv's Old North and city center. Some apartments in projects under construction are sold directly by the developer, with no brokerage fee.",
  filters=[("all","All"),("active","Under construction"),("permit","Building permit"),("planning","Planning"),("done","Completed")], filter_label="Filter by status",
  pl_empty="No projects with this status at the moment.", pl_note="And more selected projects in Tel Aviv. Renderings are for illustration only. E&OE.",
  pp_about="About the project", pp_loc="Location", pp_specs="Project details", pp_more="More details", pp_gallery="Gallery", pp_gallery_note="Renderings are for illustration only. E&OE.",
  pp_units_eyebrow="Apartments for sale", pp_units_h="Directly from the developer, no brokerage fee", pp_units_more="Arrange a meeting", pp_plans="Floor plans", pp_plan_pdf="Download the plan (PDF)", pp_prev="Previous project", pp_next="Next project", pp_nav_label="Project navigation", crumbs_label="Breadcrumb",
  ur_title="Urban Renewal · TAMA 38 in Tel Aviv", ur_desc="How a TAMA 38 project works with Engel Real Estate: demolition and rebuild (38/2) or strengthening and renovation (38/1), resident support, the consultant team and a free feasibility check.",
  ur_eyebrow="Urban renewal", ur_h="Your building could be Tel Aviv's next building.",
  ur_lead="Engel Real Estate specialises in initiating and delivering TAMA 38 projects in Tel Aviv - from the initial check that the building meets the plan's conditions, through legal checks with the authorities and planning in all its aspects, to development, financing and construction.",
  ur_btn="Free feasibility check", ur1_eyebrow="Two tracks", ur1_h="Demolition and rebuild, or strengthening and renovation",
  t2_p_full="Building a new building from the parking basements to the top roof. The building is designed with luxurious design, a rich specification and a high construction standard.",
  t2_full=["Functional, light-filled apartments in line with planning standards","Maximising apartment area according to surveys and obtaining the maximum rights from the Tel Aviv municipality","Green building that protects the environment, saves on utility bills and ensures the building's durability for years","Acoustic insulation between apartments, common areas and the building exterior","A grand, luxurious lobby, a high-spec elevator, CCTV and intercom","A functional parking garage for all apartments - conventional or robotic","A consultation meeting with an architect for every resident, to plan the apartment interior and room layout","Regularising the bylaws and Land Registry registration in line with the new changes"],
  t1_p_full="Seismic strengthening of the building to the strictest standards, together with a comprehensive upgrade of the building and its apartments.",
  t1_full=["Enlarging apartments with building additions: sun balconies, safe rooms and additional areas","Adding an elevator","Upgrading the lobby and stairwell","High-finish exterior renovation and upgrading the building envelope","Replacing external infrastructure: sewage, electricity, water and gas","Access paths and a designed garden with advanced irrigation systems"],
  ur2_eyebrow="Resident support", ur2_statement='Throughout the project, residents receive <span class="em">support, security and transparency</span> - and updates at every stage.',
  support=[("Temporary housing financing","We provide financing for temporary housing for the duration of construction."),("Sale-law guarantees","Sale-law guarantees for the new apartments to be built."),("Moving","The support also includes moving the apartments' contents."),("Design meeting with an architect","Every resident receives a personal consultation to plan the apartment interior and room layout."),("A high, comprehensive, luxurious specification","We offer residents a high specification, and finalise with them the project details, finish level and engineering-architectural design.")],
  ur3_eyebrow="The process", ur3_h="From the first check to Land Registry registration",
  steps_full=[("Feasibility check","An initial check that the building meets the plan's conditions and is economically feasible - at no cost whatsoever."),("Due diligence & planning","Legal checks with the authorities, engineering and architectural design, and appointing the consultant team."),("Resident agreements","Guiding the residents and finalising the project details: the specification, finish level and the design that can be implemented."),("Financing & construction","Bank financing, sale-law guarantees and temporary housing financing - and construction under close supervision of quality and schedules."),("Handover & registration","Delivering the new apartments, regularising the bylaws and registering in the Land Registry.")],
  consultants_h="The consultant team on every project",
  consultants=["Architect","Structural engineer","Plumbing","Electrical","Safety","Elevators","Hydrologist","Accessibility consultant","Civil defence consultant","Acoustics consultant","Green building consultant","Soil & foundations consultant","Traffic consultant","Agronomist","Tax advisor"],
  ur4_eyebrow="Feasibility check", ur4_h="Tell us about your building",
  ur4_lead="A company representative will contact you for initial details. Our team of experts will assess the building and come back to you with a detailed answer on whether the project is economically feasible - at no cost whatsoever.",
  ur4_call="Prefer to talk?",
  ab_title="About", ab_desc="Engel Real Estate is a family-run boutique construction and development company that operates only in Tel Aviv and manages TAMA 38 projects from inception to completion.",
  ab_eyebrow="About", ab_h="A family-run boutique firm rebuilding Tel Aviv.",
  ab_lead="Engel Real Estate has been engaged in construction and development for years, and is made up of quality professionals in real estate and construction: engineers, architects, project managers, economists, lawyers and marketing managers.",
  ab_img_alt="Rendering of the Ussishkin 46 roof level overlooking Tel Aviv", ab_img_cap="Ussishkin 46 · TAMA 38/2 · under construction",
  ab1_eyebrow="Who we are", ab1_statement='The diverse experience of our leading team is a <span class="em">quality advantage</span> in the industry - and we bring it to every building.',
  ab1_ps=["Our company is experienced in managing all the aspects involved in each project, from inception to completion: from the engineering design stage, through financing, taxation and legal support, marketing and sales - to management and execution.","Our unique working method guarantees close supervision of construction quality, full responsibility for what happens on site and strict adherence to schedules and to every detail. That is how we deliver a variety of projects at the highest standards in the city of Tel Aviv.","Engel Real Estate operates only in the city of Tel Aviv, and has been chosen as a trusted partner by dozens of clients from Tel Aviv for TAMA 38 projects."],
  ab2_eyebrow="Our values", ab2_h="What guides us on every project",
  values=[("One city, one specialty","Engel Real Estate operates only in the city of Tel Aviv, and has been chosen as a trusted partner by dozens of clients from the city for TAMA 38 projects."),("Full responsibility","From planning to keys, responsibility for what happens on site is ours - with close supervision of construction quality and schedules."),("Transparency and accessibility","Residents receive support, peace of mind and regular updates at every stage of the project."),("A boutique standard","A high, comprehensive, luxurious specification, boutique buildings, and a personal consultation with an architect for every resident to plan their apartment interior.")],
  ab3_img_alt="Rendering of a living room in a new apartment", ab3_img_cap="Rendering · a new apartment at a boutique standard", ab3_eyebrow="The team", ab3_h="Quality professionals in real estate and construction",
  ab3_p="On every project we appoint leading consultants in their fields - architect, structural engineer, plumbing, electrical, safety, elevator, acoustics, green building, soil and foundations, traffic, accessibility and civil defence consultants, a hydrologist, an agronomist and a tax advisor - and any other consultant required.",
  ab3_btn1="Our projects", ab3_btn2="Talk to us",
  ct_title="Contact", ct_desc="Interested in an urban renewal project for your building, or in buying an apartment directly from the developer? Leave your details or call 03-6005955.",
  ct_eyebrow="Contact", ct_h="Get in touch",
  ct_lead="Interested in an urban renewal project, or in buying an apartment directly from the developer with no brokerage fee? Leave your details and we will get back to you shortly.",
  ct_phone="Office phone", ct_email="Email", ct_fax="Fax", ct_address="Address", ct_note="Engel Real Estate operates in Tel Aviv only.",
  legal_eyebrow="Legal", terms_h="Terms of Use", terms_desc="Terms of use for the Engel Real Estate website.",
  terms_lead="Welcome to the Engel Real Estate website (the \"Site\"). Use of the Site is subject to the terms and conditions set out below. Please read them carefully, as use of the Site indicates your agreement to them.",
  terms_contact="For questions about these terms, contact us at",
  privacy_h="Privacy Policy", privacy_desc="Privacy policy of the Engel Real Estate website.",
  privacy_lead="We are committed to protecting users' privacy and managing personal information in accordance with the law. This policy explains how we collect, use and protect your information when you use the Site.",
  a11y_h="Accessibility Statement", a11y_desc="Accessibility statement of the Engel Real Estate website: the accessibility adjustments made, the accessibility menu and how to contact us.", a11y_eyebrow="Accessibility",
  nf_title="Page not found", nf_desc="The page you were looking for does not exist.", nf_h="This page hasn't been built yet.", nf_p="The page you were looking for does not exist or has moved. You can go back to the home page or browse the projects.", nf_btn1="Home page", nf_btn2="Projects",
 ),
}

TERMS = {
 "he": [
 ("כללי", ["השימוש באתר מהווה הסכמה מצד המשתמש לכל תנאי השימוש, לרבות מדיניות הפרטיות.", "החברה שומרת לעצמה את הזכות לעדכן ולשנות את תנאי השימוש בכל עת, ולמשתמש לא תהיה כל טענה או דרישה בגין שינויים אלה."]),
 ("שימוש באתר", ["האתר מספק מידע ושירותים הקשורים לנדל״ן, ובפרט לפרויקטים של התחדשות עירונית.", "המשתמש מתחייב לעשות שימוש הוגן, חוקי וסביר באתר ולא לבצע כל פעולה שעלולה לפגוע בפעילות האתר או במשתמשים אחרים.", "החברה רשאית למנוע גישה לאתר לכל משתמש שיפר תנאים אלה או יבצע שימוש בלתי ראוי באתר."]),
 ("תוכן ומידע באתר", ["התכנים באתר ניתנים כמידע כללי בלבד ואינם מהווים ייעוץ משפטי, פיננסי או נדל״ני.", "החברה אינה מתחייבת לכך שהתוכן באתר יהיה מדויק, שלם או עדכני.", "כל הסתמכות על התכנים המופיעים באתר נעשית באחריותו הבלעדית של המשתמש."]),
 ("קישורים לאתרים חיצוניים", ["האתר עשוי לכלול קישורים לאתרים חיצוניים שאינם בשליטת החברה.", "החברה אינה אחראית לתוכן, למדיניות הפרטיות או לנכונות המידע המצוי באתרים חיצוניים אלה."]),
 ("פרטיות ואבטחת מידע", ["החברה מתחייבת לשמור על פרטיות המשתמשים בהתאם למדיניות הפרטיות שלה.", "המשתמש מסכים לכך שהחברה תעשה שימוש במידע אישי שהוא מוסר בהתאם למדיניות הפרטיות.", "למרות מאמצי החברה לאבטח את האתר, אין החברה יכולה להבטיח הגנה מוחלטת מפני חדירות בלתי מורשות."]),
 ("קניין רוחני", ["כל זכויות הקניין הרוחני באתר, לרבות טקסטים, תמונות, עיצוב, קוד תוכנה וסימני מסחר, שייכות לחברה או לצדדים שלישיים שהעניקו לה רישיון שימוש.", "אין להעתיק, לשכפל, להפיץ, לשדר או לפרסם את תכני האתר ללא אישור מראש ובכתב מהחברה."]),
 ("אחריות והגבלת אחריות", ["השימוש באתר נעשה באחריות המשתמש בלבד.", "החברה אינה אחראית לכל נזק ישיר או עקיף שייגרם כתוצאה משימוש או הסתמכות על המידע והשירותים באתר.", "החברה אינה מתחייבת שהאתר יהיה פעיל בכל עת ללא הפרעות או תקלות טכניות."]),
 ("שיפוי", ["המשתמש מתחייב לשפות את החברה בגין כל נזק, הפסד או הוצאה שייגרמו לה עקב הפרת תנאים אלה על ידי המשתמש."]),
 ("הדין החל וסמכות שיפוט", ["על השימוש באתר יחולו אך ורק דיני מדינת ישראל.", "סמכות השיפוט הבלעדית בכל הנוגע לתנאים אלה ולשימוש באתר תהיה לבתי המשפט המוסמכים בתל אביב-יפו."]),
 ],
 "en": [
 ("General", ["Use of the Site constitutes the user's agreement to all of the terms of use, including the privacy policy.", "The Company reserves the right to update and change the terms of use at any time, and the user shall have no claim or demand regarding such changes."]),
 ("Use of the Site", ["The Site provides information and services related to real estate, and in particular to urban renewal projects.", "The user undertakes to make fair, lawful and reasonable use of the Site and not to take any action that may harm the operation of the Site or other users.", "The Company may deny access to the Site to any user who breaches these terms or makes improper use of the Site."]),
 ("Content and information on the Site", ["The content on the Site is provided as general information only and does not constitute legal, financial or real-estate advice.", "The Company does not undertake that the content on the Site will be accurate, complete or up to date.", "Any reliance on the content appearing on the Site is at the user's sole responsibility."]),
 ("Links to external sites", ["The Site may include links to external sites that are not under the Company's control.", "The Company is not responsible for the content, privacy policy or accuracy of information on such external sites."]),
 ("Privacy and information security", ["The Company undertakes to protect users' privacy in accordance with its privacy policy.", "The user agrees that the Company may use personal information the user provides in accordance with the privacy policy.", "Despite the Company's efforts to secure the Site, the Company cannot guarantee absolute protection against unauthorised intrusion."]),
 ("Intellectual property", ["All intellectual property rights in the Site, including texts, images, design, software code and trademarks, belong to the Company or to third parties that have licensed their use to it.", "The Site's content may not be copied, reproduced, distributed, transmitted or published without the Company's prior written consent."]),
 ("Liability and limitation of liability", ["Use of the Site is at the user's sole responsibility.", "The Company is not liable for any direct or indirect damage caused as a result of use of, or reliance on, the information and services on the Site.", "The Company does not undertake that the Site will be available at all times without interruptions or technical faults."]),
 ("Indemnification", ["The user undertakes to indemnify the Company for any damage, loss or expense caused to it as a result of the user's breach of these terms."]),
 ("Governing law and jurisdiction", ["Use of the Site is governed solely by the laws of the State of Israel.", "Exclusive jurisdiction in all matters relating to these terms and to use of the Site shall lie with the competent courts of Tel Aviv-Jaffa."]),
 ],
}

PRIVACY = {
 "he": '''<h2>איסוף מידע</h2>
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
<p>החברה רשאית לעדכן מדיניות זו מעת לעת. עדכונים מהותיים יפורסמו באתר, והמשך השימוש באתר לאחר עדכון המדיניות מהווה הסכמה לתנאים החדשים.</p>''',
 "en": '''<h2>Information we collect</h2>
<p>We may collect personal information that you provide to us, including but not limited to: full name, email address, phone number and information submitted through forms on the Site.</p>
<p>We may also collect technical information when you use the Site, such as IP address, browser type and operating system, and access times and activity on the Site.</p>
<h2>How we use information</h2>
<ul><li>Providing services and responding to users' enquiries.</li><li>Sending updates, promotional information and important notices (subject to the user's consent).</li><li>Improving the user experience and tailoring the Site to personal needs.</li><li>Complying with the law and with law-enforcement authorities where required.</li></ul>
<h2>Sharing information with third parties</h2>
<p>We will not share personal information with third parties, except in the following cases:</p>
<ul><li>Where required to provide the services or operate the Site (such as hosting and analytics providers).</li><li>At the demand of a competent authority or as required by law.</li><li>In the event of a merger, acquisition or transfer of the Site's activity to a third party.</li></ul>
<h2>Information security</h2>
<p>We take appropriate technological and organisational measures to protect users' personal information from unauthorised access, alteration, disclosure or destruction. Despite our efforts, we cannot guarantee absolute security of the data, and use of the Site is at the user's responsibility.</p>
<h2>Cookies and tracking technologies</h2>
<p>We may use cookies and similar technologies to improve the user experience, analyse use of the Site and tailor content and advertising. You can manage cookie preferences through your browser settings and block them, but this may affect your experience on the Site.</p>
<h2>Your rights</h2>
<p>You may request to review, correct or delete the personal information collected about you, in accordance with the law. For privacy requests, contact us at <a href="mailto:{EMAIL}" style="font-weight:600">{EMAIL}</a>.</p>
<h2>Changes to this policy</h2>
<p>The Company may update this policy from time to time. Material updates will be published on the Site, and continued use of the Site after an update constitutes agreement to the new terms.</p>''',
}

A11Y = {
 "he": '''<p class="lead">אנו באנגל נדל״ן משקיעים ככל שניתן על מנת לספק לכל לקוחותינו שירות שוויוני ונגיש, בכדי לאפשר חוויית גלישה נוחה לכלל האוכלוסייה, לרבות אנשים עם מוגבלויות, בהתאם לחוק שוויון זכויות לאנשים עם מוגבלות.</p>''',
 "he_body": '''<p>באתר זה בוצעו התאמות נגישות על פי דרישות תקנות שוויון זכויות לאנשים עם מוגבלות (התאמות נגישות לשירות), התשע״ג-2013, בצורה קפדנית ככל שניתן.</p>
<p>התאמות הנגישות בוצעו על פי המלצות התקן הישראלי (ת״י 5568) לנגישות תכנים באינטרנט ברמת AA ומסמך WCAG 2.0 הבינלאומי.</p>
<h2>מידע על נגישות האתר</h2>
<p>באתר מוטמע תפריט נגישות, הנפתח באמצעות כפתור הנגישות בתחתית המסך. התפריט כולל:</p>
<ul><li>הגדלת טקסט והקטנת טקסט</li><li>גווני אפור</li><li>ניגודיות גבוהה וניגודיות הפוכה</li><li>רקע בהיר</li><li>הדגשת קישורים</li><li>פונט קריא</li><li>איפוס ההגדרות</li></ul>
<p>בנוסף, האתר נבנה עם מבנה כותרות תקין, ניווט מלא באמצעות מקלדת, טקסט חלופי לתמונות, תמיכה בהעדפת הפחתת תנועה (Reduced Motion) ותגיות ARIA בתפריטים ובטפסים.</p>
<h2>פנייה בנושא נגישות</h2>
<p>אנו ממשיכים לפעול במאמץ לשפר את נגישות האתר כחלק ממחויבותנו לאפשר לכלל האוכלוסייה לקבל שירות שווה והוגן. במידה ונתקלתם בבעיה כלשהי בנושא הנגישות, נשמח שתעדכנו אותנו ואנו נעשה כל מאמץ למצוא עבורכם פתרון מתאים ולטפל בבעיה בהקדם האפשרי.</p>
<p>טלפון: <a href="tel:{PHONE_TEL}" dir="ltr" style="font-weight:600">{PHONE}</a><br>דוא״ל: <a href="mailto:{EMAIL}" style="font-weight:600">{EMAIL}</a></p>
<h2>פרסום הצהרת הנגישות</h2>
<p>הצהרת הנגישות עודכנה ביום {A11Y_DATE}.</p>''',
 "en": '''<p class="lead">At Engel Real Estate we invest as much as possible in providing all our clients with equal and accessible service, to allow a comfortable browsing experience for the entire population, including people with disabilities, in accordance with the Equal Rights for Persons with Disabilities Law.</p>''',
 "en_body": '''<p>Accessibility adjustments were made on this site in accordance with the Equal Rights for Persons with Disabilities Regulations (Service Accessibility Adjustments), 2013, as strictly as possible.</p>
<p>The adjustments follow the recommendations of Israeli Standard 5568 for web content accessibility at level AA and the international WCAG 2.0 document.</p>
<h2>Site accessibility</h2>
<p>The site includes an accessibility menu, opened with the accessibility button at the bottom of the screen. The menu includes:</p>
<ul><li>Increase and decrease text size</li><li>Grayscale</li><li>High contrast and inverted contrast</li><li>Light background</li><li>Highlight links</li><li>Readable font</li><li>Reset settings</li></ul>
<p>In addition, the site is built with a proper heading structure, full keyboard navigation, alternative text for images, support for the Reduced Motion preference and ARIA attributes in menus and forms.</p>
<h2>Accessibility enquiries</h2>
<p>We continue to work on improving the site's accessibility as part of our commitment to providing equal and fair service to everyone. If you encounter any accessibility problem, please let us know and we will make every effort to find a suitable solution and resolve it as soon as possible.</p>
<p>Phone: <a href="tel:{PHONE_TEL}" dir="ltr" style="font-weight:600">{PHONE}</a><br>Email: <a href="mailto:{EMAIL}" style="font-weight:600">{EMAIL}</a></p>
<h2>Publication of the accessibility statement</h2>
<p>This accessibility statement was last updated on {A11Y_DATE}.</p>''',
}

# ---------------------------------------------------------------- pages
def page_home(L):
    c = C[L]; P = LANGS[L]["prefix"]
    cards = "".join(card(L, p, d=i % 3) for i, p in enumerate(PROJECTS))
    extra = preload("hero-tall", "45vw", "(min-width:900px)") + "\n" + preload("hero-wide", "100vw", "(max-width:899px)")
    facts = "".join(f"<li><b>{b}</b>{s}</li>" for b, s in c["facts"])
    t2 = "".join(f"<li>{x}</li>" for x in c["t2_home"]); t1 = "".join(f"<li>{x}</li>" for x in c["t1_home"])
    steps = "".join(f"<li><b>{b}</b><p>{s}</p></li>" for b, s in c["steps"])
    def arealist(slugs):
        out = ""
        for sl in slugs:
            p = BY_SLUG[sl]; st = c["area_status"].get(sl, STATUS[L][p["status"]])
            out += f'<li><a href="{P}/projects/{sl}/">{p["title"][L]}</a><span>{st}</span></li>'
        return out
    icons = ['<path d="M4 28h24M8 28V10l8-6 8 6v18M13 28v-8h6v8"/>', '<circle cx="16" cy="16" r="12"/><path d="M16 8v8l5 3"/>', '<path d="M3 16s5-8 13-8 13 8 13 8-5 8-13 8S3 16 3 16Z"/><circle cx="16" cy="16" r="4"/>', '<path d="M16 3 5 8v8c0 7 5 11 11 13 6-2 11-6 11-13V8L16 3Z"/><path d="m11 16 3 3 7-7"/>']
    why = "".join(f'<li class="rv" data-d="{i}"><svg class="ic" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.3">{icons[i]}</svg><b>{b}</b><p>{s}</p></li>' for i, (b, s) in enumerate(c["why"]))
    disc = "".join(f"<li>{x}</li>" for x in c["disciplines"])
    return head(L, c["home_title"], c["home_desc"], "/", extra) + header(L, "/", "/") + f'''
<section class="hero">
  <div class="wrap">
    <div class="hero__grid">
      <div class="hero__copy">
        <p class="eyebrow">{c['hero_eyebrow']}</p>
        <h1 class="h-xl">{c['hero_h']}</h1>
        <p class="lead">{c['hero_lead']}</p>
        <div class="actions"><a class="btn btn--solid" href="{P}/urban-renewal/#feasibility">{c['hero_btn1']} {ARROW}</a><a class="btn btn--ghost" href="{P}/projects/">{c['hero_btn2']}</a></div>
      </div>
      <div class="hero__media">
        {pic("hero-tall", c['hero_alt'], "(min-width:1320px) 600px, (min-width:900px) 45vw, 0px", eager=True, cls="tall")}
        {pic("hero-wide", c['hero_alt'], "(max-width:899px) 100vw, 0px", eager=True, cls="wide")}
        <div class="hero__cap">{c['hero_cap']}<b>{c['hero_cap_b']}</b></div>
      </div>
    </div>
    <div class="facts"><ul>{facts}</ul></div>
  </div>
</section>

<section class="section" id="projects">
  <div class="wrap">
    <div class="section-head">
      <div class="rv"><p class="eyebrow"><span class="num">01</span> {c['s1_eyebrow']}</p><h2 class="h-l">{c['s1_h']}</h2></div>
      <a class="link more rv" href="{P}/projects/">{c['s1_more']} {ARROW}</a>
    </div>
    <div class="grid grid--3">{cards}</div>
  </div>
</section>

<section class="section section--dark grain">
  <div class="wrap">
    <div class="split split--wide">
      <div class="rv"><p class="eyebrow"><span class="num">02</span> {c['s2_eyebrow']}</p><p class="statement">{c['s2_statement']}</p></div>
      <div class="rv" data-d="1">
        <p class="lead" style="max-width:none">{c['s2_lead']}</p>
        <p style="color:var(--on-dark-2)">{c['s2_p']}</p>
        <ul class="tags" style="margin:26px 0 30px">{disc}</ul>
        <a class="btn btn--ghost" href="{P}/about/">{c['s2_btn']} {ARROW}</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div class="rv"><p class="eyebrow"><span class="num">03</span> {c['s3_eyebrow']}</p><h2 class="h-l">{c['s3_h']}</h2></div>
      <a class="link more rv" href="{P}/urban-renewal/">{c['s3_more']} {ARROW}</a>
    </div>
    <div class="tracks">
      <div class="track rv"><p class="track__k">{c['t2_k']}</p><h3>{c['t2_h']}</h3><p>{c['t2_p']}</p><ul>{t2}</ul></div>
      <div class="track rv" data-d="1"><p class="track__k">{c['t1_k']}</p><h3>{c['t1_h']}</h3><p>{c['t1_p']}</p><ul>{t1}</ul></div>
    </div>
    <ol class="steps rv" style="margin-top:clamp(40px,5vw,72px)">{steps}</ol>
  </div>
</section>

<section class="section--stone">
  <div class="band">{pic("yarkon-panorama", c['band_alt'], "100vw")}</div>
  <div class="wrap section">
    <div class="section-head"><div class="rv"><p class="eyebrow"><span class="num">04</span> {c['s4_eyebrow']}</p><h2 class="h-l">{c['s4_h']}</h2></div></div>
    <div class="areas">
      <div class="area rv"><h3>{c['area1_h']}</h3><p>{c['area1_p']}</p><ul>{arealist(["ussishkin-46","ussishkin-52","prague-3","bartenura-3-5"])}</ul></div>
      <div class="area rv" data-d="1"><h3>{c['area2_h']}</h3><p>{c['area2_p']}</p><ul>{arealist(["berdichevsky-17","marmorek-26"])}</ul></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div class="rv"><p class="eyebrow"><span class="num">05</span> {c['s5_eyebrow']}</p><h2 class="h-l">{c['s5_h']}</h2></div></div>
    <ul class="why">{why}</ul>
  </div>
</section>
''' + cta_section(L) + footer(L)

def page_projects(L):
    c = C[L]
    cards = "".join(card(L, p, d=i % 3) for i, p in enumerate(PROJECTS))
    filters = "".join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k=="all" else "false"}">{n}</button>' for k, n in c["filters"])
    return head(L, c["pl_title"], c["pl_desc"], "/projects/") + header(L, "/projects/", "/projects/") + f'''
<section class="page-head"><div class="wrap"><p class="eyebrow">{c['pl_eyebrow']}</p><h1 class="h-xl">{c['pl_h']}</h1><p class="lead">{c['pl_lead']}</p></div></section>
<section class="section--tight" style="padding-top:0">
  <div class="wrap">
    <div class="filters" role="group" aria-label="{c['filter_label']}">{filters}</div>
    <div class="grid grid--3">{cards}</div>
    <p class="empty" hidden>{c['pl_empty']}</p>
    <p class="note" style="margin-top:36px">{c['pl_note']}</p>
  </div>
</section>
''' + cta_section(L) + footer(L)

def page_project(L, p, i):
    c = C[L]; t = T[L]; P = LANGS[L]["prefix"]
    prev = PROJECTS[i - 1]; nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    hero_img = p["wide"] or p["card"]
    path = f"/projects/{p['slug']}/"
    extra = preload(hero_img, "(min-width:1320px) 1208px, 92vw")
    specs = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in p["specs"][L])
    loc = "".join(f'<li><span class="n">0{n+1}</span><p>{x}</p></li>' for n, x in enumerate(p["location"][L]))
    gallery = ""
    if p["gallery"]:
        figs = "".join(f'<figure class="{cls}">{pic(name, alt[L], "(min-width:1320px) 1208px, 92vw" if cls else "(min-width:760px) 45vw, 92vw")}<figcaption>{cap[L]}</figcaption></figure>' for name, alt, cap, cls in p["gallery"])
        gallery = f'<section class="section--tight"><div class="wrap"><p class="eyebrow">{c["pp_gallery"]}</p><div class="gallery">{figs}</div><p class="note" style="margin-top:14px">{c["pp_gallery_note"]}</p></div></section>'
    units = ""
    if p["units"]:
        note = p.get("units_note")
        def unit_html(u):
            rows = u["rows"][L]
            body = f'<ul>{"".join(f"<li><span>{k}</span><span>{v}</span></li>" for k, v in rows)}</ul>' if rows else f'<p class="unit__note">{note[L] if note else ""}</p>'
            return f'<div class="unit rv"><h3>{u["name"][L]}</h3><p class="sub">{u["sub"][L]}</p>{body}</div>'
        us = "".join(unit_html(u) for u in p["units"])
        plans = ""
        if p.get("plans"):
            figs = "".join(f'<figure class="plan">{pic(name, cap[L], "(min-width:760px) 45vw, 92vw")}<figcaption>{cap[L]}</figcaption></figure>' for name, cap in p["plans"])
            pdf = f'<a class="btn btn--ghost" href="{p["plan_pdf"]}" download>{c["pp_plan_pdf"]} {ARROW}</a>' if p.get("plan_pdf") else ""
            plans = f'<div class="plans"><p class="eyebrow" style="margin-top:44px">{c["pp_plans"]}</p><div class="gallery gallery--plans">{figs}</div><div class="actions" style="margin-top:22px">{pdf}</div></div>'
        units = f'''<section class="section section--stone"><div class="wrap">
  <div class="section-head"><div class="rv"><p class="eyebrow">{c['pp_units_eyebrow']}</p><h2 class="h-l">{c['pp_units_h']}</h2></div><a class="link more rv" href="{P}/contact/?project={p['slug']}">{c['pp_units_more']} {ARROW}</a></div>
  <div class="units">{us}</div>
  {plans}
</div></section>'''
    extras = ""
    for g in p.get("extras", []):
        figs = "".join(f'<figure>{pic(name, cap[L], "(min-width:760px) 45vw, 92vw")}<figcaption>{cap[L]}</figcaption></figure>' for name, cap in g["imgs"])
        extras += f'<section class="section--tight"><div class="wrap"><p class="eyebrow">{g["title"][L]}</p><div class="gallery">{figs}</div></div></section>'
    head_html = f'<div><p class="eyebrow">{p["area"][L]} · {t["tlv"]}</p><h1 class="h-xl">{p["title"][L]}</h1></div><span class="pill" data-s="{p["status"]}">{STATUS[L][p["status"]]}</span>'
    if p["wide"]:
        hero_block = f'<div class="proj-hero__media">{pic(hero_img, t["card_alt"].format(t=p["title"][L]), "(min-width:1320px) 1208px, 92vw", eager=True)}</div><div class="proj-hero__head">{head_html}</div>'
    else:
        hero_block = f'<div class="proj-hero__compact"><div class="proj-hero__thumb">{pic(hero_img, t["card_alt"].format(t=p["title"][L]), "(min-width:900px) 340px, 70vw", eager=True)}</div><div class="proj-hero__head proj-hero__head--compact">{head_html}</div></div>'
    return head(L, f"{p['title'][L]} - {p['type'][L]}", f"{p['title'][L]}, {p['area'][L]} {t['tlv']}. {p['short'][L]}", path, extra) + header(L, "/projects/", path) + f'''
<section class="proj-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="{c['crumbs_label']}"><a href="{P}/">{t['crumbs_home']}</a><span>/</span><a href="{P}/projects/">{t['crumbs_projects']}</a><span>/</span><span>{p['title'][L]}</span></nav>
    {hero_block}
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">{c['pp_about']}</p>
        <p class="lead" style="max-width:none">{p['overview'][L][0]}</p>
        {"".join(f"<p>{x}</p>" for x in p['overview'][L][1:])}
        <p class="eyebrow" style="margin-top:40px">{c['pp_loc']}</p>
        <ul class="list-hair">{loc}</ul>
      </div>
      <div class="split__sticky">
        <p class="eyebrow">{c['pp_specs']}</p>
        <dl class="specs">{specs}</dl>
        <div class="actions" style="margin-top:28px"><a class="btn btn--solid" href="{P}/contact/?project={p['slug']}">{c['pp_more']} {ARROW}</a><a class="btn btn--ghost" href="tel:{PHONE_TEL}"><span dir="ltr">{PHONE}</span></a></div>
      </div>
    </div>
  </div>
</section>
{gallery}
{extras}
{units}
<section class="section--tight"><div class="wrap">
  <nav class="proj-nav" aria-label="{c['pp_nav_label']}">
    <a href="{P}/projects/{prev['slug']}/"><small>{c['pp_prev']}</small><b>{prev['title'][L]}</b></a>
    <a class="next" href="{P}/projects/{nxt['slug']}/"><small>{c['pp_next']}</small><b>{nxt['title'][L]}</b></a>
  </nav>
</div></section>
''' + cta_section(L) + footer(L)

def page_urban(L):
    c = C[L]
    t2 = "".join(f"<li>{x}</li>" for x in c["t2_full"]); t1 = "".join(f"<li>{x}</li>" for x in c["t1_full"])
    sup = "".join(f'<li><span class="n">0{i+1}</span><div><b>{b}</b><p>{s}</p></div></li>' for i, (b, s) in enumerate(c["support"]))
    steps = "".join(f"<li><b>{b}</b><p>{s}</p></li>" for b, s in c["steps_full"])
    cons = "".join(f"<li>{x}</li>" for x in c["consultants"])
    return head(L, c["ur_title"], c["ur_desc"], "/urban-renewal/") + header(L, "/urban-renewal/", "/urban-renewal/") + f'''
<section class="page-head">
  <div class="wrap">
    <p class="eyebrow">{c['ur_eyebrow']}</p>
    <h1 class="h-xl">{c['ur_h']}</h1>
    <p class="lead">{c['ur_lead']}</p>
    <div class="actions" style="margin-top:30px"><a class="btn btn--solid" href="#feasibility">{c['ur_btn']} {ARROW}</a></div>
  </div>
</section>
<section class="section section--paper" style="border-top:1px solid var(--line)">
  <div class="wrap">
    <div class="section-head"><div class="rv"><p class="eyebrow"><span class="num">01</span> {c['ur1_eyebrow']}</p><h2 class="h-l">{c['ur1_h']}</h2></div></div>
    <div class="tracks">
      <div class="track rv"><p class="track__k">{c['t2_k']}</p><h3>{c['t2_h']}</h3><p>{c['t2_p_full']}</p><ul>{t2}</ul></div>
      <div class="track rv" data-d="1"><p class="track__k">{c['t1_k']}</p><h3>{c['t1_h']}</h3><p>{c['t1_p_full']}</p><ul>{t1}</ul></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="split split--wide">
      <div class="rv"><p class="eyebrow"><span class="num">02</span> {c['ur2_eyebrow']}</p><p class="statement">{c['ur2_statement']}</p></div>
      <div class="rv" data-d="1"><ul class="list-hair">{sup}</ul></div>
    </div>
  </div>
</section>
<section class="section section--dark grain">
  <div class="wrap">
    <div class="section-head"><div class="rv"><p class="eyebrow"><span class="num">03</span> {c['ur3_eyebrow']}</p><h2 class="h-l">{c['ur3_h']}</h2></div></div>
    <ol class="steps rv">{steps}</ol>
    <div class="rv" style="margin-top:clamp(40px,5vw,72px)"><p class="eyebrow">{c['consultants_h']}</p><ul class="tags">{cons}</ul></div>
  </div>
</section>
<section class="section" id="feasibility">
  <div class="wrap">
    <div class="split">
      <div class="split__sticky">
        <p class="eyebrow"><span class="num">04</span> {c['ur4_eyebrow']}</p>
        <h2 class="h-l">{c['ur4_h']}</h2>
        <p class="lead" style="margin-top:20px">{c['ur4_lead']}</p>
        <p class="note">{c['ur4_call']} <a href="tel:{PHONE_TEL}" dir="ltr" style="font-weight:600">{PHONE}</a></p>
      </div>
      <div>{form(L, "feasibility")}</div>
    </div>
  </div>
</section>
''' + footer(L)

def page_about(L):
    c = C[L]; P = LANGS[L]["prefix"]
    ps = "".join(f"<p>{x}</p>" for x in c["ab1_ps"])
    vals = "".join(f'<li><span class="n">0{i+1}</span><div><b>{b}</b><p>{s}</p></div></li>' for i, (b, s) in enumerate(c["values"]))
    disc = "".join(f"<li>{x}</li>" for x in c["disciplines"])
    return head(L, c["ab_title"], c["ab_desc"], "/about/") + header(L, "/about/", "/about/") + f'''
<section class="page-head"><div class="wrap"><p class="eyebrow">{c['ab_eyebrow']}</p><h1 class="h-xl">{c['ab_h']}</h1><p class="lead">{c['ab_lead']}</p></div></section>
<section class="section--tight" style="padding-top:0">
  <div class="wrap"><figure class="fig" style="aspect-ratio:2/1">{pic("ussishkin-46-roof", c['ab_img_alt'], "(min-width:1320px) 1208px, 92vw", eager=True)}<figcaption>{c['ab_img_cap']}</figcaption></figure></div>
</section>
<section class="section">
  <div class="wrap">
    <div class="split split--wide">
      <div class="rv"><p class="eyebrow"><span class="num">01</span> {c['ab1_eyebrow']}</p><p class="statement">{c['ab1_statement']}</p></div>
      <div class="rv" data-d="1">{ps}</div>
    </div>
  </div>
</section>
<section class="section section--dark grain">
  <div class="wrap">
    <div class="section-head"><div class="rv"><p class="eyebrow"><span class="num">02</span> {c['ab2_eyebrow']}</p><h2 class="h-l">{c['ab2_h']}</h2></div></div>
    <ul class="list-hair rv">{vals}</ul>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="split">
      <figure class="fig rv" style="aspect-ratio:3/2">{pic("interior-living", c['ab3_img_alt'], "(min-width:900px) 45vw, 92vw")}<figcaption>{c['ab3_img_cap']}</figcaption></figure>
      <div class="rv" data-d="1">
        <p class="eyebrow"><span class="num">03</span> {c['ab3_eyebrow']}</p>
        <h2 class="h-m">{c['ab3_h']}</h2>
        <p style="margin-top:18px">{c['ab3_p']}</p>
        <ul class="tags" style="margin:22px 0 30px">{disc}</ul>
        <div class="actions"><a class="btn btn--solid" href="{P}/projects/">{c['ab3_btn1']} {ARROW}</a><a class="btn btn--ghost" href="{P}/contact/">{c['ab3_btn2']}</a></div>
      </div>
    </div>
  </div>
</section>
''' + cta_section(L) + footer(L)

def page_contact(L):
    c = C[L]; lg = LANGS[L]
    return head(L, c["ct_title"], c["ct_desc"], "/contact/") + header(L, "/contact/", "/contact/") + f'''
<section class="page-head"><div class="wrap"><p class="eyebrow">{c['ct_eyebrow']}</p><h1 class="h-xl">{c['ct_h']}</h1><p class="lead">{c['ct_lead']}</p></div></section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="split">
      <div>
        <ul class="contact-list">
          <li><small>{c['ct_phone']}</small><a class="ltr" href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><small>{c['ct_email']}</small><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><small>{c['ct_fax']}</small><span class="ltr">{FAX}</span></li>
          <li><small>{c['ct_address']}</small><span>{lg['address']}</span></li>
        </ul>
        <p class="note" style="margin-top:28px">{c['ct_note']}</p>
      </div>
      <div>{form(L, "contact")}</div>
    </div>
  </div>
</section>
''' + footer(L)

def page_terms(L):
    c = C[L]
    body = "".join(f"<h2>{i+1}. {h}</h2>" + "".join(f"<p>{i+1}.{j+1}. {s}</p>" for j, s in enumerate(ps)) for i, (h, ps) in enumerate(TERMS[L]))
    return head(L, c["terms_h"], c["terms_desc"], "/terms/") + header(L, "", "/terms/") + f'''
<section class="page-head"><div class="wrap"><p class="eyebrow">{c['legal_eyebrow']}</p><h1 class="h-xl">{c['terms_h']}</h1><p class="lead">{c['terms_lead']}</p></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="prose">{body}<p style="margin-top:2em">{c['terms_contact']} <a href="mailto:{EMAIL}" style="font-weight:600">{EMAIL}</a>.</p></div></div></section>
''' + footer(L)

def page_privacy(L):
    c = C[L]
    return head(L, c["privacy_h"], c["privacy_desc"], "/privacy/") + header(L, "", "/privacy/") + f'''
<section class="page-head"><div class="wrap"><p class="eyebrow">{c['legal_eyebrow']}</p><h1 class="h-xl">{c['privacy_h']}</h1><p class="lead">{c['privacy_lead']}</p></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="prose">{PRIVACY[L].format(EMAIL=EMAIL)}</div></div></section>
''' + footer(L)

def page_accessibility(L):
    c = C[L]
    return head(L, c["a11y_h"], c["a11y_desc"], "/accessibility/") + header(L, "", "/accessibility/") + f'''
<section class="page-head"><div class="wrap"><p class="eyebrow">{c['a11y_eyebrow']}</p><h1 class="h-xl">{c['a11y_h']}</h1>{A11Y[L]}</div></section>
<section class="section" style="padding-top:0"><div class="wrap"><div class="prose">{A11Y[L+"_body"].format(PHONE=PHONE, PHONE_TEL=PHONE_TEL, EMAIL=EMAIL, A11Y_DATE=A11Y_DATE)}</div></div></section>
''' + footer(L)

def page_404(L):
    c = C[L]; P = LANGS[L]["prefix"]
    return head(L, c["nf_title"], c["nf_desc"], "/404.html") + header(L, "", "/") + f'''
<section class="page-head" style="min-height:50vh"><div class="wrap"><p class="eyebrow">404</p><h1 class="h-xl">{c['nf_h']}</h1><p class="lead">{c['nf_p']}</p><div class="actions" style="margin-top:28px"><a class="btn btn--solid" href="{P}/">{c['nf_btn1']} {ARROW}</a><a class="btn btn--ghost" href="{P}/projects/">{c['nf_btn2']}</a></div></div></section>
''' + footer(L)

HEADERS = '''/*
  X-Robots-Tag: noindex
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN

/assets/*
  Cache-Control: public, max-age=31536000, immutable
'''

if __name__ == "__main__":
    for L in ("he", "en"):
        write(L, "/", page_home(L))
        write(L, "/projects/", page_projects(L))
        for i, p in enumerate(PROJECTS): write(L, f"/projects/{p['slug']}/", page_project(L, p, i))
        write(L, "/urban-renewal/", page_urban(L))
        write(L, "/about/", page_about(L))
        write(L, "/contact/", page_contact(L))
        write(L, "/terms/", page_terms(L))
        write(L, "/privacy/", page_privacy(L))
        write(L, "/accessibility/", page_accessibility(L))
    urls = []
    for L in ("he", "en"):
        P = LANGS[L]["prefix"]
        for path in ["/", "/projects/"] + [f"/projects/{p['slug']}/" for p in PROJECTS] + ["/urban-renewal/", "/about/", "/contact/", "/terms/", "/privacy/", "/accessibility/"]:
            urls.append(f'<url><loc>{SITE_URL}{P}{path}</loc><xhtml:link rel="alternate" hreflang="he" href="{SITE_URL}{path}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}/en{path}"/></url>')
    write("he", "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>'+"\n"+'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+"\n"+"\n".join(urls)+"\n</urlset>\n")
    write("he", "404.html", page_404("he"))
    write("he", "_headers", HEADERS if PREVIEW else HEADERS.replace("  X-Robots-Tag: noindex\n", ""))
    write("he", "robots.txt", "User-agent: *\nDisallow: /\n" if PREVIEW else f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
