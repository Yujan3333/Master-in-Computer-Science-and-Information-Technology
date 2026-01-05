 Based on the **PDF content (Unit 2: Dependence Analysis and Testing)**, here’s how you test dependency in loops:
   
---
   
## **Dependence Testing in Loops**
   
   Dependence testing determines whether two array references in a loop nest **access the same memory location** in different iterations, which may prevent parallelization.
   
   ### **General Problem Form**
   
   Given two array references in a loop nest:
   
   $$
   A(f_1(I_1, \dots, I_n)) \quad \text{and} \quad A(f_2(I_1, \dots, I_n))
   $$
   
   We check if there exist **two iteration vectors** $\vec{i}$ and $\vec{j}$ such that:
   
   $$
   f_1(\vec{i}) = f_2(\vec{j}) \quad \text{and} \quad \vec{i} \neq \vec{j}
   $$
   
   If such vectors exist, there is a **loop-carried dependence**.
   
   ---
   
## **Methods of Dependence Testing**
   
### **1. GCD (Greatest Common Divisor) Test**
   
   * Used for **linear subscript expressions** of the form:
     $a \cdot I + c_1$ and $a \cdot I + c_2$
   
   * The equation to solve:
   
   $$
   a \cdot i + c_1 = a \cdot j + c_2
   $$
   
   Rewriting:
   
   $$
   a \cdot (i - j) = c_2 - c_1
   $$
   
   * **Condition:** If $\text{GCD}(a, \text{step}) \mid (c_2 - c_1)$, then dependence **may** exist.
   
   * Example from PDF (Page 38):
   
   $$
   \text{DO } I = 1, N
   $$
   $$
   A(4I+2) = \dots
   $$
   $$
   \dots = A(2I+1)
   $$
   
   Equation:
   
   $$
   4i + 2 = 2j + 1 \Rightarrow 4i - 2j = -1
   $$
   
   $\text{GCD}(4, 2) = 2$.
   Does $2$ divide $-1$? **No** → **no dependence**.
   
   ---
   
### **2. Strong SIV Test**
   
   For subscripts of form:
   
   $$
   I + c_1 \quad \text{and} \quad I + c_2
   $$
   
   * Let $d = c_2 - c_1$
   
   * If $d$ is **integer** and $|d| < (\text{upper bound} - \text{lower bound})$, dependence exists.
   
   * Example:
   
   $$
   A(I+10) = A(I) + B
   $$
   
   Here $d = 10 - 0 = 10$, so dependence exists if loop runs more than $10$ iterations.
   
   ---
   
### **3. Weak Zero SIV Test**
   
   For subscripts:
   
   $$
   I + c_1 \quad \text{and} \quad c_2
   $$
   
   Solve:
   
   $$
   I + c_1 = c_2 \Rightarrow I = c_2 - c_1
   $$
   
   If $I$ is within loop bounds → **dependence exists for that iteration**.
   
   * Example (PDF Page 43):
   
   $$
   \text{DO } I = 1, N
   $$
   $$
   A(I, N) = A(1, N) + A(N, N)
   $$
   
   Here $A(1,N)$ is loop-invariant, but $A(N,N)$ causes dependence.
   
   ---
   
### **4. Weak Crossing SIV Test**
   
   For subscripts:
   
   $$
   I + c_1 \quad \text{and} \quad -I + c_2
   $$
   
   Solve:
   
   $$
   i + c_1 = -j + c_2 \Rightarrow i + j = c_2 - c_1
   $$
   
   If solution exists within iteration space → dependence.
   
   * Example (PDF Page 44):
   
   $$
   \text{DO } I = 1, N
   $$
   $$
   A(I) = A(N - I + 1) + C
   $$
   
   This has **cross-iteration dependence**, solved by **splitting loop into two halves**.
   
   ---
   
## **Steps in Dependence Testing**
   
   1. **Classify subscripts** as ZIV, SIV, or MIV.
   2. **Apply appropriate test** for each subscript pair:
   
      * ZIV → trivial (no index, easy)
      * SIV → use Strong/Weak SIV, GCD test
      * MIV → use **GCD for multiple indices** or advanced tests (Banerjee, Omega test)
   3. **Combine results** across dimensions:
      Dependence exists if **all dimensions** show possible dependence.
   4. **Determine dependence type**:
   
      * **True dependence (RAW)** → flow-sensitive
      * **Anti-dependence (WAR)** → write after read
      * **Output dependence (WAW)** → write after write
   
   ---
   
## **Example from PDF (Page 26)**
   
   ```fortran
   DO I = 1, N
     DO J = 1, N
       S1: C[I,J] = A[I,J] + Y[J]
       S2: Y[J] = C[I,J] + X[I]
       S3: X[I] = Y[J] + X[I]
     END DO
   END DO
   ```
   
   **Testing:**
   
   * **S1 → S2**: True & Anti-dependence on $C[I,J]$ and $Y[J]$
   * **S2 → S3**: True & Anti-dependence on $Y[J]$
   * **S1 → S3**: Output dependence on $X[I]$
   * Use **GCD test** for each subscript pair
   
   ---
   
## **Conclusion**
   
   Dependence testing uses:
   
   1. **GCD Test** for linear subscript equations
   2. **SIV Tests** for single index variables
   3. **MIV Tests** for multiple indices
   4. **Direction & Distance vectors** to characterize dependence
   
   If **no dependence** exists → loop can be parallelized/vectorized.
   If dependence exists → apply transformations (loop splitting, alignment, etc.) to break dependence.
   
   ---
