- [RGIS-Lab-2-Futher](RGIS-Lab-2-Futher.md)
- [RGIS-Lab-2-Further-PLUS](RGIS-Lab-2-Further-PLUS.md)
## Practical Workflow in QGIS: School Data of Kathmandu Valley from OpenStreetMap


# Part A: Download School Data from OpenStreetMap

## Step 1: Open Overpass Turbo

Go to:

Overpass Turbo

[https://www.overpass-turbo.eu/](https://www.overpass-turbo.eu/)

---

## Step 2: Use Wizard

Click **Wizard** and type:

```text
amenity=school in Kathmandu Valley
```

Or use:

```text
amenity=school in Kathmandu
```

Click **Build Query** → **Run**

==PROBLEM==
- *the above part only gives kathmandu metropolitan city not the whole valley*\

**BELOW FOCUS ON THE ktm , lalitpur and Bhaktapur**
- *there is lalitpur in INDIA as well*
- [https://www.overpass-turbo.eu/](https://www.overpass-turbo.eu/)
```md

/*
Kathmandu Valley Schools (Nepal specific)
*/
[out:json][timeout:25];

// fetch areas (force Nepal)
{{geocodeArea:Kathmandu, Nepal}}->.ktm;
{{geocodeArea:Lalitpur, Nepal}}->.lalitpur;
{{geocodeArea:Bhaktapur, Nepal}}->.bhaktapur;

// combine areas
(.ktm; .lalitpur; .bhaktapur;)->.searchArea;

// gather results
nwr["amenity"="school"](area.searchArea);

// print results
out geom;

```

---

## Step 3: Export Data

After schools appear:

* Click **Export**
* Choose **GeoJSON** or **Shapefile**

Save file.

---

# Part B: Load Data into QGIS

Open QGIS

## Add Layers:

1. School OSM data
2. Municipal boundary map
3. Road network map

---

# Part C: Convert Polygon Schools to Points

Some schools may be polygons (school compound).

## Use Centroid Tool:

```text
Vector → Geometry Tools → Centroids
```

This creates center points.

---

## Merge Point Layers

Merge:

* Original school points
* Centroid points

Use:

```text
Vector → Data Management Tools → Merge Vector Layers
```

Final output = All schools as points.

---

# Question (i)

## Identify all schools within 2 km radius of Department of Chemistry, Tribhuvan University

---

## Step 1: Locate Department of Chemistry

Search location of:

Department of Chemistry, Tribhuvan University

Add as point layer.

---

## Step 2: Create Buffer

```text
Vector → Geoprocessing Tools → Buffer
```

Parameters:

* Input = Chemistry Department point
* Distance = **2000 meters**

Output = 2 km buffer zone

---

## Step 3: Select Schools Inside Buffer

Use:

```text
Select by Location
```

Condition:

* Schools intersect buffer

Output:

All schools within 2 km radius.

---

# Question (ii)

## Create map layer and database table for schools inside Kathmandu Metropolitan City


==First GET THE MAP LIKE ROAD AND SCHOOLS==
- [https://www.overpass-turbo.eu/](https://www.overpass-turbo.eu/)
```md
[out:json][timeout:25];

// Kathmandu Metropolitan City boundary
{{geocodeArea:Kathmandu Metropolitan City, Nepal}}->.area;

relation(area.area)["boundary"="administrative"];

out geom;
```

---

## Step 1: Use Boundary Layer

Use municipal boundary of:

Kathmandu Metropolitan City


---

## Step 2: Extract Schools Inside Boundary

Use:

```text
Vector → Geoprocessing → Clip
```

OR

```text
Select by Location
```

Condition:

Schools within Kathmandu Metropolitan boundary.

---

## Step 3: Save New Layer

Right click selected schools:

```text
Export → Save Selected Features As
```

Name:

```text
Kathmandu_Schools.shp
```

---

## Step 4: Open Attribute Table

This becomes database table containing:

* Name
* ID
* Coordinates
* Tags

---

# Question (iii)

## Determine number of schools within 1 km buffer of Ring Road

---

## Step 1: Select Ring Road

Use road network map.

Identify:

Kathmandu Ring Road

---

## Step 2: Create Buffer

```text
Buffer distance = 1000 meters
```

around Ring Road.

---

## Step 3: Select Schools Inside Buffer

Use:

```text
Select by Location
```

Schools intersect 1 km Ring Road buffer.

---

## Step 4: Count Schools

Open attribute table:

Number of selected features = Total schools.

---

## Step 5: Save Separate Layer

```text
RingRoad_1km_Schools.shp
```

---

# Final Outputs Required

| Output | Result                                                          |
| ------ | --------------------------------------------------------------- |
| i      | Schools within 2 km of Chemistry Department TU                  |
| ii     | Schools inside Kathmandu Metropolitan City                      |
| iii    | Number of schools within 1 km Ring Road buffer + separate layer |

---

# Suggested Map Styling

## Two Theme Display:

### Point Schools

* Blue circle symbols

### Polygon Schools

* Green fill polygons

---

# Final Submission Items

1. QGIS project file (.qgz)
2. Shapefiles / GeoJSON outputs
3. Attribute tables
4. Final map layouts with legend, north arrow, scale

---

# Short Exam Answer

Downloaded school data from OSM using Overpass Turbo. Imported into QGIS. Converted polygons into centroids and merged with point schools. Created 2 km buffer around Department of Chemistry TU and selected nearby schools. Extracted schools within Kathmandu Metropolitan boundary. Created 1 km Ring Road buffer and counted schools inside it. Generated separate map layers and database tables.
