#assignment #RGIS 
## Hyperspectral Image vs Multispectral Image

### Multispectral Image

A **multispectral image** captures data in a **few broad spectral bands**.
Usually it contains **3–15 bands** such as:

* Red
* Green
* Blue
* Near Infrared (NIR)
* Shortwave Infrared (SWIR)

The bands are **wide and separated**.

Example:

* Landsat satellite images
* Sentinel-2 images

### Hyperspectral Image

A **hyperspectral image** captures data in **hundreds of very narrow contiguous bands** across the electromagnetic spectrum.

Characteristics:

* Very fine spectral resolution
* Continuous spectral information
* Helps identify materials precisely

Example:

* Mineral detection
* Vegetation species analysis
* Military target detection

---

## Main Difference

| Feature                 | Multispectral Image                                                                         | Hyperspectral Image                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Number of bands         | Multispectral images contain only a few spectral bands, usually between 3 and 15 bands.     | Hyperspectral images contain hundreds of spectral bands, often more than 100 contiguous bands.                       |
| Band width              | Each band is broad and covers a large portion of the electromagnetic spectrum.              | Each band is extremely narrow, covering a very small wavelength range.                                               |
| Spectral continuity     | The bands are separated from each other and do not provide continuous spectral information. | The bands are continuous and adjacent, giving a complete spectral signature of objects.                              |
| Spectral resolution     | Spectral resolution is lower because fewer and wider bands are used.                        | Spectral resolution is very high due to the use of many narrow bands.                                                |
| Data volume             | Produces less data, so storage and transmission are easier.                                 | Produces a huge amount of data, requiring large storage and high processing power.                                   |
| Material identification | Can identify general land cover types such as water, vegetation, and urban areas.           | Can identify specific materials such as minerals, crop species, soil types, and chemicals accurately.                |
| Image processing        | Processing is simpler and computationally less expensive.                                   | Processing is complex and requires advanced algorithms and high-performance computing.                               |
| Cost                    | Sensors and processing systems are comparatively cheaper.                                   | Sensors and processing systems are expensive because of high spectral detail.                                        |
| Accuracy                | Provides moderate classification and detection accuracy.                                    | Provides very high classification and detection accuracy.                                                            |
| Applications            | Used in weather monitoring, agriculture, land use mapping, and environmental studies.       | Used in mineral exploration, precision agriculture, military surveillance, medical imaging, and scientific research. |
| Examples                | Landsat, Sentinel-2, SPOT satellites.                                                       | CASI, AVIRIS, Hyperion sensors.                                                                                      |
| Data acquisition speed  | Faster acquisition and easier handling of data.                                             | Slower acquisition and more difficult handling due to massive data size.                                             |


---

## Illustration

### Multispectral

Bands are broad and separated:

```text
|----Blue----|      |----Green----|      |----Red----|
```

### Hyperspectral

Bands are narrow and continuous:

```text
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
```

---

## CASI Band Overlap Problem

### Given

* Total spectral range:

  $$0.90\ \mu m - 0.40\ \mu m = 0.50\ \mu m$$

* Number of channels = 288

* Width of each band = 1.8 nm

Convert spectral range into nanometres:

$$0.50\ \mu m = 500\ nm$$

---

### Step 1: Compute spacing available per channel

$$\text{Spacing per channel}=\frac{500}{288}$$

$$\approx 1.736\ nm$$

---

### Step 2: Compare with actual band width

Actual band width:

$$1.8\ nm$$

Available spacing:

$$1.736\ nm$$

Since:

$$1.8 > 1.736$$

the bands slightly overlap.

---

## Amount of Overlap

Overlap per adjacent band:

$$1.8 - 1.736 = 0.064\ nm$$

---

## Final Answer

Yes, there will be a slight overlap between adjacent bands because each band width (1.8 nm) is greater than the available spacing between channels (approximately 1.736 nm). The overlap is about:

$$0.064\ nm$$
