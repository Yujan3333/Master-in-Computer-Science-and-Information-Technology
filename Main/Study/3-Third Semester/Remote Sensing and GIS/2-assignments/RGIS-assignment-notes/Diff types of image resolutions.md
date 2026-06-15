#RGIS #assignment 

# **3. Describe the Different Types of Image Resolutions. Why is a Local Raster Operation Also Called a Cell-by-Cell Operation? Explain with Examples.**

## **A. Types of Image Resolution**

According to the concepts discussed in **Bhatta's GIS and Remote Sensing**, image resolution refers to the ability of a remote sensing system to distinguish information in space, wavelength, brightness, and time. The four main types are:

---

## **1. Spatial Resolution**

Spatial resolution refers to the **size of the ground area represented by a single pixel** in an image.

### Characteristics

* Determines the level of detail visible in an image.
* Smaller pixel size = higher spatial resolution.
* Larger pixel size = lower spatial resolution.

### Examples

* 1 m resolution: buildings, roads, and small features can be identified.
* 30 m resolution (e.g., Landsat): suitable for land-use and land-cover mapping.
* 250 m resolution (e.g., MODIS): suitable for regional studies.

### Illustration

```
1 m Resolution      30 m Resolution

[][][][][][][]      [][][][]
[][][][][][][]      [][][][]
[][][][][][][]      [][][][]
(More Detail)       (Less Detail)
```

---

## **2. Spectral Resolution**

Spectral resolution refers to the **ability of a sensor to distinguish fine wavelength intervals** of the electromagnetic spectrum.

### Characteristics

* Depends on the number and width of spectral bands.
* More and narrower bands provide higher spectral resolution.

### Examples

* Panchromatic image: 1 broad band.
* Multispectral image: several bands (Blue, Green, Red, NIR).
* Hyperspectral image: hundreds of narrow bands.

### Applications

* Vegetation analysis
* Mineral identification
* Water quality assessment

---

## **3. Radiometric Resolution**

Radiometric resolution refers to the **sensor's ability to detect small differences in energy intensity**.

### Characteristics

Measured in bits.

| Resolution | Number of Gray Levels |
| ---------- | --------------------- |
| 8-bit      | 256                   |
| 10-bit     | 1024                  |
| 11-bit     | 2048                  |
| 16-bit     | 65536                 |

Higher radiometric resolution allows detection of subtle brightness differences.

### Example

A 16-bit image can distinguish far more brightness levels than an 8-bit image.

---

## **4. Temporal Resolution**

Temporal resolution refers to the **frequency with which a sensor revisits the same area**.

### Examples

| Satellite   | Revisit Time |
| ----------- | ------------ |
| Landsat-8/9 | 16 days      |
| Sentinel-2  | 5 days       |
| MODIS       | 1–2 days     |

### Applications

* Crop monitoring
* Flood mapping
* Deforestation detection
* Disaster management

---

# **B. Why is a Local Raster Operation Called a Cell-by-Cell Operation?**

## **Definition**

A **local raster operation** computes the value of each output cell using **only the corresponding input cell value(s)** at the same location.

Since each raster cell is processed independently without considering neighboring cells, it is called a **cell-by-cell operation**.

---

## **Why "Cell-by-Cell"?**

For every raster cell:

```
Output Cell Value
        ↓
Depends only on
        ↓
Input Cell Value
```

No surrounding cells are involved in the calculation.

---

## **Example 1: Multiplication by a Constant**

Input Raster:

| 2 | 3 | 4  |
| - | - | -- |
| 5 | 6 | 7  |
| 8 | 9 | 10 |

Operation:

$$Output = Input \times 2$$

Output Raster:

| 4  | 6  | 8  |
| -- | -- | -- |
| 10 | 12 | 14 |
| 16 | 18 | 20 |

Each cell is processed independently.

---

## **Example 2: Reclassification**

Input Land Use Raster:

| Value | Class       |
| ----- | ----------- |
| 1     | Forest      |
| 2     | Agriculture |
| 3     | Water       |

Reclassification Rule:

* Forest → 10
* Agriculture → 20
* Water → 30

Input Raster:

| 1 | 2 | 3 |
| - | - | - |
| 2 | 1 | 3 |
| 1 | 2 | 2 |

Output Raster:

| 10 | 20 | 30 |
| -- | -- | -- |
| 20 | 10 | 30 |
| 10 | 20 | 20 |

Each cell is converted individually.

---

## **Example 3: Threshold Operation**

Rule:

$$\text{If Value} > 50 \rightarrow 1$$

$$\text{Else} \rightarrow 0$$

Input Raster:

| 40 | 60 | 30 |
| -- | -- | -- |
| 55 | 80 | 20 |

Output Raster:

| 0 | 1 | 0 |
| - | - | - |
| 1 | 1 | 0 |

Again, each cell is evaluated separately.

---

# **Conclusion**

The four major image resolutions are:

1. **Spatial Resolution** – pixel size on the ground.
2. **Spectral Resolution** – ability to distinguish wavelength bands.
3. **Radiometric Resolution** – ability to detect brightness differences.
4. **Temporal Resolution** – frequency of data acquisition.

A **local raster operation** is called a **cell-by-cell operation** because the output value of each cell is calculated using only the value of the corresponding input cell, without considering neighboring cells. Common examples include arithmetic operations, reclassification, and thresholding.
