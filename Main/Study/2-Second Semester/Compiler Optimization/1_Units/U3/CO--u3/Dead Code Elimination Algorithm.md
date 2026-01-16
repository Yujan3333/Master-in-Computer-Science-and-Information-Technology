## **Algorithm for Dead Code Elimination (Worklist Method)**

**Goal:** Remove statements whose results are never used (dead code).

---

### **Procedure: `eliminate_dead_code(P)`**

**Input:** Program `P` with statements and their **def-use chains**.
**Output:** Program `P` with dead statements removed.

---

**Step 1: Initialization**

* Let **worklist** = set of all **absolutely useful statements**.
  (Statements that are always useful, e.g., I/O operations, `return` statements, volatile memory writes.)

---

**Step 2: Mark useful statements**

```
while worklist is not empty do
    x = an arbitrary element of worklist
    mark x as useful
    remove x from worklist
    for each statement y such that y defines a variable used in x (i.e., (y,x) in def-use chain)
        if y is not marked useful then
            add y to worklist
```

* **Explanation:**

  * Start with “absolutely useful” statements.
  * Trace **backwards through def-use chains**: if a statement produces a value that a useful statement uses, it is itself useful.
  * Repeat until no new statements are added.

---

**Step 3: Delete dead statements**

* Delete every statement **not marked as useful**.
* The program now contains only **live statements**.

---

### **Pseudo-code (exam-friendly)**

```
procedure eliminate_dead_code(P):
    worklist = {absolutely useful statements}

    while worklist ≠ ∅ do
        x = select arbitrary element from worklist
        mark x as useful
        remove x from worklist
        for all y such that y defines a variable used in x (def-use relation)
            if y not marked useful then
                add y to worklist

    delete every statement not marked useful
end procedure
```

#### [Explanation of dead code elimination algorithm](Explanation%20of%20dead%20code%20elimination%20algorithm.md)

---

### **Notes**

1. **Absolutely useful statements:**

   * Return statements, I/O operations, function calls with side effects.

2. **Dead statements:**

   * Assignments whose result is never used.

3. **Worklist algorithm:**

   * Efficient because it **propagates usefulness backward** through the program.

---

