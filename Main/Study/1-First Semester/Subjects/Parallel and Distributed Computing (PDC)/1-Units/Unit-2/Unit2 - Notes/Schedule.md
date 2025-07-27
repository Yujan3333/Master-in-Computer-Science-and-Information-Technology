
## 🧠 **What Is a Schedule in Parallel Computing?**

A **schedule** tells:

* **Which processor** a task will run on
* **When** that task will begin execution

It must also **respect task dependencies** and **account for communication delays** between tasks assigned to different processors.

---

## 📐 **Formal Definition of Schedule**

$$
f : V \rightarrow \{1, 2, ..., m\} \times \{0, 1, ..., \infty\}
$$

Where:

* $V$: Set of **tasks** (usually nodes in a task graph)
* $f(v) = (i, t)$: Task $v$ is scheduled to start on **processor $P_i$** at **time $t$**
* $m$: Number of processors
* $t \in \mathbb{N} \cup \{0\}$: Start time of task $v$

---

## 📊 **Gantt Chart Overview**

A **Gantt chart** is a visual representation of:

* Time on the horizontal axis
* Processors on the vertical axis
* Task execution bars (usually labeled and color-coded)
* **Shaded regions** = communication delays (waiting time before task can begin due to data dependencies)

---

## 🔄 **Why Communication Delays Matter**

When:

* Task A runs on Processor $P_1$
* Task B (dependent on A) runs on Processor $P_2$

Then:

* A must **finish**, and
* The output of A must be **transferred** to $P_2$ before B can start
* This creates a **communication delay**

So the schedule must account for:

$$
\text{Start\_time}(B) \geq \text{Finish\_time}(A) + \text{Communication\_delay}
$$

---

## ✅ **Key Terms Summary**

| Term                | Meaning                                         |
| ------------------- | ----------------------------------------------- |
| $f(v)$              | Scheduling function for task $v$                |
| $P_i$               | Processor assigned to task                      |
| $t$                 | Start time of task                              |
| Communication delay | Extra time due to inter-processor data transfer |
| Gantt chart         | Visual timeline of task executions              |

---

## 📌 Use Cases

* **Multiprocessor scheduling**
* **Workflow scheduling in clouds**
* **Real-time embedded systems**
* **DAG-based parallel programming**

---
