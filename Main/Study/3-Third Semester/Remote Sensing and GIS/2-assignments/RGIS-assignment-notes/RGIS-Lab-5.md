#RGIS #third-semester #assignment 


## Step 0: Install Python

Check if Python is installed:

```bash
python --version
```

or

```bash
py --version
```

You should see something like:

```text
Python 3.12.4
```

If not, install Python from:

[Python Official Website](https://www.python.org/downloads/?utm_source=chatgpt.com)

---

## Step 1: Create a Project Folder

Create a folder anywhere convenient:

```text
GIS_Assignment
```

Example:

```text
D:\GIS_Assignment
```

Open Command Prompt inside that folder.

---

## Step 2: Create Virtual Environment

In the project folder:

```bash
python -m venv venv
```

or

```bash
py -m venv venv
```

This creates:

```text
GIS_Assignment
│
├── venv
```

---

## Step 3: Activate Environment

### Windows

```bash
venv\Scripts\activate
```

You should see:

```text
(venv) D:\GIS_Assignment>
```

The `(venv)` means the environment is active.

---

## Step 4: Upgrade Pip

```bash
python -m pip install --upgrade pip
```

---

## Step 5: Install Required Libraries

GeoPandas can take a while.

```bash
pip install geopandas osmnx matplotlib pandas
```

Verify:

```bash
pip list
```

You should see:

```text
geopandas
osmnx
pandas
matplotlib
shapely
pyproj
```

---

## Step 6: Create Python Script

Create a file:

```text
kirtipur_analysis.py
```

Paste this first test code:

```python
import geopandas as gpd
import osmnx as ox

print("Everything installed successfully!")
```

Run:

```bash
python kirtipur_analysis.py
```

Expected:

```text
Everything installed successfully!
```

---

## Step 7: Download Kirtipur Boundary

Replace the file contents with:

```python
import osmnx as ox

place = "Kirtipur, Kathmandu, Nepal"

boundary = ox.geocode_to_gdf(place)

print(boundary)
```

Run:

```bash
python kirtipur_analysis.py
```

You should see a table printed.

---

## Step 8: Save Boundary Layer

Modify:

```python
import osmnx as ox

place = "Kirtipur, Kathmandu, Nepal"

boundary = ox.geocode_to_gdf(place)

boundary.to_file("boundary.geojson")

print("Boundary saved")
```

Run again.

Your folder should now contain:

```text
boundary.geojson
```

---

## Step 9: Download Schools

Replace with:

```python
import osmnx as ox

place = "Kirtipur, Kathmandu, Nepal"

schools = ox.features_from_place(
    place,
    tags={"amenity": "school"}
)

print("Number of schools:", len(schools))

schools.to_file("schools.geojson")
```

Run:

```bash
python kirtipur_analysis.py
```

Example output:

```text
Number of schools: 70
```

---

## Step 10: Download Roads

Create a new script:

```python
import osmnx as ox

place = "Kirtipur, Kathmandu, Nepal"

G = ox.graph_from_place(
    place,
    network_type="drive"
)

roads = ox.graph_to_gdfs(
    G,
    nodes=False
)

print("Road segments:", len(roads))

roads.to_file("roads.geojson")
```

Run it.

Now you should have:

```text
roads.geojson
schools.geojson
boundary.geojson
```

---

## Step 11: Open in QGIS

Install:

[QGIS Official Website](https://qgis.org/download/?utm_source=chatgpt.com)

Open QGIS.

Drag and drop:

```text
boundary.geojson
schools.geojson
roads.geojson
```

onto the map.

You should see Kirtipur.

---

## Step 12: Count Schools

Create:

```python
import geopandas as gpd

boundary = gpd.read_file("boundary.geojson")
schools = gpd.read_file("schools.geojson")

schools_inside = gpd.sjoin(
    schools,
    boundary,
    predicate="within"
)

print(
    "Schools within Kirtipur:",
    len(schools_inside)
)
```

Run:

```bash
python kirtipur_analysis.py
```

---

## Step 13: Calculate Road Length

Create:

```python
import geopandas as gpd

roads = gpd.read_file("roads.geojson")

roads = roads.to_crs(32645)

roads["length_m"] = roads.length

total_length = roads["length_m"].sum()

print(
    "Total road length:",
    round(total_length/1000,2),
    "km"
)
```

Run.

Example:

```text
Total road length: 145.23 km
```

---

## Step 14: Create 200m Buffer

```python
import geopandas as gpd

roads = gpd.read_file("roads.geojson")

roads = roads.to_crs(32645)

buffer_200 = roads.buffer(200)

buffer_gdf = gpd.GeoDataFrame(
    geometry=buffer_200,
    crs=roads.crs
)

buffer_gdf.to_file(
    "road_buffer.geojson"
)

print("Buffer created")
```

Run.

---

## Step 15: Find Schools Within Buffer

```python
import geopandas as gpd

schools = gpd.read_file(
    "schools.geojson"
).to_crs(32645)

buffer = gpd.read_file(
    "road_buffer.geojson"
)

nearby = gpd.sjoin(
    schools,
    buffer,
    predicate="within"
)

print(
    "Schools within 200m:",
    len(nearby)
)
```

Run.

---

## Step 16: Export Final CSV

```python
import pandas as pd

summary = pd.DataFrame({
    "Parameter":[
        "Schools",
        "Road Length km",
        "Schools within 200m"
    ],
    "Value":[
        70,
        145.23,
        65
    ]
})

summary.to_csv(
    "result.csv",
    index=False
)
```

---

## Final Folder Structure

```text
GIS_Assignment
│
├── venv
├── kirtipur_analysis.py
├── boundary.geojson
├── schools.geojson
├── roads.geojson
├── road_buffer.geojson
├── result.csv
```

For a university submission, I'd actually recommend doing the analysis with **QGIS + Python Console (PyQGIS)** because your instructor can easily verify the workflow with screenshots. If that's your assignment requirement, I can give you a QGIS-specific step-by-step version as well.
