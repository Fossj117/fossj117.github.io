import json
R=[]
def add(name,nb,lat,lon,unc,ev,rt,conf,year,date,title,url,quote,notes="",extra=None):
    R.append(dict(id=len(R)+1,location_name=name,neighborhood=nb,lat=lat,lon=lon,uncertainty_m=unc,evidence_type=ev,roost_type=rt,confidence=conf,year=year,date_or_period=date,source_title=title,source_url=url,quote=quote,notes=notes,extra_sources=extra or []))

# ---------- ROOST REPORTS ----------
add("Trees on Surrey Street (one-block street off Putnam Ave, Riverside)","Riverside, Cambridge",42.36875,-71.11395,120,"roost","tree","high",2024,"c. March 2024 ('they often roost' there); corroborated Aug 2021 and Nov 2021",
 "Reddit r/CambridgeMA: Where did the turkey family go? (comment by cane_stanco)","https://old.reddit.com/r/CambridgeMA/comments/1buqp69/where_did_the_turkey_family_go/",
 "They often roost in the trees on Surrey street. Come to think of it, I haven't noticed them in a bit. However, I haven't been around that much this winter.",
 "Best-supported roost in the dataset: three independent sources (2021 r/aww comment 'sleep in the trees nearby just off of Putnam Avenue'; iNaturalist 2021-11-20 'Sleeping in a tree' geotagged on Surrey St; this 2024 comment) converge on the same block. Specific tree not identified.",
 [{"title":"Reddit r/aww (Aug 2021): 'The Turkeys sleep in the trees nearby just off of Putnam Avenue'","url":"https://old.reddit.com/r/aww/comments/p56hsc/a_turkey_and_its_reflection/"},
  {"title":"iNaturalist 101579905 (2021-11-20, 7:36 pm): 'Sleeping in a tree' at Surrey St","url":"https://www.inaturalist.org/observations/101579905"}])
add("Trees on Linnaean Street near Mass Ave","Agassiz / Neighborhood 9, Cambridge",42.3831,-71.1225,300,"roost","tree","medium",2024,"c. March 2024",
 "Reddit r/CambridgeMA: Where did the turkey family go? (comments by robotpatrols, Reasonable_Move9518)","https://old.reddit.com/r/CambridgeMA/comments/1buqp69/where_did_the_turkey_family_go/",
 "I saw them in the trees on Linnaean the other day. [reply:] They sleep in trees so you'll only see them there around dawn or dusk ... And the whole flock takes over one tree.",
 "Seen in trees on Linnaean; thread confirms flock roosts as a group in one bare tree at dawn/dusk in winter. Time of day not stated for the Linnaean sighting, so medium.")
add("Tree on Surrey St near Putnam Ave (iNaturalist geotag)","Riverside, Cambridge",42.36871,-71.11375,50,"roost","tree","high",2021,"2021-11-20, 7:36 pm",
 "iNaturalist observation 101579905 (Wild Turkey)","https://www.inaturalist.org/observations/101579905",
 "Sleeping in a tree","Geotagged observation after dark with explicit 'sleeping'. Coordinates as recorded on iNaturalist. Same block as the Surrey St roost reports.")
add("Tree at Quincy St @ Harvard St (by Lamont Library / Barker Center)","Harvard campus, Cambridge",42.37319,-71.11469,50,"roost","tree","medium",2026,"2026-08-12, 7:40 pm (dusk)",
 "iNaturalist observation 392547032 (Wild Turkey)","https://www.inaturalist.org/observations/392547032",
 "Four turkeys, maybe more. There were two in the tree.","Birds already up in a tree at dusk; roosting likely but not stated. Most recent report in this set.")
add("Trees near Oxford St / Hammond St (north of Harvard Science Center)","Baldwin / Agassiz, Cambridge",42.37879,-71.11642,50,"roost","tree","medium",2024,"2024-01-15, 4:45 pm (January dusk)",
 "iNaturalist observation 196887280 (Wild Turkey)","https://www.inaturalist.org/observations/196887280",
 "flock of turkeys, some nested in trees","Flock going up into trees at winter dusk = classic roosting behaviour; 'nested' is the observer's wording.")
add("Pin oak in courtyard next to the Harvard Science Center","Harvard campus, Cambridge",42.3766,-71.1160,80,"roost","tree","high",2012,"c. early spring 2012 (night; recounted June 2016)",
 "Julie Zickefoose blog: Wild Turkeys Take Cambridge!","http://juliezickefoose.blogspot.com/2016/06/wild-turkeys-take-cambridge.html",
 "on a brink-of-spring night when I looked up into a tree next to the Harvard U. Science Center and saw what looked like a bag of laundry in a pin oak, backlit by the glowing urban sky",
 "Firsthand night-time observation by a professional naturalist; oldest report in this set.")
add("Treetops in Harvard Yard","Harvard Yard, Cambridge",42.3744,-71.1169,250,"roost","tree","high",2022,"April 2022 (described as routine)",
 "Harvard Crimson: Where the Wild Things Are: The Urban Ecology of Harvard Square","https://www.thecrimson.com/article/2022/4/7/where-the-wild-things-are/",
 "After long days of jaywalking, the wild turkeys use their limited flight ability to reach the treetops, where they rest. Late-night strolls around the Yard reveal shadowy figures silhouetted among the branches.",
 "Explicit night roosting in the Yard; which trees not specified.")
add("Trees in the Old Yard and around Quincy & Prescott Streets","Harvard campus, Cambridge",42.3750,-71.1140,300,"roost","tree","medium",2019,"Nov 2019 (describing prior 2-3 years)",
 "Harvard Gazette: Harvard's thriving wild turkey population","https://news.harvard.edu/gazette/story/2019/11/harvards-thriving-wild-turkey-population/",
 "where they like to roost high in trees (yes, they fly) ... much more noticeable in the Old Yard in the last two or three years, migrating from favored trees along the Charles River to the main campus and areas around Quincy and Prescott streets.",
 "Harvard landscape-services supervisor quoted; area-level only.")
add("Favored roost trees along the Charles River beside Harvard's river houses","Riverside / Memorial Drive, Cambridge",42.3695,-71.1210,700,"roost","tree","medium",2019,"Nov 2019 (describing roughly 2015-2017 and earlier)",
 "Harvard Gazette: Harvard's thriving wild turkey population","https://news.harvard.edu/gazette/story/2019/11/harvards-thriving-wild-turkey-population/",
 "migrating from favored trees along the Charles River to the main campus",
 "Historical: birds reportedly shifted away from the river toward the Yard after ~2017. Stretch of river not specified.",
 [{"title":"The Serene City (2025) restating the Gazette","url":"https://theserenecity.substack.com/p/the-wild-turkeys-of-harvard-square"}])
add("Large trees around Harvard Square and among the Brattle Street (Tory Row) mansions","Harvard Square / Brattle St, Cambridge",42.3768,-71.1275,900,"roost","tree","medium",2025,"Nov 6, 2025",
 "The Serene City (Susan Cooke, Substack): The wild turkeys of Harvard Square","https://theserenecity.substack.com/p/the-wild-turkeys-of-harvard-square",
 "probably due to the many large trees around Harvard Square and tucked among the mansions of historic Brattle Street ... They roost in those trees, but also find it useful to walk down Brattle in both directions and all around the Square.",
 "Resident's general characterisation, not a specific observed tree; large uncertainty along Brattle St.")
add("Wooded backyards on Turkey Hill (author's and neighbour's trees)","Turkey Hill, Arlington (town inferred from the hill name)",42.4245,-71.1735,800,"roost","tree","medium",2021,"late December 2021",
 "Oliver Knill (Harvard Math): Sleep over turkeys","https://legacy-www.math.harvard.edu/~knill/various/turkey/index.html",
 "We live on Turkey hill and our house has some forest in the back. A good dozen turkeys slept there over night in late december. ... The dots in the trees are all turkeys.",
 "Firsthand with photos, but outside Cambridge and exact address not given.")
add("Trees near a residence in Medford (Tufts / South Medford area)","Medford",42.40231,-71.08641,200,"roost","tree","high",2023,"2023-09-26",
 "iNaturalist observation 184993985 (Wild Turkey)","https://www.inaturalist.org/observations/184993985",
 "The two turkeys roost in nearby trees at night.","Outside Cambridge; included for regional context.")
add("Tree in Charlestown (near Boston National Historical Park)","Charlestown, Boston",42.37436,-71.05641,50,"roost","tree","low",2025,"2025-04-25, 7:00 pm",
 "iNaturalist observation 278042932 (Wild Turkey)","https://www.inaturalist.org/observations/278042932",
 "Wild turkey in tree.","Single bird in a tree in the evening; roosting not stated. Outside Cambridge.")

add("Old crab apple over the picnic table in the gully below the MCZ courtyard (26 Oxford St)","Harvard campus / Agassiz, Cambridge",42.3786,-71.1155,60,"roost","tree","high",2012,"November 2012 ('several nights')",
 "Harvard Campus Nature Watch log (in Harvard Recycling Update, Fall 2020, PDF)","https://www.energyandfacilities.harvard.edu/sites/default/files/Recycling%20Update%20Fall%202020.pdf",
 "WILD TURKEY roosts several nights in the old crab apple over the little picnic table in the gully below the Museum of Comparative Zoology courtyard",
 "Most precisely described roost tree in the dataset (single bird, 2012). Same log notes a turkey in a berry tree near Wadsworth House, Oct 2014. Found via the prior effort in this folder.")
add("Trees just off Putnam Ave near Mass Ave","Riverside / Cambridgeport, Cambridge",42.3695,-71.1125,250,"roost","tree","medium",2021,"August 2021",
 "Reddit r/aww: A Turkey and its Reflection (poster's comment)","https://old.reddit.com/r/aww/comments/p56hsc/a_turkey_and_its_reflection/",
 "Cambridge, MA. At the intersection of Mass Ave and Putnam. The Turkeys sleep in the trees nearby just off of Putnam Avenue.",
 "Secondhand/general; consistent with the Surrey St roost 150 m away. Found via the prior effort in this folder.")
add("Tree across from Baldwin (Maria L. Baldwin School) playground, Oxford St","Baldwin / Agassiz, Cambridge",42.3830,-71.1178,120,"roost","tree","medium",2022,"winter 2021-22 (comment Jan 2023: 'last winter')",
 "Reddit r/CambridgeMA: Harvard Turkey learning new tricks (comment by itamarst)","https://old.reddit.com/r/CambridgeMA/comments/10k9vnp/harvard_turkey_learning_new_tricks/",
 "They also roost together on trees here in Cambridge. Seen a bunch of turkeys on a tree across from Baldwin playground on Oxford St. last winter, and one turkey _very_ high up on a tree near Graham & Parks more recently.",
 "Group in a tree in winter, framed by the commenter as roosting. 450 m north of the Oxford/Hammond dusk report. Found via the prior effort in this folder.")
add("Tree near Graham & Parks School, 44 Linnaean St","Agassiz / Neighborhood 9, Cambridge",42.3827,-71.1237,150,"roost","tree","low",2023,"c. Jan 2023",
 "Reddit r/CambridgeMA: Harvard Turkey learning new tricks (comment by itamarst)","https://old.reddit.com/r/CambridgeMA/comments/10k9vnp/harvard_turkey_learning_new_tricks/",
 "one turkey _very_ high up on a tree near Graham & Parks more recently","Single bird high in a tree; time of day not given. Found via the prior effort in this folder.")
add("Near the Domino's on Mass Ave (1033 Mass Ave) - historical roost","Mid-Cambridge, Cambridge",42.3697,-71.1122,200,"roost","unknown","low",2018,"'by no means recent' as of June 2023 (year unknown; plotted as c. 2018)",
 "Reddit r/boston: Where are the turkeys? (comment by kpyna)","https://old.reddit.com/r/boston/comments/14g2cpk/where_are_the_turkeys/",
 "This is by no means a recent sighting but they used to roost near the Domino's on Mass Ave.","Vague and undated; 250 m from the Surrey/Putnam roost cluster, so probably the same roost area. Found via the prior effort in this folder.")
add("Trees on Avon Hill St (commenter's guess for the Porter-Harvard flock)","Avon Hill, Cambridge",42.3847,-71.1245,300,"roost","tree","low",2023,"June 2023",
 "Reddit r/boston: Where are the turkeys? (comment by andrewsinclair)","https://old.reddit.com/r/boston/comments/14g2cpk/where_are_the_turkeys/",
 "I think these live in trees on Avon Hill St.","Explicitly a guess ('I think'). Found via the prior effort in this folder.")
add("'Tree by Harvard' with at least 8 turkeys (photo; exact place not given)","Harvard area, Cambridge",42.3760,-71.1165,500,"roost","tree","low",2021,"winter 2020-21 (posted Oct 2021)",
 "Reddit r/boston: Don't be suspicious (comment with imgur photo)","https://old.reddit.com/r/boston/comments/qbpbl6/dont_be_suspicious_dont_be_suspicious/",
 "At least 8 turkeys in this tree by Harvard that I took last winter.","Photo of a flock roost-style in one tree; location too vague to place. Found via the prior effort in this folder.")

# ---------- DAYTIME / HANGOUT (weak evidence for nearby roost) ----------
add("Trees and rooftops behind the Museum of Comparative Zoology (26 Oxford St)","Harvard campus / Agassiz, Cambridge",42.3785,-71.1150,100,"daytime_only","tree/roof","low",2018,"March 2018 (early morning)",
 "Ernst Mayr Library blog: Wild Turkeys Roosting at the MCZ","https://library.mcz.harvard.edu/blog/wild-turkeys-roosting-mcz",
 "On a recent early spring morning, a dog startled a flock of turkeys up to trees and rooftops behind the Museum of Comparative Zoology.",
 "Flock flushed into trees/roofs in the morning; shows perch sites used near the Science Center / Oxford St roosts, 150 m away.")
add("Huron Avenue and neighbouring streets (flock 'jumps up in the trees')","Huron Village, Cambridge",42.3810,-71.1370,600,"daytime_only","tree","low",2023,"March 2023",
 "Boston 25 News: Cambridge residents concerned after wild turkeys seen attacking people","https://www.boston25news.com/news/local/cambridge-residents-concerned-after-wild-turkeys-seen-attacking-people/GDPQPJCW55GQHF5OZB3YSR3D5Y/",
 "They travel in big herds and jump up in the trees",
 "Resident description; plus the March 2023 mail-carrier attack on Huron Ave. A resident flock this established almost certainly roosts within a few blocks, but no roost tree is named.",
 [{"title":"Patch: MA Mail Carrier Needs Surgery After Aggressive Turkey Attack (Huron Ave)","url":"https://new.patch.com/massachusetts/cambridge/ma-mail-carrier-needs-surgery-after-aggressive-turkey-attack"},
  {"title":"Reddit (2026): house on Huron Ave with turkeys in yard/porch","url":"https://old.reddit.com/r/CambridgeMA/comments/1u29xtx/gang_of_turkeys_jumps_blue_bike_rider_on_mass_ave/"}])
add("Trees on Observatory Hill (Concord Ave / Garden St)","Observatory Hill, Cambridge",42.38301,-71.13411,50,"daytime_only","tree","low",2025,"2025-02-13, 12:10 pm",
 "iNaturalist observation 278242838 (Wild Turkey)","https://www.inaturalist.org/observations/278242838",
 "Tree turkeys!","Birds up in trees at midday (winter). Perching site, not a confirmed overnight roost.")
add("Landscaped lot / park across from Walgreens & The Abbey, Mass Ave at Linnaean St","Agassiz / Neighborhood 9, Cambridge",42.3838,-71.1222,100,"daytime_only","unknown","medium",2024,"2024 (recurring; 'usually about 10-15')",
 "Reddit r/CambridgeMA: Turkey sanctuary","https://old.reddit.com/r/CambridgeMA/comments/1dqqnjb/turkey_sanctuary/",
 "elevated turkey toilet and nap haven across from the Abbey ... [other thread:] There are usually about 10-15 in the park across from the Walgreens at Linnean.",
 "Daytime loafing/napping site of the Linnaean/Surrey flock; 200 m from the Surrey St roost report.",
 [{"title":"Reddit: Where did the turkey family go? (comments)","url":"https://old.reddit.com/r/CambridgeMA/comments/1buqp69/where_did_the_turkey_family_go/"}])
add("Mass Ave between Shepard St and Linnaean St (repeated evening sightings)","Agassiz / Porter Square, Cambridge",42.3819,-71.1197,300,"daytime_only","unknown","low",2026,"2024-2026 (e.g. 2026-08-03 7:58 pm, 2026-05-15 7:00 pm, 2025-06-14 7:21 pm)",
 "iNaturalist observation 388790933 (Wild Turkey, Mass Ave @ Shepard St)","https://www.inaturalist.org/observations/388790933",
 "(cluster of evening observations on Mass Ave near Shepard St)","Summer evening sightings (well before dusk) consistent with the flock working back toward the Surrey/Linnaean roost area.")
add("Avon Hill neighbourhood (resident flock, window smashed)","Avon Hill, Cambridge",42.3848,-71.1225,500,"daytime_only","unknown","low",2017,"Sept 2017",
 "NBC Boston: City Looks to Tackle Issue of Turkeys Terrorizing Neighborhoods","https://www.nbcboston.com/news/local/cambridge-massachusetts-looks-to-tackle-issue-of-turkeys-terrorizing-neighborhoods/28789/",
 "Several turkeys have been spotted in the Avon Hill section of Cambridge ... 'They are sure they own the neighborhood.'",
 "Earliest Avon Hill/Agassiz flock report; same hill as the 2024 Surrey/Linnaean roost reports.")
add("Harvard Art Museums / Bryant St / Kirkland & Irving St","Harvard / Agassiz, Cambridge",42.3752,-71.1135,300,"daytime_only","unknown","low",2024,"March 2024",
 "Reddit r/CambridgeMA: Where did the turkey family go?","https://old.reddit.com/r/CambridgeMA/comments/1buqp69/where_did_the_turkey_family_go/",
 "They were at the Harvard Art Museum for a while ... Saw them on Bryant St (right behind the museum) ... See them almost every day near Kirkland/ Irving street.")
add("Near Harvard Divinity School & American Academy of Arts and Sciences (Francis Ave / Irving St)","Agassiz / Norton's Woods, Cambridge",42.3790,-71.1135,250,"daytime_only","unknown","low",2025,"fall 2025 (mornings; last seen Oct 31, 2025)",
 "Boston.com: Gobble watch: Where readers are spotting wild turkeys across Greater Boston","https://www.boston.com/community/readers-say/2025/11/26/wild-turkey-sightings-greater-boston/",
 "I try to walk around that area to look for them most every morning. I haven't seen any since 31 October.","Morning sightings near Norton's Woods, a plausible roost woodland, but no roost stated.")
add("Cambridge Common","Harvard Square, Cambridge",42.3758,-71.1208,200,"daytime_only","unknown","low",2025,"Nov 2025 (also Nov 2022, 2026)",
 "Boston.com: Gobble watch (reader photo, Cambridge Common)","https://www.boston.com/community/readers-say/2025/11/26/wild-turkey-sightings-greater-boston/",
 "Cambridge Common - reader photo","",
 [{"title":"Harvard Animal Law & Policy Clinic (2022): foraging in Cambridge Common","url":"https://animal.law.harvard.edu/news-article/the-cambridge-turkeys"},
  {"title":"Reddit (2026): followed around Cambridge Common / from Marathon Sports","url":"https://old.reddit.com/r/CambridgeMA/comments/1u29xtx/gang_of_turkeys_jumps_blue_bike_rider_on_mass_ave/"}])
add("Traffic island at Mass Ave & Harvard St (opposite Hong Kong / Grafton Street)","Harvard Square, Cambridge",42.3721,-71.1155,50,"daytime_only","unknown","low",2021,"April 2021 (three weeks)",
 "Cambridge Day: Turkeys take over Harvard Square traffic island","https://www.cambridgeday.com/2021/04/29/turkeys-take-over-harvard-square-traffic-island-prime-real-estate-amid-top-shopping-and-dining/",
 "Three turkeys now at home for three weeks on the traffic island at Massachusetts Avenue and Harvard Street, across from the Hong Kong and Grafton Street eateries.",
 "Same block as the Quincy St @ Harvard St dusk-tree report (2026) and Harvard St/Remington St sleeping-tree report (2021).")
add("Eastern Harvard Yard by Lamont, Widener & Houghton; Canaday Hall (hens with poults)","Harvard Yard, Cambridge",42.3738,-71.1155,150,"daytime_only","unknown","low",2019,"June 2019; spring 2019",
 "Harvard Magazine: Baby Turkey Season Comes to Harvard","https://www.harvardmagazine.com/2019/06/baby-turkey-season-comes-to-harvard",
 "a hen turkey and her seven poults appear to have settled near the eastern end of Harvard Yard, by Lamont, Widener, and Houghton libraries.","",
 [{"title":"Harvard Gazette (2019): hen with brood near Canaday Hall","url":"https://news.harvard.edu/gazette/story/2019/11/harvards-thriving-wild-turkey-population/"}])
add("Linden St / Holyoke St / Bow St daily circuit of 'the Harvard Square turkey'","Harvard Square, Cambridge",42.3725,-71.1172,200,"daytime_only","unknown","low",2016,"Jan 2016",
 "Boston Globe: Wild turkey finds a home in Harvard Square","https://www.bostonglobe.com/metro/2016/01/13/the-legend-harvard-turkey/PnVpP20s754bspnVfbBlFN/story.html",
 "No one seems sure where, exactly, it sleeps... a near-daily trip to the Harvard Bureau of Study Counsel on Linden Street","Article explicitly says the roost was unknown.")
add("Elmwood (Harvard president's residence, 33 Elmwood Ave) grounds","Brattle St / Elmwood, Cambridge",42.3770,-71.1312,150,"daytime_only","unknown","low",2019,"Nov 2019 ('past seven years')",
 "Harvard Gazette: Harvard's thriving wild turkey population","https://news.harvard.edu/gazette/story/2019/11/harvards-thriving-wild-turkey-population/",
 "The birds have been on the grounds for about the past seven years","Large wooded estate on Brattle St; consistent with the 2025 'Brattle Street trees' roost description.")
add("Brattle St a few blocks beyond the small park at Fresh Pond (family in the road)","West Cambridge / Fresh Pond, Cambridge",42.3835,-71.1400,400,"daytime_only","unknown","low",2025,"Nov 2025 (morning)",
 "The Serene City: The wild turkeys of Harvard Square","https://theserenecity.substack.com/p/the-wild-turkeys-of-harvard-square",
 "we were driving down Brattle, a few blocks beyond the small park at Fresh Pond ... a big family of them was right in front of us, in the middle of the lane.")
add("Mount Auburn Cemetery","West Cambridge / Watertown line",42.3710,-71.1450,500,"daytime_only","unknown","low",2024,"2012-2024 (recurring)",
 "Boston.com: Wild turkeys are roving Mount Auburn Cemetery","https://www.boston.com/culture/lifestyle/2015/10/26/wild-turkeys-are-roving-mount-auburn-cemetery-do-not-let-them-intimidate-you/",
 "Wild turkeys have been taking up residence at Mount Auburn Cemetery",
 "175 acres of mature trees with a resident flock: the most likely large roost site in the area, but no source in this search explicitly describes night roosting there.",
 [{"title":"Harvard Gazette (2019) photo: turkeys among gravestones","url":"https://news.harvard.edu/gazette/story/2019/11/harvards-thriving-wild-turkey-population/"},
  {"title":"iNaturalist 159976320 (2023-05-05, 8:09 pm, Watertown side)","url":"https://www.inaturalist.org/observations/159976320"},
  {"title":"Reddit (2024): 'Saw a bunch at Mt Auburn Cemetery yesterday'","url":"https://old.reddit.com/r/CambridgeMA/comments/1buqp69/where_did_the_turkey_family_go/"}])
add("Mass Ave & Putnam Ave / Old Cambridge Baptist Church / 1050 Mass Ave","Mid-Cambridge / Riverside, Cambridge",42.3690,-71.1110,300,"daytime_only","unknown","low",2025,"2022-2025",
 "Universal Hub: Turkeys (Cambridge items, Nov 2024 & Jan 2025)","https://www.universalhub.com/wildlife/turkeys",
 "a turkey rafter at a bus stop at Massachusetts and Putnam avenues in Cambridge ... a turkey mob outside 1050 Massachusetts Ave.","",
 [{"title":"Reddit (2024): family around Putnam & Mass Ave; Old Cambridge Baptist Church","url":"https://old.reddit.com/r/CambridgeMA/comments/1buqp69/where_did_the_turkey_family_go/"}])
add("Mass Ave near Central Kitchen","Central Square, Cambridge",42.3652,-71.1035,120,"daytime_only","unknown","low",2014,"April 2014",
 "CBS Boston: Turkey Sightings Reported In Boston, Cambridge","https://www.cbsnews.com/boston/news/turkey-sightings-reported-in-boston-cambridge/",
 "Turkey on Mass Av near Central Kitchen")
add("Central Street, Spring Hill / Somerville Ave ('the Somerville Turkey', roosted on fences)","Spring Hill, Somerville",42.3878,-71.1050,400,"daytime_only","fence","low",2020,"2020 (bird euthanized Dec 2020)",
 "Boston Globe: A Somerville turkey that became a neighborhood icon is no more","https://www.bostonglobe.com/2020/12/17/metro/somerville-turkey-that-became-neighborhood-icon-is-no-more/",
 "strutting through the neighborhood, hiding in bushes, roosting on fences, and sometimes causing traffic jams on Central Street","",
 [{"title":"Greg Cook / Wonderland (2020): turkey vs. police, Somerville Ave at Central St","url":"https://gregcookland.com/wonderland/2020/11/19/turkeys/"}])
add("Berry tree near Wadsworth House / Faculty Club lawn, Harvard Yard","Harvard Yard, Cambridge",42.3733,-71.1180,120,"daytime_only","tree","low",2014,"October 2014",
 "Harvard Campus Nature Watch log (Harvard Recycling Update, Fall 2020, PDF)","https://www.energyandfacilities.harvard.edu/sites/default/files/Recycling%20Update%20Fall%202020.pdf",
 "Female WILD TURKEY jumps down from a berry tree near Wadsworth House to feed in the grass","Daytime perch; earliest Harvard Yard record here.")
add("Triangle at Mass Ave / Putnam Ave / Mt Auburn St ('always there')","Riverside, Cambridge",42.3699,-71.1131,100,"daytime_only","unknown","low",2023,"June 2023",
 "Reddit r/boston: Where are the turkeys? (comment by wombatofevil)","https://old.reddit.com/r/boston/comments/14g2cpk/where_are_the_turkeys/",
 "somehow they live at the triangle intersection of mass ave/putnam st/mt. auburn in cambridge. They're always there","Daytime base of the flock that roosts on Surrey St.")
json.dump(R,open('turkey_roost_reports.json','w'),indent=1)
print(len(R),"records;",sum(r['evidence_type']=='roost' for r in R),"roost")
