## **Definition–Use Graph (DU Graph)**

**Definition:**
A Definition–Use graph is a graph that shows an edge from **each definition of a variable** to **all possible uses** of that variable during program execution.

**Function:**
It shows **where variables are defined and where they are used**.

**Usage:**
Used heavily in **compiler optimizations and program transformations**.

---

### **Definition–Use Sets (for a Basic Block b)**

* **Uses(b):** Variables used before being defined in block *b*
* **Defout(b):** Variables defined in block *b*
* **Killed(b):** Definitions overwritten in block *b*
