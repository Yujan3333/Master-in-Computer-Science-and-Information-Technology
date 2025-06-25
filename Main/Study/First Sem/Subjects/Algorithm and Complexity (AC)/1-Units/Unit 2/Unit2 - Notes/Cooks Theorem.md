### 🔥 **Cook’s Theorem (Simple Summary)**

**Statement**:

> Any problem in **NP** can be **converted (reduced)** in **polynomial time** into an instance of the **Boolean Satisfiability Problem (SAT)**.

In other words:

> If you can solve **SAT**, then you can solve **any NP problem**.

---

### 🤔 Why is it Important?

- It shows that **SAT is NP-complete** — the **first** problem proven to be so.
    
- It forms the **foundation** of NP-completeness theory.
    

---

### 📌 Two Parts of the Proof:

1. **SAT is in NP**:
    
    - If you give me a solution (a truth assignment), I can check if it satisfies the formula **in polynomial time**.
        
2. **Every NP problem reduces to SAT**:
    
    - Suppose a problem can be solved by some **non-deterministic Turing machine** in polynomial time.
        
    - We can **encode the steps** of that machine's computation as a **Boolean formula**.
        
    - That formula is satisfiable **if and only if** the machine **accepts** the input.
        
    - This encoding takes **polynomial time**, so it's an efficient reduction.
        

---

### 📘 Corollary:

> If we can solve SAT in polynomial time, then **P = NP**.

Because SAT is as hard as any NP problem!

---

### 🚀 Final Takeaway:

Cook’s Theorem proves that **SAT is the hardest problem in NP** — solving SAT efficiently means you can solve **every** NP problem efficiently.