#RGIS #assignment 
# Difference Between Photogrammetry and LiDAR Technology

| Basis                  | Photogrammetry                                                                       | LiDAR                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| Definition             | Technique of obtaining measurements and spatial information from photographs/images. | Active remote sensing technology that measures distance using laser pulses. |
| Principle              | Uses overlapping aerial or satellite images and stereoscopic vision.                 | Uses laser ranging and time-of-flight principle.                            |
| Sensor Type            | Passive sensor (depends on sunlight or reflected light).                             | Active sensor (emits its own laser energy).                                 |
| Data Source            | Digital cameras, aerial photos, UAV images, satellite images.                        | Laser scanners mounted on aircraft, drones, or ground platforms.            |
| Output                 | Orthophotos, 3D models, contour maps, DEMs.                                          | Dense 3D point clouds, DEMs, DTMs, canopy height models.                    |
| Accuracy               | Good horizontal accuracy; elevation accuracy depends on image quality and overlap.   | Very high vertical accuracy and precise elevation measurement.              |
| Vegetation Penetration | Cannot penetrate dense vegetation effectively.                                       | Laser pulses can partially penetrate vegetation and reach the ground.       |
| Weather Dependence     | Requires good lighting and clear weather.                                            | Can operate day and night; some limitations in heavy rain/fog.              |
| Data Processing        | Image matching and stereoscopic interpretation required.                             | Point cloud classification and filtering required.                          |
| Cost                   | Generally lower cost.                                                                | Higher equipment and operational cost.                                      |
| Applications           | Mapping, urban planning, topographic mapping, archaeology.                           | Forest analysis, flood modeling, terrain mapping, corridor mapping.         |

---
# Generation of DEM/DTM in Photogrammetric Process

## 1. Image Acquisition

Aerial photographs or UAV images are captured with sufficient overlap to obtain stereoscopic coverage of the terrain.

Typical overlap:

* **Forward overlap:** about **60%**
* **Side overlap:** about **20–30%**

The overlap ensures that the same ground features appear in two adjacent images.

---

## 2. Interior Orientation

The internal geometry of the camera is established using:

* Focal length
* Principal point
* Lens distortion parameters

This recreates the camera geometry during image acquisition.

---

## 3. Exterior Orientation

The position and orientation of the camera at the time of image capture are determined using:

* Ground Control Points (GCPs)
* GPS/INS data

The six exterior orientation parameters are:

* Position: $X,;Y,;Z$
* Rotation: Omega $(\omega)$, Phi $(\phi)$, and Kappa $(\kappa)$

---

## 4. Aerial Triangulation (Block Adjustment)

Tie points between overlapping photographs are identified and adjusted mathematically.

Using **block adjustment**, all images are connected into a single coordinate system and accurate sensor model information is obtained for 3D reconstruction.

---

## 5. Stereo Image Formation

Two overlapping photographs form a **stereo pair**.

Using stereoscopic viewing, the terrain appears three-dimensional because of **[parallax](parallax.md)** (difference in the image position of the same object in two photographs).

The amount of [parallax](parallax.md) is directly related to the elevation of ground features.

---

## 6. Automatic Elevation Extraction (Image Matching)

Common ground points appearing in the overlap area are automatically identified using **Digital Image Matching (Auto-correlation)**.

Using the sensor model information obtained from **block adjustment**, the matched image points are transformed into **3D ground coordinates $(X,Y,Z)$**.

The software calculates the **parallax** of each matching point to determine its elevation.

Elevation points may also be collected manually using stereoplotters, but modern photogrammetric systems mainly use **automatic or semi-automatic image matching**.

---

## 7. DEM Generation

The extracted **3D elevation points** are interpolated to create a continuous elevation surface.

Common interpolation methods include:

* TIN (Triangulated Irregular Network)
* Grid Interpolation
* Kriging

The resulting **DEM** represents the Earth's surface and, according to this textbook, **may include vegetation, buildings, and other surface objects if they have not been removed**.

---

## 8. DTM Generation

The **DTM** is generated by processing the DEM.

During this process:

* Buildings are removed.
* Trees and vegetation are removed.
* Other surface objects are removed.

Only the **bare-earth elevation points** are retained to produce the final terrain model.

Thus:

* **DEM** → Terrain + surface objects (if not removed)
* **DTM** → Bare-earth terrain only

---

## Flow Diagram

```text
Image Acquisition
        ↓
Interior Orientation
        ↓
Exterior Orientation
        ↓
Aerial Triangulation (Block Adjustment)
        ↓
Stereo Image Formation
        ↓
Digital Image Matching (Auto-correlation)
        ↓
Parallax Calculation
        ↓
3D Point Extraction (X, Y, Z)
        ↓
Interpolation (TIN / Grid / Kriging)
        ↓
DEM
        ↓
Remove Buildings, Trees & Other Objects
        ↓
DTM
```


---
---

# Applications of DEM/DTM

* Contour generation
* Watershed and drainage analysis
* Flood hazard mapping
* Urban planning
* Road and railway design
* 3D terrain visualization
* Orthorectification of satellite images


