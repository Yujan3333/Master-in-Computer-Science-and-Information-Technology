#rgis #third-semester 

## Local Raster Operation (GIS)

### Definition

A **Local Raster Operation** is a raster analysis in which the **output value of each cell depends only on the value(s) of the corresponding cell at the same location** in one or more input raster layers.

In simple words:

> **Each cell is processed independently, without considering neighboring cells.**

---

## Example 1: Single Raster (Multiply by 2)

### Input Raster (3 × 3)

```text
1   2   3
4   5   6
7   8   9
```

### Operation

```text
Output = Input × 2
```

Each cell is multiplied by **2** independently.

### Output Raster

```text
2    4    6
8   10   12
14  16   18
```

**Calculation:**

* 1 × 2 = 2
* 2 × 2 = 4
* 3 × 2 = 6
* 4 × 2 = 8
* 5 × 2 = 10
* 6 × 2 = 12
* 7 × 2 = 14
* 8 × 2 = 16
* 9 × 2 = 18

**Observation:** Each output cell is calculated using **only the input cell at the same location**.

---

## Example 2: Two Raster Layers (Addition)

### Raster A

```text
2   4   6
3   5   7
1   8   9
```

### Raster B

```text
1   2   3
4   5   6
7   8   9
```

### Operation

```text
Output = Raster A + Raster B
```

### Output Raster

```text
3    6    9
7   10   13
8   16   18
```

**Calculation:**

* 2 + 1 = 3
* 4 + 2 = 6
* 6 + 3 = 9
* 3 + 4 = 7
* 5 + 5 = 10
* 7 + 6 = 13
* 1 + 7 = 8
* 8 + 8 = 16
* 9 + 9 = 18

Again, only the **corresponding cells** are used.

---

## Characteristics

* Operates on **one cell at a time**.
* Does **not** use neighboring cells.
* Each output cell depends only on the corresponding input cell(s).
* Simple and fast to compute.

---

## Types of Local Operations

### 1. Arithmetic Operations

Examples:

* Addition (+)
* Subtraction (−)
* Multiplication (×)
* Division (÷)

Example:

* Elevation × 0.3048 (convert feet to meters)

---

### 2. Logical Operations

Examples:

* >
* <
* =
* AND
* OR

Example:

```text
Elevation > 1000 m
```

Output:

* 1 = True
* 0 = False

---

### 3. Conditional Operations

Example:

```text
If Temperature > 35°C
    High Risk
Else
    Low Risk
```

---

### 4. Mathematical Functions

Examples:

* Square
* Square root
* Logarithm
* Exponential

---

## Applications

* Land suitability analysis
* Flood risk mapping
* Temperature mapping
* Vegetation index (NDVI)
* Reclassification
* Map algebra calculations

---

## Difference from Other Raster Operations

| Operation                | Uses Neighboring Cells?         | Example                                          |
| ------------------------ | ------------------------------- | ------------------------------------------------ |
| **Local**                | ❌ No                            | Multiply by 2, Add two rasters, Reclassification |
| **Focal (Neighborhood)** | ✅ Yes                           | Mean filter, Smoothing                           |
| **Zonal**                | Uses all cells in the same zone | Average elevation of a district                  |
| **Global**               | Uses the entire raster          | Maximum elevation in the whole raster            |

---

## Exam Answer (5 Marks)

**Local Raster Operation** is a raster analysis method in which the value of each output cell is calculated using only the value(s) of the corresponding cell at the same location in one or more input raster layers. Neighboring cells are not considered.

**Examples:**

* Multiply every raster cell by 2.
* Add two raster layers cell-by-cell.
* Reclassification.
* Logical and conditional operations.

**Applications:**

* Land suitability analysis
* NDVI calculation
* Flood risk assessment
* Temperature and elevation analysis

### **Memory Tip**

**Local = Same Location**

Think of it as solving each cell **independently**:

* One raster: **Input × 2**
* Two rasters: **Cell A + Cell B**
* **Never looks at neighboring cells.**
