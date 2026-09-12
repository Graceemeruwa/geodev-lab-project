# geodev-lab-project

# Health facility distribution and population load in Ila LGA, Osun State

## The question

How many health facilities does each ward in Ila Local Government Area, Osun State contain, and how many residents does a single facility have to cover in each of those wards?

## Why it is worth doing

Ila is a largely rural local government of about 303 square kilometres, run from Ila Orangun and split into eleven wards. Provision tends to gather around the headquarters town, leaving outlying wards thinner without anyone having planned it that way.

A facility count on its own hides this. Three clinics covering 2,500 residents and three covering 22,000 give the same number while describing different situations. Dividing ward population across the facilities present converts the count into a measure of load, which is what shows where the strain actually falls.

The local government health department and the Osun State Primary Health Care Development Board both have to choose where new primary health centres go and which existing ones need staffing first. Neither choice currently rests on a ward-level figure.

Built over twelve months with GeoDev Lab Africa, Cohort One.

## Study area

Ila Local Government Area, Osun State, Nigeria. Headquarters at Ila Orangun, approximately 8.02 degrees north and 4.90 degrees east. Around 303 square kilometres, eleven wards.

All analysis is carried out in EPSG:32631, UTM zone 31 north.

## Data

GRID3 is the primary source for this project.

| Layer | Source | Type |
|---|---|---|
| Ward boundaries | GRID3 NGA Operational Wards v3.0 | polygon |
| LGA boundary | GRID3 NGA Operational LGA Boundaries | polygon |
| Health facilities | GRID3 NGA Health Facilities v3.0 | point |
| Population estimates | GRID3 NGA gridded population, 100 m | raster |
| Settlement extents | GRID3 NGA Settlement Extents v4.1 | polygon |
| Facility cross-check | Nigeria Health Facility Registry | table |
| Roads | OpenStreetMap via QuickOSM | line |

## Repository contents

- `project-brief.md` is the full project brief.
- `data-notes.md` records every layer, its source, its version, its date and its quality assessment.
- `month-1-summary.md` records the first analysis, what was expected and what came out.
- `data/raw/` holds downloaded files exactly as they arrived and is never edited.
- `data/processed/` holds everything derived from them.

## Attribution

GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development). Operational Wards v3.0, Operational LGA Boundaries, Health Facilities v3.0, Settlement Extents v4.1, and gridded population estimates.

Nigeria Health Facility Registry, Federal Ministry of Health.

© OpenStreetMap contributors.
