#rgis #third-semester #old-que #exam-paper-answer 

# Question 1

## (a) Explain why filtering is applied in pre-processing even before enhancement or transformation.

### Filtering in Pre-processing

**Filtering** is the process of removing unwanted noise and improving image quality before further processing. It is performed during **pre-processing** because enhancement and transformation techniques work best on clean, accurate data.

### Why filtering is applied before enhancement or transformation

1. **Removes noise**

   * Eliminates random noise caused by sensors or transmission errors.

2. **Improves image quality**

   * Produces smoother and clearer images.

3. **Increases classification accuracy**

   * Clean images lead to better object identification and land-cover classification.

4. **Prevents error amplification**

   * If enhancement is applied to a noisy image, the noise is also enhanced.

5. **Improves feature extraction**

   * Roads, rivers, buildings, and vegetation become easier to identify.

6. **Provides reliable analysis**

   * Image transformations such as NDVI or PCA produce more accurate results.

### Example

A satellite image contains "salt-and-pepper" noise. If contrast stretching is applied directly, the noise also becomes more visible. Applying a **median filter** first removes the noise, producing a cleaner image for enhancement.

### Conclusion

Filtering is performed before enhancement or transformation to remove noise, improve image quality, and ensure accurate analysis and classification.

---

## (b) Differentiate between supervised and unsupervised classification techniques with suitable examples.

| Supervised Classification                                 | Unsupervised Classification                   |
| --------------------------------------------------------- | --------------------------------------------- |
| Uses training samples provided by the user.               | No training samples are required.             |
| User defines land-cover classes.                          | Computer automatically groups similar pixels. |
| More accurate.                                            | Less accurate.                                |
| Requires expert knowledge.                                | Minimal human involvement.                    |
| More time-consuming.                                      | Faster.                                       |
| Example algorithms: Maximum Likelihood, Minimum Distance. | Example algorithms: K-Means, ISODATA.         |

### Examples

**Supervised Classification:**

* A user selects training areas for **forest, water, and urban** land. The software classifies the remaining pixels based on these samples.

**Unsupervised Classification:**

* The software automatically groups pixels into clusters. The user later labels the clusters as **forest, water, agriculture**, etc.

### Conclusion

Supervised classification provides higher accuracy but requires training data, whereas unsupervised classification is automatic and suitable when prior knowledge is unavailable.

---

# Question 2

## (a) Describe the key components of a Geographic Information System (GIS).

A **Geographic Information System (GIS)** is a computer-based system used to collect, store, manage, analyze, and display geographic data.

### Five Key Components

### 1. Hardware

Physical devices used for GIS.

Examples:

* Computers
* GPS/GNSS receivers
* Printers
* Servers

---

### 2. Software

Programs used to process and analyze spatial data.

Examples:

* QGIS
* ArcGIS
* GRASS GIS

---

### 3. Data

The most important component.

* **Spatial data:** Location of objects (roads, rivers, buildings).
* **Attribute data:** Descriptive information (name, population, area).

---

### 4. People

Users who operate GIS.

Examples:

* Surveyors
* Engineers
* Researchers
* Government agencies

---

### 5. Methods

Procedures and standards used for collecting, analyzing, and presenting data.

---

## (b) Explain how GIS integrates spatial and attribute information.

GIS combines:

* **Spatial information (Where?)** → Location, coordinates, shape.
* **Attribute information (What?)** → Name, population, land use, area.

### Example

A school on a GIS map contains:

**Spatial data**

* Latitude
* Longitude

**Attribute data**

* School name
* Number of students
* Principal
* Year established

By linking these two types of information, GIS enables efficient mapping, querying, and spatial analysis.

---

## (c) Explain how GNSS improves the accuracy of Remote Sensing and GIS applications.

**GNSS (Global Navigation Satellite System)** provides accurate position, navigation, and timing information.

### Role of GNSS

1. Provides accurate geographic coordinates.
2. Helps collect reliable **ground truth data**.
3. Improves geometric correction of satellite images.
4. Supports accurate map creation.
5. Enables precise field surveys.
6. Integrates field observations with GIS databases.
7. Improves image classification and validation.

### Applications

* Agriculture
* Disaster management
* Urban planning
* Land surveying
* Environmental monitoring

### Conclusion

GNSS improves the positional accuracy of remote sensing data and GIS analyses, making mapping and decision-making more reliable.

---

# Question 3

## (a) What is meant by Ground Truthing and why is it necessary in Remote Sensing?

### Definition

**Ground truthing** is the process of collecting actual information directly from the Earth's surface to verify and validate remote sensing data.

### Why it is necessary

1. Verifies satellite image interpretation.
2. Improves classification accuracy.
3. Reduces mapping errors.
4. Provides training data for supervised classification.
5. Validates remote sensing results.
6. Supports scientific research and decision-making.

### Example

A satellite image classifies an area as forest. Field visits confirm the tree species and vegetation density, validating the classification.

---

## (b) Explain the photogrammetric process in detail.

Photogrammetry is the science of obtaining accurate measurements and maps from photographs.

### Stages of the Photogrammetric Process

### 1. Image Acquisition

* Images are captured using aircraft, drones, or satellites.
* Overlapping photographs are collected.

↓

### 2. Image Orientation

* Determines the position and direction of the camera.
* Includes:

  * Interior orientation
  * Exterior orientation
  * Relative orientation
  * Absolute orientation

↓

### 3. Triangulation

* Calculates the coordinates of unknown points using overlapping images and ground control points.

↓

### 4. Stereo Model Compilation

* Two overlapping photographs are combined to produce a 3D stereo model.

↓

### 5. Stereoscopic Viewing

* The stereo model is viewed with a stereoscope or digital software to perceive depth.

↓

### 6. Stereoscopic Measurement

* Heights, distances, areas, and volumes are measured from the stereo model.

↓

### 7. DTM/DEM Generation

* A **Digital Elevation Model (DEM)** or **Digital Terrain Model (DTM)** is created to represent terrain elevation.

↓

### 8. Orthorectification

* Removes geometric distortions caused by terrain, camera tilt, and sensor geometry.
* Produces an accurate **orthophoto**.

↓

### 9. Feature Extraction

* Roads, buildings, rivers, forests, and other features are extracted.

↓

### 10. Final Map Generation

* Topographic maps, contour maps, thematic maps, and 3D models are produced for GIS and planning.

### Flow Diagram

```text
Image Acquisition
        ↓
Image Orientation
        ↓
Triangulation
        ↓
Stereo Model
        ↓
Stereoscopic Viewing
        ↓
Measurements
        ↓
DEM / DTM Generation
        ↓
Orthorectification
        ↓
Feature Extraction
        ↓
Final Map Generation
```

### Applications of Photogrammetry

* Topographic mapping
* Urban planning
* Engineering
* Forestry
* Agriculture
* Disaster management

### Conclusion

Photogrammetry converts overlapping aerial or satellite images into accurate maps and 3D models, making it an essential technique for surveying, GIS, and remote sensing.
