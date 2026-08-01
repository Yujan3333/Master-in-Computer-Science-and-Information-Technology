#ippr #third-semester 

# Hough Transform

## Definition

The **Hough Transform** is a feature extraction technique used to **detect geometric shapes** (such as **lines, circles, and ellipses**) in an image.

It works by transforming points in the **image (spatial) domain** into a **parameter space**, where shapes can be identified by finding peaks (maximum votes).

It is widely used in **edge detection**, **computer vision**, and **image analysis**.

---

# Need for Hough Transform

Suppose an edge image contains broken or noisy lines.

Normal edge detection only finds edge pixels.

The Hough Transform groups these edge pixels together to detect the complete line or shape.

---

# Principle

A straight line is usually written as

$$
y=mx+c
$$

However, this form fails for **vertical lines** because the slope becomes infinite.

Therefore, the Hough Transform uses the **polar form** of a line:

$$
\rho=x\cos\theta+y\sin\theta
$$

where

* $\rho$ = Perpendicular distance from the origin to the line
* $\theta$ = Angle between the perpendicular and the x-axis

---

# Working Procedure

### Step 1: Detect Edges

Use an edge detector (e.g., Sobel or Canny) to obtain edge pixels.

---

### Step 2: Transform to Parameter Space

For every edge pixel $(x,y)$, compute all possible values of

$$
\rho=x\cos\theta+y\sin\theta
$$

for different values of $\theta$.

Each edge pixel votes for possible lines.

---

### Step 3: Voting

Store votes in an **accumulator array**.

If many edge pixels vote for the same $(\rho,\theta)$, it indicates the presence of a line.

---

### Step 4: Detect Peaks

Find the peaks (maximum votes) in the accumulator.

Each peak corresponds to a detected line.

---

# Block Diagram

```text
Input Image
      │
      ▼
Edge Detection
      │
      ▼
Hough Transform
      │
      ▼
Accumulator Array
      │
      ▼
Peak Detection
      │
      ▼
Detected Lines
```

---

# Example

Suppose three edge points lie on the same line.

```
Image Space

•
    •
        •
```

Each point is transformed into a curve in parameter space.

```
Parameter Space

\      /
 \    /
  \  /
   ●
```

The curves intersect at one point.

That intersection represents the detected line.

---

# Advantages

* Detects lines even when edges are broken.
* Robust to image noise.
* Can detect multiple lines simultaneously.
* Can also detect circles and ellipses.

---

# Disadvantages

* Computationally expensive.
* Requires large memory for the accumulator.
* Accuracy depends on parameter resolution.

---

# Applications

* Lane detection in autonomous vehicles.
* Road and railway detection in satellite images.
* Medical image analysis.
* Document analysis.
* Shape recognition.
* Computer vision.

---

# Exam Answer (5 Marks)

**Definition:**
The **Hough Transform** is a feature extraction technique used to detect geometric shapes such as **lines, circles, and ellipses** in an image by transforming image points into a parameter space.

The equation of a line in Hough space is

$$
\rho=x\cos\theta+y\sin\theta
$$

where $\rho$ is the perpendicular distance from the origin and $\theta$ is the angle of the normal to the line.

**Working:**

1. Detect edges in the image.

2. Transform each edge point into the parameter space using

   $$
   \rho=x\cos\theta+y\sin\theta
   $$

3. Store votes in an accumulator array.

4. Find peaks in the accumulator.

5. Each peak corresponds to a detected line.

**Applications:**

* Line detection
* Circle detection
* Lane detection
* Medical imaging
* Computer vision

---

## Memory Trick

Think of the Hough Transform as a **voting system**:

* Every **edge pixel votes** for all the lines that could pass through it.
* The line that receives the **most votes wins** and is identified as the actual line in the image.

This "voting" concept is the key idea to remember for exams.
