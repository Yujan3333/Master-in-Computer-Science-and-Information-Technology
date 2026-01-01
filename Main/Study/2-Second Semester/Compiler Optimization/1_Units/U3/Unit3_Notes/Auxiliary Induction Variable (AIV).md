   #### **Definition**
   
   An **auxiliary induction variable (AIV)** is a variable inside a loop whose value changes by a **constant amount on each iteration**, but **it is not the loop control variable**.
   
   ---
   
   #### **Key Points (Write in Exam)**
   
   * It is **derived from a basic induction variable**
   * Updated using a **linear expression**
   * Changes in a **regular, predictable pattern**
   * Used mainly for **array indexing or address calculation**
   * Helps the compiler in **optimization and dependence analysis**
   
   ---
   
   #### **General Form**
   
   If `I` is a basic induction variable, then an auxiliary induction variable `K` is defined as:
   
   $$
   K = a \times I + b
   $$
   
   where `a` and `b` are constants.
   
   ---
   
   #### **Example**
   
   ```fortran
   DO I = 1, 10
      K = K + 2
      A(K) = A(K) + 1
   END DO
   ```
   
   * `I` → **Basic induction variable**
   * `K` → **Auxiliary induction variable**
   * `K` changes as: `2, 4, 6, 8, ...`
   * Increment is **constant (2)**
   
   ---
   
   #### **From Your Code**
   
   ```fortran
   KI = KI + INC
   ```
   
   * `INC` is loop invariant
   * `KI` increases by a constant each iteration
   * Therefore, **KI is an auxiliary induction variable**
   
   ---
   
   #### **Why It Is Important in Compiler Optimization**
   
   * Makes **array subscripts analyzable**
   * Enables **strength reduction**
   * Helps detect **loop dependencies**
   * Supports **parallelization**
   
   ---
   
   #### **One-Line Exam Answer**
   
   > An auxiliary induction variable is a loop variable other than the loop index whose value changes by a constant amount on each iteration and can be expressed as a linear function of the basic induction variable.
   
   ---