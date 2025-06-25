You have a **Boolean formula**:

(x∨¬y)∧(y∨z)(x∨¬y)∧(y∨z)

- This formula has **two parts** connected by $\land$ (AND).
    
- Each part is called a **clause**:
    
    - **Clause 1**: $x \lor \neg y$ means "$x$ OR NOT $y$".
        
    - **Clause 2**: $y \lor z$ means "$y$ OR $z$".
        

---

### Candidate Assignment:

You are given values for the variables:

- $x = \text{true}$,
    
- $y = \text{false}$,
    
- $z = \text{true}$.
    

---

### Verification Process:

1. **Clause 1: $x \lor \neg y$**
    
    - $x$ is **true** (given).
        
    - $y$ is **false**, so $\neg y$ (NOT $y$) is **true**.
        
    - The clause evaluates to: $\text{true} \lor \text{true} = \text{true}$.
        
    - Since at least one part of the OR is true, **Clause 1 is satisfied**.
        
2. **Clause 2: $y \lor z$**
    
    - $y$ is **false**.
        
    - $z$ is **true**.
        
    - The clause evaluates to: $\text{false} \lor \text{true} = \text{true}$.
        
    - **Clause 2 is satisfied**.
        

---

### Conclusion:

- The entire formula is the AND ($\land$) of the two clauses.
    
- Since **both clauses are true**, the formula evaluates to **true** under this assignment.
    
- Therefore, the **assignment satisfies the formula**.
    

---

### Why This Matters for SAT ∈ NP:

- A candidate solution can be **verified quickly** by plugging in the values and evaluating the formula.
    
- The verification process involves simple logical operations (OR, AND, NOT) and runs in **polynomial time** (linear in formula size).
    
- This shows that **SAT is in NP**, as solutions are efficiently verifiable.
    

---

### Summary:

- **Verification** involves evaluating the formula under a given assignment.
    
- The process is **efficient** (polynomial time).
    
- Thus, **SAT ∈ NP** because solutions can be verified quickly.