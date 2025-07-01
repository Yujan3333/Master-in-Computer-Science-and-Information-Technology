
## 🧠 **Boundedness in Petri Nets**

### ✅ **Definition:**

**Boundedness** is a property of a Petri Net that ensures the number of tokens in each place does **not grow indefinitely** during execution.

---

### 🔹 **Place-level Boundedness:**

A **place $P$** is said to be **k-bounded** if the number of tokens in $P$ never exceeds a finite integer $k$ in **any reachable marking**.

* Mathematically:

  $$
  \forall M \in R(M_0),\quad M(P) \leq k
  $$
* If $k = 1$, then $P$ is called **safe**.

---

### 🔹 **Net-level Boundedness:**

* A Petri Net is **k-bounded** if **every place** in the net is k-bounded.
* A Petri Net is said to be **bounded** if there exists **some finite k** such that it is k-bounded for that value.

---

### 💡 **Why Boundedness Matters:**

* Prevents **overflow or resource exhaustion** in real systems.
* Ensures the system has **finite memory requirements**.
* Helps detect **safety violations** like multiple processes entering a critical section.

---

### 📝 **Example:**

If a place represents a buffer that can hold max 3 items:

* The net should be **3-bounded** at that place.

---

### 🧾 **In Exam: You Can Write Like This**

> A place $P$ in a Petri Net is **k-bounded** if the number of tokens in it never exceeds a finite number $k$ in any reachable marking. That is, $M(P) \leq k$ for all reachable markings $M$.
>
> A Petri Net is **bounded** if every place is k-bounded for some finite $k$. It ensures that no place will have an unbounded number of tokens.
>
> Boundedness is essential for **resource control**, **buffer limits**, and ensuring **safe execution** of systems.

---
