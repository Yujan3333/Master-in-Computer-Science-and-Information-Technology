
# 🔵 1. Point-in-Polygon (Hand-Draw Style Figure)

### ✏️ Stick Diagram

```
        Polygon A              Polygon B
     +-------------+      +-------------+
     |             |      |             |
     |    P1 •     |      |     • P2    |
     |             |      |             |
     +-------------+      +-------------+

                • P3 (outside)
```

---

### 🧠 Explanation (from figure)

* P1 is inside **Polygon A**
* P2 is inside **Polygon B**
* P3 is **outside all polygons**

👉 No shape changes — only attribute assignment

---

### 📊 Attribute Tables

**Input Point Layer**

| Point_ID | Name |
| -------- | ---- |
| P1       | A    |
| P2       | B    |
| P3       | C    |

**Input Polygon Layer**

| Poly_ID | Zone  |
| ------- | ----- |
| A       | Urban |
| B       | Rural |

**Output (After Overlay)**

| Point_ID | Name | Zone  |
| -------- | ---- | ----- |
| P1       | A    | Urban |
| P2       | B    | Rural |
| P3       | C    | NULL  |

---

### 🎯 What to write in exam (short line)

> Each point is assigned attributes of the polygon within which it lies.

---

# 🔴 2. Line-in-Polygon (Hand-Draw Style Figure)

### ✏️ Stick Diagram

```
        Polygon A          Polygon B          Polygon C
     +-----------+     +-----------+     +-----------+
     |           |     |           |     |           |
-----|-----------|-----|-----------|-----|-----------|----
     |           |     |           |     |           |
     +-----------+     +-----------+     +-----------+

        S1                S2                S3
```

---

### 🧠 Explanation (from figure)

* One line passes through **3 polygons**
* It gets **split at boundaries**
* Result:

  * S1 inside Polygon A
  * S2 inside Polygon B
  * S3 inside Polygon C

---

### 📊 Attribute Tables

**Input Line Layer**

| Line_ID | Name      |
| ------- | --------- |
| L1      | Highway 1 |

**Input Polygon Layer**

| Poly_ID | Zone   |
| ------- | ------ |
| A       | Urban  |
| B       | Rural  |
| C       | Forest |

---

### 🔥 Output (After Overlay)

| Segment_ID | Line_ID | Name      | Zone   |
| ---------- | ------- | --------- | ------ |
| S1         | L1      | Highway 1 | Urban  |
| S2         | L1      | Highway 1 | Rural  |
| S3         | L1      | Highway 1 | Forest |

---

# ❗ Why More Features? (From Figure)

From 1 line:

```
-------------------------
```

Becomes:

```
----|----|----
 S1   S2   S3
```

👉 Because line is **cut at each polygon boundary**

---

# 🧠 Easy Memory (Exam Tip)

* **Point-in-polygon** → “Check where point lies”
* **Line-in-polygon** → “Cut line + assign area”

---

# ✍️ If You Draw in Exam, Do This:

### For Point-in-Polygon:

* Draw 2 boxes (polygons)
* Put dots inside
* Label P1, P2

### For Line-in-Polygon:

* Draw 3 boxes
* Draw one straight line crossing all
* Mark split points (|)

---

