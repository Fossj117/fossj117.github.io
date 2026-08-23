# Handoff: integrating the Cambridge turkey roost map into a Jekyll blog

Written 2026-08-23 by the agent that built the map. Audience: the agent implementing this in the blog repo.
Owner's stated preferences: **simple, clear visual design; a street basemap with street names and usual reference points; dates must be visible and recent vs. older reports distinguishable.**

## 1. What the materials are

| File | What it is |
|---|---|
| `turkey_roost_map.html` | Standalone Leaflet 1.9.4 map, ~40 KB, no build step. Data is inlined as `const DATA = [...]` (line ~56). Loads Leaflet CSS/JS from `https://unpkg.com/leaflet@1.9.4/dist/` and tiles from `https://tile.openstreetmap.org/{z}/{x}/{y}.png`. No other dependencies. |
| `turkey_roost_reports.json` | The 40 records (array of objects). Source of truth for the map data. |
| `turkey_roost_reports.csv` | Same 40 records flattened (extra_sources omitted) — intended as a downloadable "source list". |
| `turkey_roost_records.py` | Hand-curated Python that generates the JSON (edit this to add/correct reports). |
| `build_turkey_roost_map.py` | `python3 build_turkey_roost_map.py out.html out.csv in.json` — regenerates HTML+CSV from the JSON. |
| `README_turkey_roosts.md` | Method, findings, cross-check against an earlier effort. Good material for the blog post's prose. |

### Record schema (JSON)
```
id (int), location_name, neighborhood, lat, lon (WGS84 decimal),
uncertainty_m (int; radius of the drawn circle),
evidence_type: "roost" | "daytime_only",
roost_type: "tree" | "tree/roof" | "fence" | "unknown",
confidence: "high" | "medium" | "low",
year (int; used by the date slider and outline style),
date_or_period (free text shown to readers),
source_title, source_url, quote (verbatim, <=300 chars), notes,
extra_sources: [{title, url}, ...]   (may be empty)
```
Content: 20 `roost` records, 20 `daytime_only`; years 2012–2026; most in Cambridge MA (a few context points in Arlington, Medford, Charlestown, Somerville). All coordinates are placements from text descriptions, not GPS — the uncertainty circle is a judgment call and should stay visible.

### What the map does (so it can be reproduced or restyled faithfully)
- Left sidebar (360 px) + map. Map centre `[42.3765, -71.118]`, zoom 14; scale bar.
- Each record = a filled circle of radius `uncertainty_m` (non-interactive) + a clickable dot.
  - Colour: roost = orange `#f4a261` / stroke `#b5561d`; daytime_only = grey `#bbb` / `#777`.
  - Recency via outline: `year>=2024` solid 3 px; `2019–2023` 1.5 px; `<2019` 2 px dashed `4 4`.
  - Circles > 500 m are drawn fainter (fillOpacity 0.06) so area-level reports don't dominate.
- Popup: name, neighbourhood, tags (roost/daytime, roost_type, confidence), date + ±uncertainty, blockquote quote, source link (`target=_blank`), extra source links, notes.
- Sidebar filters: evidence type checkboxes, confidence checkboxes, year slider (2012–2026, "show reports from YEAR onward"), live count, clickable list sorted roost-first then newest-first, and a caveat note. All filter logic is in the inline `<script>`; function `refresh()` re-renders list and layers.

## 2. Integration options

### Option A — iframe (recommended first pass; no edits to the map)
1. Copy to the repo: `assets/turkeys/turkey_roost_map.html`, `assets/turkeys/turkey_roost_reports.csv`, optionally `.json`.
   The HTML has **no front matter**, so Jekyll copies it verbatim. Confirm `assets/` is not in `exclude:` in `_config.yml`.
2. In the post/page:
   ```html
   <iframe src="{{ '/assets/turkeys/turkey_roost_map.html' | relative_url }}"
           style="width:100%;height:80vh;min-height:520px;border:0"
           title="Cambridge MA wild turkey roost map" loading="lazy"></iframe>
   ```
   plus a link: `[Download the source list (CSV)]({{ '/assets/turkeys/turkey_roost_reports.csv' | relative_url }})`.
3. On narrow screens the sidebar is `min-width:300px`, so inside a mobile-width iframe the map gets squeezed. If that matters, wrap the iframe in a container with `min-width:700px; overflow-x:auto`, or do Option B and add a media query that stacks the sidebar above the map.

### Option B — native page, data in `_data/` (cleaner, theme-styled, editable in-repo)
1. `_data/turkey_roosts.json` ← copy of `turkey_roost_reports.json`. Keep the CSV under `assets/` for download.
2. New page (e.g. `turkeys.md` or a post) with front matter and `layout:` of your choice. Paste from `turkey_roost_map.html`:
   - the two Leaflet `<link>`/`<script>` tags (head or top of body),
   - the `<style>` block,
   - `<div id="wrap">…</div>`,
   - the `<script>` block.
   **Do not** paste `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`.
3. Replace the data line: `const DATA = {{ site.data.turkey_roosts | jsonify }};`
4. CSS changes needed inside a layout:
   - `html,body{…height:100%}` → delete the `html,body` rule (keep only the font if wanted, scoped to `#wrap`).
   - `#wrap{display:flex;height:100%}` → `#wrap{display:flex;height:80vh;min-height:520px}`.
   - Scope generic selectors (`h1`, `label`, `fieldset`, `legend`, `blockquote`, `input[type=range]`) under `#wrap …` so they don't restyle the rest of the page. The `.leaflet-popup-content` rules can stay global.
   - Optional responsive rule: `@media (max-width:700px){#wrap{flex-direction:column;height:auto}#side{width:auto;max-height:40vh}#map{height:60vh}}`.
5. Liquid caveat: the inline JS contains `{{`/`}}`? — **No**, it uses template literals with `${…}` only, which Liquid ignores. But if the theme runs Markdown on the page, wrap the HTML block in `{% raw %}…{% endraw %}` *except* the `jsonify` line, or put the whole thing in an `_includes/turkey_map.html` and `{% include turkey_map.html %}` from the post (Liquid is still processed inside includes, so the `jsonify` line works there). Using an include is the tidiest.
6. Optional source table rendered from the same data (readers can browse without the CSV):
   ```liquid
   | # | Location | Type | Conf. | Date | Source |
   |---|---|---|---|---|---|
   {% for r in site.data.turkey_roosts %}| {{ r.id }} | {{ r.location_name }} | {{ r.evidence_type }} | {{ r.confidence }} | {{ r.date_or_period }} | [{{ r.source_title | truncate: 60 }}]({{ r.source_url }}) |
   {% endfor %}
   ```
   (Needs kramdown tables; ensure no blank line inside the loop output.)

### Option C — JS fetches the JSON at runtime
Keep `DATA` out of the HTML: `const DATA = await (await fetch('/assets/turkeys/turkey_roost_reports.json')).json();` (wrap the script in an async IIFE). Works for both A and B; avoids duplicating data but breaks when the page is opened from `file://`. Not needed unless the data will be updated often.

## 3. Things to check / decide in the blog repo
- **baseurl**: use `relative_url` for all paths if `_config.yml` sets `baseurl` (GitHub Pages project sites).
- **CSP / headers**: if the site sends a Content-Security-Policy (Netlify `_headers`, etc.), allow `unpkg.com` (script+style) and `tile.openstreetmap.org` (img). Most Jekyll sites set none.
- **Tiles**: OSM's public tile server is fine for a personal blog. If traffic is heavy or you want a quieter look, swap the one `L.tileLayer(...)` URL for CARTO Voyager/Positron or Stadia/MapTiler (free tiers, attribution required). Owner wants street names visible, so avoid label-less styles.
- **Leaflet from a CDN vs vendored**: vendoring `leaflet.css/.js` (+ `images/` folder for marker icons — not used here, only circleMarkers) into `assets/vendor/leaflet/` removes the external dependency entirely. Optional.
- **Theme conflicts**: some themes set `img{max-width:100%}` and `box-sizing` rules that can distort Leaflet tiles; Leaflet's own CSS usually wins, but if tiles look misaligned add `.leaflet-container img{max-width:none!important}`.
- **Dark themes**: the sidebar uses fixed light colours (`#fafafa`, `#222`); adjust `#side` background/text to theme variables if the site is dark.
- **Updating data later**: edit `turkey_roost_records.py` → `python3 turkey_roost_records.py` → copy the JSON to `_data/` (B) or rerun `build_turkey_roost_map.py` and recopy the HTML (A).

## 4. Suggested post content (from README_turkey_roosts.md)
Three roost clusters: (1) Surrey St / Putnam Ave, Riverside — best supported, three independent sources 2021–2024; (2) Harvard north campus / Baldwin–Agassiz (Science Center pin oak 2012, MCZ crab apple 2012, Oxford/Hammond 2024, Baldwin playground 2021–22, Linnaean St 2023–24); (3) Harvard Yard / Quincy St (2019, 2022, Aug 2026). Brattle St / Charles River / Mount Auburn Cemetery have only area-level claims. Caveat for readers: coordinates are placed from textual descriptions; turkeys change roost trees often, so markers mean "places turkeys have been reported roosting", not fixed roosts.
