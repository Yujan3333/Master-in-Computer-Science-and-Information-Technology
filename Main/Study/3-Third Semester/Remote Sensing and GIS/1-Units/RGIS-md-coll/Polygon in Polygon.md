
#rgis #third-semester 
# Polygon-in-Polygon Overlay

## Definition

**Polygon-in-Polygon overlay** is a GIS overlay operation where **two polygon layers are overlaid** to create **new polygons**. Each new polygon contains the **combined attributes** of both input polygon layers.

It is also called a **polygon overlay** or **polygon intersection**.

---

## How It Works

**Input Layers**

* Polygon Layer 1 (e.g., Land Use)
* Polygon Layer 2 (e.g., Administrative Boundaries)

Steps:

1. Overlay the two polygon layers.
2. Find where their boundaries intersect.
3. Split polygons at the intersections.
4. Create new polygons.
5. Assign attributes from **both** layers to each new polygon.

---

## Illustration

### Input

```text
Polygon Layer 1 (Land Use)

+-----------------------+
|                       |
|       Forest          |
|                       |
+-----------------------+


Polygon Layer 2 (District)

          +-------------+
          |             |
          |  District A |
          |             |
          +-------------+
```

The district overlaps only part of the forest.

---

### Overlay Result

```text
+-----------------------+
|        |              |
| Forest |  Forest      |
| + D.A  |              |
|        |              |
+-----------------------+
```

The original forest polygon is split into:

* Forest inside District A
* Forest outside District A

Each becomes a **new polygon**.

---

## Example Attribute Tables

### Input Polygon Layer 1

| Poly_ID | Land Use |
| ------- | -------- |
| P1      | Forest   |

### Input Polygon Layer 2

| Poly_ID | District |
| ------- | -------- |
| D1      | North    |

### Output After Overlay

| New_Poly | Land Use | District         |
| -------- | -------- | ---------------- |
| N1       | Forest   | North            |
| N2       | Forest   | Outside District |

---

## Applications

* Land-use analysis by district
* Forest area within municipalities
* Soil type within administrative boundaries
* Flood zones within villages
* Environmental planning

---

# Comparison of Overlay Operations

| Overlay Type           | Input               | Output                                |
| ---------------------- | ------------------- | ------------------------------------- |
| **Point-in-Polygon**   | Points + Polygons   | Points receive polygon attributes     |
| **Line-in-Polygon**    | Lines + Polygons    | Lines split into segments             |
| **Polygon-in-Polygon** | Polygons + Polygons | New polygons with combined attributes |

---

## Memory Trick

* **Point + Polygon** → **Point gets attributes**
* **Line + Polygon** → **Line gets split**
* **Polygon + Polygon** → **Polygon gets split into new polygons**

The key idea is that **polygon-in-polygon combines two polygon layers**, creating **new polygons** wherever their boundaries overlap, and each new polygon inherits attributes from **both** input layers.
