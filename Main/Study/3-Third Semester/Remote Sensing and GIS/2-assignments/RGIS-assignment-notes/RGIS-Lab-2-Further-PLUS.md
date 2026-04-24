Here is exactly what you need to do in **QGIS**, step by step.

## 1. Download school data from OpenStreetMap

Go to **overpass-turbo.eu**.

Click **Wizard** and type:

```text
amenity=school in Kathmandu
```

Click **Build and Run Query**.

Then click:

**Export → GeoJSON → Download**

OSM uses `amenity=school` for schools, so this is the correct tag. ([OpenStreetMap][1])

## 2. Add the school data in QGIS

Open QGIS.

Go to:

**Layer → Add Layer → Add Vector Layer**

Select the downloaded `.geojson` file.

You may see both:

**points** = schools mapped as points
**polygons** = school areas/buildings

## 3. Convert polygon schools to points

For polygon school layer:

Go to:

**Processing Toolbox → Vector Geometry → Centroids**

Input layer: school polygon layer
Run.

This creates center points for polygon schools.

## 4. Merge school points together

Now merge:

Original school point layer
Centroid layer from polygons

Go to:

**Processing Toolbox → Vector General → Merge Vector Layers**

Select both point layers.

Save as:

```text
Kathmandu_Valley_Schools_All_Points
```

This is your main school point layer.

## 5. Add boundary and road layers

You need:

Kathmandu Valley / municipal boundary layer
Kathmandu Metropolitan City boundary
Road network layer
Ring Road layer

Add them the same way:

**Layer → Add Layer → Add Vector Layer**

Make sure all layers use the same CRS. For Nepal work, use projected CRS such as:

```text
EPSG:32645 - WGS 84 / UTM zone 45N
```

Right-click each layer → **Export → Save Features As** → choose EPSG:32645.

This is important because buffer distance must be in meters.

## 6. Question i: Schools within 2 km of Department of Chemistry, TU

First create a point for Department of Chemistry, Tribhuvan University.

Use:

**Layer → Create Layer → New GeoPackage Layer**

Geometry: Point
CRS: EPSG:32645
Add one point at Department of Chemistry, TU.

Then create 2 km buffer:

**Processing Toolbox → Vector Geometry → Buffer**

Input: Department of Chemistry point
Distance:

```text
2000
```

Dissolve: Yes
Run.

Then select schools inside buffer:

**Processing Toolbox → Vector Selection → Extract by Location**

Input layer: merged school points
Predicate: within / intersects
Compare layer: 2 km buffer

Save output as:

```text
Schools_Within_2km_TU_Chemistry
```

## 7. Question ii: Schools inside Kathmandu Metropolitan City

Use Kathmandu Metropolitan City boundary.

Go to:

**Processing Toolbox → Vector Selection → Extract by Location**

Input layer: merged school points
Predicate: within
Compare layer: Kathmandu Metropolitan City boundary

Save as:

```text
Schools_Kathmandu_Metropolitan_City
```

This creates both:

map layer
attribute/database table

To see the table:

Right-click layer → **Open Attribute Table**

## 8. Question iii: Schools within 1 km buffer of Ring Road

First make sure you have the Ring Road line layer.

If your road layer has many roads, select Ring Road:

Open road layer attribute table
Search/filter name contains:

```text
Ring Road
```

Export selected feature:

Right-click road layer → **Export → Save Selected Features As**

Name it:

```text
Ring_Road
```

Now create 1 km buffer:

**Processing Toolbox → Vector Geometry → Buffer**

Input: Ring_Road
Distance:

```text
1000
```

Dissolve: Yes
Run.

Then extract schools within that buffer:

**Processing Toolbox → Vector Selection → Extract by Location**

Input layer: merged school points
Predicate: within / intersects
Compare layer: Ring Road 1 km buffer

Save as:

```text
Schools_Within_1km_Ring_Road
```

To count schools:

Right-click `Schools_Within_1km_Ring_Road` → **Show Feature Count**

or open attribute table and check total number at bottom.

## 9. Final outputs you should submit

You should have these layers:

```text
Kathmandu_Valley_Schools_All_Points
Schools_Within_2km_TU_Chemistry
Schools_Kathmandu_Metropolitan_City
Ring_Road_1km_Buffer
Schools_Within_1km_Ring_Road
```

And tables:

```text
Schools_Within_2km_TU_Chemistry table
Schools_Kathmandu_Metropolitan_City table
Schools_Within_1km_Ring_Road table
```

## 10. Make final map

Use different colors:

All schools: gray small dots
2 km TU schools: red dots
KMC schools: blue dots
Ring Road buffer schools: green dots
Ring Road buffer: transparent polygon
KMC boundary: outline only
Ring Road: thick black line

Then go to:

**Project → New Print Layout**

Add map, legend, scale bar, north arrow, title.

Title example:

```text
School Distribution Analysis in Kathmandu Valley
```

Use **Export as PDF**.

[1]: https://wiki.openstreetmap.org/wiki/Tag%3Aamenity%3Dschool?utm_source=chatgpt.com "Tag:amenity=school - OpenStreetMap Wiki"
