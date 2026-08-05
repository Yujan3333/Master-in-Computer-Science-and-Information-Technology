#rgis #third-semester 

# Unit 9: Digital Image Processing (Overview)

**Exam Weight:** **3 Hours (Theory)**

This chapter explains how digital images obtained from remote sensing sensors are processed using computers to improve image quality and extract useful information.

---

# Topics Covered

1. Introduction
2. Categorization of Image Processing
3. Image Processing Systems
4. Digital Image
5. Media for Digital Data Recording, Storage, and Distribution
6. Data Formats of Digital Image
7. Header Information
8. Display of Digital Image
9. Pre-processing
10. Image Enhancement
11. Image Transformation
12. Image Classification

---

# 1. Introduction

**Digital Image Processing (DIP)** is the process of using computers to manipulate, analyze, and improve digital images.

The objectives are to:

* Improve image quality
* Remove errors and noise
* Extract useful information
* Classify land cover
* Prepare images for GIS analysis

---

## Applications

* Agriculture
* Forestry
* Urban planning
* Disaster management
* Environmental monitoring
* Medical imaging
* Military surveillance

---

# 2. Categorization of Image Processing

Digital image processing can be divided into four major stages.

```text
Image Acquisition
       │
       ▼
Pre-processing
       │
       ▼
Image Enhancement / Transformation
       │
       ▼
Image Classification
```

---

## A. Image Acquisition

The image is captured by:

* Satellite
* Aircraft
* Drone

---

## B. Pre-processing

Removes distortions and errors.

---

## C. Enhancement / Transformation

Improves image quality for interpretation.

---

## D. Classification

Assigns pixels to different land-cover classes.

---

# 3. Image Processing Systems

A digital image processing system consists of:

```text
Input Device
      │
      ▼
Computer
      │
      ▼
Image Processing Software
      │
      ▼
Storage
      │
      ▼
Output Device
```

---

## Components

### Input

* Satellite data
* Scanner
* Camera

---

### Computer

Processes image data.

---

### Software

Examples:

* QGIS
* ArcGIS
* ERDAS Imagine
* ENVI

---

### Storage

* Hard disk
* SSD
* Cloud storage

---

### Output

* Monitor
* Printer
* GIS database

---

# 4. Digital Image

A digital image consists of **pixels arranged in rows and columns**.

Each pixel contains a **Digital Number (DN)** representing the brightness value.

Example:

```text
125 130 140
120 135 145
115 125 150
```

---

# 5. Media for Digital Data Recording, Storage, and Distribution

Digital images can be stored on different media.

Examples:

* Hard disk
* SSD
* DVD
* USB drive
* Cloud storage
* Network servers

---

## Advantages

* Easy sharing
* Backup
* Long-term storage

---

# 6. Data Formats of Digital Image

Different formats are used to store digital images.

---

## Common Formats

### TIFF (.tif)

* High quality
* Widely used in GIS

---

### GeoTIFF

* TIFF with geographic coordinates
* Most common GIS format

---

### JPEG (.jpg)

* Compressed
* Small file size
* Some loss of quality

---

### PNG (.png)

* Lossless compression
* Good for graphics

---

### BMP (.bmp)

* Uncompressed
* Large file size

---

### HDF

Used for scientific satellite data.

---

### NetCDF

Stores multidimensional environmental data.

---

## Comparison

| Format  | Compression | GIS Support |
| ------- | ----------- | ----------- |
| TIFF    | No/Lossless | Excellent   |
| GeoTIFF | No/Lossless | Excellent   |
| JPEG    | Lossy       | Limited     |
| PNG     | Lossless    | Moderate    |
| BMP     | None        | Limited     |

---

# 7. Header Information

Every digital image file contains **header information**.

The header stores metadata describing the image.

---

## Includes

* Image dimensions
* Number of bands
* Pixel size
* Coordinate system
* Projection
* Data type
* Acquisition date
* Sensor name

---

## Importance

* Correct display
* GIS compatibility
* Accurate processing

---

# 8. Display of Digital Image

Images can be displayed in different ways.

---

## A. Grayscale Display
- Single spectral band
- Uses shades of gray.

Example:

* Black
* Gray
* White

---

## B. Color Composite

Combines three spectral bands.

Examples:

### True Color Composite

In a True Color Composite, the visible bands are assigned to their natural display colors.

| Spectral Band | Display Color |
| ------------- | ------------- |
| Red           | Red           |
| Green         | Green         |
| Blue          | Blue          |


Produces natural-looking images.

---

### False Color Composite
In a False Color Composite, spectral bands are assigned to different display colors.

| Spectral Band       | Display Color |
| ------------------- | ------------- |
| Near Infrared (NIR) | Red           |
| Red                 | Green         |
| Green               | Blue          |


Near-infrared is displayed as red.

Healthy vegetation appears **red**.

---

# 9. Pre-processing

Pre-processing removes errors before analysis.

---

## Types

### A. Radiometric Correction

Removes sensor and atmospheric effects.

Corrects brightness values.

---

### B. Geometric Correction

Corrects geometric distortions.

Aligns the image with map coordinates.

---

### C. Atmospheric Correction

Removes atmospheric scattering and absorption effects.

---

### D. Noise Removal

Removes random unwanted signals.

---

## Importance

* Improves accuracy
* Required before classification
* Makes images comparable

---

# 10. Image Enhancement

Image enhancement improves visual appearance.

---

## Techniques

### Contrast Stretching

Increases brightness contrast.

---

### Histogram Equalization

Redistributes brightness values.

---

### Filtering

Removes noise or sharpens edges.

---

### Edge Enhancement

Highlights boundaries.

---

## Applications

* Better visual interpretation
* Object detection
* Mapping

---

# 11. Image Transformation

Image transformation converts image data into another form to highlight specific information.

---

## Common Transformations

### Principal Component Analysis (PCA)

Reduces redundant information.

---

### Vegetation Indices

Example:

NDVI (Normalized Difference Vegetation Index)

Used for vegetation analysis.

---

### Band Ratio

Compares spectral bands.

Useful for geology and vegetation studies.

---

## Applications

* Agriculture
* Mineral exploration
* Land-cover analysis

---

# 12. Image Classification

Image classification groups pixels into meaningful categories.

Examples:

* Forest
* Water
* Urban
* Agriculture
* Barren land

---

## Types

### A. Supervised Classification

The user provides training samples.

Examples:

* Maximum Likelihood
* Minimum Distance

---

### B. Unsupervised Classification

The computer automatically groups similar pixels.

Example:

* K-means clustering
* ISODATA

---

## Supervised vs Unsupervised

| Supervised         | Unsupervised         |
| ------------------ | -------------------- |
| Uses training data | No training data     |
| Higher accuracy    | Faster               |
| Human involvement  | Automatic clustering |

---

# Overall Digital Image Processing Workflow

```text
Image Acquisition
        │
        ▼
Pre-processing
        │
        ▼
Image Enhancement
        │
        ▼
Image Transformation
        │
        ▼
Image Classification
        │
        ▼
Information Extraction
```

---

# Advantages of Digital Image Processing

* Improves image quality
* Removes noise
* Increases interpretation accuracy
* Enables automatic classification
* Easy GIS integration
* Fast processing

---

# Limitations

* Requires skilled users
* Expensive software
* Large storage requirements
* Complex algorithms
* High computational cost

---

# Frequently Asked Exam Questions

1. Define Digital Image Processing.
2. Explain the stages of digital image processing.
3. What are the components of an image processing system?
4. Explain different digital image formats.
5. What is header information?
6. Explain image pre-processing.
7. Describe image enhancement techniques.
8. What is image transformation? Give examples.
9. Differentiate supervised and unsupervised image classification.

---

# Quick Revision (1-Minute Summary)

| Topic                    | Key Point                                                                    |
| ------------------------ | ---------------------------------------------------------------------------- |
| Digital Image Processing | Computer-based processing of digital images                                  |
| Stages                   | Acquisition → Pre-processing → Enhancement → Transformation → Classification |
| Processing System        | Input, Computer, Software, Storage, Output                                   |
| Formats                  | TIFF, GeoTIFF, JPEG, PNG, BMP, HDF, NetCDF                                   |
| Header Information       | Metadata (size, bands, projection, etc.)                                     |
| Pre-processing           | Radiometric, Geometric, Atmospheric correction, Noise removal                |
| Enhancement              | Contrast stretching, Histogram equalization, Filtering                       |
| Transformation           | PCA, NDVI, Band ratio                                                        |
| Classification           | Supervised and Unsupervised                                                  |

### **Exam tip**

The most frequently asked topics in Unit 9 are:

* **Stages of Digital Image Processing**
* **Pre-processing techniques**
* **Image Enhancement**
* **Image Classification (Supervised vs Unsupervised)**
* **Header Information**
* **Data Formats (especially GeoTIFF and TIFF)**

These topics are commonly tested in short notes and long-answer questions.
