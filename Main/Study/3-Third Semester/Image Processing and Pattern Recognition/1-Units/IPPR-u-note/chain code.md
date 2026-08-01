#ippr #third-semester 

   
   **8.** Define chain code. Find the $8\text{--directional}$ chain code for following image in clockwise direction. Assume the starting position is third pixel from the top starting position.
---
   
   ### **Grid Representation (Figure)**
   
   Legend:
   
   * `1` = Shaded/Foreground Pixel
   * `0` = White/Background Pixel
   
   ```text
   Row \ Col   0  1  2  3  4  5  6  7
   ----------------------------------
   Row  0 |    0  0  1  1  1  1  0  0
   Row  1 |    0  1  1  0  0  1  1  0
   Row  2 |    1  1  0  0  0  0  1  1
   Row  3 |    1  1  0  0  0  0  1  1
   Row  4 |    1  0  0  0  0  1  1  0
   Row  5 |    0  0  0  0  1  1  0  0
   Row  6 |    0  0  0  1  1  0  0  0
   Row  7 |    0  0  1  1  0  0  0  0
   Row  8 |    0  1  1  0  0  0  0  0
   Row  9 |    1  1  0  0  0  0  0  0
   Row 10 |    1  1  0  0  0  0  0  0
   Row 11 |    1  1  1  1  1  1  1  1
   Row 12 |    1  1  1  1  1  1  1  1
   
   ```


```md art

      +----+----+----+----+----+----+----+----+----+----+
      |    |    |    |####|####|####|####|    |    |    |
      +----+----+----+----+----+----+----+----+----+----+
      |    |    |####|####|####|####|####|####|    |    |
      +----+----+----+----+----+----+----+----+----+----+
      |    |####|####|    |    |    |    |####|####|    |
      +----+----+----+----+----+----+----+----+----+----+
      |    |####|####|    |    |    |    |####|####|    |
      +----+----+----+----+----+----+----+----+----+----+
      |    |####|    |    |    |    |    |####|####|    |
      +----+----+----+----+----+----+----+----+----+----+
      |    |    |    |    |    |    |####|####|    |    |
      +----+----+----+----+----+----+----+----+----+----+
      |    |    |    |    |    |####|####|    |    |    |
      +----+----+----+----+----+----+----+----+----+----+
      |    |    |    |    |####|####|    |    |    |    |
      +----+----+----+----+----+----+----+----+----+----+
      |    |    |    |####|####|    |    |    |    |    |
      +----+----+----+----+----+----+----+----+----+----+
      |    |    |####|####|    |    |    |    |    |    |
      +----+----+----+----+----+----+----+----+----+----+
      |    |####|####|    |    |    |    |    |    |    |
      +----+----+----+----+----+----+----+----+----+----+
```




   *(Note: The starting pixel specified in the prompt is at **Row 0, Column 2**).*
![](../../../../../../Images/Third_Sem_Images/chain%20code.png)

---

## (a) Define Chain Code **[1 Mark]**

### Definition

A **chain code** is a *boundary representation technique* used to describe the shape of an object by recording the **direction of movement** from one boundary pixel to the next.

Each direction is represented by a number.

It is mainly used for:

* Boundary representation
* Shape analysis
* Object recognition
* Pattern recognition

---

## 8-Directional Chain Code

The standard Freeman 8-directional chain code is

```text
        3   2   1
         \  |  /
      4 -- P -- 0
         /  |  \
        5   6   7
```

| Direction  | Code |
| ---------- | ---- |
| East       | 0    |
| North-East | 1    |
| North      | 2    |
| North-West | 3    |
| West       | 4    |
| South-West | 5    |
| South      | 6    |
| South-East | 7    |

---

## Steps to Find the 8-Directional Chain Code

1. Select the **starting boundary pixel** (as specified in the question).
2. Move **clockwise** along the object's boundary.
3. Record the direction number for each movement.
4. Continue until you return to the starting pixel.

---

## Example

Consider the following square boundary.

```text
■■■
■ □
■■■
```

Suppose we start from the **top-left corner** and move clockwise.

Movement:

* Right → Right
* Down → Down
* Left → Left
* Up → Up

Using the direction table,

* Right = 0
* Down = 6
* Left = 4
* Up = 2

Therefore,

$$
\boxed{0,;0,;6,;6,;4,;4,;2,;2}
$$

is the **8-directional chain code**.

---

## Advantages

* Compact boundary representation.
* Easy to store and transmit.
* Useful for shape matching and object recognition.
* Translation invariant (if the starting point is fixed).

---

## Disadvantages

* Depends on the starting point.
* Sensitive to noise.
* Rotation changes the chain code.

---

## **Exam Answer (5 Marks)**

**Chain Code:**
A chain code is a boundary representation method that represents an object's boundary by recording the direction of movement from one boundary pixel to the next. In the **8-directional chain code**, each movement is assigned a direction number from **0 to 7**.

The direction numbering is:

| Direction  | Code |
| ---------- | ---- |
| East       | 0    |
| North-East | 1    |
| North      | 2    |
| North-West | 3    |
| West       | 4    |
| South-West | 5    |
| South      | 6    |
| South-East | 7    |

To obtain the chain code, choose the specified starting pixel, trace the boundary in the clockwise direction, record the direction of each movement, and stop when the starting pixel is reached again.

---

## ⭐ Exam Tip

For numerical questions, always remember this direction numbering:

```text
        3   2   1
         \  |  /
      4 -- P -- 0
         /  |  \
        5   6   7
```

The chain code depends on:

* The **starting pixel**.
* The **direction of traversal** (clockwise or anticlockwise).

**Upload the question's image**, and I'll compute the exact 8-directional chain code step by step.
