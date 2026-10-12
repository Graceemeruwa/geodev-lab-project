# Week 3: data preparation and quality checks

**Project:** Distribution of health facilities in Ila Local Government Area, Osun State, and the population they serve
GeoDev Lab Africa, Cohort One. Month 1, Week 3.

---

## The coordinate system I chose, and why

**Working CRS: EPSG:32631, WGS 84 / UTM zone 31N. Units are metres.**

Every source layer arrived in EPSG:4326, WGS 84 geographic, whose units are degrees of latitude and longitude. Degrees are angles rather than distances, so any area or distance calculated in that system is measured in square degrees and means nothing on the ground. One degree of longitude is about 111 kilometres at the equator and zero at the pole, so the unit changes size depending on where you stand.

Ila Local Government Area is centred on Ila Orangun at approximately 8.02 degrees north and 4.90 degrees east. UTM zone 31N spans 0 to 6 degrees east, which places Ila comfortably inside it and less than two degrees from the zone's central meridian at 3 degrees east. Distortion is minimal at that distance, so areas and distances computed in EPSG:32631 are reliable for this study area.

The project CRS and every layer CRS were set to EPSG:32631 so the two agree. They are separate settings in QGIS and both matter.

**Confirmed after reprojection.** The Ila LGA boundary reports an extent of 699,082 to 720,648 metres east and 867,258 to 895,321 metres north. Valid UTM eastings fall roughly between 166,000 and 834,000, so these sit comfortably inside the zone. That bounding box measures about 21.6 by 28.1 kilometres, enclosing roughly 605 square kilometres. Ila LGA is published at about 303 square kilometres, so the boundary fills a little over half its bounding box, which is what an irregular outline of that size should do.

---

## What I reprojected and what I clipped

**Reprojected.** All four layers moved from EPSG:4326 to EPSG:32631 using Vector, Data Management Tools, Reproject Layer. The coordinates change, the features stay in the same real place.

- Ila LGA boundary, 1 polygon
- Ila wards, 11 polygons
- Health facilities, 91 points
- Roads, 2,053 lines

**Clipped.** The eleven ward polygons were dissolved into a single outline and exported as the study area, then used as the overlay layer to cut everything else down to it with Vector, Geoprocessing Tools, Clip. Both input and overlay were confirmed to be in EPSG:32631 before each clip, since a clip between mismatched systems returns nothing or returns something wrong.

The first round of clipping used the LGA boundary instead. That was changed once the overlay showed the two outlines disagreeing, for the reason set out under problems below.

**Order of operations.** Reprojection ran before clipping so that both layers in every clip shared one coordinate system.

**Nothing in `data/raw/` was modified.** Every output was written into `data/processed/`.

---

## The five quality checks

### 1. Completeness

Is everything there that should be?

The ward layer returns exactly 11 polygons for Ila, which agrees with the eleven political wards the local government is administered as. That count passes.

The health facility layer is the concern. GRID3 describes it in its own documentation as a non-exhaustive, non-validated geographic representation of health facility points. Ninety-one points fall inside Ila. That figure is not a census of what exists, and a ward returning a low count has to be read as unverified rather than unserved.

I compared the facility points against satellite imagery over Ila Orangun, where I know the ground, and against facilities I am personally aware of. Result: the points present correspond to real facilities, and the dataset is usable for a relative comparison between wards rather than as an absolute inventory.

Road coverage is dense around Ila Orangun and thins toward the outlying rural wards, which matches the settlement pattern rather than indicating a mapping gap in the built-up core.

### 2. Currency

When was it made, and has the world changed since?

- Operational Wards v3.0, published July 2026. Current.
- Health Facilities v3.0, published August 2026. Current.
- Operational LGA Boundaries, published December 2020. Five and a half years old.
- OpenStreetMap roads, extracted for this project in Week 2. Current as at extraction, though individual road features carry their own last-edited dates and many are older.

The LGA boundary is the weak link. It predates the ward layer by more than five years, and administrative boundaries in Nigeria do change. Ila Central Local Council Development Area was carved out of Ila in 2017 and appears in neither layer, since LCDAs are state creations that are not carried in federally aligned boundary sets. The analysis therefore works with the eleven wards of the federally recognised local government, which is stated rather than assumed.

### 3. Positional accuracy

Is it in the right place?

The ward and LGA boundaries were overlaid on satellite imagery. Boundary lines follow recognisable features such as roads and watercourses where they should, and no systematic offset is visible between the vector edges and the imagery beneath them.

Health facility points were checked against imagery in Ila Orangun, where building compounds are clearly visible. Points sit on or close to identifiable compounds rather than being displaced in a consistent direction, so there is no systematic shift to correct for.

Positional accuracy at the scale of a few tens of metres does not affect this project's result. The analysis assigns each facility to the ward it falls within, and ward polygons are kilometres across, so a facility would need to be displaced very badly to land in the wrong ward. The exception is facilities sitting close to a ward boundary line, which are flagged below.

### 4. Attribute accuracy

Are the labels right?

Ward names were read down in full and checked against the eleven wards Ila is known to comprise. Names are internally consistent within the layer, with no ward appearing twice under variant spellings.

The facility type column is the one that carries risk. Ninety-one facilities across eleven wards averages just over eight per ward, which is high for a largely rural local government of this size, and it indicates the layer counts facilities of several different kinds rather than primary health centres alone. Counting all ninety-one as equivalent would overstate provision. The type column is therefore treated as load-bearing, and the Week 4 analysis reports counts by type as well as in total.

Key columns were sorted and the extremes inspected at both ends for blank values, trailing whitespace and case variants, since those are what silently split one category into several.

### 5. Fitness for purpose

Is this the right data for this question?

The ward boundaries are fit for purpose. They are the operational unit the question is asked in, and they are current.

The facility layer is fit for the question as worded, which asks how many facilities each ward contains. It is not fit for a question about facility capacity, staffing or service quality, none of which it records. It is also not fit for producing an absolute statement that a ward has no facility, because the dataset is non-exhaustive by its publisher's own description.

The LGA boundary is fit for defining a study area, which is all it is used for.

The road layer is not yet used in analysis. It is not fit for separating paved from unpaved roads, because the `surface` tag is sparsely populated across this extract, which rules out the road-surface refinement until a better source is found.

---

## Problems found, and what I did about them

**Reprojected into the wrong UTM zone, then corrected.** The first reprojection sent every layer to EPSG:32632, UTM zone 32N. The layers drew in the correct place on screen and QGIS raised no error. Checking the layer extent exposed it: eastings ran from about 37,984 to 52,795 metres, whereas valid UTM eastings fall roughly between 166,000 and 834,000. Ila sits at 4.9 degrees east, and zone 32N covers 6 to 12 degrees east, so the data had been projected into a zone it does not belong to and was more than four degrees from that zone's central meridian, where distortion is at its worst. **Fixed.** Everything was reprojected again from the untouched files in `data/raw/` to EPSG:32631. The LGA boundary now reports an extent of 699,082 to 720,648 metres east and 867,258 to 895,321 metres north, well inside the valid range for zone 31N, and the area figures are trustworthy.

**The LGA boundary and the ward boundaries do not coincide. Confirmed and resolved.** Overlaying the two showed them diverging along most of the perimeter rather than in one place. The ward layer is complete, with eleven polygons filling the interior and no gap between them, so no ward is missing. The disagreement is between two products published five and a half years apart, and it is largest on the eastern side, where the December 2020 LGA outline bulges several kilometres beyond the 2026 ward coverage. Elsewhere the wards extend slightly beyond the LGA line instead.

The consequence matters. Because everything was first clipped to the LGA boundary, a number of health facility points sit inside the study area but inside no ward. Visible on the eastern side of the map, these would be assigned null by a spatial join and would disappear from ward counts silently. **Fixed.** The study area was redefined as the eleven ward polygons dissolved into one, and every layer was reclipped to that. The facility count fell from 91 to 48 as a result, a loss of 43 points, and the road count fell from 2,053 to 1,082. The analysis unit and the study area now describe the same ground, and no facility is left orphaned between two boundaries.

**LGA boundary and ward boundaries differ in age by more than five years. Resolved by changing the study area.** The two outlines disagree along most of the perimeter. Rather than choose between them at every point of difference, the study area was rebuilt from the wards themselves, which are the newer product and the unit the analysis runs on. The LGA boundary is retained for context and is no longer used to cut anything.

**Facility types are mixed. Flagged and carried into Week 4.** The ninety-one points are not ninety-one equivalent facilities. Results will be reported by type as well as in total so the figure is not read as ninety-one primary health centres.

**Facilities near ward boundaries. Flagged.** Any facility point sitting on or very close to a boundary line will be assigned to one side by the spatial join without announcing which. These are identified and checked individually at the point they affect a ward's count.

**Road surface tag is sparse. Flagged.** Paved and unpaved roads cannot be separated reliably from this extract, so any travel-distance work later in the year treats all roads as equivalent unless a better surface source is found.

---

## Where the analysis-ready file lives

```
data/
  raw/                                 untouched downloads
  processed/
    ila_study_area.gpkg                eleven wards dissolved into one outline, EPSG:32631
    ila_analysis_ready.gpkg            all four layers, clipped and reprojected
```

`ila_analysis_ready.gpkg` holds four layers, every one clipped to the dissolved ward outline and projected to EPSG:32631:

| Layer | Geometry |
|---|---|
| `ila_lga` | Polygon |
| `ila_wards` | Polygon |
| `ila_health_facilities` | Point |
| `ila_roads` | Line |

Feature counts after the reclip:

| Layer | Features before reclip | Features after reclip | Geometry |
|---|---|---|---|
| `ila_lga` | 1 | 1 | Polygon |
| `ila_wards` | 11 | 11 | Polygon |
| `ila_health_facilities` | 91 | 48 | Point |
| `ila_roads` | 2,053 | 1,082 | Line |

Forty-three of the original ninety-one facility points fell in the gap between the LGA boundary and the ward coverage and are excluded from the study area now that it is defined by the wards themselves. That is not a small correction. Had the analysis proceeded on the LGA-clipped set, close to half the facility points used would have belonged to no ward at all, and any spatial join against them would have returned null without explanation.

Study area extent, EPSG:32631: 699,082 to 720,648 metres east, 867,258 to 895,321 metres north for the LGA boundary retained as context.

GeoPackage was chosen over shapefile because it holds several layers in one file, places no ten-character limit on field names, and does not break when a single file is moved without its companions.

---

## Attribution

GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development). Operational Wards v3.0, Operational LGA Boundaries, and Health Facilities v3.0.

© OpenStreetMap contributors.
