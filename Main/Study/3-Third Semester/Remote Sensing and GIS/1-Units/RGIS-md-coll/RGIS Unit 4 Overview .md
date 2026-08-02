#rgis #third-semester 

# Unit 4: Digital Imaging (Overview)

**Exam Weight:** 4 Hours (Theory)

This chapter explains how modern remote sensing systems capture and process **digital images**. It introduces digital images, sensors, scanning techniques, hyperspectral imaging, thermal remote sensing, and other sensors.

---

# 1. Introduction

Unlike traditional photographic imaging, **digital imaging** records information as **digital numbers (DN values)** instead of film.

A sensor detects electromagnetic energy reflected or emitted from the Earth's surface and converts it into digital data that computers can process.

Digital imaging is now the standard in remote sensing because it is more accurate, easier to store, and suitable for computer analysis.

---

# 2. Digital Image

A **digital image** is an image made up of tiny square elements called **pixels (picture elements)**.

Each pixel stores a **Digital Number (DN)** representing the brightness or energy received by the sensor.

### Example

```
+----+----+----+
|120 |135 |140 |
+----+----+----+
|115 |130 |145 |
+----+----+----+
|110 |125 |150 |
+----+----+----+
```

Each number is a pixel value.

---

## Components of a Digital Image

* **Pixel:** Smallest unit of an image.
* **Rows and Columns:** Pixels are arranged in a grid.
* **Digital Number (DN):** Brightness value of a pixel.

---

## Advantages of Digital Images

* Easy to store
* Easy to edit
* Computer processing
* High accuracy
* Multiple spectral bands
* Suitable for GIS integration

---

# 3. Sensor

A **sensor** is a device that detects electromagnetic radiation and converts it into electrical signals or digital values.

## Types of Sensors

### A. Passive Sensor

* Uses natural energy from the Sun.
* Measures reflected or emitted radiation.

**Examples**

* Landsat
* Sentinel-2

---

### B. Active Sensor

* Generates its own energy.
* Measures the reflected signal.

**Examples**

* Radar
* LiDAR

---

## Functions of a Sensor

* Detect energy
* Convert energy into electrical signals
* Store or transmit digital data

---

# 4. Imaging by Scanning Technique

Most satellite images are produced using **scanning techniques**.

The sensor scans the Earth's surface line by line.

There are two major scanning methods.

---

## A. Across-Track Scanning (Whiskbroom Scanner)

![Image](https://images.openai.com/static-rsc-4/f2i0q0LLcQ8WnfSv0bygIMjCPpPYnw8YoL1nlpcpRIPCqc4F39JEgS-SAI1fMWt9XsfEUA29zPOySTiZ1-OBb6FoL6r-cth9VEfuIzGGctcNQB4cJuHkuNtD8BFFCDVjh0JzMw3L3UkLuQa5Aty-98xzYzPlixKXWC8ptwAaTZsznZaR9W3vLVNLh9_ERakC?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/VnFfCfNw57ApcucozTxdcdpOPwqavlMaCsrH9dAShpPZywFWMBx_Ed9zpJqSozpFm_PnAshE6pkvP5EBE8Y4frTjxUU5PjqjblW6FfWRc5rolWuNwr02rYHYfU713NcVFWtpuzRYkZcBXzKAlAHb2ntARzZZhAtdl8T4735OQ-tzj2EyXJR-MOoqBnRuMwi2?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/s34yByca1I21N2hDufsqzAXPZSPURve2bgEoNNXP-gzuTtoJr75sJdklHWNCgDYHbaRSdRtpK5_nlXBvd-iM4NGB_zQvy0Kkw6UEat492JImqcNrKBhE0jCGIrx3BeujAnnoudBI7WEJCZfq063zbTm4gjkyLpmuxO5OOcOKUSVLA4q_BtXasr_qds3wVC3H?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ZvgHJYUyw4Drs7Nsx4xSa9W75D8NTVLz6uGA0ryGS-dM0KTfJADFQmokYQIFbza3EqBnmH1h9IgaJ0meJePIi6Q9rEYftvFMr4xFIIpaNo7Z32UdaYlJSFVzldr5JOmRBJuA4gfztDKHtj-MojKaOnEMQ6NDrwoYZLErGBGbTP9d0FY5lnDiiBr_V6SM8UvE?purpose=fullsize)

A rotating mirror moves **side to side** across the satellite's path.

The satellite moves forward while the mirror scans across the ground.

### Characteristics

* Uses one or a few detectors.
* Mirror scans left and right.
* Older technology.

### Advantages

* Simple detector design.
* Good calibration.

### Disadvantages

* Moving parts can wear out.
* Slower image acquisition.

### Example

* Landsat MSS
* Landsat TM

---

## B. Along-Track Scanning (Pushbroom Scanner)

![Image](https://images.openai.com/static-rsc-4/zAK4JgFQQcShQ4PdZ58cl0jdNvVqsDHKpWFFIuBUtHXo9KyJib4AxFXBDdZ_fSFwJJHPfoFSAIILwLyYtGj01hAqdZoYs706Zw4Ev-HMIxmE4qudUW1vKI1gbnrQFixjlEazXuTsl4Ws2nI_hjOYfGCZsolRh7Piewdc0lBbvngUXExdNWnsIvtm5Kbk9ocb?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/JGiaAwHhPVXRIu5-EydZgQZ15w7AuuqWmLGfzwNy_vNHE1XIsWhwbMc5-ARtXcmn0QQ8lLlrKlDerzRzpg4uDQNb4IxhyiZMSzfPkvV6m2gmS1QNS6W0GG24JQZ-0UazmceOz4F4SU0RHi0GubCy5oKBY5QbYlxq0MdD0O_HTV2etTV5OdaOTqVxH0ukjh7q?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/UdhfRGcT5RqQGt2A1om6w27aKVixePSviw1nK4CFuLytaX9dMlUjqHNIVGARhezGWG0Zr-ZhSTXhX8NvQVoKON6V8G5RZ6D6TuJUExDvwTX-oR3JmztUXzelNE0aDKbJV2jbZ8OTc-UH7x69zhY0IWe8YR9VWbm2X36u_GpxugMhWpLTWHM9qACGwnbh5P6j?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/6MbqWwmZAkjQdyLL2tYJvpVub4g_UAVyFfFSHoHkop0-YN3TWP172mF6nS8umSGV3tK8y7sLUk6i8rsAAMHOY-u2uz_JHZusw6diB7cfvpwCGjf6CWEohFQVWfGzKqhbJnXWAvLlDjgPsdCrZPbHYtSHt5bDjODFLlu9vr5_yy0wlJF8MtmYu8SbJllXVU5D?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/8tFNll-Poud89lzW02jw0YYUnExzh9X3RUSX0GKniueeUTU2qU5XYvIZweKaA2PeGv3s--2naXezZ_TSsdU3-QzgfhvCfiFtZiZJMPU9f3Q4AdXJ3AuKGBr7vJ2SYTgj9v8r4-lmcaRxNvjkk2QA-XnQCL6W6K1GFCQhrZZEWoGl_JZB_sk0C_cqSr_gS5vp?purpose=fullsize)

Uses a **linear array of detectors**.

The satellite moves forward, and all pixels in a row are captured simultaneously.

### Characteristics

* No moving mirror.
* Hundreds or thousands of detectors.

### Advantages

* Faster
* Better image quality
* Higher reliability
* Less mechanical complexity

### Disadvantages

* Detector calibration is more difficult.

### Example

* Sentinel-2
* SPOT
* IRS

---

## Whiskbroom vs Pushbroom

| Whiskbroom (Across-Track) | Pushbroom (Along-Track) |
| ------------------------- | ----------------------- |
| Rotating mirror           | Linear detector array   |
| Few detectors             | Many detectors          |
| Moving parts              | No moving parts         |
| Older technology          | Modern technology       |
| Slower                    | Faster                  |

---

# 5. Hyper-spectral Imaging

![Image](https://images.openai.com/static-rsc-4/reLiM4eG4cLIQn1zvjo6M57eBPeMUDu8wOpFqhwEDzvfTNZT4HQXu1zHhaUmLhU4YVnVdaedXPo-_ObM6ZCbunJ4wSJcP9Ufqj7o48e2JVxC3TTPQHtWE3vOIsGcXmJoRFqVtSjVkj14Li9UQfnPhM9e3hDro7iHrAr0RyMKhFIf7rmNe0HIEh7FQzJzB6rW?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/D4M4nqaFiunsEBcqTOQJfTzGuaOou0Fz4xVEfCdiMIrWX_-qIDY0a05TN9ScH2h1IApLWCZaiLocLoooUXU7Icc8UiszBSiQtzryuJP-4Y09vHzhnBKtTjOrFgRQCsH_Day64tPYKIBGWl23TXSaGByQJQ-7bRjjdSPHuDMQbgHbICjpDGenzFJX5oIT-eRV?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/-d_P-gronLb075FELN93mG26reUlmRdssHmvTi98J7GymfWOI8mw4T2XFHqA8Kc6lcUzL6L6xw2UwBf1jkMxiTyVja1rvhTNba1m0c0uPTvgYXJv7USjIrn_EG8-6wzmad1hwrMboiPGAB0AHcXbNa5tKIy2ISkg-r4DG5zFVnKMLJ8MsqxnMV_Eg0KMCd8Q?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/IQHxVfe-LCoFUNmUk50kQAbOb8EphSp5jndqaSFPsWlrzYT_UH0E-9IIOCk3E7Wm6c28iSPgJKYwCBm2bT0Q20tSQL7fheLD9Kidu21MqZHzFHTfnFAQtaPJGkJS0cxmEP6y2uxhToxGfcLlG8X5fqQyGyG8tw2xWIlZy49P2a7pmfsl7aMBQ7z_CL5L60pM?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/h2waVZlPAFRQ7TIEmkuQpilYjnGFmTHETe96-UX1qB8NZ5cPTJ2wRXo3aVFnldRPTU_CW56O_uBPCUHxxRe_wKMrR_oimM4UdWECjl503Xyl-A4K1rzHUSAZPSxaIdtCL85DIv1Va8avrd_c5Cfo54gQu-UGQitUFcXP9ToITqRtH79itobhNt9ZCn3Jsefz?purpose=fullsize)

A **hyperspectral sensor** records **hundreds of very narrow spectral bands**.

Unlike ordinary cameras, hyperspectral sensors can distinguish materials with very similar spectral characteristics.

### Applications

* Mineral exploration
* Agriculture
* Crop health monitoring
* Environmental monitoring
* Water quality analysis
* Geological mapping

---

## Multispectral vs Hyperspectral

| Multispectral             | Hyperspectral                    |
| ------------------------- | -------------------------------- |
| Few bands (3–15)          | Hundreds of bands                |
| Wider bands               | Very narrow bands                |
| General classification    | Detailed material identification |
| Lower spectral resolution | Higher spectral resolution       |

---

# 6. Imaging by Non-Scanning Technique

![Image](https://images.openai.com/static-rsc-4/tijUpzQGeA7TaIqkTz0XBpA0HXUJ985Cc9i0LhaeFoSOspvq6FPdGfSV8xBwvo0Dn7JkFabZhkikL0SO9rH9ZGWMAY5ym91bX-AUYH6mBEpbnHRNI1maN7kl46UF982hJohPo8R41Ea2pYjNdqRlN-liPb0RBwHtISUdvslP-6HtKVR8XxuCUWQbvGAUjsyQ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Ro9STyv7hGj3ogXyKZfbP2PbYuR0xHL-lLfQByvqemk2Vu8h6qVuBP6hsFmhS7UQi4SqGpYQTAJeeK3MRNIPag-X3mD1VWRWG2fXxTJ8SZn6huKPalz5ssfQLM9catVzchqbMGTbZxzwSD8PWu5rMvmCFrKPcdgZCgEKsuEGsbdQ2EzN1zv5_3RxYH_DEUoY?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/mwFfUwG5GPG8fxyos5VQ_fktgGMfzT4__gxi-bjMADZVHWgV_D8YaQZADWQPk7Gvg3qXqhpvUaXAcxq85XKc0J5s5fJO-Udg6kSbOzcvM4RKLG4-KoYsyZZwELXbkDPgT7ZutxI94tks_dPopy_Ye2XXZn9KL_zJNalM5RMOUIDAJV6W32iorS1g9wiG98XQ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/oL61pnTe6imFGEVL3BdxCfUEURUEHStRos72n_e2JVD9-ApYKG0uexmuQ3xQuydgrrtTVKv11AokN0sgUCp6IwECSUoO2F5lTwxZFXedMOJaaHx-xHF2WpyDlr9yNghV03CwVlmO7jaWctF2m9qZ0J5LkKvyXwSjADWZyZMqG5H02MS9mzOmW81PmGLhGpkj?purpose=fullsize)

In **non-scanning imaging**, the sensor captures the **entire image at once**, similar to a digital camera.

### Characteristics

* No line-by-line scanning.
* Faster image capture.
* Common in aerial photography and drones.

### Advantages

* High spatial resolution
* Less geometric distortion
* Simple image acquisition

### Disadvantages

* Covers a smaller area than scanning sensors.

---

# 7. Thermal Remote Sensing

![Image](https://images.openai.com/static-rsc-4/-Py7poX1kgkSCWTqwrA9g0sL83OeeMDRURAAw7wBnf9zsbOz45l7Oq-9KJrZSf4or-PYzrjUjZHFAJl8L9RgHy-hW0-7nqQ5e9vLkDusmLanQ3SepKN1BoRkT6vMRodg_PRq1NJru-mAdlYMEz8y5QM8-6GWoowRQlt0J2G_kZpjZ3LK0hO65f0xT2fJ2mNP?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/eXVdG5t3k-OKxhMuJNkAoFB56pIKEuNhsEOkpWntIqiMUcdKsbc1D45ZR93hCSTNgMR_Q8Um2MY3Xhr_juBnSx4UTS1yb-HaYISvFU29HCG8a-CnAxWEB-IL6noQBZ607-W7XEtABQJYiLoFtBAiRjR2dkZ3eGs1wT58FHTUPdsZykfpFxSB0J6AQUINoeR4?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/51kd890SEGUNQKYV6q3Cv30wvahs_WooEDgBwS1o32gHU-P_UKj02Zd8Qwy3ixEYnb-SsWj65gvyug1E27a2bkoCQGwcCzynswJQ-7sBsqpSlUMROyJaFIEXHcbdiONVSez2sZpfChlj1DakbOO0tKYt-rd6egG3YBR8cQF2XxcsZAEoXu8NXTGnU6Tp_23z?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Vhu-Dsk5Q7E7zvBGEXckXLu9gcyVvHG-i8QUzPHtAr5TTihWUqvXF2FZhDFkjAFroo4EHrHRVkkhDHuevUXkB1rANCywmJJO1oXnyuiKBCd8AmLmc6_yDbBFdHYYN99-6fYzXStmBdOcK4lga69XThaJQS7Y0gYHbx_nlDvwuvE-A7DJcNuTQMC7ophtapv4?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/tpO82ZfOczfkIKfiVVeRms94tSDNxIRORZl3q6_ewBlnF1_IWYRHqLw4sOdVQ5T11_TT7oh7iPDv9VwdAVwaYSzBS5ZsPFq-y7-YGmmL6jLSKOnxo_6QDE-1rXn51su4h98q2iO3Akypg2uZePM-xb0aZno-_XRkmxK4j6402huCOFIKYGbSiwxkCw7iXHbR?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/uUfwFEnJE1LQYrQuV7WBgWBx9Xc1Oo95-9-An4peVG2PpsxEv9RUT1sY5d83IAhzUTqYugMHiqZOLOLeIq39FqTyQ5_yITBEfipKr_B1c84g7JyPEPamka4T2n7M2SAmY7zhv160ssbxytzJDQ2bfEs-9siliBN5UZyGz4c-UsakNmNkuaqXsOpeeOtgNXVx?purpose=fullsize)

Thermal remote sensing detects **thermal infrared radiation emitted by objects**.

Unlike visible sensors, thermal sensors measure **temperature differences**.

### Characteristics

* Works both day and night.
* Measures emitted energy.
* Useful for temperature mapping.

### Applications

* Forest fire detection
* Volcano monitoring
* Urban heat island studies
* Water temperature mapping
* Industrial heat leakage
* Drought monitoring

---

## Advantages

* Operates at night.
* Detects temperature differences.
* Useful for disaster monitoring.

---

## Limitations

* Lower spatial resolution.
* Affected by atmospheric conditions.
* Difficult to distinguish objects with similar temperatures.

---

# 8. Other Sensors

Besides optical and thermal sensors, remote sensing uses several specialized sensors.

## Radar (Radio Detection and Ranging)

* Active sensor.
* Uses microwave energy.
* Works day and night.
* Can penetrate clouds.

Applications:

* Flood mapping
* Forest monitoring
* Surface deformation studies

---

## LiDAR (Light Detection and Ranging)

* Active sensor.
* Uses laser pulses.
* Produces accurate elevation data.

Applications:

* Digital Elevation Models (DEM)
* Forest height measurement
* Urban 3D mapping

---

## Microwave Sensors

* Use microwave radiation.
* Can operate in all weather conditions.

Applications:

* Ocean monitoring
* Soil moisture estimation
* Ice and snow mapping

---

# Comparison of Major Sensor Types

| Sensor        | Active/Passive | Main Use                  |
| ------------- | -------------- | ------------------------- |
| Optical       | Passive        | Land cover mapping        |
| Thermal       | Passive        | Temperature measurement   |
| Radar         | Active         | Cloud-penetrating imaging |
| LiDAR         | Active         | Elevation and 3D mapping  |
| Hyperspectral | Passive        | Material identification   |

---

# Advantages of Digital Imaging

* High accuracy
* Easy storage and transmission
* Computer-based analysis
* Multi-band imaging
* GIS compatibility
* Image enhancement and classification
* Long-term digital archive

---

# Limitations of Digital Imaging

* Large storage requirements
* Expensive sensors
* Requires skilled processing
* Sensitive to atmospheric effects (optical sensors)
* Complex software needed

---

# Frequently Asked Exam Questions (Unit 4)

1. Define a digital image. Explain its components.
2. What is a sensor? Explain passive and active sensors.
3. Explain imaging by scanning techniques.
4. Differentiate between whiskbroom and pushbroom scanners.
5. What is hyperspectral imaging? Mention its applications.
6. Explain imaging by non-scanning techniques.
7. Describe thermal remote sensing with its applications.
8. Write short notes on Radar and LiDAR.

---

# Quick Revision (1-Minute Summary)

* **Digital Image:** Grid of pixels with Digital Number (DN) values.
* **Sensor:** Detects EM radiation and converts it into digital data.
* **Whiskbroom Scanner:** Rotating mirror; scans across the satellite path.
* **Pushbroom Scanner:** Linear detector array; scans along the satellite path.
* **Hyperspectral Imaging:** Hundreds of narrow spectral bands for detailed material identification.
* **Non-Scanning Technique:** Captures the whole image at once.
* **Thermal Remote Sensing:** Measures emitted infrared radiation to detect temperature.
* **Radar:** Active microwave sensor; works day/night and through clouds.
* **LiDAR:** Active laser sensor; used for precise elevation and 3D mapping.

**Exam tip:** The highest-priority topics in Unit 4 are **Whiskbroom vs Pushbroom scanning**, **Hyperspectral Imaging**, **Thermal Remote Sensing**, and **Radar vs LiDAR**. These are the most commonly tested concepts in theory exams.
