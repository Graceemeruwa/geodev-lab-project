# Project brief

GeoDev Lab Africa, Cohort One. Month 1.

---

## Part 1: The question

How much tree canopy did the University of Ibadan campus lose between 2000 and 2025, and how much above-ground carbon was lost with it?

---

## Part 2: Why it matters

The University of Ibadan holds about 1,185 hectares in the middle of a city of several million people, and it is one of the few large tree-covered blocks left inside Ibadan. Roughly 671 hectares is developed campus, 514 hectares is an undeveloped extension site, and 106 hectares is the Ajibode resettlement area.

The Directorate of Physical Planning and Project Management would use the answer. When a new building site is proposed, nobody can currently say how much canopy has already gone or what it was worth in carbon. A per-parcel figure gives that office a baseline it does not have.

The Department of Forest Production and Products teaches this material and holds field plots on campus, so the result can be checked against ground measurements rather than standing alone.

---

## Part 3: The data I need

1. Campus boundary, split into developed campus, extension site and Ajibode area. Polygons.
2. Tree canopy cover in the year 2000, as percentage cover per pixel. Raster, 30 m.
3. Year of canopy loss for every pixel that lost cover, 2001 to 2025. Raster, 30 m.
4. Above-ground biomass in tonnes per hectare, for two widely separated years. Raster, 100 m.
5. Optical satellite imagery for visual verification of claimed loss. Raster, 10 m.
6. Roads, buildings and land use inside the campus. Vector.

---

## Part 4: Where each dataset comes from

**1. Campus boundary.** No open authoritative boundary exists for the university estate, so I am digitising it. Base outline from OpenStreetMap, extracted with the QuickOSM plugin in QGIS using key `amenity` value `university` and key `landuse` with no value. Corrected by hand against Sentinel-2 and satellite basemap imagery, and split into the three parcels. Published area figures for checking my result against are at https://physicalplanning.ui.edu.ng/history. Output as GeoPackage, under 1 MB.

**2 and 3. Canopy cover 2000, and year of loss.** Hansen Global Forest Change, University of Maryland GLAD laboratory with Google, release GFC-2025-v1.13, covering 2000 to 2025 at 30 m. Download page: https://storage.googleapis.com/earthenginepartners-hansen/GFC-2025-v1.13/download.html

Ibadan falls in granule `10N_000E`. Files needed:

```
Hansen_GFC-2025-v1.13_treecover2000_10N_000E.tif
Hansen_GFC-2025-v1.13_lossyear_10N_000E.tif
Hansen_GFC-2025-v1.13_datamask_10N_000E.tif
```

Each granule is 10 degrees square, in the region of 100 to 500 MB. Clipped to the campus immediately on download.

**4. Above-ground biomass.** ESA Climate Change Initiative Biomass, version 7.0, at 100 m, annually for 2005 to 2012 and 2015 to 2024. Taking 2010 and 2024 as the comparison years. Portal: https://climate.esa.int/en/projects/biomass/data/ Catalogue record: https://catalogue.ceda.ac.uk/uuid/6429d1aafe1e43b9b414e4a5a7f8b903/

Biomass converts to carbon using the IPCC default carbon fraction of 0.47, and to carbon dioxide equivalent by multiplying by 44 divided by 12.

**5. Optical imagery.** Copernicus Data Space Ecosystem, https://dataspace.copernicus.eu. Sentinel-2 Level 2A, 10 m, free with registration.

**6. Roads, buildings and land use.** OpenStreetMap via QuickOSM, keys `highway`, `building` and `landuse`, extracted to the campus boundary.

**The hardest dataset, downloaded first.** The Hansen `lossyear` granule. It is the largest file and the only source carrying the year of loss, which the whole question depends on. If the campus holds too few loss pixels to measure, the question changes, and I need to know that in week one.

---

## Part 5: What I would build

A canopy and carbon record for the University of Ibadan estate that rebuilds itself rather than being recalculated by hand.

It holds the campus boundary, ingests each new annual release of the forest change and biomass products, recomputes canopy area and estimated carbon stock for each of the three parcels, and presents the result as a map and a short table that somebody in the physical planning office can open without knowing what a coordinate reference system is.

---

## Attribution

Hansen, M. C. et al. 2013. High-Resolution Global Maps of 21st-Century Forest Cover Change. Science 342: 850 to 853.

Santoro, M. and Cartus, O. 2026. ESA Biomass Climate Change Initiative (Biomass_cci), v7.0. NERC EDS Centre for Environmental Data Analysis. doi:10.5285/6429d1aafe1e43b9b414e4a5a7f8b903

© OpenStreetMap contributors. Contains modified Copernicus Sentinel data.
