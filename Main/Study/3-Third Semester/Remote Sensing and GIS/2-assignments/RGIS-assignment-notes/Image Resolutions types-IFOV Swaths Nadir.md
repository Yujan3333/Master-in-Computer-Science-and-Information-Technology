#RGIS #assignment 
# Different Types of Image Resolution in Remote Sensing

Image resolution refers to the ability of a remote sensing system to distinguish details in an image. Higher resolution means more detail can be identified. The main types of resolutions are:

---

# 1. Spatial Resolution

Spatial resolution refers to the size of the ground area represented by one pixel in an image.

* It indicates the smallest object that can be detected.
* Measured in meters.

### Examples

* 30 m resolution → one pixel represents $30 \times 30$ m ground area.
* 1 m resolution → finer detail.

### Interpretation

* High spatial resolution → more detail, smaller pixels.
* Low spatial resolution → less detail, larger pixels.

## Example

* Landsat-8: 30 m
* Sentinel-2: 10 m

### Illustration

```text
High Spatial Resolution
+--+--+--+--+
|##|##|..|..|
+--+--+--+--+
|##|##|..|..|
+--+--+--+--+

Low Spatial Resolution
+------+------+
| #### | .... |
+------+------+
```

---

# 2. Spectral Resolution

Spectral resolution refers to the sensor's ability to distinguish fine wavelength intervals in the electromagnetic spectrum.

* Determined by number and width of spectral bands.
* Narrow bands → high spectral resolution.

### Types

* Panchromatic → single broad band
* Multispectral → few broad bands
* Hyperspectral → hundreds of narrow bands

### Illustration

```text
Electromagnetic Spectrum
|----Blue----|----Green----|----Red----|

Low Spectral Resolution:
|-----------Single Broad Band-----------|

High Spectral Resolution:
|--B1--|--B2--|--B3--|--B4--|--B5--|
```

---

# 3. Radiometric Resolution

Radiometric resolution refers to the sensor's sensitivity to detect slight differences in energy or brightness.

* Expressed in bits.
* Higher bit depth → more gray levels.

## Formula

$$2^n$$

where:

* $n$ = number of bits

### Examples

* 8-bit image → $2^8 = 256$ gray levels
* 11-bit image → $2^{11} = 2048$ gray levels

### Illustration

```text
Low Radiometric Resolution:
Dark ---- Light
  0  50 100 150 255

High Radiometric Resolution:
0 1 2 3 4 .... 2047
```

---

# 4. Temporal Resolution

Temporal resolution refers to the time interval required for a satellite to revisit and capture the same area again.

* Also called revisit period.

### Examples

* MODIS: daily
* Landsat: 16 days
* Sentinel-2: 5 days

### Importance

Useful in:

* Flood monitoring
* Crop monitoring
* Disaster management
* Land-use change detection

### Illustration

```text
Day 1 ---- Day 5 ---- Day 10
   ↑         ↑          ↑
 Image     Image      Image
```

---

# IFOV (Instantaneous Field of View)

IFOV is the angular cone of visibility of a sensor at a particular instant.

* It determines the ground area viewed by a single detector element.
* Smaller IFOV → higher spatial resolution.

## Relationship

```text
Small IFOV  → Small Ground Area → Better Detail
Large IFOV  → Large Ground Area → Lower Detail
```

### Illustration

```text
           Satellite
               *
              / \
             /   \
            /IFOV \
           /       \
----------Ground Surface----------
         Small Ground Cell
```

---

# Swath

Swath is the total width of the ground area covered by a sensor during one pass of the satellite.

* Wider swath covers larger area.
* Narrow swath gives more detail but less coverage.

### Illustration

```text
        Satellite Path
              ↑
              |
   <-------------------->
          Swath Width

=================================
          Ground Surface
=================================
```

### Example

* MODIS → very wide swath
* High-resolution satellites → narrow swath

---

# Nadir

Nadir is the point on the Earth's surface directly below the sensor or satellite.

* Viewing directly downward gives minimum distortion.
* Areas away from nadir experience geometric distortion.

### Illustration

```text
             Satellite
                 *
                 |
                 |
                 |
              Nadir
                 ↓
--------------------------------
          Earth's Surface
```

---

# Relationship Between IFOV, Swath and Nadir

| Term  | Meaning                                   | Importance                           |
| ----- | ----------------------------------------- | ------------------------------------ |
| IFOV  | Area seen by one detector instantaneously | Determines spatial resolution        |
| Swath | Total width covered during one pass       | Determines coverage area             |
| Nadir | Point directly below sensor               | Reference point for viewing geometry |

---

# Summary

* Spatial resolution → size of pixel on ground.
* Spectral resolution → ability to distinguish wavelengths.
* Radiometric resolution → sensitivity to brightness differences.
* Temporal resolution → revisit frequency.
* IFOV controls ground detail captured by a detector.
* Swath determines total coverage width.
* Nadir is the point directly beneath the satellite sensor.
