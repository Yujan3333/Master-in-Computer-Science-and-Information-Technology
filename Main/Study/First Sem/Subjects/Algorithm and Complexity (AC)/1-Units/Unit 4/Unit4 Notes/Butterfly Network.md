### 🦋 Butterfly Network
A Butterfly Network is a special network topology used in parallel computing — especially useful for routing, sorting, and prefix computations.

### 🔸 Basic Idea:
It is structured in levels and rows, and connects processors in a way that supports fast communication with fewer wires than a hypercube.

### 🔹 Key Properties:

| Feature                   | Description                                                          |
| ------------------------- | -------------------------------------------------------------------- |
| **Notation**              | A node is written as **⟨r, l⟩**                                      |
|                           | → `r` is the **row** (a d-bit binary string)                         |
|                           | → `l` is the **level** (0 to d)                                      |
| **Processors**            | (d + 1) × 2ᵈ                                                         |
| **Links**                 | d × 2ᵈ⁺¹                                                             |
| **Diameter**              | 2d (max steps from source to destination)                            |
| **Unique Path**           | From any source ⟨r, 0⟩ to ⟨r’, d⟩, there is a **unique greedy path** |
| **Structure Type**        | **Multistage interconnection network**                               |
| **Relation to Hypercube** | Collapsing all rows in each level gives a **Hypercube (Hₙ)**         |
