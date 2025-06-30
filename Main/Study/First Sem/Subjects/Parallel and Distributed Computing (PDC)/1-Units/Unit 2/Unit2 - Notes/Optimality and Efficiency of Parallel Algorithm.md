
### ✅ 1. **Work**

$$
W(N) = T(N) \times P(N)
$$

* **Work** represents the **total number of operations** done by all processors.
* It's like summing up what every processor does during the entire execution.
* If you run the algorithm in **parallel** using $P(N)$ processors for $T(N)$ time, that’s the total work.

> ⚠️ In a good parallel algorithm, work should be **close to or not worse than** the time taken by a good sequential algorithm.

---

### ✅ 2. **Speedup**

$$
\text{Speedup} = \frac{t(N)}{T(N)}
$$

Where:

* $t(N)$: time to solve the problem **sequentially**
* $T(N)$: time to solve it **in parallel** using $P(N)$ processors

🧠 **Speedup** shows how much faster your parallel version is compared to sequential.

> Ideally, we want:

$$
\text{Speedup} \approx P(N) \quad \text{(Linear speedup)}
$$

---

### ✅ 3. **Efficiency**

$$
\text{Efficiency} = \frac{\text{Speedup}}{P(N)} = \frac{t(N)}{T(N) \cdot P(N)}
$$

Efficiency tells us **how well processors are being utilized**.

| Efficiency Value | Meaning                                               |
| ---------------- | ----------------------------------------------------- |
| 1 (or 100%)      | Perfect utilization — all processors fully used       |
| < 1              | Some processors idle or doing less useful work        |
| Very low         | Poor algorithm or too many processors for small input |

---

### 🧮 Summary Table:

| Metric     | Formula                        | Meaning                          |
| ---------- | ------------------------------ | -------------------------------- |
| Work       | $W(N) = T(N) \cdot P(N)$       | Total effort of all processors   |
| Speedup    | $\frac{t(N)}{T(N)}$            | How much faster than sequential  |
| Efficiency | $\frac{t(N)}{T(N) \cdot P(N)}$ | How well processors are utilized |

---

## 📘 Example

Let’s say:

* Sequential time: $t(N) = 100$
* Parallel time: $T(N) = 20$
* Number of processors: $P(N) = 10$

Then:

* **Work**: $20 \times 10 = 200$
* **Speedup**: $100 / 20 = 5$
* **Efficiency**: $5 / 10 = 0.5$ → 50%

---
