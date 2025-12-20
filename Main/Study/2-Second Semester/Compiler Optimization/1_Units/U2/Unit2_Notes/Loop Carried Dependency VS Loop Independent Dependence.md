- [Loop Carried Dependency](Loop%20Carried%20Dependency.md)
- [Loop Independent Dependence](Loop%20Independent%20Dependence.md)

---
## Key Differences (Exam-Friendly Table)

| Feature                  | Loop-Independent | Loop-Carried      |
| ------------------------ | ---------------- | ----------------- |
| Dependency location      | Same iteration   | Across iterations |
| Exists if loop runs once | Yes              | No                |
| Affects parallelism      | Less             | More              |
| Example                  | `A[i] → A[i]`    | `A[i-1] → A[i]`   |

---

## One-Line Memory Trick (Very Useful in Exams)

* **Loop-Independent** → *Within the same loop body*
* **Loop-Carried** → *Carried from one iteration to another*

---

## 5-Marks Answer (Ready to Write)

> **Loop-independent dependence** occurs when two statements within the same loop iteration depend on each other. The dependence exists even if the loop executes only once.
>
> **Loop-carried dependence** occurs when a statement in one iteration depends on data produced in a previous iteration. This type of dependence restricts parallel execution of loop iterations.

---

