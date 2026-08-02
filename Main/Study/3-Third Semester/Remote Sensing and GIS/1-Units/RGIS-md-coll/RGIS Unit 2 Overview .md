#rgis #third-semester 
# Unit 2: Types of Remote Sensing and Sensor Characteristics (Overview)

**Exam Weight:** 3 Hours (Theory)

This chapter explains:

* Types of remote sensing
* Characteristics of remote sensing images
* Satellite orbits
* Swath and nadir
* Sensor resolutions
* Image referencing systems

---

# 1. Introduction

Remote sensing systems differ based on:

* Source of energy
* Platform (satellite, aircraft, drone)
* Sensor type
* Orbit
* Resolution

The quality and usefulness of remote sensing data depend mainly on the **sensor characteristics**.

---

# 2. Types of Remote Sensing

Remote sensing is classified into two main types based on the **source of energy**.

## A. Passive Remote Sensing

Passive sensors **do not produce their own energy**. They detect **natural radiation**, usually sunlight reflected from the Earth's surface or thermal energy emitted by objects.

### Energy Source

* Sun (reflected energy)
* Earth's thermal emission

### Examples

* Landsat
* Sentinel-2
* SPOT

### Advantages

* Simple system
* Lower power requirement
* Good for vegetation and land cover mapping

### Limitations

* Cannot work well at night (except thermal sensors)
* Cloud cover affects images

---

## B. Active Remote Sensing

Active sensors **generate their own electromagnetic energy**, send it toward the Earth's surface, and measure the reflected signal.

### Energy Source

* Sensor itself

### Examples

* Radar (SAR)
* LiDAR

### Advantages

* Works day and night
* Can penetrate clouds (Radar)
* Useful for elevation mapping

### Limitations

* More expensive
* Higher power consumption
* More complex processing

---

## Passive vs Active Remote Sensing

| Passive             | Active                     |
| ------------------- | -------------------------- |
| Uses natural energy | Generates its own energy   |
| Depends on sunlight | Independent of sunlight    |
| Affected by clouds  | Radar works through clouds |
| Simple sensors      | Complex sensors            |
| Example: Landsat    | Example: Radar, LiDAR      |

---

# 3. Characteristics of Image

A remote sensing image has several characteristics that help identify objects.

Important image characteristics include:

* Tone/Brightness
* Color
* Texture
* Pattern
* Shape
* Size
* Shadow
* Location
* Association

These are also called **image interpretation elements** and are discussed in more detail in Unit 8.

---

# 4. Orbital Characteristics of Satellite

Satellites move around the Earth in different types of orbits.

The two most common are:

## A. Geostationary Orbit (GEO)

* Height: approximately **35,786 km**
* Moves with Earth's rotation
* Appears fixed over one location
* Covers a very large area
* Lower spatial resolution
* High temporal resolution (continuous monitoring)

### Applications

* Weather forecasting
* Communication
* Cyclone monitoring

Examples:

* INSAT
* GOES

---

## B. Polar (Sun-Synchronous) Orbit

* Height: approximately **500–1000 km**
* Passes near the North and South Poles
* Earth rotates beneath the satellite
* Covers the entire Earth over time
* Higher spatial resolution

### Applications

* Mapping
* Agriculture
* Forest monitoring
* Land use analysis

Examples:

* Landsat
* Sentinel
* IRS

---

## Geostationary vs Polar Orbit

| Geostationary            | Polar                     |
| ------------------------ | ------------------------- |
| 35,786 km                | 500–1000 km               |
| Fixed over one point     | Passes over poles         |
| Continuous observation   | Global coverage           |
| Lower spatial resolution | Higher spatial resolution |
| Weather monitoring       | Earth mapping             |

---

# 5. Remote Sensing Satellites

Remote sensing satellites carry sensors that collect data about the Earth's surface.

Examples include:

* Landsat
* Sentinel
* IRS (Indian Remote Sensing)
* SPOT
* IKONOS
* WorldView

Applications:

* Agriculture
* Forestry
* Urban planning
* Disaster management
* Environmental monitoring

---

# 6. Concept of Swath and Nadir

These are important exam topics.

## Swath

The **swath** is the width of the Earth's surface covered by the sensor during one satellite pass.

### Simple Definition

> Swath is the strip of Earth's surface imaged by a sensor in one pass.

### Large Swath

* Covers more area
* Lower detail

### Small Swath

* Covers less area
* Higher detail

---

## Nadir

The **nadir** is the point on the Earth's surface directly below the sensor.

```
Satellite
    |
    |
    ▼
  Nadir
```

It is the point where image distortion is minimum.

---

## Swath vs Nadir

| Swath                   | Nadir                       |
| ----------------------- | --------------------------- |
| Width covered by sensor | Point directly below sensor |
| Large area              | Single point                |
| Determines coverage     | Determines viewing geometry |

---

# 7. Sensor Resolutions

**Resolution** means the ability of a sensor to distinguish details.

There are four main types.

---

## A. Spatial Resolution

It refers to the **smallest object that can be detected**.

Measured in meters.

Example:

* 30 m resolution → each pixel represents 30 × 30 m.
* 1 m resolution → finer detail.

Higher spatial resolution means more detail.

---

## B. Spectral Resolution

It refers to the sensor's ability to distinguish different wavelengths (spectral bands).

Examples:

* RGB camera: 3 bands
* Multispectral sensor: several bands
* Hyperspectral sensor: hundreds of narrow bands

Higher spectral resolution helps identify different materials.

---

## C. Temporal Resolution

It is the **time interval between successive observations** of the same location.

Example:

* Daily revisit → high temporal resolution.
* Every 16 days → lower temporal resolution.

Useful for monitoring crop growth, floods, and forest fires.

---

## D. Radiometric Resolution

It refers to the sensor's ability to detect small differences in energy (brightness).

Measured in **bits**.

Examples:

* 8-bit = 256 brightness levels
* 10-bit = 1024 levels
* 12-bit = 4096 levels

Higher radiometric resolution provides more detailed brightness information.

---

## Summary of Sensor Resolutions

| Resolution  | Measures          | Unit            |
| ----------- | ----------------- | --------------- |
| Spatial     | Object size       | Meter (m)       |
| Spectral    | Wavelength bands  | Number of bands |
| Temporal    | Revisit time      | Days/Hours      |
| Radiometric | Brightness levels | Bits            |

---

# 8. Image Referencing System

An image referencing system identifies the exact location of every pixel on the Earth's surface.

Common methods include:

* Geographic Coordinate System (Latitude and Longitude)
* Universal Transverse Mercator (UTM)
* Grid systems

Purpose:

* Locate features accurately.
* Overlay images with maps and GIS data.
* Perform measurements and spatial analysis.

---

# Frequently Asked Exam Questions (Unit 2)

1. Define passive and active remote sensing. Compare them.
2. Explain geostationary and polar orbits with differences.
3. Define swath and nadir with diagrams.
4. What is spatial resolution? Explain the four types of sensor resolution.
5. What is an image referencing system?
6. Write short notes on remote sensing satellites.

---

# Quick Revision (1-Minute Summary)

* **Passive Remote Sensing:** Uses natural energy (Sun).
* **Active Remote Sensing:** Generates its own energy (Radar, LiDAR).
* **Geostationary Orbit:** 35,786 km, fixed over one location, weather monitoring.
* **Polar Orbit:** 500–1000 km, covers the whole Earth, mapping.
* **Swath:** Width of Earth's surface covered in one satellite pass.
* **Nadir:** Point directly below the sensor.
* **Four Sensor Resolutions:** Spatial, Spectral, Temporal, and Radiometric.
* **Image Referencing System:** Assigns geographic coordinates to image pixels for accurate mapping and GIS integration.

**Exam tip:** The highest-priority topics in Unit 2 are **Passive vs Active Remote Sensing**, **Geostationary vs Polar Orbit**, **Swath & Nadir**, and the **four types of sensor resolution**. These are asked frequently in both short and long questions.
