#rgis #third-semester 

Here's a slightly expanded but still **simple, exam-friendly** version.

# 11. Orthorectification

## Definition

**Orthorectification** is the process of **correcting geometric distortions** in an aerial photograph or satellite image so that the image has the **correct shape, scale, and position**.

The corrected image is called an **orthophoto (orthoimage)**.

---

## Why is Orthorectification Needed?

Raw aerial or satellite images may be distorted because of:

* 📷 **Camera tilt** – The camera is not perfectly vertical.
* ⛰️ **Terrain relief** – Hills and mountains make objects appear displaced.
* 🛰️ **Sensor distortions** – Errors caused by the imaging sensor.
* 🌍 **Earth's curvature and rotation** (sometimes corrected as part of the processing).

Without correction, distances and locations are not accurate.

---

## Orthorectification Process

```text
Raw Image
     │
Correct camera tilt
     │
Correct terrain relief (using DEM/DTM)
     │
Correct sensor distortions
     │
Orthophoto (Geometrically Correct Image)
```

---

## Advantages

* ✅ Provides **accurate measurements** of distance and area.
* ✅ Has a **uniform scale** across the entire image.
* ✅ Can be used directly in **GIS** with other spatial data.
* ✅ Improves map accuracy.
* ✅ Suitable for mapping, surveying, and engineering applications.

---

## Applications

* Topographic mapping
* Urban planning
* Land-use mapping
* Cadastral mapping
* Infrastructure planning
* Disaster management

---

## Simple Example

Imagine taking a photo of a football field while standing at one corner.

* The field appears **tilted** and the far end looks **smaller**.
* After **orthorectification**, the field appears as if viewed **straight from above**, with the **correct shape and size**.

---

### Exam Definition (2 Marks)

> **Orthorectification** is the process of removing geometric distortions caused by camera tilt, terrain relief, and sensor errors from aerial or satellite images to produce an **orthophoto** with accurate scale, position, and geometry.
