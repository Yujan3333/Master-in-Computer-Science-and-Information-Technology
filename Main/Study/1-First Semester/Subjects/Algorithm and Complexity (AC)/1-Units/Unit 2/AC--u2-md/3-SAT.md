### **Definition of 3-SAT**

3-SAT is a restricted case of the Boolean Satisfiability Problem (SAT) where:

- The formula is in **Conjunctive Normal Form (CNF)**
    
- Each clause contains exactly **three literals**
    

A **literal** is either:

- A variable $x_i$ (positive literal)
    
- Its negation $\neg x_i$ (negative literal)
    

A **3-CNF formula** has the form:

$φ=⋀i=1m(li1∨li2∨li3)φ=i=1⋀m​(li1​∨li2​∨li3​)$

where each $l_{ij}$ is a literal and $m$ is the number of clauses.

---

### **Example of 3-SAT Formula**

$(x1∨x1∨x2)∧(¬x1∨¬x2∨¬x2)∧(¬x1∨x2∨x2)(x1​∨x1​∨x2​)∧(¬x1​∨¬x2​∨¬x2​)∧(¬x1​∨x2​∨x2​)$

**Properties:**

1. CNF structure (conjunction of disjunctive clauses)
    
2. Each clause has exactly 3 literals (repetitions allowed)
    

---

### **The Language of 3-SAT**

3SAT={φ∣φ is a satisfiable 3-CNF formula}3SAT={φ∣φ is a satisfiable 3-CNF formula}

**Interpretation:**

- Contains all 3-CNF formulas for which there exists a truth assignment making $\varphi$ evaluate to true
    
- The assignment must satisfy all clauses simultaneously
    

---

### **Computational Significance**

3-SAT is **NP-Complete** because:

1. **Membership in NP:**
    
    - Verification takes polynomial time
        
    - Given assignment, evaluate each clause in $O(1)$ time per clause
        
2. **NP-Hardness:**
    
    - All NP problems polynomial-time reduce to 3-SAT
        
    - Shown via Cook-Levin theorem and subsequent refinements
        

**Key Implication:**

P=NP  ⟺  3-SAT has a polynomial-time algorithmP=NP⟺3-SAT has a polynomial-time algorithm

---

### **Relation to General SAT**

|Feature|General SAT|3-SAT|
|---|---|---|
|Clause size|Any length|Exactly 3 literals|
|Complexity|NP-Complete|NP-Complete|
|Proof utility|Fundamental|More convenient|

**Why 3-literals suffice:**

- Any SAT formula can be transformed to 3-SAT via polynomial reduction
    
- The 3-literal restriction maintains full expressive power for NP-completeness
    

---

### **Practical Applications**

1. **Complexity Theory:**
    
    - Standard starting point for NP-completeness proofs
        
    - Used in Cook-Levin theorem
        
2. **Computer Engineering:**
    
    - Circuit design verification
        
    - FPGA routing problems
        
3. **Artificial Intelligence:**
    
    - Constraint satisfaction problems
        
    - Automated planning systems
        
4. **Mathematical Logic:**
    
    - Proof complexity analysis
        
    - Model checking
        

---

### **Key Exam Points**

1. **Definition:**
    
    - 3-CNF form with exactly 3 literals per clause
        
2. **Complexity Status:**
    
    - NP-Complete (both in NP and NP-Hard)
        
3. **Theoretical Importance:**
    
    - Canonical NP-complete problem
        
    - Basis for most polynomial-time reductions
        
4. **Practical Relevance:**
    
    - Benchmark for SAT solvers
        
    - Foundation for many real-world applications