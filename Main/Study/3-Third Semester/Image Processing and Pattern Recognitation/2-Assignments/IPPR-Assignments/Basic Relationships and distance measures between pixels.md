
# 1. Basic Relationships Between Pixels

In digital image processing, understanding how pixels relate to each other is essential for tasks like segmentation, edge detection, and object recognition.

## (a) Neighbors of a Pixel

Let a pixel be at position $(x,y)$.

### 1. 4-neighbors ($N_4$)

Pixels that share a side with $(x,y)$:

$$N_4(x,y)={(x+1,y),(x-1,y),(x,y+1),(x,y-1)}$$

---

### 2. Diagonal neighbors ($N_D$)

Pixels that touch at the corners:

$$N_D(x,y)={(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)}$$

---

### 3. 8-neighbors ($N_8$)

Combination of 4-neighbors and diagonal neighbors:

$$N_8(x,y)=N_4(x,y)\cup N_D(x,y)$$

---

## (b) Adjacency

Adjacency defines whether two pixels are considered “connected”.

### 1. 4-adjacency

Two pixels are 4-adjacent if one is in $N_4$ of the other.

---

### 2. 8-adjacency

Two pixels are 8-adjacent if one is in $N_8$.

---

### 3. m-adjacency (mixed adjacency)

Used to remove ambiguity in 8-adjacency:

Two pixels are m-adjacent if:

* They are in $N_4$, OR
* They are in $N_D$ **and** their common 4-neighbors are not in the set

👉 Helps avoid multiple connection paths.

---

## (c) Connectivity

Connectivity determines whether a group of pixels forms a region.

* A set of pixels is **connected** if there exists a path between every pair of pixels.
* Types:

  * 4-connected
  * 8-connected
  * m-connected

---

## (d) Regions and Boundaries

* **Region**: A connected set of pixels with similar properties (e.g., intensity)
* **Boundary**: Pixels that separate regions

---

# 2. Distance Measures Between Pixels

Distance measures quantify how far two pixels are from each other.

Let two pixels be:
$$(x,y)\text{ and }(s,t)$$

---

## (a) Euclidean Distance

The straight-line distance:

$$D_E=\sqrt{(x-s)^2+(y-t)^2}$$

✔ Most accurate
❌ Computationally expensive

---

## (b) City Block Distance (D4 distance)

Also called Manhattan distance:

$$D_4=|x-s|+|y-t|$$

✔ Movement allowed only in horizontal and vertical directions
✔ Used with 4-adjacency

---

## (c) Chessboard Distance (D8 distance)

Maximum of coordinate differences:

$$D_8=\max(|x-s|,|y-t|)$$

✔ Movement allowed in all 8 directions
✔ Used with 8-adjacency

---

# Summary Table

| Concept      | Description                         |
| ------------ | ----------------------------------- |
| $N_4$        | 4-neighbors (up, down, left, right) |
| $N_D$        | Diagonal neighbors                  |
| $N_8$        | All surrounding pixels              |
| Adjacency    | Defines direct connection           |
| Connectivity | Defines connected regions           |
| $D_E$        | Euclidean distance                  |
| $D_4$        | City block distance                 |
| $D_8$        | Chessboard distance                 |

---

# Key Exam Points (Very Important)

* $N_8 = N_4 + N_D$
* m-adjacency removes ambiguity in diagonal connections
* $D_4$ → 4-direction movement
* $D_8$ → 8-direction movement
* Euclidean distance is the most natural but costly

---
