## **1. Flow-Sensitive Analysis**
- **Meaning**: It considers the **order of statements** (control flow) in the program.
- **Example**: A dependence from `A(I)` to `A(I+1)` is **flow-sensitive** if there is an execution path where `A(I)` is written before `A(I+1)` is read.
- **Use in loops**: Determines if a dependence is **loop-carried** (across iterations) or **loop-independent** (within same iteration).

---

## **2. Flow-Insensitive Analysis**
- **Meaning**: Ignores execution order; assumes **any statement can execute in any order**.
- **Example**: Just checks if `A(I)` and `A(I+1)` *might* refer to same location, without checking if write happens before read in actual flow.
- **Result**: More conservative (finds more possible dependences), but can overestimate → may prevent optimizations unnecessarily.

---

## **3. Loop Fission (Loop Distribution)**
- **Meaning**: Splitting a single loop into **multiple separate loops**, each containing a subset of the original statements.
- **Purpose**: To **separate independent statements** so they can be optimized/parallelized individually.
- **Condition**: Possible if there is **no dependence** between statements being separated.
- **Example**:
  ```c
  for(i=0; i<N; i++) {
      A[i] = B[i] + C;   // Independent
      D[i] = A[i] * 2;   // Depends on first
  }
  ```
  If `D[i] = A[i] * 2` is moved to a second loop, but that would require `A[i]` computed first → not always legal due to dependence.

But if statements are independent:
  ```c
  for(i=0; i<N; i++) {
      A[i] = B[i] + C;   // Group 1
      E[i] = F[i] + G;   // Group 2 (independent)
  }
  ```
  Can split into:
  ```c
  for(i=0; i<N; i++) A[i] = B[i] + C;
  for(i=0; i<N; i++) E[i] = F[i] + G;
  ```

---

## **Connection Between Them**
- **Flow-sensitive analysis** tells if statements can be **reordered or split** (loop fission).
- **Flow-insensitive analysis** might falsely say "cannot split" due to ignoring execution order.
- **Loop fission** uses **dependence analysis** (flow-sensitive preferred) to decide if splitting is safe.

---

**Simple Summary**:
- **Flow-sensitive** = cares about order ✅ more precise for optimization.
- **Flow-insensitive** = ignores order ❌ safer but may block optimizations.
- **Loop fission** = splitting a loop into multiple loops when statements are independent (needs good dependence analysis).