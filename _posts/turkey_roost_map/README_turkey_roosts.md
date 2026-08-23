# Cambridge, MA wild turkey roost map (2026-08-23)

**Files**
- `turkey_roost_map.html` — self-contained Leaflet map (OpenStreetMap basemap via CDN). Open in a browser.
- `turkey_roost_reports.csv` / `.json` — the 40 reports with coordinates, uncertainty radius, evidence type, confidence, year, source URL and quote.
- `turkey_roost_records.py` — the hand-curated source list (edit this to add/correct reports), writes the JSON.
- `build_turkey_roost_map.py` — regenerates the HTML/CSV from the JSON:
  `python3 turkey_roost_records.py && python3 build_turkey_roost_map.py turkey_roost_map.html turkey_roost_reports.csv turkey_roost_reports.json`
- `cambridge_turkey_roost_map_verified*.{html,csv}` — the earlier effort, left untouched.

**How reports were classified**
- *Evidence type*: `roost` = source describes turkeys sleeping/perched overnight or going up at dusk / seen up at dawn; `daytime_only` = flock location only (weak hint at a nearby roost; turkeys usually roost within a few hundred metres of where they spend the day).
- *Confidence*: high = firsthand, explicit roosting, specific spot; medium = explicit roosting but vague spot or secondhand; low = inferred or daytime only.
- *Uncertainty radius*: my judgment of how precisely the source pins the place (~30–60 m for a named tree/geotag, ~150 m for a street or block, 300–500 m for a park/campus area, 800–1000 m for "Brattle Street" or "along the Charles").
- *Date*: every record carries a year; the map's slider hides older reports and marker outlines distinguish 2024+, 2019–2023, and pre-2019. Turkeys change roost trees often, so older reports mark areas turkeys have used, not fixed roosts.

**Main findings (roost evidence)**
1. **Surrey St / Putnam Ave, Riverside** — best supported: three independent sources (r/aww Aug 2021, iNaturalist geotagged "Sleeping in a tree" Nov 2021, r/CambridgeMA "often roost in the trees on Surrey street" 2024), plus an undated "used to roost near the Domino's" and the flock's daytime base at the Mass Ave/Putnam/Mt Auburn triangle.
2. **Harvard north campus / Baldwin–Agassiz** — pin oak by the Science Center (2012), crab apple below the MCZ courtyard (2012, several nights), Oxford/Hammond dusk flock (Jan 2024), tree opposite Baldwin playground on Oxford St (winter 2021–22), trees on Linnaean St / near Graham & Parks (2023–24); daytime base at the Mass Ave–Linnaean lot.
3. **Harvard Yard / Quincy St** — Crimson 2022 (night silhouettes in Yard treetops), Gazette 2019 (Old Yard, Quincy & Prescott), iNaturalist Aug 2026 (two up a tree at dusk, Quincy @ Harvard St).
4. **Brattle St / Charles River** — only area-level descriptions (Gazette 2019 river trees, Serene City 2025 Brattle St trees); Elmwood and Mount Auburn Cemetery are strong candidates but no source explicitly describes night roosting there.
5. Out-of-Cambridge context: Turkey Hill Arlington (Dec 2021 photos), Medford (2023), Charlestown (2025).

**Cross-check against the earlier effort in this folder**
- Independently re-found 6 of its 13 sites (Science Center pin oak, Harvard Yard, Quincy/Prescott, Charles River trees, Surrey St, Linnaean St).
- Missed by me and now added after verification: MCZ crab apple (Harvard Campus Nature Watch log, Nov 2012), Putnam Ave sleeping trees (r/aww 2021), Baldwin playground tree and Graham & Parks tree (r/CambridgeMA 2023), Domino's historical roost and Avon Hill St guess (r/boston 2023), "tree by Harvard" photo (r/boston 2021).
- Correction to my own draft: I had placed Surrey St in Agassiz; it is in Riverside (the earlier effort had it right).
- New in this version, not in the earlier effort: iNaturalist roost/dusk observations (Surrey St 2021, Oxford/Hammond 2024, Quincy St 2026), Harvard Crimson/Gazette details, The Serene City (2025), Turkey Hill (Knill), Medford/Charlestown, plus ~20 dated daytime-flock records and the date/recency handling.

**Porting to Jekyll**
The HTML is standalone: copy it into the site (e.g. `assets/turkey_roost_map.html`) and embed with
`<iframe src="/assets/turkey_roost_map.html" style="width:100%;height:80vh;border:0"></iframe>`,
or paste the `<link>`/`<script>` tags, the `#wrap` markup and the `<script>` block into a layout-free page. Data is inline (`const DATA = [...]`); swap it for `{{ site.data.turkey_roosts | jsonify }}` if you'd rather keep the records in `_data/`. Only external dependencies: Leaflet 1.9.4 (unpkg) and OSM tiles.
