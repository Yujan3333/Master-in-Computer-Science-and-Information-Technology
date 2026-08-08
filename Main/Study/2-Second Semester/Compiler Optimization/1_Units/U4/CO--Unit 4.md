#second-semester #compiler-optimization 
### Loop Interchange
- The process of switching the nesting order of loops like exchanging the inner loop with the outer loop
---
### [Loop Unrolling](CO--u4-md/Loop%20Unrolling.md)
- Main focus is to reduce the number of steps in loop operation techniques

---
### [Loop Invariant](CO--u4-md/Loop%20Invariant.md)

---
### Loop Fusion
- Mixing two identical loops

---
### Fusion Safety
- Sometimes dependency comes so be careful

---
### [Loop Vectorization](CO--u4-md/Loop%20Vectorization.md)
- scalar operation(*single operation at once*) into a vector operation (*multiple operation at once*)

---
### [Loop Skewing](CO--u4-md/Loop%20Skewing.md)
- transformation that *reshapes* the *iteration space* to make it possible to express the *existing parallelism* with *conventional parallel loops*

---
### [Scalar Expansion](CO--u4-md/Scalar%20Expansion.md)

#### [Program Explanation - Scalar Expansion](CO--u4-md/Program%20Explanation%20-%20Scalar%20Expansion.md)

---
### Array Renaming
- Arrays location can be sometimes reused that leads to unnecessary dependency
- **TARGET** - Remove the cycle from the dependency graph

---
### Node Splitting
- Sometimes Array renaming is not enough hence this is required

---
### Index Set Splitting
#### 1️⃣ Threshold Analysis
#### 2️⃣ Loop Peeling
#### [3️⃣Section Based Splitting](CO--u4-md/3️⃣Section%20Based%20Splitting.md)

---
### Alignment

---
### Code Replication

---
### Parallel Code Generation and Its Problem
