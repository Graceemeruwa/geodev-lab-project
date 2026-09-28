# Month 1 summary

## Question

How many health facilities does each ward in Ila Local Government Area, Osun State contain, and how many residents does a single facility have to cover in each of those wards?

## Operation

Counted GRID3 health facility points inside each of the eleven ward polygons with Count Points in Polygon, summed the GRID3 modelled population inside each ward with zonal statistics, and divided population by facility count to give residents per facility. I chose a point count and a division because the question asks for a count per ward and a load per facility, and a per-ward comparison is what a health department needs to rank wards.

## Expected

From the project brief: facilities would cluster in the wards nearest the headquarters town and thin out toward the outlying wards, and a raw count would therefore hide which wards were most stretched once population was taken into account.

## Got

48 facilities across eleven wards serving a modelled 149,378 people, an average of about 3,100 residents per facility. Oke Ejigbo III has the heaviest load at about 6,400 residents per facility, and Oke Ejigbo II the lightest at about 760. Eyindi has no facility listed for about 2,100 residents. Five of the eleven wards sit above the LGA average.

The full table is in `week-4-analysis.md` and the map is `maps/ila-facility-load.png`.

I checked the result four ways: the eleven ward counts sum to the 48 facilities in the clipped layer, the ward count stayed at eleven, the population total was compared against the 2006 census figure, and I counted the facility points in Oke Ejigbo I by hand and found nine, matching the table.

## What surprised me

The count and the load do not move together. Oke Ejigbo I has the most facilities of any ward, nine, and carries a below-average load. Oke Ejigbo III has four facilities and 17 percent of the LGA's population, which puts it at more than double the average load. A count on its own would have ranked these two wrongly.

Forty-three of the ninety-one facility points in my first download sat in the gap between the LGA boundary and the ward boundaries. Clipping to the LGA outline, the obvious choice, would have left nearly half my facility points in no ward at all and dropped them silently from every ward count. Redefining the study area as the wards themselves brought the total to 48.

My first population result was wrong by a factor of twenty. I had run zonal statistics on the GRID3 mastergrid, a raster of 0s and 1s marking populated cells, and counted 3,123 cells instead of people. Comparing the total against the 2006 census figure of 62,049 caught it before it reached the ranking.

I also entered the first reprojection in UTM zone 32N. The layers drew in the right place with no error, and only the extent, with eastings far below the valid range, exposed it. Ila belongs in zone 31N.

## What data I still need

- **A road network with speeds**, to replace ward membership with travel distance. A ward can be well supplied on paper and still be a long journey from its nearest facility.
- **Facility type in usable form**, so a primary health centre is not counted as equivalent to a small clinic.
- **An independent second facility list**, the Nigeria Health Facility Registry, to test how complete the GRID3 layer is and to settle whether Eyindi genuinely has no facility.
- **Population by age**, to see the load among children under five and women of childbearing age, who use primary care most.
