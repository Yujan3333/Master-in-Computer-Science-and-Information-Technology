- [Point in polygon and line in polygon in figure](RGIS-assignment-notes/Point%20in%20polygon%20and%20line%20in%20polygon%20in%20figure.md)

# Point-in-Polygon and Line-in-Polygon Overlay

## 1. Point-in-Polygon (PIP) Overlay

### Concept

**Point-in-Polygon (PIP)** is a GIS overlay operation used to determine **which polygon contains each point**. After finding the containing polygon, the polygon's attributes are assigned to the point.

---

### How It Works

**Input Layers**

* **Point Layer:** Schools, hospitals, wells, accident locations, etc.
* **Polygon Layer:** Districts, municipalities, land-use zones, watersheds, etc.

For every point:

1. Check whether the point lies inside a polygon.
2. If it does, assign that polygon's attributes to the point.

---

### Illustration

#### Input

```text
                District D1
      +---------------------------+
      |                           |
      |      ● P1 (School A)      |
      |                           |
      +---------------------------+

                District D2
      +---------------------------+
      |                           |
      |        ● P2 (School B)    |
      |                           |
      +---------------------------+
```

#### Output

```text
P1 → District D1
P2 → District D2
```

---

### Example Attribute Tables

#### Input Point Layer

| Point_ID | Name     |
| -------- | -------- |
| P1       | School A |
| P2       | School B |

#### Input Polygon Layer

| Poly_ID | District | Population |
| ------- | -------- | ---------- |
| D1      | North    | 50,000     |
| D2      | South    | 70,000     |

#### Output After Overlay

| Point_ID | Name     | District | Population |
| -------- | -------- | -------- | ---------- |
| P1       | School A | North    | 50,000     |
| P2       | School B | South    | 70,000     |

---

### Applications

* Assigning schools to districts
* Identifying which municipality a hospital belongs to
* Finding the watershed containing a monitoring station
* Zoning and land administration

---

# 2. Line-in-Polygon Overlay

### Concept

**Line-in-Polygon Overlay** determines which polygons a line passes through. Whenever the line crosses a polygon boundary, it is **split into separate line segments**, and each segment receives the attributes of the polygon in which it lies.

---

### How It Works

**Input Layers**

* **Line Layer:** Roads, rivers, railways, pipelines
* **Polygon Layer:** Districts, land-use zones, administrative boundaries

Processing steps:

1. Check where the line intersects polygon boundaries.
2. Split the line at every boundary crossing.
3. Assign polygon attributes to each new segment.

---

### Illustration

#### Input

```text
             District D1        District D2

      +----------------+----------------+
      |                |                |
------|----------------|----------------|------
 Road |                |                |
      |                |                |
      +----------------+----------------+
```

The road crosses from **District D1** into **District D2**.

---

#### Output

```text
Segment S1                 Segment S2

------=====================|=====================------

       District D1              District D2
```

The original road becomes **two separate road segments**.

---

### Example Attribute Tables

#### Input Line Layer

| Line_ID | Road_Name |
| ------- | --------- |
| L1      | Highway 1 |

#### Input Polygon Layer

| Poly_ID | District |
| ------- | -------- |
| D1      | North    |
| D2      | South    |

#### Output After Overlay

| Segment_ID | Line_ID | Road_Name | District |
| ---------- | ------- | --------- | -------- |
| S1         | L1      | Highway 1 | North    |
| S2         | L1      | Highway 1 | South    |

---

# 3. Why Does Line-in-Polygon Produce More Features?

A **single line** may pass through **many polygons**.

Each time the line crosses a polygon boundary:

* the line is **split**
* a **new segment** is created

Therefore,

```text
One Road
    │
    ▼

District A
──────────────┐
              │
District B
──────────────┐
              │
District C

↓

Road Segment 1
Road Segment 2
Road Segment 3
```

Thus,

**Input:** 1 road

**Output:** 3 road segments

Each segment has different polygon attributes.

---

# 4. Real-World Applications

## Point-in-Polygon

* Assign schools to municipalities.
* Determine which district contains a hospital.
* Find which watershed contains a rainfall station.
* Identify accident locations within police jurisdictions.

---

## Line-in-Polygon

* Divide roads by administrative districts.
* Divide rivers by ecological zones.
* Divide pipelines by land ownership.
* Divide highways by maintenance jurisdiction.

---

# Difference Between Point-in-Polygon and Line-in-Polygon

| Feature            | Point-in-Polygon                    | Line-in-Polygon                               |
| ------------------ | ----------------------------------- | --------------------------------------------- |
| Input              | Points + Polygons                   | Lines + Polygons                              |
| Operation          | Finds polygon containing each point | Splits lines at polygon boundaries            |
| Output             | Same number of points               | Usually more line segments                    |
| Attribute Transfer | Point receives polygon attributes   | Each line segment receives polygon attributes |
| Example            | School assigned to a district       | Road divided into district-wise segments      |
