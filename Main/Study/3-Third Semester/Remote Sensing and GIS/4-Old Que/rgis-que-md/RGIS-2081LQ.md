#rgis #third-semester #old-que #exam-paper-answer 

# Group A: Long Answer Questions (Attempt any TWO)

---

# Question 1

## (a) Discuss the elements of visual image interpretation.

Visual image interpretation is the process of identifying and analyzing objects on aerial photographs or satellite images using human observation.

### Elements of Visual Image Interpretation

### 1. Tone (Brightness)

* Relative lightness or darkness of an object.
* Example:

  * Water → Dark
  * Concrete → Bright

---

### 2. Color

* Different objects appear in different colors.
* Example:

  * Vegetation → Green
  * Water → Blue

---

### 3. Texture

* Frequency of tonal variation (smooth or rough appearance).
* Example:

  * Water → Smooth
  * Forest → Rough

---

### 4. Pattern

* Spatial arrangement of objects.
* Example:

  * Agricultural fields → Regular pattern
  * Forest → Irregular pattern

---

### 5. Shape

* Characteristic outline of an object.
* Example:

  * Airport → Long runway
  * Stadium → Circular

---

### 6. Size

* Physical dimensions of an object.
* Example:

  * Highway → Wide
  * Road → Narrow

---

### 7. Shadow

* Helps determine height and shape.
* Example:

  * Tall buildings cast long shadows.

---

### 8. Site (Location)

* Geographic position of an object.
* Example:

  * Bridge → Over a river
  * Harbor → Along a coast

---

### 9. Association

* Relationship between nearby objects.
* Example:

  * Railway station → Railway tracks
  * School → Playground

---

## (b) How is Digital Image Interpretation different from Visual Image Interpretation?

| Visual Image Interpretation                  | Digital Image Interpretation                     |
| -------------------------------------------- | ------------------------------------------------ |
| Done by human experts.                       | Done by computers using algorithms.              |
| Based on tone, color, texture, pattern, etc. | Based on pixel values and mathematical analysis. |
| Subjective.                                  | Objective.                                       |
| Slower.                                      | Faster.                                          |
| Best for small or complex areas.             | Suitable for large datasets.                     |
| Depends on interpreter experience.           | Depends on software and algorithms.              |

---

## (c) Explain common image processing functions with illustrations.

Image processing functions improve image quality and extract useful information.

### 1. Pre-processing

* Removes noise and corrects distortions.
* Examples:

  * Radiometric correction
  * Geometric correction
  * Atmospheric correction

```
Raw Image
    ↓
Pre-processing
    ↓
Corrected Image
```

---

### 2. Image Enhancement

* Improves image appearance.
* Techniques:

  * Contrast stretching
  * Histogram equalization
  * Filtering
  * Edge enhancement

```
Low Contrast
      ↓
Contrast Stretching
      ↓
High Contrast
```

---

### 3. Image Transformation

* Converts image data into a more useful form.
* Examples:

  * NDVI
  * PCA
  * Band Ratio

---

### 4. Image Classification

* Groups pixels into land-cover classes.
* Types:

  * Supervised
  * Unsupervised

```
Satellite Image
        ↓
Classification
        ↓
Forest | Water | Urban | Agriculture
```

---

# Question 2

## (a) Outline the steps of how RADAR works.

**RADAR (Radio Detection and Ranging)** is an active microwave remote sensing system that transmits microwave signals and records the reflected energy.

### Working Steps

1. Radar transmitter generates microwave pulses.
2. Antenna transmits the pulses toward the Earth's surface.
3. Pulses strike objects on the ground.
4. Objects reflect part of the energy (backscatter).
5. Antenna receives the reflected signals.
6. Receiver converts the signals into electrical form.
7. Signal processor processes the data.
8. A radar image is produced.

### Diagram

```text
Radar Transmitter
        │
Microwave Pulse
        ▼
Earth Surface
        │
Backscattered Signal
        ▼
Receiver
        │
Signal Processing
        ▼
Radar Image
```

---

## (b) How are Airborne Radars different from Space-borne Radars?

| Airborne Radar                | Space-borne Radar                       |
| ----------------------------- | --------------------------------------- |
| Mounted on aircraft or drones | Mounted on satellites                   |
| Low altitude                  | High altitude                           |
| Small area coverage           | Large area coverage                     |
| Very high spatial resolution  | Moderate to high resolution             |
| Flexible operation            | Fixed orbital path                      |
| Suitable for local surveys    | Suitable for regional/global monitoring |

### Examples

* **Airborne Radar:** Radar mounted on an aircraft for flood mapping.
* **Space-borne Radar:** Sentinel-1 SAR satellite for global monitoring.

---

# Question 3

## (a) Explain GIS and its functions.

### Definition

**Geographic Information System (GIS)** is a computer-based system used to collect, store, manage, analyze, and display geographically referenced information.

---

### Functions of GIS

1. Data Capture
2. Data Storage
3. Data Editing
4. Data Management
5. Spatial Analysis
6. Data Retrieval
7. Map Production
8. Visualization
9. Decision Support

---

## (b) How can GPS and Remote Sensing data be integrated with GIS?

### Integration Process

```text
GPS
      │
Ground Coordinates
      │
      ▼
Remote Sensing Images
      │
Image Processing
      │
      ▼
GIS Database
      │
Spatial Analysis
      │
      ▼
Maps & Reports
```

### Role of GPS

* Provides accurate coordinates.
* Collects ground truth data.
* Supports field surveys.

### Role of Remote Sensing

* Provides satellite or aerial images.
* Supplies land-use and environmental information.

### Benefits

* Accurate mapping.
* Better spatial analysis.
* Improved decision-making.
* Efficient disaster management.
* Supports urban planning and agriculture.

---

## (c) Describe the different types of geospatial data models.

A **geospatial data model** is a method of representing geographic features in GIS.

### 1. Raster Data Model

Represents the Earth's surface as a grid of pixels (cells).

**Characteristics**

* Each cell stores a value.
* Suitable for continuous data.

**Examples**

* Satellite images
* DEM
* Temperature maps

```
□ □ □ □
□ □ □ □
□ □ □ □
```

**Advantages**

* Simple structure.
* Best for continuous phenomena.

**Disadvantages**

* Large file size.
* Lower positional accuracy for discrete features.

---

### 2. Vector Data Model

Represents features using geometric objects.

* **Point:** Schools, wells.
* **Line:** Roads, rivers.
* **Polygon:** Lakes, forests, districts.

```
Point     •
Line      ─────
Polygon   □
```

**Advantages**

* High positional accuracy.
* Smaller storage for discrete objects.
* Easy editing.

**Disadvantages**

* More complex data structure.

---

## Raster vs Vector

| Raster                    | Vector                                |
| ------------------------- | ------------------------------------- |
| Pixels (cells)            | Points, lines, polygons               |
| Best for continuous data  | Best for discrete features            |
| Larger file size          | Smaller file size                     |
| Used for satellite images | Used for roads, buildings, boundaries |

---

## Conclusion

GIS integrates **GPS**, **remote sensing**, and **geospatial data models (Raster and Vector)** to capture, analyze, and present spatial information effectively. It is widely used in mapping, planning, environmental monitoring, and decision-making.
