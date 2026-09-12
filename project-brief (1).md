# Project brief

GeoDev Lab Africa, Cohort One. Month 1.

---

## The topic

Mapping where health facilities sit across Ila Local Government Area in Osun State, and measuring the size of the population each one has to serve.

---

## The question

How many health facilities does each ward in Ila Local Government Area, Osun State contain, and how many residents does a single facility have to cover in each of those wards?

---

## Why it is worth doing

Ila is a mostly rural local government of roughly 303 square kilometres in the Igbomina country of north-eastern Osun, administered from Ila Orangun and divided into eleven wards. Facilities in a place like this cluster around the headquarters town by default, not by anybody's decision, and the wards furthest from Ila Orangun tend to carry the thinnest provision.

Counting facilities alone would not reveal that. Three clinics serving 2,500 people and three clinics serving 22,000 produce the same number and describe entirely different realities. Once population is divided across the facilities that exist, the count becomes a measure of load, and load is what tells a planner which ward is genuinely stretched.

There is a practical audience for the answer. The local government health department, along with the Osun State Primary Health Care Development Board, has to decide where the next primary health centre belongs and which existing ones need staff before they need construction. Neither decision is currently backed by a ward-level figure.

There is also a reason for me to be the one doing it. I know the area and I know some of these facilities by sight, so when a ward comes back empty I can judge whether that reflects the ground or reflects a gap in the dataset. That distinction is the difference between a finding and a mistake, and no software will make it for me.

Finally, the question scales properly across the twelve months. This month it is a count and a division. Later it becomes travel distance along real roads instead of ward membership, then a model of where a new facility would relieve the most people, then a service somebody can query without opening QGIS at all.

---

## The data I need

1. Ward boundaries for Ila LGA. Polygons, eleven expected.
2. The Ila LGA boundary itself, to fix the study area. Polygon.
3. Health facility locations carrying type, level and ownership. Points.
4. Gridded population estimates covering the LGA. Raster.
5. Settlement extents, to see how the population within each ward is arranged. Polygons.
6. An independent second list of facilities, for cross-checking. Points or table.
7. Road network, for context now and travel distance later. Lines.

---

## Where each dataset comes from

GRID3 is the primary source for this project. Everything except the roads and the cross-check comes from it.

**Ward and LGA boundaries.** GRID3 NGA Operational Wards v3.0, released July 2026, which lists Osun among the states it covers. The LGA outline comes from GRID3 NGA Operational LGA Boundaries. Both are available at https://data.grid3.org as GeoPackage. The ward file spans every included state, so I filter down to Ila and export those eleven polygons on their own. Expect 10 to 40 MB before filtering.

**Health facilities.** GRID3 NGA Health Facilities v3.0, released August 2026, from https://data.grid3.org. It consolidates records from the Nigeria Health Facility Registry with GRID3's own field collection, and it carries the type and ownership attributes the analysis needs. Version 3.0 covers a selection of states rather than all of them, so if Osun is absent I fall back to Health Facilities v2.0, which is national in scope. Downloaded as GeoPackage and clipped to Ila.

**Population.** GRID3 NGA gridded population estimates at 100 metre resolution, from https://data.grid3.org. Summed per ward using zonal statistics. For a sanity check, the 2006 census put Ila LGA at 62,049 people, so a modelled 2026 total should sit comfortably above that without leaving the same order of magnitude.

**Settlement extents.** GRID3 NGA Settlement Extents v4.1, released August 2026, from https://data.grid3.org. Reveals whether a ward's residents are concentrated in one town or spread across scattered hamlets, which changes what a facility count actually means for the people in it.

**Cross-check source.** The Nigeria Health Facility Registry maintained by the Federal Ministry of Health, at https://hfr.health.gov.ng, filterable to state and LGA. Setting its Ila list beside the GRID3 points shows me how complete either source is before I put a number in front of anyone.

**Roads.** OpenStreetMap, pulled with the QuickOSM plugin inside QGIS using the key `highway` with no value specified, then clipped to the Ila boundary. Attribution required: © OpenStreetMap contributors.

**The riskiest dataset, fetched first.** The GRID3 health facility layer. The entire question rests on it, so week one is spent confirming that Osun is included and that Ila returns enough facility points to work with. If it does not, the question gets reshaped now rather than in month four.

---

## What I would build

A ward-level coverage record for Ila that regenerates itself instead of being redone by hand.

It stores the eleven ward boundaries, takes in each new release of the GRID3 facility and population layers, recalculates facility count and residents per facility for every ward, and returns a ranked map and table that a health department officer can read without knowing what a coordinate reference system is. When GRID3 publishes its next facility version, the ranking refreshes without anybody repeating this month's work.

---

## Attribution

GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development). Operational Wards v3.0, Operational LGA Boundaries, Health Facilities v3.0, Settlement Extents v4.1, and gridded population estimates. Citation as given on each dataset page.

Nigeria Health Facility Registry, Federal Ministry of Health.

© OpenStreetMap contributors.
