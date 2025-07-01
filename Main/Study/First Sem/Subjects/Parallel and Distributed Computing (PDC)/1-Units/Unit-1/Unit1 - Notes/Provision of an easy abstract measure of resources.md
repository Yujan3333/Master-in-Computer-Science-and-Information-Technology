
## ⏱️ **Time and Space Complexity: DTM vs NDTM**

---

### ✅ **1. DTM (Deterministic Turing Machine):**

* In a **DTM**, we measure:

  * **Time complexity**: Total **number of moves** (transitions) the machine makes from start to halt.
  * **Space complexity**: Total **number of tape cells scanned** during computation.

> 💡 **Key Assumption**:
> Each move (read/write/shift) counts as **one unit of time**.
> Each unique cell visited is counted once in **space**.

---

### ✅ **2. NDTM (Non-Deterministic Turing Machine):**

* Since NDTMs can **make multiple moves in parallel**, their complexity is measured differently.

* **Time complexity** of an NDTM is defined as:

  > The **length of the shortest accepting computation path**, i.e., the number of moves in the **fastest sequence** that leads to acceptance.

* We do **not** count all branches — only the **best-case accepting path** is considered for time complexity.

> 💡 If no accepting path exists, the input is **rejected**.

---

### 📝 **Key Comparison Table:**

| Model    | Time Complexity                          | Space Complexity                              |
| -------- | ---------------------------------------- | --------------------------------------------- |
| **DTM**  | Total number of steps (sequential)       | Number of distinct tape cells scanned         |
| **NDTM** | Number of steps in *some accepting path* | Usually similar to DTM; counted over the path |

---

### 📝 **Exam Answer Example:**

> In a **Deterministic Turing Machine (DTM)**, each move is counted as one unit of **time**, and each tape cell scanned is counted as **space**. The **total time complexity** is the number of moves the machine makes to reach a halting state.
>
> In a **Non-Deterministic Turing Machine (NDTM)**, **time complexity** is defined as the **number of steps** in the **shortest accepting computation path**. Since NDTMs can explore multiple branches simultaneously, only the accepting path is considered.
>
> This highlights how complexity measurement differs between sequential and non-deterministic models.

---
