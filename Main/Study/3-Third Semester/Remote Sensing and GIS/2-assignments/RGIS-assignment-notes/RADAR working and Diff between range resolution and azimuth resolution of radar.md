#assignment #RGIS #third-semester 
## Steps of RADAR Working

1. **Transmission of Pulse**
   Radar transmits short bursts of electromagnetic waves toward a target using an antenna.

2. **Propagation Through Atmosphere**
   The radar waves travel through space at the speed of light.

3. **Reflection from Target**
   When the waves hit an object (aircraft, terrain, ship, etc.), part of the energy is reflected back.

4. **Reception of Echo**
   The radar antenna receives the reflected signal (echo).

5. **Signal Processing**
   The received echo is amplified and processed to determine target information.

6. **Measurement of Range**
   Distance is calculated from the time delay between transmission and reception:

$$   R=\frac{ct}{2}$$

   where:

   * $R$ = range
   * $c$ = speed of light
   * $t$ = round-trip travel time

7. **Display of Target Information**
   Radar displays target position, distance, direction, and sometimes velocity.

---

# Difference Between Range Resolution and Azimuth Resolution

| Feature     | Range Resolution                                                     | Azimuth Resolution                                                            |
| ----------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Definition  | Ability to distinguish two targets at different distances from radar | Ability to distinguish two targets at the same range but different directions |
| Depends On  | Pulse duration (or bandwidth)                                        | Antenna beamwidth                                                             |
| Direction   | Along radar line of sight                                            | Perpendicular to radar line of sight                                          |
| Improved By | Shorter pulse duration                                               | Larger antenna length                                                         |
| Formula     | $\Delta R=\frac{c\tau}{2}$                                           | $\Delta A=\frac{R\lambda}{L}$                                                 |

where:

* $\tau$ = pulse duration
* $\lambda$ = wavelength
* $L$ = antenna length
* $R$ = target distance

---

# Numerical Problem

### Given

* Pulse duration:
  $\tau=0.5\ \mu s =0.5\times10^{-6}\ s$

* Wavelength:
  $\lambda=0.04\ m$

* Antenna length:
  $L=2\ m$

* Target distance:
  $R=15\ km=15000\ m$

* Speed of light:
  $c=3\times10^8\ m/s$

---

## 1. Range Resolution

Formula:

$$\Delta R=\frac{c\tau}{2}$$

Substituting values:

$$
\Delta R=\frac{(3\times10^8)(0.5\times10^{-6})}{2}
$$

$$
\Delta R=\frac{150}{2}
$$

$$
\Delta R=75\ m
$$

### Range Resolution = **75 m**

---

## 2. Azimuth Resolution

Formula:

$$\Delta A=\frac{R\lambda}{L}$$

Substituting values:

$$
\Delta A=\frac{(15000)(0.04)}{2}
$$

$$
\Delta A=\frac{600}{2}
$$

$$
\Delta A=300\ m
$$

### Azimuth Resolution = **300 m**

---

# Final Answers

* **Range Resolution = 75 m**
* **Azimuth Resolution = 300 m**
