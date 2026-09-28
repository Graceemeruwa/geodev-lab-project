# Data notes

**Project:** Distribution of health facilities in Ila Local Government Area, Osun State, and the population they serve
**Week 2 submission.** GeoDev Lab Africa, Cohort One.

All layers were downloaded into `data/raw/`. Nothing in `data/raw/` has been edited. Figures below are the final, corrected counts, established after the boundary problem described in the Week 3 note was found and fixed. The original download counts before that correction are also given for the record.

---

## Layers in the project

| Layer | Downloaded | Final, after Week 3 correction | Geometry |
|---|---|---|---|
| `Ila_LGA` | 1 | 1, retained for context only | Polygon |
| `Ila_LGA_Wards` | 11 | 11 | Polygon |
| `Ila_LGA_Health_Facility` | 91 | 48 | Point |
| `Ila_LGA_Roads` | 2,053 | 1,082 | Line |

---

## 1. GRID3 NGA Operational Wards v3.0

**Source:** GRID3 Data Hub
**Link:** https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v3-0/about
**Version and date published:** v3.0, July 2026
**Format:** GeoPackage
**Features after filtering to Ila:** 11
**Geometry type:** Polygon
**CRS as downloaded:** EPSG:4326, WGS84
**Key columns:** ward name, LGA name, state name, GRID3 identifier codes

The dataset covers 24 states: Abia, Adamawa, Bauchi, Bayelsa, Borno, Delta, Enugu, FCT Abuja, Gombe, Jigawa, Kaduna, Kano, Katsina, Kebbi, Kogi, Kwara, Nasarawa, Niger, Ogun, Osun, Oyo, Sokoto, Yobe and Zamfara. Osun is included, so Ila is covered at ward level.

Ila Local Government Area is administered as eleven political wards, and the filtered layer returns exactly eleven polygons.

GRID3 states that these boundaries are intended for operational use and have not undergone full validation by the relevant government authorities.

---

## 2. GRID3 NGA Operational LGA Boundaries

**Source:** GRID3 Data Hub
**Link:** https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about
**Version and date published:** December 2020
**Format:** GeoPackage
**Features after filtering to Ila:** 1
**Geometry type:** Polygon
**CRS as downloaded:** EPSG:4326, WGS84
**Key columns:** LGA name, state name, GRID3 identifier codes

Retained for context and orientation. It is not used to define the study area. Overlaying it against the ward layer in Week 3 showed the two outlines disagreeing along most of the perimeter, with the LGA boundary extending several kilometres beyond the ward coverage in places. The full finding and its consequence are recorded in `week-3-data-preparation.md`.

---

## 3. GRID3 NGA Health Facilities v3.0

**Source:** GRID3 Data Hub
**Link:** https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-v2-0/about
**Version:** v3.0
**Format:** GeoPackage
**Features inside the LGA boundary, as first downloaded:** 91
**Features inside the ward study area, after Week 3 correction:** 48
**Geometry type:** Point
**CRS as downloaded:** EPSG:4326, WGS84
**Key columns:** facility name, facility type, ownership, ward, LGA, state

This is the primary dataset for the project. It covers the same 24 states as the ward layer, Osun included.

The download page address contains `v2-0` while the dataset description and the layer name give v3.0. The layer used in this project is v3.0.

GRID3 describes this dataset as a non-exhaustive, non-validated geographic representation of health facility points. A ward returning a low count is unverified rather than unserved, and the final result is worded with that in mind.

Forty-three of the ninety-one facility points fell between the LGA boundary and the ward coverage and were excluded once the study area was redefined as the wards themselves. Forty-eight facilities across eleven wards averages a little over four per ward, which is a plausible density for a largely rural local government of this size.

---

## 4. OpenStreetMap roads

**Source:** OpenStreetMap, extracted with the QuickOSM plugin inside QGIS
**Link:** https://www.openstreetmap.org
**Query:** key `highway`, no value, extent set to the Ila LGA layer
**Format:** GeoPackage
**Features, as first extracted:** 2,053
**Features inside the ward study area, after Week 3 correction:** 1,082
**Geometry type:** Line
**CRS as extracted:** EPSG:4326, WGS84
**Key columns:** `highway`, `name`, `surface`, OSM identifier

Provides context this month. Needed properly later, when ward membership is replaced by travel distance along the network.

The `surface` column is sparsely populated, which is typical of OpenStreetMap coverage in Nigeria outside major cities. Paved and unpaved roads cannot be reliably separated across the whole network on this data alone.

Attribution required: © OpenStreetMap contributors.

---

## 5. GRID3 NGA Population Estimates v3.0

**Source:** GRID3 Data Hub
**Link:** https://data.grid3.org
**Format:** GeoTIFF
**Geometry type:** Raster, one band, Float32
**Resolution:** 0.000833 degrees, about 3 arc-seconds or roughly 100 metres
**CRS as downloaded:** EPSG:4326, WGS84
**Used for:** population total per ward, by zonal statistics

The estimates were produced by WorldPop at the University of Southampton, which combined the 2022 to 2023 National Malaria Elimination Programme headcount data with settlement footprints and geospatial covariates in a hierarchical model, then scaled the results to the UN World Population Prospects July 2025 median national projections.

These are modelled estimates, not counts. The raster was left in EPSG:4326, because reprojecting a population raster resamples its cells and changes the total. The eleven ward totals sum to 149,378 against a 2006 census figure of 62,049 for the LGA.

---

## 6. GRID3 NGA Population mastergrid, downloaded and rejected

**Source:** GRID3 Data Hub, the second download on the population dataset page
**File:** `NGA_population_v3_0_mastergrid.tif`
**Format:** GeoTIFF, Float32, 14,392 by 11,532 cells
**CRS:** EPSG:4326, WGS84
**Value range:** minimum 0, maximum 1

This file is a reference grid that marks which cells count as populated. Every cell holds 0 or 1, so it carries no population counts. Zonal statistics run on it returned 3,123 for the whole LGA, a count of populated cells rather than of people, which was caught by comparing against the census figure. It stays in `data/raw/` for the record and was not used in any result.

---

## Not yet used

GRID3 NGA Settlement Extents v4.1, August 2026, named in the project brief, has not been used in this month's analysis.

---

## Attribution

GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development). Operational Wards v3.0, Operational LGA Boundaries, and Health Facilities v3.0.

© OpenStreetMap contributors.
