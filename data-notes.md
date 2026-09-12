# Data notes

**Project:** Distribution of health facilities in Ila Local Government Area, Osun State, and the population they serve
**Week 2 submission.** GeoDev Lab Africa, Cohort One.

All layers were downloaded into `data/raw/` and opened in QGIS. Nothing in `data/raw/` has been edited. Filtered and clipped working copies sit in `data/processed/`.

---

## Layers in the project

| Layer | Features | Geometry | Source |
|---|---|---|---|
| `Ila_LGA` | 1 | Polygon | GRID3 NGA Operational LGA Boundaries |
| `Ila_LGA_Wards` | 11 | Polygon | GRID3 NGA Operational Wards v3.0 |
| `Ila_LGA_Health_Facility` | 91 | Point | GRID3 NGA Health Facilities v3.0 |
| `Ila_LGA_Roads` | 2,053 | Line | OpenStreetMap via QuickOSM |

---

## 1. GRID3 NGA Operational Wards v3.0

**Source:** GRID3 Data Hub
**Link:** https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v3-0/about
**Version and date published:** v3.0, July 2026
**Format:** GeoPackage
**Features after filtering to Ila:** 11
**Geometry type:** Polygon
**CRS:** EPSG:4326, WGS84
**Key columns:** ward name, LGA name, state name, and GRID3 identifier codes

The dataset provides operational ward boundaries for 24 states: Abia, Adamawa, Bauchi, Bayelsa, Borno, Delta, Enugu, FCT Abuja, Gombe, Jigawa, Kaduna, Kano, Katsina, Kebbi, Kogi, Kwara, Nasarawa, Niger, Ogun, Osun, Oyo, Sokoto, Yobe and Zamfara. Osun is among them, so Ila is covered at ward level and no fallback to LGA boundaries was required.

Ila Local Government Area is administered as eleven political wards and the filtered layer returns exactly eleven polygons. The count agrees with the published administrative structure.

GRID3 states that these boundaries are intended for operational use and have not undergone full validation by the relevant government authorities. Every figure in this project therefore describes the GRID3 operational ward set rather than a boundary set formally approved by Osun State.

---

## 2. GRID3 NGA Operational LGA Boundaries

**Source:** GRID3 Data Hub
**Link:** https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about
**Version and date published:** December 2020
**Format:** GeoPackage
**Features after filtering to Ila:** 1
**Geometry type:** Polygon
**CRS:** EPSG:4326, WGS84
**Key columns:** LGA name, state name, and GRID3 identifier codes

This layer defines the study area and confirms that the eleven filtered wards belong to Ila. Nothing is measured from it directly.

It carries a December 2020 publication date while the ward layer carries July 2026, a gap of six years. Boundary sets published that far apart are not guaranteed to align exactly, and where the two differ the ward layer is treated as the authority for this project, since it is the newer product and the unit the analysis runs on.

Ila Central Local Council Development Area was carved out of Ila in 2017 and does not appear as a separate unit in either GRID3 layer. LCDAs are state creations and are not carried in federally aligned boundary sets, so the analysis works with the eleven wards of the federally recognised local government.

---

## 3. GRID3 NGA Health Facilities v3.0

**Source:** GRID3 Data Hub
**Link:** https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-v2-0/about
**Version:** v3.0
**Format:** GeoPackage
**Features inside Ila LGA:** 91
**Geometry type:** Point
**CRS:** EPSG:4326, WGS84
**Key columns:** facility name, facility type, ownership, ward, LGA, state

This is the primary dataset for the project. It covers the same 24 states as the ward layer, Osun included.

The download page address contains `v2-0` while the dataset description and the layer itself are v3.0. The address is recorded here exactly as used so the download remains reproducible.

GRID3 describes this dataset as a non-exhaustive, non-validated geographic representation of health facility points. Non-exhaustive is the operative term. A ward returning a low count is unverified rather than unserved, and the Week 4 result is worded to reflect that.

Ninety-one facilities across eleven wards averages just over eight per ward. Set against the 2006 census figure of 62,049 residents for the LGA, that is a high density for a largely rural local government, and it indicates the layer counts facilities of several different kinds rather than primary health centres alone. The facility type column is therefore treated as load-bearing, and facilities are not counted as equivalent to one another without reference to it.

---

## 4. OpenStreetMap roads

**Source:** OpenStreetMap, extracted with the QuickOSM plugin inside QGIS
**Link:** https://www.openstreetmap.org
**Query:** key `highway`, no value, extent set to the Ila LGA layer
**Format:** GeoPackage
**Features:** 2,053
**Geometry type:** Line
**CRS:** EPSG:4326, WGS84
**Key columns:** `highway`, `name`, `surface`, OSM identifier

Roads provide context this month. They carry the analysis later, when ward membership is replaced by travel distance along the network.

Feature count is not the same as road count. OpenStreetMap splits a single road into separate segments wherever tagging changes, so 2,053 lines represent considerably fewer distinct roads. Coverage is dense around Ila Orangun and thins toward the outlying rural wards, which matches the settlement pattern of the local government.

The `surface` column is sparsely populated, as is typical of OpenStreetMap coverage in Nigeria outside major cities. Paved and unpaved roads cannot be reliably separated across the whole network on this data alone.

Attribution required: © OpenStreetMap contributors.

---

## Next datasets

Named in the project brief and scheduled for the weeks ahead.

- GRID3 NGA gridded population estimates, to convert facility counts into residents per facility.
- GRID3 NGA Settlement Extents v4.1, August 2026, to show how each ward's population is distributed.
- Nigeria Health Facility Registry, https://hfr.health.gov.ng, as an independent list to set against the 91 GRID3 points.

---

## Attribution

GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development). Operational Wards v3.0, Operational LGA Boundaries, and Health Facilities v3.0.

© OpenStreetMap contributors.
