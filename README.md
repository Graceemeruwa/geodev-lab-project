# geodev-lab-project

# University of Ibadan deforestation and carbon loss, 2000 to 2025

How much tree canopy did the University of Ibadan campus lose between 2000 and 2025, and how much above-ground carbon was lost with it?

Built over twelve months with GeoDev Lab Africa, Cohort One.

## Study area

The University of Ibadan estate in Ibadan North LGA, Oyo State, Nigeria, at approximately 7.44 degrees north, 3.90 degrees east. About 1,185 hectares across three parcels: developed campus, Ajibode resettlement area, and undeveloped extension site.

All analysis is carried out in EPSG:32631, UTM zone 31 north.

## Data

| Layer | Source | Resolution | Coverage |
|---|---|---|---|
| Campus boundary | Digitised from OpenStreetMap and Sentinel-2 imagery | vector | 3 parcels |
| Tree canopy cover 2000 | Hansen Global Forest Change GFC-2025-v1.13 | 30 m | year 2000 baseline |
| Year of canopy loss | Hansen Global Forest Change GFC-2025-v1.13 | 30 m | 2001 to 2025 |
| Above-ground biomass | ESA CCI Biomass v7.0 | 100 m | 2005 to 2012, 2015 to 2024 |
| Optical imagery | Copernicus Sentinel-2 Level 2A | 10 m | 2015 to present |
| Roads, buildings, land use | OpenStreetMap via QuickOSM | vector | current |

## Repository contents

- `project-brief.md` is the full project brief.
- `data-notes.md` records every layer, its source, its version, its date and its quality assessment.
- `month-1-summary.md` records the first analysis, what was expected and what came out.
- `data/raw/` holds downloaded files exactly as they arrived and is never edited.
- `data/processed/` holds everything derived from them.

## Attribution

Hansen, M. C. et al. 2013. High-Resolution Global Maps of 21st-Century Forest Cover Change. Science 342: 850 to 853.

Santoro, M. and Cartus, O. 2026. ESA Biomass Climate Change Initiative (Biomass_cci), v7.0. NERC EDS Centre for Environmental Data Analysis. doi:10.5285/6429d1aafe1e43b9b414e4a5a7f8b903

© OpenStreetMap contributors. Contains modified Copernicus Sentinel data.
