#rgis #third-semester 

---

# 1. Image Acquisition

**Illustration**

```text
Satellite/Sensor
       ↓
 Raw Digital Image
```

---

# 2. Image Preprocessing

(Removes errors)

**Illustration**

```text
Raw Image
    ↓
Geometric Correction
Radiometric Correction
Atmospheric Correction
    ↓
Corrected Image
```

Or

```text
Distorted Image
      ↓
Correction
      ↓
Correct Image
```

---

# 3. Image Enhancement

(Improves image appearance)

**Illustration**

```text
Low Contrast
      ↓
Histogram Equalization
      ↓
High Contrast
```

or

```text
Dark Image
      ↓
Contrast Stretching
      ↓
Bright Image
```

---

# 4. Image Transformation

(Convert image into another form)

Examples:

* PCA
* NDVI
* Band Ratio

**Illustration**

```text
Band 1 + Band 2 + Band 3
          ↓
 Image Transformation
          ↓
 New Image
```

---

# 5. Image Classification

Assign pixels to land-cover classes.

**Illustration**

```text
Satellite Image
       ↓
Classification
       ↓

Forest
Water
Urban
Agriculture
```

---

# 6. Image Interpretation

Extract useful information.

**Illustration**

```text
Classified Image
        ↓
Feature Extraction
        ↓
Roads
Buildings
Rivers
Forest
```

---

# 7. Output Generation

Produce maps and reports.

**Illustration**

```text
Processed Image
        ↓
Maps
Reports
GIS Database
```

---

# Complete Flow Diagram (Best Illustration)

For a **10-mark answer**, this single diagram is often enough:

```text
Image Acquisition
        ↓
Preprocessing
        ↓
Image Enhancement
        ↓
Image Transformation
        ↓
Image Classification
        ↓
Interpretation & Analysis
        ↓
Output (Maps / Reports / GIS)
```

---


