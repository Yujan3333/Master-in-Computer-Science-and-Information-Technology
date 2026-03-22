# Simple Image Formation Model

*(Based on Digital Image Processing)*

---

# 1. Basic Definition

A digital image is represented as a 2D function:

$$f(x,y)$$

* $(x,y)$ → spatial coordinates
* $f(x,y)$ → intensity (gray level) at that point
* Intensity is proportional to **energy from a physical source**

---

# 2. Basic Condition

Image intensity must be:

$$0\le f(x,y)<\infty$$

* Always **non-negative**
* Always **finite**

---

# 3. Components of Image Formation

An image is formed by two components:

### (a) Illumination $i(x,y)$

* Light incident on the scene
* Depends on source (sun, lamp, etc.)

$$0\le i(x,y)<\infty$$

---

### (b) Reflectance $r(x,y)$

* Fraction of light reflected by objects
* Depends on surface properties

$$0\le r(x,y)\le1$$

* 0 → total absorption (black)
* 1 → total reflection (white)

---

# 4. Image Formation Equation

The image is formed as:

$$f(x,y)=i(x,y)\cdot r(x,y)$$

👉 Image = Illumination × Reflectance

---

# 5. Interpretation

* Bright image → high illumination or high reflectance

* Dark image → low illumination or low reflectance

* Illumination → controlled by source

* Reflectance → controlled by objects

---

# 6. Intensity (Gray Level Range)

Let intensity be:

$$l=f(x,y)$$

Then:

$$L_{min}\le l\le L_{max}$$

* $L_{min}$ → minimum intensity (black)
* $L_{max}$ → maximum intensity (white)

👉 This range is called **gray scale**

---

## Practical Representation

Usually scaled to:

* $[0,1]$ OR
* $[0,L-1]$ (e.g., 0–255 in 8-bit images)

---

# 7. Key Points for Exams

* Image is a function: $f(x,y)$
* Must satisfy: $0\le f(x,y)<\infty$
* Formed by:
  $$f(x,y)=i(x,y)\cdot r(x,y)$$
* Reflectance range: $0$ to $1$
* Gray level range: $L_{min}$ to $L_{max}$
* Common scaling: $[0,1]$ or $[0,255]$

---
