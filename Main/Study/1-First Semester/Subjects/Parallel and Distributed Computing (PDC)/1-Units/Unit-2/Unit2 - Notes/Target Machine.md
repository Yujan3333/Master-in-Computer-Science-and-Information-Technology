
## 🧠 **Formal Model of a Parallel Target Machine**

The machine is represented by the tuple:

$$
(P, P_{ij}, S_i, I_i, B_i, R_{ij})
$$

---

### 🔍 **Components Explained**

| Symbol                           | Description                                                                      |
| -------------------------------- | -------------------------------------------------------------------------------- |
| $P = \{ P_1, P_2, \dots, P_m \}$ | Set of **m heterogeneous processors**                                            |
| $P_{ij}$                         | **Interconnection topology matrix** (1 if Pi and Pj are connected, 0 otherwise)  |
| $S_i$                            | **Speed** of processor $P_i$ (e.g., instructions per unit time)                  |
| $I_i$                            | **Startup cost** to send a message **from** processor $P_i$                      |
| $B_i$                            | **Startup cost** to **start a process** on processor $P_i$                       |
| $R_{ij}$                         | **Transmission rate** (e.g., bytes per second) over link between $P_i$ and $P_j$ |

---

## ⏱️ **Execution Time Formula**

Let $A_k$ be the amount of computation needed to perform task $t_k$.
Then, the **execution time** of task $t_k$ on processor $P_j$ is:

$$
T_{kj} = \frac{A_k}{S_j} + B_j
$$

> ✅ **Explanation**:

* $\frac{A_k}{S_j}$: time to compute based on how fast processor $P_j$ is
* $B_j$: startup overhead for initiating task on $P_j$

---

## 📡 **Communication Time Between Processors**

If task $t_i$ (executed on $P_x$) needs to send $D_{ij}$ units of data to task $t_j$ (executed on $P_y$), the **communication time** is:

$$
C_{ij} = I_x + \frac{D_{ij}}{R_{xy}}
$$

> ✅ **Explanation**:

* $I_x$: startup time to send from $P_x$
* $R_{xy}$: bandwidth of the link between $P_x$ and $P_y$
* $D_{ij}$: size of data to be transferred

---

## 📊 Summary Table

| Parameter         | Meaning                                         |
| ----------------- | ----------------------------------------------- |
| $T_{kj}$          | Execution time of task $k$ on processor $j$     |
| $\frac{A_k}{S_j}$ | Pure computation time                           |
| $B_j$             | Process startup time                            |
| $I_j$             | Message startup time                            |
| $R_{ij}$          | Link speed between processors $P_i$ and $P_j$   |
| $D_{ij}$          | Data to be transferred from task $t_i$ to $t_j$ |

---

## ✅ Final Notes

This model helps in:

* Mapping tasks efficiently to processors
* Considering both computation and communication costs
* Designing **schedulers** for **heterogeneous** systems (like cloud or distributed computing)

---
