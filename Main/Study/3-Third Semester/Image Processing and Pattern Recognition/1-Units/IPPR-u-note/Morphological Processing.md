#ippr #third-semester 

Erosion and dilation are the two basic operations in **morphological image processing** — used mainly on binary (black & white) images to shrink, grow, or reshape objects using a small shape called a **structuring element (SE)**.

## Structuring Element (SE)
A small matrix (e.g., 3×3) with a defined origin, used as a "probe" that slides over the image. Common shapes: square, cross, disk.

## Dilation
**Definition:** Dilation *grows* or *thickens* objects in a binary image.

**Formula:**
$$A \oplus B = \{z \mid (\hat{B})_z \cap A \neq \emptyset\}$$

**Rule:** Place the structuring element B at every pixel position; if **any** part of B overlaps a foreground (1) pixel of A, the origin pixel becomes 1 (foreground) in the output.

**Effect:**
- Fills small holes and gaps
- Bridges narrow breaks
- Expands boundaries of objects
- Increases object size

## Erosion
**Definition:** Erosion *shrinks* or *thins* objects in a binary image.

**Formula:**
$$A \ominus B = \{z \mid (B)_z \subseteq A\}$$

**Rule:** Place B at every pixel position; the origin pixel stays 1 only if **all** pixels of B fit entirely within the foreground region of A. Otherwise it becomes 0.

**Effect:**
- Removes small noise/protrusions
- Shrinks object boundaries
- Can break thin connections between objects
- Decreases object size

Let me show you this visually with a worked example on a small grid — it makes the "grows vs shrinks" difference much clearer than words alone.This example uses a solid 3×3 square as the original foreground region and a 3×3 structuring element:

- **Dilation** grows it by one pixel in every direction — the new boundary sits outside the dashed outline of the original.
- **Erosion** shrinks it by one pixel in every direction — since the square was only 3×3, everything except the exact center pixel gets stripped away.

## Why this matters (typical exam angle)
- **Duality:** Erosion of A by B is equivalent to the complement of dilation of the complement of A: $(A \ominus B)^c = A^c \oplus \hat{B}$.
- **Applications:** Dilation is used to fill gaps/connect broken parts; erosion is used to remove noise and thin objects. Combined, they give you **opening** (erosion then dilation — removes small protrusions/noise, keeps overall shape) and **closing** (dilation then erosion — fills small holes/gaps, keeps overall shape).
- Both are directly connected to **pattern recognition** because these operations clean up shapes before feature extraction/classification — which is likely why Preboard-83 paired them in a single question.

---
# Morphological Processes in Digital Image Processing

Morphological processing is a technique used to process **binary and grayscale images** based on their **shape**. It uses a small pattern called a **structuring element (SE)** to modify objects in an image.

The two basic morphological operations are:

1. **Dilation**
2. **Erosion**

---

## 1. Dilation

### Definition

**Dilation** adds pixels to the boundaries of objects, making them **grow larger**.

### Purpose

* Expands objects
* Fills small holes
* Connects nearby objects
* Repairs broken boundaries

### Operation

For a binary image (A) and structuring element (B),

$$[
A \oplus B
]$$

where:

* (A) = input image
* (B) = structuring element
* ($\oplus$) = dilation operator

### Example

Original image

```
0 0 0 0 0
0 1 1 0 0
0 1 1 0 0
0 0 0 0 0
```

After dilation

```
0 1 1 1 0
1 1 1 1 1
1 1 1 1 1
0 1 1 1 0
```

The object becomes **thicker**.

### Applications

* Connecting broken characters
* Filling gaps
* Increasing object size
* Joining nearby objects

---

## 2. Erosion

### Definition

**Erosion** removes pixels from the boundaries of objects, making them **smaller**.

### Purpose

* Removes small noise
* Separates connected objects
* Shrinks objects
* Eliminates thin protrusions

### Operation

$$[
A \ominus B
]$$

where:

* (A) = input image
* (B) = structuring element
* ($\ominus$) = erosion operator

### Example

Original image

```
0 0 0 0 0
0 1 1 0 0
0 1 1 0 0
0 0 0 0 0
```

After erosion

```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```

Using a (3 \times 3) structuring element, the small object disappears because it is too small to fully contain the structuring element.

### Applications

* Removing noise
* Separating touching objects
* Thinning objects
* Eliminating small unwanted details

---

## Difference Between Dilation and Erosion

| Dilation                | Erosion                     |
| ----------------------- | --------------------------- |
| Adds pixels             | Removes pixels              |
| Object grows            | Object shrinks              |
| Fills small holes       | Removes small objects/noise |
| Connects nearby objects | Separates connected objects |
| Expands boundaries      | Contracts boundaries        |

---

## Exam Answer (5 Marks)

**Morphological processing** is a shape-based image processing technique that uses a **structuring element** to modify objects in an image.

### Dilation

* Adds pixels to object boundaries.
* Makes objects larger.
* Used to fill holes, connect nearby objects, and repair broken boundaries.
* Formula:
$$  [
  A \oplus B
  ]$$

### Erosion

* Removes pixels from object boundaries.
* Makes objects smaller.
* Used to remove noise, separate connected objects, and shrink objects.
* Formula:
$$  [
  A \ominus B
  ]$$

**Key Difference:** Dilation expands objects, whereas erosion shrinks them.
