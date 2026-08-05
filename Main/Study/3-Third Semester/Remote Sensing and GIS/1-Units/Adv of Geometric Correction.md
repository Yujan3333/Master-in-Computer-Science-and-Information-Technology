#rgis #third-semester 
# Geometric Correction

## Definition

**Geometric correction** is the process of **removing geometric distortions from a satellite image or aerial photograph** so that the image accurately represents the Earth's surface in its correct geographic location.

After geometric correction, every pixel is placed in its **true position** according to a map coordinate system.

---

## Why is Geometric Correction Needed?

Satellite images may be distorted due to:

* Satellite motion
* Earth's rotation
* Sensor tilt
* Terrain relief (mountains and valleys)
* Curvature of the Earth
* Atmospheric refraction

These distortions make objects appear in the wrong location.

---

## Before and After Geometric Correction

```text
Before Correction

Road
   \
    \
     \
      River

(Objects are shifted)
```

```text
After Correction

Road ----------
             |
             |
River ~~~~~~~|

(Objects are in their correct positions)
```

---

# Steps of Geometric Correction

1. Identify **Ground Control Points (GCPs)**.
2. Match image coordinates with real-world coordinates.
3. Apply a geometric transformation.
4. Resample pixel values (Nearest Neighbor, Bilinear, or Cubic Convolution).
5. Produce the corrected image.

---

# Advantages of Geometric Correction

### 1. Improves Positional Accuracy

Objects appear in their correct geographic locations.

### 2. Enables Accurate Distance and Area Measurement

Measurements of length, area, and direction become reliable.

### 3. Allows Overlay with GIS Data

Corrected images can be accurately overlaid with maps, GPS data, and other GIS layers.

### 4. Facilitates Change Detection

Images from different dates can be compared accurately to detect land-use or environmental changes.

### 5. Supports Accurate Mapping

Produces maps suitable for surveying, planning, and navigation.

### 6. Reduces Image Distortion

Removes distortions caused by the sensor, satellite movement, terrain, and Earth's curvature.

### 7. Improves Image Interpretation

Objects are displayed in their correct shape and position, making interpretation easier.

---

# Applications

* Land use and land cover mapping
* Urban planning
* Disaster management
* Agriculture
* Environmental monitoring
* Topographic map preparation

---

# Exam Answer (5 Marks)

**Geometric correction** is the process of removing geometric distortions from remotely sensed images so that each pixel is placed in its correct geographic position. Distortions may occur due to satellite motion, sensor tilt, Earth's rotation, terrain relief, and Earth's curvature. Geometric correction uses **Ground Control Points (GCPs)** and transformation methods to align the image with a map coordinate system.

### Advantages

* Improves positional accuracy.
* Enables accurate distance and area measurements.
* Allows integration with GIS and GPS data.
* Facilitates change detection using multi-date images.
* Reduces geometric distortions.
* Improves mapping and image interpretation.

---

## Memory Trick

Think of a **crooked map**.

* **Before geometric correction:** Roads, rivers, and buildings are shifted or distorted.
* **After geometric correction:** Everything is moved back to its **correct geographic location**.

**Remember:**
**Geometric correction = Correcting the *position* and *shape* of image features so they match the real world.**
