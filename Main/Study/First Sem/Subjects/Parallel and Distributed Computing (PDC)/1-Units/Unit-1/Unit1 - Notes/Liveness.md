
## 🔄 **Liveness in Petri Nets**

### ✅ **Definition:**

**Liveness** ensures that **transitions remain active** in a Petri Net and can eventually fire during the system's execution — **no part of the system becomes permanently disabled**.

---

### 🔹 **Transition-Level Liveness:**

A **transition $t$** is said to be **live** if, **from every reachable marking $M$**, it is **possible** to eventually fire $t$ (maybe not immediately, but after some sequence of transitions).

* Formally:

  $$
  \forall M \in R(M_0),\ \exists M' \in R(M)\ \text{such that}\ M' [t⟩
  $$

---

### 🔹 **Dead and Quasi-Live Transitions:**

* A **dead transition** is one that **can never fire again** from any reachable marking.
* A **quasi-live** transition is one that **can fire at least once**, but **not guaranteed** to be enabled again in the future.

---

### 🔹 **Net-Level Liveness:**

* A Petri Net is **live** if **every transition** in the net is live.
* This means **no transition gets permanently disabled**, regardless of the execution path.

---

### 🔎 **Why Liveness Matters:**

* Prevents **starvation** or **deadlocks**
* Ensures **all parts of the system remain usable**
* Essential in modeling **fairness**, **concurrency**, and **non-blocking systems**

---

### 📝 **In Exam: You Can Write Like This**

> A transition $t$ is said to be **live** if, from **every reachable marking**, it is **possible to eventually fire** $t$. Formally,
>
> $$
> \forall M \in R(M_0),\ \exists M' \in R(M)\ \text{such that}\ M' [t⟩
> $$
>
> * A transition is **dead** if it can **never be fired again**.
> * A transition is **quasi-live** if it can be fired **at least once**, but may not be **enabled again**.
> * A Petri Net is **live** if **all its transitions** are live.
>
> Liveness ensures **no part of the system becomes inactive or deadlocked**, which is crucial for designing **fair and responsive systems**.
