You're now referring to the **schedule length**, also known as the **makespan** — an important metric in parallel task scheduling.

Let’s break it down step by step:

---

## 🧠 **What is Schedule Length (Makespan)?**

> The **schedule length** is the **total time** it takes to complete **all tasks**, i.e., the **time when the last task finishes**.

---

### 🧮 **Formal Definition**

Given a schedule function:

$$
f(i) = (j, t)
$$

This means:

* Task $i$ starts at **time $t$** on **processor $P_j$**
* $T_{ij}$: is the **execution time** of task $i$ on processor $P_j$

Then the **schedule length** (or **makespan**) is:

$$
\text{length}(f) = \max \{ t + T_{ij} \;|\; f(i) = (j, t) \}
$$

---

### 🧾 **Explanation**

* For **each task $i$**:

  * You look at when it **starts**: $t$
  * Add how long it **runs**: $T_{ij}$
  * That gives its **finish time**
* Take the **maximum** of all finish times → that is the total **schedule length**

---

### ✅ Why It's Important

* It tells you how **efficient** your schedule is
* Goal of most scheduling algorithms: **minimize the makespan**
* Lower makespan = faster program execution = better processor utilization

---

### 🧠 Example

| Task | Processor | Start Time (t) | Execution Time (T) | Finish Time $t + T$ |
| ---- | --------- | -------------- | ------------------ | ------------------- |
| T1   | P1        | 0              | 10                 | 10                  |
| T2   | P2        | 2              | 12                 | 14                  |
| T3   | P3        | 5              | 8                  | 13                  |

Then:

$$
\text{length}(f) = \max\{10, 14, 13\} = \boxed{14}
$$

---

## ✅ Summary

| Term            | Meaning                                                                                      |
| --------------- | -------------------------------------------------------------------------------------------- |
| $f(i) = (j, t)$ | Task $i$ is scheduled on $P_j$ at time $t$                                                   |
| $T_{ij}$        | Time it takes for task $i$ on processor $j$                                                  |
| **length(f)**   | The **maximum finish time** of all tasks — the total time needed to finish the full schedule |

---

