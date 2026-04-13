
- [Difference Raster and Vector Model](Difference%20Raster%20and%20Vector%20Model.md)
# ✍️ **Q4. Raster vs Vector Data Model + Raster Overlay Operations**

---

# ✅ **1. Raster and Vector Data Models**

GIS represents spatial data using two main models: **Raster** and **Vector**.

---

## 🔹 **Raster Data Model**

## 🔸 **Definition**

Raster data represents geographic data as a **grid of cells (pixels)**, where each cell has a value.

---

## 🔸 **Characteristics**

* Data stored in rows and columns
* Each pixel represents an area
* Suitable for continuous data

---

## 🔸 **Examples**

* Satellite images
* Temperature maps
* Elevation (DEM)

---

## 🔸 **Advantages**

* Simple structure
* Suitable for image processing
* Good for continuous data

---

## 🔸 **Disadvantages**

* Large storage required
* Less precise for boundaries

---

## 🔹 **Vector Data Model**

## 🔸 **Definition**

Vector data represents geographic features using **points, lines, and polygons**.

---

## 🔸 **Types**

* Point → location (e.g., well, school)
* Line → roads, rivers
* Polygon → areas (land use, district)

---

## 🔸 **Advantages**

* High accuracy
* Efficient storage
* Good for discrete features

---

## 🔸 **Disadvantages**

* Complex structure
* Not suitable for continuous data

---

## ✏️ **Diagram (Draw this)**

```id="v1"
Raster:            Vector:

[ ][ ][ ]          • Point
[ ][ ][ ]          ─── Line
[ ][ ][ ]          ⬜ Polygon
```

---

# 🔍 **Key Differences**

| Feature   | Raster            | Vector                  |
| --------- | ----------------- | ----------------------- |
| Structure | Grid cells        | Points, lines, polygons |
| Data type | Continuous        | Discrete                |
| Accuracy  | Low (pixel-based) | High                    |
| Storage   | Large             | Efficient               |

---

# ✅ **2. Raster Image Overlay Operations**

Raster overlay combines multiple raster layers to produce new output.

---

## 🔹 **1. Boolean Overlay**

### 🔸 **Definition**

Uses logical operations:

* AND
* OR
* NOT

---

### 🔸 **Example**

Suitable area = (Forest AND Near Water)

---

---

## 🔹 **2. Arithmetic Overlay**

### 🔸 **Definition**

Performs mathematical operations on raster layers:

* Addition
* Subtraction
* Multiplication

---

### 🔸 **Example**

Total rainfall = Layer1 + Layer2

---

---

## 🔹 **3. Weighted Overlay**

### 🔸 **Definition**

Each raster layer is assigned a **weight based on importance**, and a combined result is calculated.

---

### 🔸 **Example**

Site suitability:

* Slope (40%)
* Soil (30%)
* Water (30%)

---

---

## 🔹 **4. Conditional Overlay**

### 🔸 **Definition**

Uses conditions (if–else logic) to select data.

---

### 🔸 **Example**

IF slope < 15° → Suitable
ELSE → Not suitable

---

---

# 🎯 **Importance in GIS**

* Helps in **decision making**
* Used in:

  * Site selection
  * Environmental analysis
  * Resource management

---

# ✅ **Conclusion**

Raster and vector models are fundamental ways of representing spatial data in GIS. Raster overlay operations such as Boolean, arithmetic, weighted, and conditional overlays are essential tools for spatial analysis and decision-making.

---

