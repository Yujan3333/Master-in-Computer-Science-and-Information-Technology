
## 🔄 **Simulation of NDTM using DTM**

### ✅ **Concept:**

Although **NDTMs** are theoretical machines that can make **multiple choices simultaneously**, they can be **simulated by a DTM** using a process that mimics **unbounded parallelism**.

---

### 🔹 **How the Simulation Works:**

1. **Multiple Choices**:
   At each decision point, an NDTM may have **multiple transitions** (choices) to follow.

2. **DTM Simulation**:
   A **DTM simulates** this behavior by:

   * **Making multiple copies** of itself for each possible choice.
   * **Each copy** explores a different branch (node) in the **computation tree**.

3. **Tree Traversal**:
   The DTM simulates an **OR-tree**, where each **path** represents a possible computation of the NDTM.

4. **Halting Condition**:

   * If **any copy** reaches an **accepting state**, the DTM halts and **accepts the input**.
   * If a **branch fails**, only that copy terminates.
   * The DTM continues exploring until it either **finds an accepting path** or exhausts all possibilities.

---

### 📝 **Key Points:**

* The DTM explores **all possible computation paths** of the NDTM.
* This is done **sequentially** (e.g., using breadth-first search) since real DTMs can't truly fork copies.
* The simulation is possible but may take **exponential time**.

---

### 📝 **Exam Answer Example:**

> A **Non-Deterministic Turing Machine (NDTM)** can be simulated by a **Deterministic Turing Machine (DTM)** by allowing **unbounded parallelism**.
>
> Whenever the NDTM makes a choice, the DTM **creates multiple copies of itself**, one for each possible choice. Each copy proceeds along a separate computation path (node in an **OR-tree**).
>
> If any copy **reaches an accepting state**, the DTM **halts and accepts**. If a copy fails, it simply **terminates** without affecting the others.
>
> Though simulation is possible, it may require **exponential time**, making it less efficient than true non-determinism.

---

