# engelnadlan

Speculative redesign of [engelnadlan.co.il](https://www.engelnadlan.co.il/) – a boutique
urban-renewal (TAMA 38) developer working only in Tel Aviv. Static, Hebrew-first (RTL) with a
full English mirror under `/en/`, dependency-free, built for Cloudflare Pages.

## Status

| | |
|---|---|
| **Domain** | `https://engelnadlan.co.il` |
| **Pages URL** | `https://engelnadlan.pages.dev` |
| **Storage mode** | `Standard` (`standard`) |
| **Storage account** | `jetvaults` |
| **Public storage** | `https://jetvaults.blob.core.windows.net/engelnadlan/` |
| **Private storage** | `https://jetvaults.blob.core.windows.net/engelnadlan-private/` |
| **Public container** | `engelnadlan` |
| **Private container** | `engelnadlan-private` |
| **Activated** | No |

## Nameservers

Set these at your domain registrar:

```
gordon.ns.cloudflare.com
sureena.ns.cloudflare.com
```

## Layout

```
tools/build.py            page generator – ALL copy (he + en), project data and page templates live here
tools/optimize_images.py  turns the original renderings into responsive AVIF + WebP variants
wwwroot/                  the deployed site (only this folder is served)
  index.html              home
  projects/               listing + one folder per project (ussishkin-46, prague-3, ...)
  urban-renewal/          התחדשות עירונית + feasibility form (#feasibility)
  about/  contact/  terms/  privacy/  accessibility/  404.html
  en/                     English (LTR) mirror of every page; header has a language switch
  assets/css/site.css     hand-written stylesheet (self-hosted @font-face rules at the top)
  assets/js/site.js       ~3 KB: mobile menu, scroll reveal, project filter, form submit
  assets/js/a11y.js       accessibility menu (mirrors + translates itself on /en/ pages)
  assets/fonts/           Frank Ruhl Libre 300/400 + Assistant 300/400/600, hebrew + latin subsets
  assets/img/             generated AVIF/WebP variants (do not edit by hand)
  _headers                Cloudflare Pages headers (noindex while in preview, immutable asset cache)
  robots.txt              Disallow all while in preview
```

## Local run

```powershell
python tools/build.py            # regenerate the HTML pages (needs Pillow: pip install pillow)
cd wwwroot; python -m http.server 8765
# open http://127.0.0.1:8765/
```

Edit copy/projects in `tools/build.py` and rebuild. Edit styles directly in `wwwroot/assets/css/site.css`.

### Images

Originals are not committed (60 MB). To regenerate the optimized variants, put the source
files in a folder and run:

```powershell
python tools/optimize_images.py <folder-with-originals>
```

The manifest at the top of that script maps each output name to a source file, crop ratio,
focal point and the widths to emit.

## Deploy

Any push to `main` publishes through Cloudflare Pages. Only `wwwroot/` is served.

### Going live checklist

1. In `tools/build.py` set `PREVIEW = False` (removes `noindex`, adds canonical URLs, opens robots.txt).
2. Put a real Web3Forms access key in `WEB3FORMS_KEY` so the contact / feasibility forms deliver to office@engelnadlan.co.il.
3. Rebuild, review, push.
4. Point the nameservers above at Cloudflare and run the JetVaults activation workflow.
