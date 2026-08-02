#rgis #third-semester 

# Unit 5: Microwave Remote Sensing (Overview)

**Exam Weight:** 4 Hours (Theory)

This chapter explains **microwave remote sensing**, one of the most important techniques in remote sensing because it can operate **day and night** and is **less affected by weather conditions**. It covers passive and active microwave sensing, radar imaging, airborne and space-borne radars, and radar systems.

---

# 1. Introduction

**Microwave remote sensing** uses **microwave electromagnetic waves** (approximately **1 mm to 1 m wavelength**) to collect information about the Earth's surface.

Unlike visible light, microwaves can:

* Pass through clouds
* Operate at night
* Penetrate rain, fog, and smoke (to some extent)

This makes microwave remote sensing ideal for all-weather monitoring.

---

# Characteristics of Microwaves

* Long wavelength
* Less affected by atmospheric conditions
* Can penetrate clouds
* Can operate day and night
* Sensitive to surface roughness and moisture

---

# Applications

* Flood monitoring
* Soil moisture estimation
* Ocean observation
* Ice and snow mapping
* Forest monitoring
* Disaster management
* Military surveillance

---

# 2. Passive Microwave Remote Sensing

Passive microwave sensors **do not transmit energy**. They detect the **natural microwave radiation** emitted by the Earth's surface.

## Working Principle

```text
Earth Surface
      │
 Natural Microwave Emission
      │
      ▼
 Passive Sensor
      │
      ▼
   Data
```

### Characteristics

* Uses natural microwave emission.
* Low energy requirement.
* Lower spatial resolution than active systems.

### Advantages

* Simple system
* Lower cost
* Measures natural emissions

### Limitations

* Weak signals
* Lower image quality
* Limited spatial resolution

### Applications

* Soil moisture
* Sea surface temperature
* Atmospheric studies
* Snow monitoring

---

# 3. Active Microwave Remote Sensing

Active microwave sensors **generate their own microwave energy**, send it toward the Earth's surface, and record the reflected signal.

## Working Principle

```text
Radar Sensor
      │
 Microwave Pulse
      ▼
Earth Surface
      │
 Reflected Signal (Backscatter)
      ▼
 Radar Sensor
```

### Characteristics

* Generates its own energy.
* Works day and night.
* Can image through clouds.

### Advantages

* High resolution
* Weather independent
* Measures distance and elevation

### Limitations

* Expensive
* Complex data processing
* Speckle noise in images

### Applications

* Flood mapping
* Earthquake monitoring
* Topographic mapping
* Forest studies
* Military reconnaissance

---

# Passive vs Active Microwave Remote Sensing

| Passive                            | Active                         |
| ---------------------------------- | ------------------------------ |
| Detects natural microwave emission | Emits its own microwave energy |
| No transmitter                     | Has transmitter and receiver   |
| Lower spatial resolution           | Higher spatial resolution      |
| Simple system                      | Complex system                 |
| Example: Microwave Radiometer      | Example: Radar (SAR)           |

---

# 4. Radar Imaging

![Image](https://images.openai.com/static-rsc-4/Y5gUqPfFP6gck4cLCSNA0dwQRH9MpcAKmPn0cv7k-oZq11lGihfdfAaXb8GL_Gy_UMh4_CyaFU9z-Zuw2uHnoG43jUbsqkQBKMkAELrqYJFQF6dJuHDKa7zwKJEkU1LeTO7c7DpoK9nO0GX6oC3mp36vKhRdbA29oQyyq02i-et9tXCCyIHvjWxqTyXGR4pi?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/MpwhaUym2K_UThQJzVlaAXElylwen6KLtiwOUWL5s_wa83tzrwNqMmJPPF_4bePw-Lh2mLlgRIz3SmKRh9gsQucHNEcImnpg1Ur2REudh7sQK3aTe_8nK09XsBTd9y3uhzbH6joVoRYbkUQfOQED_syO3mROGKBLkPIianFrj1poJF-j6J2o6xeYzOMhUs1w?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/UU9CZGvU5LSitZr9J-D1ToS3sUPc4zbpLn_gSzxavJJLS5_TSvc07aMFLi3_4JIT4o9a2DXlkmsl0hGwoKSOvZTAM2ilLyfjEZgpMsMEcYzwGYedmPuY3azdpCj4v8fMBlEFfRF_3dKQjEc2B1y1PqulNe4bw3ZoHkQgDHbI4WU6Qw8yRsOzsZzY05Um7FEQ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/uCy8cWYkd2Jt1BwRikWeiX8bkM0CTVeOERb3ZqbHjEvVNF1RA6jdEmYfXjEGCGLWjd0nblr8Ek1DC5fhZN3FHNn6fp6GZmeYVtla1FgVicahwxegBPCh1_LtG3lHf5-3-vfr_Z1Xz8vq7ZQh1oTvANAw7jJL1v9IgsbbZlzmGidXcFmqHER91PRunW-dNpNP?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ZdDHQ4fYCOA7P1lgekikxugVSDVRDEHzeW9u3ynlnYoL3gm5Rs4886DQdlaEcrc1xyOZdLr3GZFupZwi4PJJxawMmzDGrAeJ7TCJDk6S-4LFCigV4wojujsVqbdF3pAJghEi3nA7xhxBl3uFXZHZRoIW_yGdxniyJ7AH36u3vAK78-MZ2O5vW-RBup25aZSU?purpose=fullsize)

**Radar (Radio Detection and Ranging)** is the most widely used active microwave remote sensing system.

It works by:

1. Transmitting microwave pulses.
2. The pulses hit the Earth's surface.
3. Objects reflect part of the energy.
4. The radar receives the reflected signal (**backscatter**).
5. A radar image is formed.

---

## Backscatter

**Backscatter** is the portion of microwave energy reflected back toward the radar sensor.

The amount of backscatter depends on:

* Surface roughness
* Moisture content
* Shape of objects
* Angle of incidence

---

## Bright and Dark Areas in Radar Images

* **Smooth surfaces (water):** Reflect energy away from the sensor → appear **dark**.
* **Rough surfaces (buildings, forests):** Reflect more energy back → appear **bright**.

---

# Advantages of Radar Imaging

* Works day and night.
* Not affected by clouds or fog.
* Can monitor floods during storms.
* Detects surface roughness.
* Provides information about terrain.

---

# Limitations of Radar Imaging

* Speckle noise
* Geometric distortions (foreshortening, layover, shadow)
* Complex image interpretation

---

# 5. Airborne vs Space-borne Radars

## Airborne Radar

![Image](https://images.openai.com/static-rsc-4/EEtHDEMGePp_cdi2twn76PKNp57I1R1IHAzzxf-CLL2bMAvemyeFL1cu3asPiluamXJ7xIV5uoL7uazorb8QNPbI4bEyJHqplPWViAjzQPoMQVB_pvOaeimhrjW1rnWd_Kdki3jKv9ztO6NY9TvLRDJljiMbhe4LorDIN_5mRTLeZj3h2HbtJtxslMgwFWzD?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/F16t7hJssZpvDTbyhGb93_-VYBuIVHZi1bb1R99XulKu-yJsasS2btaJZGMRxiZ4iKlo3cwZTfeKV96QQOmZn_BWwI1wCC2nmg9FHO9R1vDMqfa3rEkdTBX6McRilABeDe4dsSYw_SVzzHmPRDN4fmjmIIjOBH68PxCYJlZawzPNjbIoEHB04GX4OEaFEGBR?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/-Oi2in1mXIS-MrJkU98kt5QnZIeM4pVpjdD7NmwIQj95ZukBNQFijCB-hQaKq01ZnWs72TkMTIFvlYKDDEGJdumn5bmxNPONi3nXI6NAJ5ErzMeWiDH9c--grJWYdsKBQ2v45hICi8TwAQqYBB5Sew6OrYG0X-5_yz0Y634fTTjoPKNV2b81Cy6_ko2NG1_U?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/vi4KoV4W_e0oCtE14rccNHsqOqycmlLC0TaraIpxN9cSJoHGsknIqy4Xyranm4824pFl6alcA5kEV0Qz8f19lvTwx5DhiOOquPusvZ8O0yLDaWbPrG5a1RAgzoMtpOWF2vsUKTQIJI7GCB2ilHuZLZXMQOGRmdO5vH7zWYikrflFXEa_yb-pXJAlN4jR0ESL?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/QHbx4gN79I2E7lIbXL65vfN_aU8qcE_W-jYU1qhEU8QSiANJi7IQ4kNkpjHhFp0nVt_gzCt_DS_qeqmrE-TTMFdByQ_gc5UKX4uYXi37Lv7UrIGmIxGj5PEw5lsCG7Xx_2dkj1d1Omo_EVI-7uDa4pRfAUpRMB_xNvHGbFFt3hZ91jEOLL2TSgqGT0Cod3Vg?purpose=fullsize)

Radar mounted on an aircraft.

### Characteristics

* Low altitude
* Small coverage
* High spatial resolution
* Flexible data collection

### Applications

* Local surveys
* Disaster assessment
* Engineering projects

---

## Space-borne Radar

![Image](https://images.openai.com/static-rsc-4/L15zHGJqHBXnBCJ6HnR10iMFCn1Kz5fdlUD39T-ivqv09WJA1XVfkeyKOVozCt6LOyjTqW_cewR74x5yJq6pqfx5Whk5cyl9p9gzPI3Fbj3JvHL64F02VDDX20iQYYSoRm4wNyUzE2jFkM0hbb1KLEr50oqbeZeDtAjCLc5pBtFl_vLeVWVfZBW2wtApeGTI?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/3wcOZDh8eH9jSClWA3B8iGZONBejFLn237Q-zV_tob5dI7NfH4P2fcegyjTnNbBPs6_2PV0kvPzPgr3miGsiHIuWbXmbB4x_aJQNXjxjwiWinvm6lOXQXIJzP1u9ue6cngAM16KoOhM0mI9RdPwb613etRw0ZGqT-TiB6CfnM8FvCcv6nhoGqNkPLMtAyQuP?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/WOkGCetNc00Oue_jc0PbkUbrX37Z0_4FkM6hOuQRSyPxTCfa0Aq90TRy9vGQdjIWuDHEpDkw9DxgIX8q2R4CVx4GbFI5wGmk8GFpZV978-TKbpTyLFvy8huXnxA_iTonfmT5JTLYUuW9UQP72787wkYkHWxlrth0fcDzXTihMvv5AQgQEEmWJ9rHZcRKDwmC?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/zapIjABnRabmu1GpYydIq18cpP1HKBxfXbZ9XV8KD9tzdH7Nwwbg4N5hRJ3rkBY67VV996y8bEwpfoQfcrXGV5nP2lssTG-d7nAhp5Fdta4PbMRnqJn1f6gsl62r52YwiHU8gq8bM4puSyUObSxm_pNSOl3g3mkcpesaA4okqkCwfXDpY-Jkg-EevLkAePe3?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/67Cku3WoRoGeXuaVBcUxOrbWis0Yats6Yv3EdG_xeRPujD_-U2AeHJSoBYsk3zJgJtSVpaLzWjMMj7Xe07Mi7862AH01KTv685Eutj1dHDfhHX76H74e2xty3Ny5UDa1MJE4qerJNXt3ajkiL5fOIqkTNOy-cUZPXYT8-vvZ5WsewdEeEIO4J5EmTveDRsSy?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/4HmElX8gRov0Z9XvcCycOwh3FGX91QWPVWbdjSPVLmsq_lmtAkR5OEEeybKd35MapHOzyrFwWEgXPW8-BFOiFe6YwChYInRWEpHXZYX-AQ8W02kUrpcAmBbTG5y_gweE0NMXj-APg9-rE5LIfPcmyyeS16IhGZqO1UWiCp7Wcls6Ac8QxmEytNdFT_Ct-0Us?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/mf17LeUPaG4cxuWG0URJJOLYubvgcBirkRxN-n_FCgUYfPAHi574v3SkyWspDE_UKPVjmU_dr7TOQcuIXWeCwIdf84X4xAK228poAzXal_f39nloweMn8ajJM8V885Evs1X01ULYhF4Kn5q7JV6qEH1GmG7IxaFsOxQ2Bgy_lkGd68XMWm0WUrbpBUijM5e0?purpose=fullsize)

Radar mounted on a satellite.

### Characteristics

* High altitude
* Large coverage
* Regular observations
* Global monitoring

### Applications

* Agriculture
* Forestry
* Flood monitoring
* Climate studies
* Ocean observation

---

## Airborne vs Space-borne Radar

| Airborne Radar            | Space-borne Radar           |
| ------------------------- | --------------------------- |
| Aircraft platform         | Satellite platform          |
| Low altitude              | High altitude               |
| Small coverage            | Large coverage              |
| Higher spatial resolution | Moderate to high resolution |
| Flexible operation        | Fixed satellite orbit       |

---

# 6. Radar Systems

A radar system consists of several components.

```text
Transmitter
      │
      ▼
Antenna
      │
Microwave Pulse
      ▼
Earth Surface
      │
Backscatter
      ▼
Receiver
      │
Signal Processor
      ▼
Radar Image
```

---

## Main Components

### 1. Transmitter

Produces microwave pulses.

---

### 2. Antenna

Transmits and receives microwave signals.

---

### 3. Receiver

Receives the reflected energy.

---

### 4. Signal Processor

Converts radar signals into usable images.

---

### 5. Display System

Shows the processed radar image.

---

# Types of Radar

## Real Aperture Radar (RAR)

* Physical antenna determines resolution.
* Lower resolution.
* Older technology.

---

## Synthetic Aperture Radar (SAR)

* Uses satellite motion to simulate a very large antenna.
* High spatial resolution.
* Most modern radar satellites use SAR.

Examples:

* Sentinel-1
* RADARSAT

---

## RAR vs SAR

| RAR              | SAR                |
| ---------------- | ------------------ |
| Real antenna     | Synthetic antenna  |
| Lower resolution | Higher resolution  |
| Simple system    | Complex processing |
| Older technology | Modern technology  |

---

# Advantages of Microwave Remote Sensing

* Operates day and night.
* Works in cloudy and rainy conditions.
* Can penetrate clouds and smoke.
* Sensitive to soil moisture.
* Suitable for disaster monitoring.
* Useful for ocean and polar studies.

---

# Limitations of Microwave Remote Sensing

* Expensive instruments.
* Complex image interpretation.
* Speckle noise.
* High data processing requirements.
* Lower visual quality than optical images.

---

# Frequently Asked Exam Questions (Unit 5)

1. What is microwave remote sensing?
2. Differentiate between passive and active microwave remote sensing.
3. Explain the working principle of radar imaging.
4. What is backscatter? What factors affect it?
5. Differentiate between airborne and space-borne radars.
6. Explain the components of a radar system.
7. Compare Real Aperture Radar (RAR) and Synthetic Aperture Radar (SAR).
8. Write the advantages and limitations of microwave remote sensing.

---

# Quick Revision (1-Minute Summary)

* **Microwave Remote Sensing:** Uses microwave wavelengths (about 1 mm–1 m).
* **Passive Microwave:** Detects natural microwave emissions (e.g., radiometers).
* **Active Microwave:** Emits microwaves and measures backscatter (e.g., Radar/SAR).
* **Backscatter:** Reflected microwave energy returning to the radar.
* **Smooth surfaces (water):** Dark in radar images.
* **Rough surfaces (forests/buildings):** Bright in radar images.
* **Airborne Radar:** Aircraft-based, high resolution, small coverage.
* **Space-borne Radar:** Satellite-based, wide coverage, regular monitoring.
* **SAR:** Modern radar system with high spatial resolution.

**Exam tip:** The most frequently asked topics in Unit 5 are **Passive vs Active Microwave Remote Sensing**, **Radar Imaging and Backscatter**, **Airborne vs Space-borne Radar**, and **SAR vs RAR**. These are important for both short-answer and long-answer questions.
