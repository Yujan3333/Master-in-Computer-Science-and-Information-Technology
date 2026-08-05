#rgis #third-semester #old-que #exam-paper-answer 

# Group B – Short Answer Questions (Attempt ALL)

---

# 1. How is Raster (Image) Data Represented in GIS? Explain the importance of scale in satellite image interpretation and discuss how changes in scale influence the identification and classification of geographic features.

## Raster Data Representation in GIS

Raster data represents geographic information as a **grid of equally sized cells (pixels)**. Each pixel stores a value representing a characteristic of that location, such as color, elevation, or temperature.

### Representation

```text
+----+----+----+----+
| 12 | 15 | 18 | 20 |
+----+----+----+----+
| 10 | 14 | 17 | 21 |
+----+----+----+----+
|  8 | 11 | 16 | 19 |
+----+----+----+----+
```

Each cell contains a numeric value.

### Uses

* Satellite imagery
* DEM (Digital Elevation Model)
* Land cover maps
* Temperature maps

---

## Importance of Scale

**Scale** is the ratio between a distance on the image/map and the corresponding distance on the ground.

### Importance

* Determines the level of detail visible.
* Affects measurement accuracy.
* Helps identify geographic features correctly.
* Influences map interpretation and classification.

---

## Effect of Scale

### Large Scale (e.g., 1:10,000)

* Shows **more detail**.
* Small objects (buildings, roads) are visible.
* Better for urban mapping.

### Small Scale (e.g., 1:1,000,000)

* Covers a **larger area**.
* Shows **less detail**.
* Suitable for regional or national mapping.

---

# 2. Describe the Concept and Importance of Thermal Remote Sensing.

## Concept

**Thermal remote sensing** detects and measures the **thermal infrared radiation emitted** by objects to estimate their surface temperature.

Unlike visible remote sensing, thermal sensing records **emitted energy**, not reflected sunlight.

---

## Working Principle

1. Objects absorb solar energy.
2. They emit thermal infrared radiation.
3. Thermal sensors detect this radiation.
4. The signals are processed to produce thermal images.

---

## Importance

* Detects forest fires.
* Monitors volcanic activity.
* Studies urban heat islands.
* Measures water temperature.
* Supports drought monitoring.
* Detects industrial heat pollution.

---

# 3. Describe Relief Displacement with Illustrations. Numerical

## Relief Displacement

**Relief displacement** is the apparent outward displacement of tall objects from the center of a vertical aerial photograph due to their height.

Objects appear to lean **away from the principal point**.

### Illustration

```text
        Photo Center
             ●
             │
             │
        Tower Base
             │
             ▲
             │
         Tower Top
```

The top of the tower appears farther from the photo center than the base.

---

## Formula

$$
d=\frac{r\times h}{H}
$$

Where:

* $d$ = Relief displacement
* $r$ = Radial distance
* $h$ = Height of object
* $H$ = Flying height above the base

Rearranging,

$$
h=\frac{dH}{r}
$$

---

### Given

Relief displacement:

$$
d=2.5\ \text{mm}
$$

Radial distance:

$$
r=60\ \text{mm}
$$

Flying height:

$$
H=1240\ \text{m}
$$

---

### Calculation

$$
h=\frac{2.5\times1240}{60}
$$

$$
h=\frac{3100}{60}
$$

$$
h=51.67\ \text{m}
$$

### Final Answer

$$
\boxed{h\approx51.7\ \text{m}}
$$

---

# 4. Differentiate between Photogrammetry and LiDAR Technology with Examples.

| Photogrammetry                   | LiDAR                                             |
| -------------------------------- | ------------------------------------------------- |
| Uses overlapping photographs.    | Uses laser pulses.                                |
| Passive sensing.                 | Active sensing.                                   |
| Depends on sunlight.             | Independent of sunlight.                          |
| Lower cost.                      | Higher cost.                                      |
| Less effective in dense forests. | Can estimate ground elevation beneath vegetation. |
| Generates 3D models from images. | Generates accurate 3D point clouds.               |

### Examples

**Photogrammetry**

* Drone images used to prepare topographic maps.

**LiDAR**

* Airborne LiDAR used to create high-accuracy elevation models for flood analysis.

---

# 5. Differentiate between Spatial, Spectral, Temporal, and Radiometric Resolution with Suitable Examples.

| Resolution                 | Meaning                                                              | Example                                                                                                 |
| -------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Spatial Resolution**     | Size of the smallest object or ground area represented by one pixel. | 1 m imagery can show individual buildings; 30 m imagery cannot.                                         |
| **Spectral Resolution**    | Ability to distinguish different wavelength bands.                   | Hyperspectral sensors have hundreds of narrow bands; multispectral sensors have a few broad bands.      |
| **Temporal Resolution**    | Frequency with which the same area is revisited.                     | A satellite imaging the same location daily has higher temporal resolution than one revisiting monthly. |
| **Radiometric Resolution** | Ability to detect small differences in brightness (energy).          | 16-bit sensors detect finer brightness differences than 8-bit sensors.                                  |

### Summary

* **Spatial Resolution** → **How small** an object can be seen.
* **Spectral Resolution** → **How many and how narrow** the wavelength bands are.
* **Temporal Resolution** → **How often** the same area is imaged.
* **Radiometric Resolution** → **How precisely** differences in brightness are detected.

---

# Exam Tips

For **5-mark questions**, focus on these key points:

* **Raster Representation:** Grid of pixels with cell values.
* **Scale:** Large scale = more detail; Small scale = larger area, less detail.
* **Thermal Remote Sensing:** Detects emitted thermal infrared radiation; applications in fire detection, drought monitoring, and environmental studies.
* **Relief Displacement Formula:**

$$
\boxed{d=\frac{rh}{H}}
\qquad\text{or}\qquad
\boxed{h=\frac{dH}{r}}
$$

* **Photogrammetry vs LiDAR:** Images vs laser pulses; passive vs active sensing.
* **Four Resolutions:** Spatial, Spectral, Temporal, and Radiometric (know the definitions and one example for each).
