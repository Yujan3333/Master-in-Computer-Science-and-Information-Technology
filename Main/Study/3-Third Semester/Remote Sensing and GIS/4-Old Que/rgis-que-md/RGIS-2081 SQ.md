#rgis #third-semester #old-que #exam-paper-answer 
# Group B: Short Answer Questions (Attempt ALL)

---

# 1. Differentiate between Raster and Vector Data Models.

| Raster Data Model                           | Vector Data Model                                   |
| ------------------------------------------- | --------------------------------------------------- |
| Represents data as **pixels (grid cells)**. | Represents data as **points, lines, and polygons**. |
| Best for **continuous** data.               | Best for **discrete** objects.                      |
| Used for satellite images and DEMs.         | Used for roads, rivers, buildings, and boundaries.  |
| Larger file size.                           | Smaller file size for discrete features.            |
| Lower positional accuracy.                  | Higher positional accuracy.                         |
| Difficult to edit individual features.      | Easy to edit and update features.                   |

### Examples

* **Raster:** Satellite image, DEM, temperature map.
* **Vector:** Road network, district boundary, river.

---

# 2. How is Photogrammetry different from LiDAR Technology? Explain how DEM/DTM can be generated in the photogrammetric process.

## Photogrammetry vs LiDAR

| Photogrammetry                                 | LiDAR                                                  |
| ---------------------------------------------- | ------------------------------------------------------ |
| Uses overlapping photographs.                  | Uses laser pulses.                                     |
| Passive sensing (depends on sunlight).         | Active sensing (emits its own laser).                  |
| Lower cost.                                    | Higher cost.                                           |
| Accuracy depends on image quality and overlap. | Very high elevation accuracy.                          |
| Difficult in dense vegetation.                 | Can penetrate vegetation to estimate ground elevation. |

---

## DEM/DTM Generation in Photogrammetry

The DEM/DTM generation process involves:

1. Capture overlapping aerial photographs.
2. Perform image orientation and triangulation.
3. Create a stereo model from overlapping images.
4. Measure elevation using stereoscopic viewing.
5. Generate elevation points.
6. Interpolate the elevation points to produce:

   * **DEM (Digital Elevation Model):** Represents the Earth's surface, including natural features and sometimes objects.
   * **DTM (Digital Terrain Model):** Represents the bare ground after removing vegetation and buildings.

### Flow Diagram

```text
Image Acquisition
        ↓
Image Orientation
        ↓
Stereo Model
        ↓
Elevation Measurement
        ↓
DEM / DTM Generation
```

---

# 3. How is a Hyperspectral Image different from a Multispectral Image? Explain with illustrations.

| Hyperspectral Image                                                     | Multispectral Image                                       |
| ----------------------------------------------------------------------- | --------------------------------------------------------- |
| Contains **hundreds of narrow spectral bands**.                         | Contains **a few broad spectral bands** (typically 3–10). |
| Provides detailed spectral information.                                 | Provides limited spectral information.                    |
| Higher spectral resolution.                                             | Lower spectral resolution.                                |
| Large data volume.                                                      | Smaller data volume.                                      |
| Used for mineral identification, crop analysis, and material detection. | Used for land-cover mapping and vegetation monitoring.    |

### Illustration

```text
Multispectral

Blue   Green   Red   NIR
 |       |      |     |

(4 broad bands)
```

```text
Hyperspectral

| | | | | | | | | | | | | | | | |

(Hundreds of narrow bands)
```

### Conclusion

* **Multispectral:** Few, broad bands.
* **Hyperspectral:** Many, narrow bands with much richer spectral detail.

---

# 4. Describe the Electromagnetic Spectrum in Remote Sensing. What are the ideal time and atmosphere for aerial Remote Sensing?

## Electromagnetic Spectrum

The **electromagnetic (EM) spectrum** is the complete range of electromagnetic radiation used in remote sensing.

It includes:

* Gamma rays
* X-rays
* Ultraviolet (UV)
* Visible light
* Infrared (IR)
* Microwave
* Radio waves

Remote sensing mainly uses:

* **Visible light (0.4–0.7 µm)** for natural color images.
* **Infrared (0.7–14 µm)** for vegetation and thermal studies.
* **Microwaves (1 mm–1 m)** for RADAR and all-weather imaging.

---

## Ideal Time for Aerial Remote Sensing

* Early morning (after sunrise) is preferred because:

  * Clear atmosphere
  * Less haze and dust
  * Stable lighting
  * Lower air turbulence
  * Better image quality

---

## Ideal Atmospheric Conditions

* Clear sky
* Cloud-free weather
* Low humidity
* Minimal smoke or dust
* Good visibility
* No rain or fog

---

# 5. Why is geometric correction useful prior to further analysis and interpretation?

**Geometric correction** is the process of removing geometric distortions from an image so that it accurately matches real-world coordinates.

## Importance

1. Corrects distortions caused by:

   * Sensor movement
   * Earth's curvature
   * Terrain relief
   * Platform tilt

2. Aligns the image with maps and GIS layers.

3. Improves measurement accuracy.

4. Enables accurate overlay with other datasets.

5. Improves classification and interpretation.

6. Essential before change detection and spatial analysis.

---

# 6. Numerical: Calculate the Scale of an Aerial Photograph

### Given

Flying height above mean sea level:

$$
H = 3000\ \text{m}
$$

Ground elevation:

$$
h = 450\ \text{m}
$$

Camera focal length:

$$
f = 150\ \text{mm}=0.15\ \text{m}
$$

### Formula

The scale of a vertical aerial photograph is:

$$
\text{Scale}=\frac{f}{H-h}
$$

Substitute the values:

$$
\text{Scale}=\frac{0.15}{3000-450}
=\frac{0.15}{2550}
=\frac{1}{17000}
$$

### Final Answer

$$
\boxed{\text{Scale}=1:17,000}
$$

**Interpretation:** **1 cm** on the photograph represents **17,000 cm (170 m)** on the ground.

---

## Exam Tips

**Frequently asked topics:**

* Raster vs Vector data models.
* Photogrammetry vs LiDAR.
* DEM vs DTM.
* Hyperspectral vs Multispectral imaging.
* Electromagnetic spectrum and ideal aerial photography conditions.
* Geometric correction.
* Numerical problems on aerial photograph scale using:

$$
\boxed{\text{Scale}=\frac{f}{H-h}}
$$
