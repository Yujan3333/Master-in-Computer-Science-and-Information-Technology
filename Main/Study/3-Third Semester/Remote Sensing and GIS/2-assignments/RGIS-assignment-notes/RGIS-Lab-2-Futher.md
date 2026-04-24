Since you are looking for a **Shapefile (.shp)** format for QGIS, you might have noticed that Overpass Turbo doesn't list ".shp" directly in the main export menu. Most GIS professionals export as **GeoJSON** first and then convert it, but here is the most efficient way to get your data into QGIS for your assignment.

### 1. How to get the data into QGIS (The .shp route)
If you specifically want a Shapefile from Overpass Turbo:
* **Method A (Direct):** In the Overpass Export menu, look for **Download/copy as GeoJSON**. 
* **Method B (The Conversion):** Once you have the GeoJSON, drag it into QGIS. Right-click the layer in QGIS > **Export** > **Save Features As...** > Change Format to **ESRI Shapefile**.

---

### 2. Performing the Analysis (Step-by-Step)

#### Task i: 2 km Radius of TU Chemistry Dept
1.  **Locate TU:** Use the `Search` bar in QGIS or a Base Map (Google Satellite) to find the Chemistry Dept.
2.  **Create Point:** `Layer` > `Create Layer` > `New Shapefile Layer` (Point). Click once on the Chemistry Dept.
3.  **Buffer:** Go to `Vector` > `Geoprocessing Tools` > `Buffer`.
    * **Distance:** `2 kilometers`.
4.  **Select Schools:** Use `Vector` > `Research Tools` > `Select by Location`. Select schools that are **within** the 2km buffer.

#### Task ii: Kathmandu Metropolitan City (KMC) Layer
1.  **Load Boundary:** Open your Municipal Map layer.
2.  **Filter KMC:** Right-click the layer > `Filter`. Type: `"NAME" = 'Kathmandu'` (or whatever the attribute name is).
3.  **Clip Schools:** Go to `Vector` > `Geoprocessing Tools` > `Intersection`.
    * **Input:** Your Merged Schools layer.
    * **Overlay:** The filtered KMC layer.
    * **Output:** This creates your **new map layer and database table** automatically.

#### Task iii: 1 km Ring Road Buffer
1.  **Filter Ring Road:** From your road network layer, select the Ring Road.
2.  **Buffer:** Run the **Buffer** tool at `1 kilometer`.
3.  **Extract:** Use `Vector` > `Geoprocessing Tools` > `Intersection` (using the Schools as Input and the Road Buffer as Overlay).
4.  **Count:** Right-click the resulting layer > **Open Attribute Table**. The number of rows is the "number of schools" you need to determine.

---

### Critical Technical Tip: The "Degree" Trap
When you run the **Buffer** tool, if the "Distance" unit is in **degrees** instead of **meters/kilometers**, your analysis will fail. 

* **Solution:** Before buffering, right-click your School layer > **Export** > **Save Features As**.
* **Change CRS:** Select **EPSG:32645 - WGS 84 / UTM zone 45N**. 
* This projection is specifically for Nepal and allows you to use meters/kilometers accurately.



---

### Summary of Workflow for your Report
1.  **Source:** Overpass Turbo (`amenity=school`).
2.  **Processing:** Geometry Centroids -> Merge -> Reproject to UTM Zone 45N.
3.  **Analysis:** Buffer (for TU and Ring Road) and Intersection (for KMC).
4.  **Export:** Save results as `.shp` for the final map layers.
