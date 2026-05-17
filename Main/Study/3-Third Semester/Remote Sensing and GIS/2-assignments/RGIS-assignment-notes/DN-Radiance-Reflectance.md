#assignment #RGIS 

# Digital Number (DN)

Digital Number (DN) is the numerical value assigned to each pixel in a digital image by a sensor after measuring the received electromagnetic energy.

* It represents the pixel brightness.
* DN values are stored as integers.
* Common ranges:

  * 8-bit image → 0–255
  * 10-bit image → 0–1023
  * 12-bit image → 0–4095

Higher DN means higher detected energy.

## Example

* Dark surface → Low DN
* Bright surface → High DN

---

# Radiance

Radiance is the amount of electromagnetic energy received by the sensor from a target per unit area, per unit solid angle, and per unit wavelength.

It represents the actual energy reaching the sensor.

Unit:

$$
W,m^{-2},sr^{-1},\mu m^{-1}
$$

where:

* $W$ = watt
* $sr$ = steradian
* $\mu m$ = micrometer

Radiance depends on:

* Surface properties
* Illumination
* Atmospheric effects
* Sensor characteristics

---

# Reflectance

Reflectance is the ratio of reflected radiation from a surface to the incoming solar radiation.

It describes how much energy a surface reflects.

Formula:

$$\rho=\frac{\text{Reflected Energy}}{\text{Incident Energy}}$$

Reflectance values usually range from 0 to 1 or as percentage.

Examples:

* Snow → High reflectance
* Water → Low reflectance

Reflectance is preferred in remote sensing because it reduces effects of:

* Sensor differences
* Solar angle variations
* Illumination conditions

---

# Conversion of DN to Radiance

DN values are converted into radiance using sensor calibration parameters.

Formula:

$$L_\lambda=\left(\frac{L_{max}-L_{min}}{QCAL_{max}-QCAL_{min}}\right)(DN-QCAL_{min})+L_{min}$$

where:

* $L_\lambda$ = spectral radiance
* $L_{max}$ = maximum radiance
* $L_{min}$ = minimum radiance
* $DN$ = digital number
* $QCAL_{max}$ = maximum quantized calibrated pixel value
* $QCAL_{min}$ = minimum quantized calibrated pixel value

This converts raw image values into physical radiance units.

---

# Conversion of Radiance to Reflectance

Radiance is converted into Top of Atmosphere (TOA) reflectance using:

$$\rho_\lambda=\frac{\pi L_\lambda d^2}{E_{sun\lambda}\cos\theta_s}$$

where:

* $\rho_\lambda$ = reflectance
* $L_\lambda$ = spectral radiance
* $d$ = Earth–Sun distance
* $E_{sun\lambda}$ = mean solar exoatmospheric irradiance
* $\theta_s$ = solar zenith angle

---

# Summary Table

| Term                | Meaning                               | Represents               |
| ------------------- | ------------------------------------- | ------------------------ |
| Digital Number (DN) | Raw pixel value                       | Relative brightness      |
| Radiance            | Energy reaching sensor                | Physical measured energy |
| Reflectance         | Ratio of reflected to incident energy | Surface property         |

---

# Conversion Flow

$$
DN \rightarrow Radiance \rightarrow Reflectance
$$

* DN → sensor-recorded value
* Radiance → calibrated energy
* Reflectance → normalized surface response
