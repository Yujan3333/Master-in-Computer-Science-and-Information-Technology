
# ✅ **A. Study Area Selection**

Choose:

* **Tribhuvan University, Kirtipur** (recommended)
  OR
* Any small area (your college, ward, etc.)

---

# ✅ **B. Data Acquisition (3 Sources REQUIRED)**

## 🔹 1. GPS / Google Earth Points

👉 Open **Google Earth**

* Mark points:

  * Gate
  * Library
  * Canteen
  * Playground
  * Department
* Save as **KML file**

---

## 🔹 2. Remote Sensing Image

Options:

* Use satellite basemap directly in QGIS
  OR
* Download from:

  * Sentinel Hub
  * Landsat
  * Google Satellite

👉 Easiest: Use **XYZ Tiles (Google Satellite in QGIS)**

---

## 🔹 3. Existing Vector Data (OSM)

👉 In QGIS:

* Go to **Plugins → Manage Plugins**
* Install: **QuickOSM**
* Search:

  * Key: `highway` (for roads)
  * Area: Kirtipur

---

# ✅ **C. Import Data into QGIS**

### Steps:

1. Open QGIS
2. Drag and drop:

   * KML file (points)
3. Add basemap:

   * Browser → XYZ Tiles → OpenStreetMap / Google
4. Add OSM data (roads)

---

# ✅ **D. Create Vector Layers**

## 🔹 1. Point Layer

* Layer → Create Layer → New Shapefile Layer
* Geometry: **Point**
* Add fields:

  * Name
  * Type
  * Description
  * Latitude
  * Longitude

👉 Add points manually using **Toggle Editing**

---

## 🔹 2. Line Layer (Road Network)

* Geometry: **Line**
* Draw roads in your area

---

## 🔹 3. Polygon Layer (Boundary / Land Use)

* Geometry: **Polygon**
* Draw:

  * University boundary
    OR
  * Land use areas

---

# ✅ **E. Attribute Table (VERY IMPORTANT)**

Each layer must have **at least 5 fields**

### Example (Point Layer):

| Name    | Type     | Category  | Description  | ID |
| ------- | -------- | --------- | ------------ | -- |
| Library | Building | Education | Main library | 1  |

👉 Open attribute table → Add values

---

# ✅ **F. Styling (Make Map Attractive)**

* Points → Different icons
* Roads → Colored lines
* Polygon → Transparent fill

---

# ✅ **G. Create Map Layout (FINAL OUTPUT)**

👉 Go to:

* **Project → New Print Layout**

Add:

* Map
* Title → *“GIS Map of Tribhuvan University”*
* Legend
* Scale bar
* North arrow

---

# ✅ **H. Export**

* Export as **PDF or Image**
* Take screenshots of:

  * Layers panel
  * Attribute table
  * Map layout

---

# 📄 **What to Submit in PDF**

### Include:

1. Title page
2. Short description (5–6 lines)
3. Screenshots:

   * Data sources
   * Layers
   * Attribute table
   * Final map
4. Final map layout

---

# ⚠️ **Common Mistakes (Avoid These)**

❌ Less than 3 data sources
❌ No attribute fields
❌ Missing legend/scale/north arrow
❌ No map title
❌ No screenshots

---

# 🎯 **Simple Workflow (Write in Assignment)**

```
Data Collection → Data Import → Layer Creation → Attribute Table → Analysis → Map Layout → Output
```

---

# ✅ **Conclusion (Write this)**

QGIS helps in integrating spatial data from different sources, creating layers, performing analysis, and producing maps for visualization.

---
