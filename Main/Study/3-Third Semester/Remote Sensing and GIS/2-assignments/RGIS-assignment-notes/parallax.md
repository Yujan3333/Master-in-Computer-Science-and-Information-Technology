#rgis #third-semester 
# Parallax in Photogrammetry

## Definition

**Parallax** is the **apparent shift in the position of an object when it is viewed from two different locations or angles**.

In photogrammetry, parallax is the **difference in the image position of the same ground point in two overlapping aerial photographs**.

It is the basic principle used to determine the **height (elevation)** of objects.

---

## Simple Example

Hold your finger in front of your face.

* Close your **left eye** and look at your finger.
* Now close your **right eye** and open the left eye.

Your finger appears to **shift its position** relative to the background.

This apparent shift is called **parallax**.

---

## In Photogrammetry

Two overlapping aerial photographs are taken from different camera positions.

```text id="jndsy3"
Camera 1          Camera 2
    ●----------------●
      \            /
       \          /
        \        /
         \      /
          \    /
           \  /
            P
```

The same ground point **P** appears at different positions in the two photographs.

The distance between these two image positions is called **parallax**.

---

## How Parallax is Used

The amount of parallax is related to the height of the object.

* **Higher objects** (buildings, trees, hills) → **Larger parallax**
* **Lower objects** (flat ground) → **Smaller parallax**

The software measures this parallax to calculate the elevation of each point.

---

## Example

Suppose two aerial photographs capture the same building.

```text id="l4fqgd"
Left Photo             Right Photo

     Building               Building
        ▲                      ▲
        │                      │
        ●                      ●

Different image positions
```

The difference in the building's image position is the **parallax**.

From this difference, the building's height can be calculated.

---

## Importance of Parallax

* Determines the elevation (height) of ground points.
* Creates **3D terrain models**.
* Generates **DEM** and **DTM**.
* Produces contour maps.
* Supports topographic mapping.

---

## Advantages

* Accurate height measurement.
* Enables 3D visualization of terrain.
* Essential for automatic DEM/DTM generation.
* Reduces the need for extensive ground surveys.

---

## Limitations

* Requires overlapping stereo images.
* Accuracy depends on image quality and camera orientation.
* Difficult in water bodies, dense forests, and low-texture areas.

---

# Exam Definition (2 Marks)

> **Parallax** is the **apparent displacement of the same object in two overlapping aerial photographs due to different camera positions. It is used to determine the elevation (height) of objects and terrain in photogrammetry.**

---

# Short Exam Answer (5 Marks)

**Parallax** is the apparent shift in the position of the same ground object when viewed in two overlapping aerial photographs taken from different camera positions. The amount of parallax is directly related to the object's elevation: **higher objects have greater parallax, while lower objects have smaller parallax**. By measuring parallax, photogrammetric software calculates the **3D coordinates (X, Y, Z)** of ground points, which are then used to generate **DEMs, DTMs, contour maps, and other topographic products**.

---

## Memory Trick

Think of traveling in a car:

* **Nearby trees** seem to move **quickly** relative to the background.
* **Distant mountains** seem to move **slowly**.

This apparent movement is **parallax**. In photogrammetry, the same idea is used with **two overlapping aerial images** to measure the **height of the terrain**.
