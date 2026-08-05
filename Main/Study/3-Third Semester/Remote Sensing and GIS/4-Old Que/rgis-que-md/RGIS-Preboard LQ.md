#rgis #third-semester #old-que #exam-paper-answer 

# Group A – Long Answer Questions (Attempt ANY TWO)

---

# Question 1

## Explain the principles of Remote Sensing with the help of the Electromagnetic Spectrum. Discuss the major types of satellite sensors (Passive and Active) and compare their characteristics, advantages, limitations, and applications in environmental monitoring and disaster management.

## (a) Principles of Remote Sensing

Remote sensing is the science of obtaining information about objects or the Earth's surface **without physical contact** by detecting electromagnetic radiation (EMR).

### Principle of Remote Sensing

1. **Energy Source**

   * The Sun is the primary source of energy for passive remote sensing.
   * Active sensors generate their own energy.

2. **Transmission through Atmosphere**

   * Electromagnetic radiation travels through the atmosphere.
   * Some energy is absorbed, scattered, or transmitted.

3. **Interaction with Target**

   * Objects reflect, absorb, or emit electromagnetic energy depending on their properties.

4. **Detection by Sensor**

   * Sensors on satellites or aircraft record the reflected or emitted energy.

5. **Data Processing**

   * Raw data is corrected and converted into digital images.

6. **Interpretation**

   * Images are analyzed to identify land cover, vegetation, water bodies, etc.

### Principle Diagram

```text
Sun / Sensor
      │
      ▼
Electromagnetic Radiation
      │
      ▼
Atmosphere
      │
      ▼
Earth Surface
      │
Reflected / Emitted Energy
      │
      ▼
Sensor
      │
      ▼
Processing
      │
      ▼
Interpretation
```

---

## Electromagnetic Spectrum

The electromagnetic spectrum is the complete range of electromagnetic radiation.

| Region                    | Approximate Wavelength | Remote Sensing Use         |
| ------------------------- | ---------------------- | -------------------------- |
| Ultraviolet               | 0.01–0.4 µm            | Atmospheric studies        |
| Visible                   | 0.4–0.7 µm             | Natural color images       |
| Near Infrared (NIR)       | 0.7–1.3 µm             | Vegetation analysis        |
| Shortwave Infrared (SWIR) | 1.3–3 µm               | Soil and moisture studies  |
| Thermal Infrared          | 3–14 µm                | Temperature mapping        |
| Microwave                 | 1 mm–1 m               | Radar, all-weather imaging |

---

## (b) Types of Satellite Sensors

### 1. Passive Sensors

Passive sensors detect **natural electromagnetic radiation** reflected or emitted by objects.

**Examples**

* Landsat
* Sentinel-2
* MODIS

#### Advantages

* Simple operation
* High-quality optical images
* Good for vegetation and land-cover mapping

#### Limitations

* Cannot operate effectively at night (except thermal sensors)
* Affected by clouds and haze

---

### 2. Active Sensors

Active sensors emit their own energy and measure the reflected signal.

**Examples**

* RADAR
* LiDAR
* Sentinel-1 SAR

#### Advantages

* Operate day and night
* Work through clouds and rain (RADAR)
* Useful for elevation and surface roughness measurements

#### Limitations

* More complex
* Expensive
* Higher power consumption

---

## Passive vs Active Sensors

| Passive Sensor      | Active Sensor              |
| ------------------- | -------------------------- |
| Uses natural energy | Emits its own energy       |
| Depends on sunlight | Independent of sunlight    |
| Affected by clouds  | Radar works through clouds |
| Lower cost          | Higher cost                |
| Example: Landsat    | Example: RADAR, LiDAR      |

---

## Applications

### Environmental Monitoring

* Deforestation
* Land-use mapping
* Vegetation monitoring
* Water quality assessment
* Climate studies

### Disaster Management

* Flood mapping
* Earthquake damage assessment
* Forest fire monitoring
* Landslide detection
* Cyclone monitoring

---

# Question 2

## Explain the concept of Spatial Databases in GIS. Discuss spatial data structures, topology, and attribute data management. How do spatial queries and overlay analysis assist in solving real-world planning and resource management problems?

## Spatial Database

A **spatial database** is a database designed to store, manage, and retrieve geographic information.

It stores:

* Spatial (location) data
* Attribute (descriptive) data

---

## Spatial Data Structures

### Raster Data

* Grid of pixels.
* Suitable for continuous data.

Examples:

* Satellite images
* DEM

---

### Vector Data

Uses:

* Points
* Lines
* Polygons

Examples:

* Schools (Point)
* Roads (Line)
* Lakes (Polygon)

---

## Topology

**Topology** describes the spatial relationships between geographic features.

### Types

* Connectivity
* Adjacency
* Containment

### Importance

* Detects mapping errors
* Supports network analysis
* Maintains data integrity

---

## Attribute Data Management

Attribute data describes spatial features.

Example:

| Road    | Width | Surface |
| ------- | ----- | ------- |
| Highway | 20 m  | Asphalt |

Functions include:

* Data storage
* Updating
* Querying
* Editing

---

## Spatial Queries

Spatial queries answer questions based on location.

Examples:

* Find hospitals within 5 km.
* Identify schools inside a municipality.
* Locate flood-prone villages.

### Benefits

* Faster decision-making
* Better planning
* Efficient resource allocation

---

## Overlay Analysis

Overlay analysis combines multiple GIS layers.

Example:

Road Layer + River Layer + Land-use Layer

↓

Best location for a new bridge.

### Applications

* Urban planning
* Agriculture
* Disaster management
* Forest management
* Site selection

---

## Conclusion

Spatial databases, topology, spatial queries, and overlay analysis enable efficient storage, analysis, and management of geographic information, supporting informed planning and resource management.

---

# Question 3

## (a) Discuss the elements of Visual Image Interpretation.

Visual image interpretation identifies objects using the following elements:

1. **Tone** – Brightness or darkness.
2. **Color** – Different colors indicate different objects.
3. **Texture** – Smooth or rough appearance.
4. **Pattern** – Spatial arrangement of objects.
5. **Shape** – Characteristic outline.
6. **Size** – Dimensions of objects.
7. **Shadow** – Indicates height and shape.
8. **Site** – Geographic location.
9. **Association** – Relationship with nearby features.

---

## (b) How is Digital Image Interpretation different from Visual Image Interpretation?

| Visual Interpretation             | Digital Interpretation             |
| --------------------------------- | ---------------------------------- |
| Done by humans                    | Done by computers                  |
| Uses visual elements              | Uses pixel values and algorithms   |
| Subjective                        | Objective                          |
| Slower                            | Faster                             |
| Suitable for small datasets       | Suitable for large datasets        |
| Depends on interpreter experience | Depends on software and algorithms |

---

## (c) Describe the Different Types of Image Resolutions.

### 1. Spatial Resolution

The ability to distinguish small objects on the ground.

* Higher spatial resolution = More detail.

Example:

* 1 m resolution shows individual buildings.
* 30 m resolution shows larger land-cover features.

---

### 2. Spectral Resolution

The ability of a sensor to distinguish different wavelength bands.

* Higher spectral resolution = More spectral bands.

Example:

* Hyperspectral images have very high spectral resolution.

---

### 3. Radiometric Resolution

The ability to detect small differences in brightness or energy.

Measured in bits:

* 8-bit = 256 brightness levels
* 16-bit = 65,536 brightness levels

Higher radiometric resolution provides better detection of subtle differences.

---

### 4. Temporal Resolution

The frequency with which a satellite revisits the same location.

Example:

* Daily revisit → High temporal resolution.
* Monthly revisit → Low temporal resolution.

---

## Summary of Image Resolutions

| Resolution  | Measures                  | Example                      |
| ----------- | ------------------------- | ---------------------------- |
| Spatial     | Object size/detail        | 1 m, 10 m, 30 m              |
| Spectral    | Number and width of bands | Multispectral, Hyperspectral |
| Radiometric | Brightness sensitivity    | 8-bit, 16-bit                |
| Temporal    | Revisit frequency         | Daily, Weekly, Monthly       |

---

## Exam Tip

For long-answer questions, remember these high-priority topics:

* **Principles of Remote Sensing** and the **Electromagnetic Spectrum**
* **Passive vs Active Sensors** (comparison with examples, advantages, limitations, and applications)
* **Spatial Databases, Topology, Spatial Queries, and Overlay Analysis**
* **Elements of Visual Image Interpretation**
* **Four Types of Image Resolution:** Spatial, Spectral, Radiometric, and Temporal
