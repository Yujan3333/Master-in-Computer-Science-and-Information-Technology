## Algorithm 1
[✅ **Algorithm 1** — *All-Pairs Comparison Only (No Elimination)*](#✅%20**Algorithm%201**%20—%20*All-Pairs%20Comparison%20Only%20(No%20Elimination)*)

---
## 
---

## Algorithm 2
### 🔢 **Given:**

* A list **L** with **n elements**: $L(1), L(2), \dots, L(n)$
* You want to find the **minimum element**
* The algorithm uses **P = \frac{n(n - 1)}{2}** processors — one for **each unique pair** of elements

---

### ⚙️ **Algorithm Breakdown:**

---

#### 🧮 Step 1: **Pairwise Comparison in Parallel**

```text
Do in parallel (Total processors = n(n−1)/2)
```

* For each unique pair $(i_1, i_2)$ where $i_1 \neq i_2$, a processor $P_i$ is assigned to compare them.
* For example, with $n = 4$, the comparisons are:

  * (1,2), (1,3), (1,4)
  * (2,3), (2,4)
  * (3,4)
    → 6 total processors.

---

#### 📥 Step 2: **Each Processor Reads Pair**

```text
Pi reads value L(i1) and L(i2)
```

* Each processor reads its **assigned two values**.

---

#### ⚖️ Step 3: **Comparison and Negative Outcome**

```text
If L(i1) ≥ L(i2)
    Pi sends negative outcome to Pi1
Else
    Pi sends negative outcome to Pi2
```

* The idea is: **eliminate the larger value**.
* If $L(i_1) \geq L(i_2)$: it **eliminates i1** (sends negative signal to i1)
* If $L(i_1) < L(i_2)$: it **eliminates i2**

This is done **for every pair**, in parallel.

---

#### ✅ Step 4: **The Winner is the Only One with No Negative Outcome**

```text
At this stage, the only active processor is Pj, 1 ≤ j ≤ n, which did not receive a negative outcome
```

* After all comparisons:

  * Any element that **lost at least one comparison** (was not smaller) gets eliminated.
  * The **only one not eliminated** is the **smallest value** (the true minimum), since it’s **smaller than all others**.

---

#### 📝 Step 5: **Output the Minimum**

```text
Pj reads the value of L(j) and writes it into the output cell
```

* The remaining processor **reads its corresponding value** and **writes it as the result** (the minimum value).

---

### 🧠 **Key Concept:**

This is an example of a **parallel minimum-finding algorithm** using a **comparison network**. It's based on **pairwise elimination**: if you lose **any** comparison, you're **not the minimum**.

---

### 🧊 Visualization (n = 4):

* Input: L = \[8, 3, 5, 2]
* Pairs:

  * (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)
* Comparisons:

  * 8 vs 3 → eliminate 8
  * 8 vs 5 → already eliminated
  * 8 vs 2 → already eliminated
  * 3 vs 5 → eliminate 5
  * 3 vs 2 → eliminate 3
  * 5 vs 2 → eliminate 5
* Result: only 2 is left

---

### 🏁 Summary:

| Step | Action                                                   |
| ---- | -------------------------------------------------------- |
| 1    | Each processor compares a unique pair of elements        |
| 2    | The larger element in each pair is "eliminated"          |
| 3    | The only index not eliminated corresponds to the minimum |
| 4    | That value is written to output                          |

---
## 
---
## Difference between the 2 algorithms
Great question! You're asking about the **difference between Algorithm 1 and Algorithm 2**, both used for **finding the smallest value** from a set of $N$ values using **parallel processing**.

Let’s compare them side-by-side:

---

### ✅ Algorithm 1 — *All-Pairs Comparison Only (No Elimination)*

### 📜 Description:

> “All possible comparisons of the pairs of the elements from the set of numbers are carried out simultaneously, each processor executing one operation of comparison.”

#### ⚙️ What it does:

* Compares **all pairs** of elements in **parallel**.
* **No elimination happens** — all processors just **report the result of the comparison**.

#### 🧠 Key Characteristics:

| Feature             | Description                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------------ |
| **Processors used** | $\frac{n(n-1)}{2}$ — one for each pair                                                           |
| **Goal**            | Collect all comparison outcomes (who is smaller than whom)                                       |
| **Elimination**     | ❌ No elimination is done                                                                         |
| **Final step**      | A separate process must find which number is smaller than all others (i.e., lost no comparisons) |
| **Output**          | Requires additional step to pick the min                                                         |

---

### ✅ **Algorithm 2** — *Parallel Elimination by Negative Outcome*

### 📜 Description:

> Each pair is compared. The **larger element is eliminated** by sending it a **negative outcome**. The element that **receives no negative outcomes** is the minimum.

#### 🧠 Key Characteristics:

| Feature             | Description                                              |
| ------------------- | -------------------------------------------------------- |
| **Processors used** | $\frac{n(n-1)}{2}$ — same as Algorithm 1                 |
| **Goal**            | Eliminate non-minimum elements during comparison         |
| **Elimination**     | ✅ Yes — element receiving a "loss" is marked             |
| **Final step**      | Pick the one element with **no losses** (i.e., true min) |
| **Output**          | Direct — the non-eliminated element is the result        |

---

### 🔍 **Main Differences:**

| Feature                            | **Algorithm 1**                         | **Algorithm 2**                         |
| ---------------------------------- | --------------------------------------- | --------------------------------------- |
| Purpose of Comparison              | Only record outcomes                    | Eliminate non-minimum values            |
| Uses comparison result for action? | ❌ No (just collects data)               | ✅ Yes (eliminates losing element)       |
| Elimination of elements?           | ❌ No                                    | ✅ Yes                                   |
| Additional work needed?            | ✅ Yes — post-processing to find the min | ❌ No — result emerges directly          |
| Output clarity                     | Indirect — needs analysis               | Direct — clearly identifies the minimum |

---

## 🧠 Analogy:

### Algorithm 1:

Like a **survey** where everyone says who they’re better than — but someone else must analyze all that data to decide the winner.

### Algorithm 2:

Like a **knockout tournament** where everyone fights everyone, and if you lose even once, you're out. The one who never loses is the winner.

---

