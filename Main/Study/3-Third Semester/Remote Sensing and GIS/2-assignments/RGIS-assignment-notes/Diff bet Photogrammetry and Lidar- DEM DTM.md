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

Aerial photographs or UAV images are captured with sufficient overlap:

* Forward overlap: about 60%
* Side overlap: about 20–30%

These overlapping images create stereoscopic coverage of the terrain.

---

## 2. Interior Orientation

The internal geometry of the camera is established using:

* Focal length
* Principal point
* Lens distortion parameters

This recreates the imaging geometry.

---

## 3. Exterior Orientation

The position and orientation of the camera during image capture are determined using:

* Ground Control Points (GCPs)
* GPS/INS data

The six orientation parameters are:

* $X,Y,Z$ position
* Omega $(\omega)$
* Phi $(\phi)$
* Kappa $(\kappa)$ rotations

---

## 4. Aerial Triangulation

Tie points between overlapping photographs are identified and adjusted mathematically to improve positional accuracy.

This step connects all images into a single coordinate system.

---

## 5. Stereo Image Formation

Two overlapping images form a stereo pair. Using stereoscopic viewing, the terrain appears in 3D due to parallax differences.

The height of objects is determined from image parallax.

---

## 6. Extraction of Elevation Data

Elevation points are collected either:

* Manually using stereoplotters, or
* Automatically using image matching algorithms

The result is a set of 3D points $(X,Y,Z)$.

---

## 7. DEM Generation

The extracted elevation points are interpolated into a continuous surface.

Common interpolation methods:

* TIN (Triangulated Irregular Network)
* Grid interpolation
* Kriging

A DEM represents elevations of the Earth's surface including vegetation and buildings if not removed.

---

## 8. DTM Generation

To generate a DTM:

* Buildings, trees, and other surface objects are removed from the DEM.
* Only bare-earth elevation points are retained.

Thus:

* **DEM** → includes terrain + surface objects
* **DTM** → represents bare-earth terrain only

---

# Simple Flow Diagram of DEM/DTM Generation

```text
Aerial Images
      ↓
Interior & Exterior Orientation
      ↓
Aerial Triangulation
      ↓
Stereo Image Formation
      ↓
Elevation Extraction
      ↓
Interpolation
      ↓
DEM
      ↓
Filtering/Removal of Objects
      ↓
DTM
```

---

# Applications of DEM/DTM

* Contour generation
* Watershed and drainage analysis
* Flood hazard mapping
* Urban planning
* Road and railway design
* 3D terrain visualization
* Orthorectification of satellite images


