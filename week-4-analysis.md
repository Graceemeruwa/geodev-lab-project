# Week 4: analysis

**Project:** Distribution of health facilities in Ila Local Government Area, Osun State, and the population they serve
GeoDev Lab Africa, Cohort One. Month 1, Week 4.

---

## The result

Across the eleven wards of Ila LGA, GRID3 lists 48 health facilities serving a modelled population of 149,378 people, an average of about 3,100 residents per facility. The load is very uneven.

- **Oke Ejigbo III carries the heaviest load**, with about 6,400 residents per facility. It holds 17 percent of the LGA's population and 8 percent of its listed facilities.
- **Oke Ejigbo II carries the lightest**, with about 760 residents per facility, more than eight times lower than Oke Ejigbo III.
- **Eyindi has no facility listed** for a modelled population of about 2,100.
- **Five of the eleven wards sit above the LGA average** of 3,112 residents per facility: Oke Ejigbo III, Iperin, Isedo I, Iperin/Eyindi and Oke Ola.
- **Facility count alone misleads.** Oke Ejigbo I has the most facilities of any ward (9) and is well below the average load, while Iperin has 8 facilities and the second heaviest load, because it is the most populous ward at 33,733 people.

---

## Results by ward

Ordered from heaviest load to lightest.

| Ward | Facilities | Population (modelled) | Residents per facility |
|---|---|---|---|
| Oke Ejigbo III | 4 | 25,725 | 6,431 |
| Iperin | 8 | 33,733 | 4,217 |
| Isedo I | 4 | 13,972 | 3,493 |
| Iperin/Eyindi | 3 | 9,869 | 3,290 |
| Oke Ola | 4 | 13,118 | 3,280 |
| Oke Ede | 2 | 5,972 | 2,986 |
| Isedo II | 3 | 8,523 | 2,841 |
| Oke Ejigbo I | 9 | 23,822 | 2,647 |
| Ajaba | 7 | 9,518 | 1,360 |
| Oke Ejigbo II | 4 | 3,042 | 760 |
| Eyindi | 0 | 2,083 | none listed |
| **Ila LGA** | **48** | **149,378** | **3,112** |

Population figures are rounded to whole people. Residents per facility is population divided by facility count, so a ward with no facility has no defined value and is reported as none listed rather than as zero or infinity.

---

## What I ran

Every layer was in EPSG:32631 before the analysis began, apart from the population raster, which was left in its native EPSG:4326. Zonal statistics transforms the polygons to the raster's coordinate system internally, and reprojecting a population raster would resample its cells and change the total.

1. **Count facilities per ward.** Vector, Analysis Tools, Count Points in Polygon, with the eleven ward polygons and the 48-point corrected facility layer. Output saved to `data/processed/`.
2. **Sum population per ward.** Processing Toolbox, Zonal statistics, sum only, using the GRID3 NGA population estimates raster. Output column `pop_sum`.
3. **Divide.** Field calculator, `"pop_sum" / "facility_count"`, giving residents per facility. Wards with no facility return null, which is correct.

---

## The checks

**Facility counts add up.** The eleven ward counts sum to 48, exactly the number of points in the clipped facility layer. Every facility is assigned to one ward, none is orphaned between boundaries, and none is counted twice.

**Eleven rows in, eleven rows out.** The ward count is unchanged from the layer as downloaded.

**One ward counted by hand.** I counted the facility points inside Oke Ejigbo I on screen and found nine, matching the count in the results table. Oke Ejigbo I has the highest count of any ward, so it is the ward where a join error would show most.

**Population total against the census.** The eleven ward totals sum to 149,378. The 2006 census recorded 62,049 people in Ila LGA, so the modelled 2026 figure is about 2.4 times larger. That is the right order of magnitude, and it is higher than national population growth alone would imply, which is consistent with a modelled estimate rather than a count.

**A wrong result was caught by this check.** The first zonal statistics run used the GRID3 mastergrid instead of the population estimates file and returned a total of 3,123, roughly twenty times below the census. The mastergrid holds a value of 0 or 1 in every cell, marking whether a cell is populated, so the tool had counted 3,123 populated cells rather than people. The run was repeated with the population estimates raster, and the mastergrid is kept in `data/raw/` and recorded in `data-notes.md` as downloaded and rejected. Without the census comparison, that first figure would have produced a ranking that looked entirely plausible and was wrong.

---

## Limitations

**Straight-line ward membership, not travel distance.** A facility counts for a ward because it sits inside the ward boundary. A resident of one ward may live closer to a facility in the next. Residents per facility describes load within administrative boundaries, not how far anyone has to travel. Eyindi shows this most clearly. It has no facility listed, but it sits in the middle of the LGA and is surrounded by wards that do have facilities, so its residents may live a short distance from one just across a ward boundary.

**The facility layer is non-exhaustive.** GRID3 describes it as a non-exhaustive, non-validated representation of health facility points. Eyindi having no facility listed means none appears in this dataset. It is not evidence that none exists.

**All facilities are counted as equal.** A facility is a facility in this analysis. The layer contains more than one kind of facility, and a primary health centre is not equivalent to a small private clinic. Weighting by type is not done here.

**Population is modelled, not counted.** GRID3 built these estimates from the 2022 to 2023 National Malaria Elimination Programme headcount data, settlement footprints and geospatial covariates, using WorldPop's hierarchical modelling, then scaled them to the UN World Population Prospects July 2025 national projections. Every figure carries modelling uncertainty and should be quoted as an estimate.

**Ward names overlap.** The layer holds Iperin, Eyindi and a separate feature named Iperin/Eyindi, whose alternative names refer back to both. They are treated as three distinct wards because they are three features in the source. If GRID3 or the local government later merges or renames them, the results for those three rows change.

**Boundaries are unvalidated.** GRID3 states that the ward boundaries are operational and have not been fully validated by the relevant government authorities.

---

## Files

- Analysis-ready data: `data/processed/ila_analysis_ready.gpkg`
- Ward results with counts and population: `data/processed/`
- Map: `maps/ila-facility-load.png`
- Summary: `month-1-summary.md`

---

## Attribution

GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development). Operational Wards v3.0, Health Facilities v3.0, and NGA Population Estimates v3.0.

© OpenStreetMap contributors.
