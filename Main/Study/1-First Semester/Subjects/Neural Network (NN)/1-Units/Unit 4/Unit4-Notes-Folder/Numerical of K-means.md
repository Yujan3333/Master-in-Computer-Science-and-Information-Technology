
- Data points:
    - p1 = (1,1)
    - p2 = (2,1)
    - p3 = (4,3)
    - p4 = (5,4)
- Initial cluster centers:
    - c1 = (1,1)
    - c2 = (2,1)
- Number of clusters: **K = 2**


---

### 📍 Step 1: Assign each point to the nearest cluster

We use **Euclidean distance**:

$$\text{Distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

---
#### Distance of each point from c1 = (1,1) and c2 = (2,1):

|Point|Distance to c1 (1,1)|Distance to c2 (2,1)|Assigned Cluster|
|---|---|---|---|
|p1=(1,1)|√((1−1)² + (1−1)²) = 0|√((2−1)² + (1−1)²) = 1|c1|
|p2=(2,1)|√((1−2)² + (1−1)²) = 1|√((2−2)² + (1−1)²) = 0|c2|
|p3=(4,3)|√((1−4)² + (1−3)²) = √13 ≈ 3.61|√((2−4)² + (1−3)²) = √8 ≈ 2.83|c2|
|p4=(5,4)|√((1−5)² + (1−4)²) = √25 = 5|√((2−5)² + (1−4)²) = √18 ≈ 4.24|c2|

✅ **Assignments after Step 1**:

- Cluster 1 (c1): {p1}
- Cluster 2 (c2): {p2, p3, p4}
---

### 🔁 Step 2: Recalculate centroids

- New **c1** = mean of (1,1) = (1,1)
- New **c2** = mean of (2,1), (4,3), (5,4)

$c_2 = \left(\frac{32+4+5}{3}, \frac{31+3+4}{3}\right) = \left(\frac{41}{3}, \frac{38}{3}\right) \approx (3.67, 2.67)$

---
### 🔁 Step 3: Reassign based on new centroids

Now use new c2 ≈ (3.67, 2.67)

|Point|Distance to c1 (1,1)|Distance to new c2 (3.67, 2.67)|Assigned Cluster|
|---|---|---|---|
|p1|0|√((3.67−1)² + (2.67−1)²) ≈ 3.21|c1|
|p2|1|√((3.67−2)² + (2.67−1)²) ≈ 2.26|c1|
|p3|√13 ≈ 3.61|√((3.67−4)² + (2.67−3)²) ≈ 0.47|c2|
|p4|5|√((3.67−5)² + (2.67−4)²) ≈ 1.89|c2|

✅ **New Assignments**:

- Cluster 1 (c1): {p1, p2}
- Cluster 2 (c2): {p3, p4}
---

### 🔁 Step 4: Recalculate centroids again

- New **c1** = mean of (1,1), (2,1) → ((1+2)/2, (1+1)/2) = (1.5, 1)
- New **c2** = mean of (4,3), (5,4) → ((4+5)/2, (3+4)/2) = (4.5, 3.5)
---

### 🔁 Step 5: Reassign again

Check if cluster assignments change using new centroids.

|Point|Distance to c1 (1.5,1)|Distance to c2 (4.5,3.5)|Assigned Cluster|
|---|---|---|---|
|p1|√((1.5−1)² + (1−1)²) = 0.5|√((4.5−1)² + (3.5−1)²) ≈ 4.30|c1|
|p2|√((1.5−2)² + (1−1)²) = 0.5|√((4.5−2)² + (3.5−1)²) ≈ 3.54|c1|
|p3|√((1.5−4)² + (1−3)²) ≈ 3.90|√((4.5−4)² + (3.5−3)²) = √0.5 ≈ 0.71|c2|
|p4|√((1.5−5)² + (1−4)²) ≈ 4.95|√((4.5−5)² + (3.5−4)²) = √0.5 ≈ 0.71|c2|

✅ No changes in assignment → **Converged**

---

### ✅ Final Clusters:

- **Cluster 1**: (1,1), (2,1)
- **Cluster 2**: (4,3), (5,4)


## Tag
#numerical