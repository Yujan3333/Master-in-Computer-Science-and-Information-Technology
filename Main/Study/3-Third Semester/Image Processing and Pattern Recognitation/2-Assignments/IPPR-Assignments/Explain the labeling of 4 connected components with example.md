# Labeling of 4-Connected Components

- [Numerical of 4-Connected Components](Numerical%20of%204-Connected%20Components.md)
---

# 1. Definition

**Connected component labeling** is the process of identifying and assigning unique labels to groups of connected pixels in a binary image.

👉 In **4-connectivity**, pixels are connected only through **horizontal and vertical neighbors**.

---

# 2. 4-Connectivity Concept

A pixel $(x,y)$ has 4-neighbors:

$$N_4(x,y)={(x+1,y),(x-1,y),(x,y+1),(x,y-1)}$$

👉 Only these neighbors are considered connected.

---

# 3. Steps for 4-Connected Component Labeling

### Step 1: Scan the Image

* Scan from **left to right, top to bottom**

---

### Step 2: For Each Pixel (value = 1)

Check its neighbors:

* **Top (already processed)**
* **Left (already processed)**

---

### Step 3: Assign Labels

Case 1: No labeled neighbors
→ Assign **new label**

Case 2: One labeled neighbor
→ Assign **same label**

Case 3: Multiple labeled neighbors
→ Assign one label and record **equivalence**

---

### Step 4: Resolve Equivalences

* Merge equivalent labels

---

### Step 5: Final Labeling

* Replace equivalent labels with a **single label**

---

# 4. Example

## Given Binary Image

| 1 | 1 | 0 | 0 |
| - | - | - | - |
| 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 |
| 0 | 0 | 0 | 0 |


---

## Step-by-Step Labeling

### First Pass (assign temporary labels)

| 1 | 1 | 0 | 0 |
| - | - | - | - |
| 1 | 0 | 0 | 2 |
| 0 | 0 | 3 | 2 |
| 0 | 0 | 0 | 0 |


* Top-left group → Label **1**
* Right group → Label **2**
* Bottom-middle → Label **3**

---

### Check Connectivity

* Label 2 pixels are connected → same component
* Label 3 is separate

---

## Final Output

| 1 | 1 | 0 | 0 |
| - | - | - | - |
| 1 | 0 | 0 | 2 |
| 0 | 0 | 3 | 2 |
| 0 | 0 | 0 | 0 |


---

# 5. Interpretation

* **Component 1** → top-left region
* **Component 2** → right region
* **Component 3** → isolated region

👉 Total components = **3**

---

# 6. Key Points for Exam

* 4-connectivity → only up, down, left, right
* Scan order → left to right, top to bottom
* Two-pass algorithm commonly used
* Handles equivalence of labels
* Used in segmentation and object detection

---
