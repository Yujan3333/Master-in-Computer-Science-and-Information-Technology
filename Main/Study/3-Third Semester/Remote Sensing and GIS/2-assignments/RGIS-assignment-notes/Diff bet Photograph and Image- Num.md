#assignment #RGIS 
# Difference Between Photograph and Image

*(Based on concepts from Remote Sensing and GIS)*

| Photograph                                                                     | Image                                                                               |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| A photograph is an analog record produced on photographic film using a camera. | An image is a digital representation of an object or scene recorded electronically. |
| Produced using chemical processes on film.                                     | Produced using electronic sensors and digital systems.                              |
| Commonly obtained from aerial cameras.                                         | Obtained from scanners, satellites, digital cameras, radar, etc.                    |
| Continuous tone representation.                                                | Composed of pixels arranged in rows and columns.                                    |
| Geometric correction is difficult.                                             | Easy to process and geometrically correct using computers.                          |
| Interpretation is mainly visual.                                               | Interpretation can be visual or digital using image processing techniques.          |
| Storage requires physical film or paper.                                       | Stored digitally in computers or storage devices.                                   |
| Copying may reduce quality.                                                    | Digital copies maintain the same quality.                                           |
| Used mainly in traditional photogrammetry.                                     | Widely used in digital photogrammetry and remote sensing.                           |
| Example: Aerial film photograph.                                               | Example: Landsat satellite image.                                                   |

---

# Calculation of Scale Factor of Aerial Photo

## Given

* Flying height above ground $(H)=2500\ \text{m}$
* Focal length $(f)=88\ \text{mm}$

Convert height into millimeters:

$$2500\ \text{m}=2500\times1000=2,500,000\ \text{mm}$$

---

# Formula for Scale of Aerial Photograph

$$S=\frac{f}{H}$$

Where:

* $S$ = scale
* $f$ = focal length
* $H$ = flying height above ground

---

# Calculation

$$S=\frac{88}{2,500,000}$$

$$S=\frac{1}{28,409.09}$$

---

# Final Answer

The scale factor of the aerial photograph is approximately:

$$\boxed{1:28,400}$$

Thus, the aerial photo scale is about **1 : 28,400**.
