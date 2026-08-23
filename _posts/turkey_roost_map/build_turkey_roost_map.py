import json, csv, re, html, sys
recs = json.load(open(sys.argv[4] if len(sys.argv)>4 else 'turkey_roost_reports.json'))
OUT_HTML = sys.argv[1]; OUT_CSV = sys.argv[2]; OUT_JSON = sys.argv[3]

# CSV + JSON list
fields = ["id","location_name","neighborhood","lat","lon","uncertainty_m","evidence_type","roost_type","confidence","year","date_or_period","source_title","source_url","quote","notes"]
with open(OUT_CSV,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
    for r in recs: w.writerow({k:r.get(k,"") for k in fields})
json.dump(recs, open(OUT_JSON,'w'), indent=1)

data_js = json.dumps(recs)
page = r'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cambridge MA Wild Turkey Roost Map</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
 html,body{margin:0;height:100%;font:14px/1.4 -apple-system,Helvetica,Arial,sans-serif;color:#222}
 #wrap{display:flex;height:100%}
 #side{width:360px;min-width:300px;overflow-y:auto;border-right:1px solid #ddd;padding:12px 14px;box-sizing:border-box;background:#fafafa}
 #map{flex:1}
 h1{font-size:17px;margin:0 0 4px}
 .sub{color:#555;font-size:12px;margin-bottom:10px}
 fieldset{border:1px solid #ddd;border-radius:4px;margin:0 0 10px;padding:6px 10px}
 legend{font-size:12px;color:#555;padding:0 4px}
 label{display:block;font-size:13px;margin:2px 0}
 .sw{display:inline-block;width:12px;height:12px;border-radius:50%;vertical-align:-1px;margin-right:5px;border:2px solid}
 .item{border-top:1px solid #e5e5e5;padding:7px 0;cursor:pointer}
 .item:hover{background:#f0f0f0}
 .item b{font-size:13px}
 .meta{font-size:12px;color:#555}
 .tag{display:inline-block;font-size:11px;padding:0 5px;border-radius:3px;background:#eee;margin-right:4px}
 .roost{background:#fde0c8;color:#8a3d00}.day{background:#e4e4e4;color:#444}
 .leaflet-popup-content{font-size:13px;max-width:300px}
 .leaflet-popup-content a{color:#0645ad}
 blockquote{margin:6px 0;padding-left:8px;border-left:3px solid #ccc;color:#444;font-style:italic}
 input[type=range]{width:100%}
 #count{font-size:12px;color:#555;margin:4px 0 8px}
 .note{font-size:11px;color:#666;margin-top:10px}
 @media (max-width:700px){
  #wrap{flex-direction:column}
  #side{order:2;width:auto;min-width:0;max-height:45%;border-right:0;border-top:1px solid #ddd}
  #map{order:1;min-height:0}
 }
</style></head><body>
<div id="wrap">
<div id="side">
 <h1>Cambridge, MA wild turkey roosts</h1>
 <div class="sub">Reported roosting/sleeping sites, plus daytime flock locations that hint at nearby roosts. Circle size = location uncertainty. Click a marker or list item for the source.</div>
 <fieldset><legend>Evidence type</legend>
  <label><input type="checkbox" class="f-ev" value="roost" checked> <span class="sw" style="background:#f4a261;border-color:#b5561d"></span>Roost report (sleeping/perched at night or dusk/dawn)</label>
  <label><input type="checkbox" class="f-ev" value="daytime_only"> <span class="sw" style="background:#bbb;border-color:#777"></span>Daytime flock location only (weak evidence)</label>
 </fieldset>
 <fieldset><legend>Confidence (roost claim + location)</legend>
  <label><input type="checkbox" class="f-conf" value="high" checked> High &mdash; firsthand, explicit roosting, specific spot</label>
  <label><input type="checkbox" class="f-conf" value="medium" checked> Medium &mdash; explicit roosting but vague spot, or secondhand</label>
  <label><input type="checkbox" class="f-conf" value="low" checked> Low &mdash; inferred / daytime only</label>
 </fieldset>
 <fieldset><legend>Report date</legend>
  <label>Show reports from <b id="yrlab"></b> onward</label>
  <input type="range" id="yr" min="2012" max="2026" step="1" value="2012">
  <div class="meta">Marker outline: solid = 2024 or later; thin = 2019&ndash;2023; dashed = before 2019.</div>
 </fieldset>
 <div id="count"></div>
 <div id="list"></div>
 <div class="note">Compiled 2026-08-23 from public web sources. Coordinates are estimates placed from the description in each source; the uncertainty circle is a judgment of how precisely the source pins the location, not a measured range. Turkeys switch roost trees frequently, so even high-confidence sites are "places turkeys have roosted", not fixed roosts.</div>
</div>
<div id="map"></div>
</div>
<script>
const DATA = __DATA__;
const map = L.map('map',{zoomControl:true,scrollWheelZoom:window.self===window.top}).setView([42.3765,-71.118],14);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);
L.control.scale({imperial:true}).addTo(map);
const col = r => r.evidence_type==='roost' ? {fill:'#f4a261',stroke:'#b5561d'} : {fill:'#bbbbbb',stroke:'#777777'};
const recency = r => r.year>=2024 ? {w:3,dash:null} : r.year>=2019 ? {w:1.5,dash:null} : {w:2,dash:'4 4'};
const layers = [];
function popupHtml(r){
  const c = r.confidence;
  let h = `<b>${r.location_name}</b><br><span class="meta">${r.neighborhood}</span><br>`;
  h += `<span class="tag ${r.evidence_type==='roost'?'roost':'day'}">${r.evidence_type==='roost'?'ROOST REPORT':'daytime only'}</span><span class="tag">${r.roost_type}</span><span class="tag">confidence: ${c}</span><br>`;
  h += `<div class="meta">Date: ${r.date_or_period} &middot; location &plusmn;${r.uncertainty_m} m</div>`;
  if(r.quote) h += `<blockquote>${r.quote}</blockquote>`;
  h += `Source: <a href="${r.source_url}" target="_blank" rel="noopener">${r.source_title}</a>`;
  if(r.extra_sources) r.extra_sources.forEach(s=>{h += `<br>Also: <a href="${s.url}" target="_blank" rel="noopener">${s.title}</a>`;});
  if(r.notes) h += `<div class="meta" style="margin-top:4px">${r.notes}</div>`;
  return h;
}
DATA.forEach(r=>{
  const c=col(r), rc=recency(r);
  const circ = L.circle([r.lat,r.lon],{radius:r.uncertainty_m,color:c.stroke,weight:rc.w,dashArray:rc.dash,fillColor:c.fill,fillOpacity:(r.uncertainty_m>500?0.06:r.evidence_type==='roost'?0.18:0.10),opacity:r.uncertainty_m>500?0.5:0.8,interactive:false});
  const dot = L.circleMarker([r.lat,r.lon],{radius:r.evidence_type==='roost'?7:5,color:c.stroke,weight:rc.w,dashArray:rc.dash,fillColor:c.fill,fillOpacity:0.95});
  const g = L.layerGroup([circ,dot]);
  dot.bindPopup(popupHtml(r));
  layers.push({r,g,dot});
});
function visible(r){
  const ev=[...document.querySelectorAll('.f-ev:checked')].map(x=>x.value);
  const cf=[...document.querySelectorAll('.f-conf:checked')].map(x=>x.value);
  const yr=+document.getElementById('yr').value;
  return ev.includes(r.evidence_type)&&cf.includes(r.confidence)&&(r.year||0)>=yr;
}
function refresh(){
  document.getElementById('yrlab').textContent=document.getElementById('yr').value;
  const list=document.getElementById('list'); list.innerHTML=''; let n=0;
  layers.sort((a,b)=>(a.r.evidence_type===b.r.evidence_type?0:a.r.evidence_type==='roost'?-1:1)||(b.r.year-a.r.year));
  layers.forEach(o=>{
    if(visible(o.r)){o.g.addTo(map);n++;
      const d=document.createElement('div');d.className='item';
      d.innerHTML=`<b>${o.r.location_name}</b><br><span class="tag ${o.r.evidence_type==='roost'?'roost':'day'}">${o.r.evidence_type==='roost'?'roost':'daytime'}</span><span class="tag">${o.r.confidence}</span><span class="meta">${o.r.date_or_period}</span>`;
      d.onclick=()=>{map.setView([o.r.lat,o.r.lon],Math.max(map.getZoom(),16));o.dot.openPopup();};
      list.appendChild(d);
    } else map.removeLayer(o.g);
  });
  document.getElementById('count').textContent=n+' of '+DATA.length+' reports shown';
}
document.querySelectorAll('input').forEach(i=>i.addEventListener('input',refresh));
refresh();
</script></body></html>'''
open(OUT_HTML,'w').write(page.replace('__DATA__',data_js))
print("wrote",OUT_HTML,len(recs),"records")
