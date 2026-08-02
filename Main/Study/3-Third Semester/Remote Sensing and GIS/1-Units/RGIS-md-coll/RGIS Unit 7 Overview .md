#rgis #third-semester 

# Unit 7: Photogrammetry (Overview)

**Exam Weight:** **6 Hours (Theory)** ⭐⭐⭐ (Very Important)

This is the **largest and one of the most important chapters** in the syllabus. It explains how **measurements, maps, and 3D models** are created from aerial photographs and satellite images.

---

# Topics Covered

1. Introduction
2. Development and Classification
3. Photogrammetric Process
4. Acquisition of Imagery and Support Data
5. Orientation and Triangulation
6. Stereo Model Compilation
7. Stereoscopic 3D Viewing
8. Stereoscopic Measurement
9. DTM/DEM Generation
10. Contour Map Generation
11. Orthorectification
12. 3D Feature Extraction
13. 3D Scene Modeling
14. Photogrammetry and LiDAR
15. Radargrammetry and Radar Interferometry
16. Limitations

---

# 1. Introduction

## Definition

**Photogrammetry** is the science and technology of obtaining **accurate measurements, maps, and 3D information** from photographs.

The word comes from:

* **Photo** = Light
* **Gramma** = Drawing/Writing
* **Metry** = Measurement

### Simple Definition

> Photogrammetry is the science of making measurements and creating maps or 3D models from photographs.

---

## Applications

* Topographic mapping
* Urban planning
* Civil engineering
* Forestry
* Agriculture
* Mining
* Archaeology
* Disaster management

---

# 2. Development and Classification

## Development

Photogrammetry has evolved through three stages:

### A. Analog Photogrammetry

* Uses printed photographs.
* Measurements made manually.
* Older technique.

---

### B. Analytical Photogrammetry

* Uses computers for calculations.
* Images are still obtained from photographs.
* More accurate than analog.

---

### C. Digital Photogrammetry

* Uses digital images and software.
* Most modern technique.
* Produces DEMs, orthophotos, and 3D models.

---

## Classification

Photogrammetry can also be classified based on the platform.

### A. Terrestrial Photogrammetry

* Camera placed on the ground.
* Used for buildings and engineering.

---

### B. Aerial Photogrammetry

* Camera mounted on aircraft or drones.
* Used for mapping large areas.

---

### C. Satellite Photogrammetry

* Images captured from satellites.
* Used for regional and global mapping.

---

# 3. Photogrammetric Process

The photogrammetric workflow consists of several steps.

```text
Image Acquisition
       │
       ▼
Image Orientation
       │
       ▼
Triangulation
       │
       ▼
Stereo Viewing
       │
       ▼
Measurements
       │
       ▼
DEM / DTM
       │
       ▼
Orthophoto
       │
       ▼
Maps / 3D Models
```

---

# 4. Acquisition of Imagery and Support Data

### Imagery

Images are collected using:

* Aircraft
* Drone
* Satellite

---

### Support Data

Additional information includes:

* GNSS coordinates
* Camera calibration
* Flight altitude
* Sensor information
* Ground Control Points (GCPs)

Support data improves measurement accuracy.

---

# 5. Orientation and Triangulation

## Orientation

Orientation determines the exact position and direction of the camera when the photograph was taken.

### Types

### Interior Orientation

* Restores camera geometry.
* Uses camera calibration parameters.

---

### Exterior Orientation

* Determines camera position and rotation in space.

---

### Relative Orientation

* Aligns two overlapping photographs.

---

### Absolute Orientation

* Places the stereo model into real-world coordinates.

---

## Triangulation

Triangulation determines unknown positions using overlapping photographs and known control points.

### Purpose

* Increase mapping accuracy.
* Reduce the number of ground control points needed.
* Improve coordinate estimation.

---

# 6. Stereo Model Compilation

Two overlapping aerial photographs are combined to create a **stereo model**.

This model provides:

* Depth
* Height
* Three-dimensional information

Applications:

* Mapping
* Terrain analysis
* Feature extraction

---

# 7. Stereoscopic 3D Viewing

![Image](https://images.openai.com/static-rsc-4/NTckHLlV5_ENaRUYpj6RRbPhfznI_CGA7N1oLDc9bmC49U9cCSa5iD8-7GxGjpQvKHww4tCeH7enZjDtJ_B5wCBH267ox0F6Qaub-mFcV18YNshztiPJw5wM3F2Cr3rqVp9WMeeAu7bkp6NsXbpm3uqTrG4RDP7Dsc_eV3vC9A7Xz7zyknhSCl6t4xvGF9ki?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/qbn4EsLZIuPNs9i4dvuKY1xHt9IspDzRMNgKB_9hKKWpAJboabcBUDAYRR4AA-mtcs2Pio40Dag5SZqEXu-khc0wOba_K0IzmIxnE_Bqjo527oPdvcqIN6Zq4rBr2xAIa-ZI_P5Nt5cL0NxZVMB9UhBMQ-IuNhPIYJRKmj2nl6d0_VZANvE4xpYDNGRKBpZw?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/c8Jvflvdz9mgy_hKy18FGOgLnXaUQOkUHNUkfJ3dm2kLBVNqaGGpppcIFeg7Gr69q5Y4gRCWVhc4laHUgQrqHk6gHue3TYdjsrC4qUAExeVBi88gmbEVnDIxooqy8JwXJsOom26FjKqlFWzkASaBhIDnmEIJNjefod0oRkz8Pe1sL044rNUGdoHG0bstD_yN?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/NFtF0PPNchk5yjnwUCd3CGrF0t4pGsQuFEbwVRMPzZDdky_Qs436EuuRNukInffdvDbQfOrVxEADgYcpFy_Z5LCRerrZSr9TDIJCoP70W6VWB9dErLutxoSVhFeYgbyAVtoxtXNhRThF4T3fW-dFykujX5EKw3Dh8K1PH4--TpnSMo_tKRqot2mLaMx9i-8s?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Ktfc1SNMtBbRM04D0Fh4hflCaA0cWgBjS7oBKnIKzSrBoOD-rcpqBskxDGlc2hrvR2Izp1ACVgLPVpmv_ac-wPYyu25HIiolJqBH4tcu8dSwXEZqbf70813UHvvVXOlKglmffLFoSBJB5jwRyvYPmkwRXPcm-QkmKohf91US71YMBzap-hxhlsyRugwuvkDP?purpose=fullsize)

## Definition

Stereoscopic viewing is the process of viewing **two overlapping photographs** so that the brain perceives a **single three-dimensional image**.

### Requirements

* Two overlapping images (usually about 60% overlap)
* Stereoscope or digital stereo viewer

### Advantages

* Height perception
* Terrain interpretation
* Better object identification

---

# 8. Stereoscopic Measurement

Measurements obtained from stereo images include:

* Height
* Distance
* Area
* Volume
* Elevation

Applications:

* Engineering
* Mining
* Forestry
* Construction

---

# 9. DTM and DEM Generation

## DEM (Digital Elevation Model)

A digital representation of **bare Earth's elevation**.

Contains elevation values only.

Applications:

* Slope analysis
* Watershed analysis
* Flood simulation

---

## DTM (Digital Terrain Model)

Contains:

* Elevation
* Terrain features
* Breaklines
* Surface characteristics

DTM is generally more detailed than a DEM.

---

## DEM vs DTM

| DEM                | DTM                          |
| ------------------ | ---------------------------- |
| Elevation only     | Elevation + terrain features |
| Simpler            | More detailed                |
| Used for elevation | Used for terrain analysis    |

---

# 10. Contour Map Generation

A contour map is produced from DEM or DTM.

### Contour Line

A line joining points having **equal elevation**.

Applications:

* Topographic mapping
* Engineering
* Land planning

---

# 11. Orthorectification

## Definition

Orthorectification is the process of removing geometric distortions from an aerial or satellite image.

The result is an **orthophoto**, where distances and positions are accurate.

### Errors Corrected

* Camera tilt
* Terrain relief
* Sensor distortion

### Advantages

* Accurate measurements
* GIS compatibility
* Correct scale

---

# 12. 3D Feature Extraction

Objects extracted include:

* Buildings
* Roads
* Rivers
* Trees
* Power lines
* Bridges

Applications:

* Smart cities
* GIS database creation
* Urban planning

---

# 13. 3D Scene Modeling

3D scene modeling creates realistic digital models of cities and landscapes.

Applications:

* Urban planning
* Tourism
* Virtual reality
* Disaster simulation
* Navigation

---

# 14. Photogrammetry and LiDAR

## Photogrammetry

* Uses photographs.
* Lower equipment cost.
* Produces color images.
* Accuracy depends on image quality.

---

## LiDAR

* Uses laser pulses.
* Produces highly accurate elevation.
* Works in low-light conditions.
* Better for dense forests.

---

## Comparison

| Photogrammetry    | LiDAR                          |
| ----------------- | ------------------------------ |
| Uses images       | Uses laser                     |
| Lower cost        | Higher cost                    |
| Color information | Accurate elevation             |
| Good for mapping  | Excellent for terrain modeling |

---

# 15. Radargrammetry and Radar Interferometry

## Radargrammetry

Uses stereo radar images to calculate:

* Height
* Terrain shape
* Surface elevation

---

## Radar Interferometry (InSAR)

Uses the phase difference between two radar images to measure:

* Ground deformation
* Earthquakes
* Volcano activity
* Land subsidence

Applications:

* Earthquake monitoring
* Volcano monitoring
* Landslide studies

---

## Radargrammetry vs InSAR

| Radargrammetry           | Radar Interferometry                |
| ------------------------ | ----------------------------------- |
| Uses stereo radar images | Uses radar phase differences        |
| Terrain mapping          | Surface deformation measurement     |
| Height estimation        | Very precise displacement detection |

---

# 16. Limitations of Photogrammetry

* Requires overlapping images.
* Weather and cloud cover affect image acquisition.
* Expensive equipment and software.
* Skilled operators required.
* Accuracy depends on image quality and ground control points.
* Dense vegetation can hide the ground.

---

# Advantages of Photogrammetry

* High accuracy
* Produces 3D information
* Cost-effective for large-area mapping
* Supports GIS
* Creates DEMs and orthophotos
* Non-contact measurement

---

# Frequently Asked Exam Questions

1. Define photogrammetry and explain its applications.
2. Explain the photogrammetric process with a diagram.
3. Differentiate analog, analytical, and digital photogrammetry.
4. Explain orientation and triangulation.
5. What is stereoscopic viewing? State its advantages.
6. Differentiate DEM and DTM.
7. Explain orthorectification.
8. Compare photogrammetry and LiDAR.
9. Differentiate Radargrammetry and Radar Interferometry.
10. Write the advantages and limitations of photogrammetry.

---

# Quick Revision (1-Minute Summary)

| Topic              | Key Point                                                             |
| ------------------ | --------------------------------------------------------------------- |
| Photogrammetry     | Making measurements and maps from photographs                         |
| Types              | Analog, Analytical, Digital                                           |
| Classification     | Terrestrial, Aerial, Satellite                                        |
| Process            | Image → Orientation → Triangulation → Stereo → DEM → Orthophoto → Map |
| Orientation        | Interior, Exterior, Relative, Absolute                                |
| Triangulation      | Determines positions using overlapping images and control points      |
| Stereo Viewing     | Two overlapping photos create a 3D view                               |
| DEM                | Elevation model                                                       |
| DTM                | Elevation + terrain features                                          |
| Orthorectification | Removes geometric distortions                                         |
| LiDAR              | Laser-based elevation mapping                                         |
| InSAR              | Measures tiny ground movements using radar phase differences          |

### **Exam tip**

The most frequently asked topics in Unit 7 are:

* **Photogrammetric process**
* **Orientation and Triangulation**
* **Stereoscopic viewing**
* **DEM vs DTM**
* **Orthorectification**
* **Photogrammetry vs LiDAR**
* **Radargrammetry vs Radar Interferometry**

These topics are commonly tested in long-answer questions and are among the highest-scoring areas in the course.
