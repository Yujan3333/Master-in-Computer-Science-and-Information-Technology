
## ✅ Given

* Domain: $D = {a,b,c,d,e}$
* Sets: $A = {a,b}$, $B = {c,d,e}$
* Relations:
  $$
  R_1 = \left\{\frac{1}{(a,c)}, \frac{1}{(a,d)}, \frac{1}{(b,e)}\right\}
  R_2 = \left\{\frac{1}{(a,d)}, \frac{1}{(a,e)}, \frac{1}{(b,e)}\right\}
  R_3 = \left\{\frac{1}{(a,d)}\right\}
  $$

> Note: The notation $\frac{1}{(x,y)}$ here represents a **fuzzy pair** with membership 1 (full membership), basically just $(x,y)$ in crisp terms.

---

## 1️⃣ Union of $R_1$ and $R_2$

**Formula**:
For fuzzy sets, union takes the **maximum membership value** for each pair. Since all pairs have membership 1, union is just the set of all unique pairs:

$$
R_1 \cup R_2 = { (a,c), (a,d), (b,e), (a,e) }
$$

**Fuzzy union formula**:

$$
\mu_{R_1 \cup R_2}(x,y) = \max{\mu_{R_1}(x,y), \mu_{R_2}(x,y)}
$$

| Pair  | $\mu_{R_1}$ | $\mu_{R_2}$ | $\mu_{R_1 \cup R_2}$ |
| ----- | ----------- | ----------- | -------------------- |
| (a,c) | 1           | 0           | max(1,0)=1           |
| (a,d) | 1           | 1           | max(1,1)=1           |
| (a,e) | 0           | 1           | max(0,1)=1           |
| (b,e) | 1           | 1           | max(1,1)=1           |
| (b,c) | 0           | 0           | 0                    |
| (b,d) | 0           | 0           | 0                    |

✅ So:

$$
R_1 \cup R_2 = \left\{\frac{1}{(a,c)}, \frac{1}{(a,d)}, \frac{1}{(a,e)}, \frac{1}{(b,e)}\right\}$$

---

## 2️⃣ Intersection of $R_1$ and $R_2$

**Formula**:
For fuzzy sets, intersection takes the **minimum membership value** for each pair. Again, since all memberships are 1, it’s just the pairs **common to both**:

$$
R_1 \cap R_2 = { (a,d), (b,e) }
$$

**Fuzzy intersection formula**:

$$
\mu_{R_1 \cap R_2}(x,y) = \min{\mu_{R_1}(x,y), \mu_{R_2}(x,y)}
$$

**Step-by-step**:

| Pair  | $\mu_{R_1}$ | $\mu_{R_2}$ | $\mu_{R_1 \cap R_2}$ |
| ----- | ----------- | ----------- | -------------------- |
| (a,c) | 1           | 0           | min(1,0)=0           |
| (a,d) | 1           | 1           | min(1,1)=1           |
| (a,e) | 0           | 1           | min(0,1)=0           |
| (b,e) | 1           | 1           | min(1,1)=1           |
| (b,c) | 0           | 0           | 0                    |
| (b,d) | 0           | 0           | 0                    |


✅ So:

$$
  R_1 \cap R_2 = \left\{ \frac{1}{(a,d)}, \frac{1}{(b,e)} \right\}
  $$

---

## 3️⃣ Check if $R_3 \subseteq R_1$

* $R_3 = { (a,d) }$
* $R_1 = { (a,c), (a,d), (b,e) }$

**Check**: Is every element of $R_3$ in $R_1$?

* $(a,d) \in R_1$ ✅

So:

$$
R_3 \subseteq R_1 \quad \text{True}
$$

---

## 4️⃣ Check if $R_3 \subseteq R_2$

* $R_3 = { (a,d) }$
* $R_2 = { (a,d), (a,e), (b,e) }$


**Fuzzy subset formula**:

$$
R_3 \subseteq R_1 \quad \text{iff} \quad \mu_{R_3}(x,y) \le \mu_{R_1}(x,y) \quad \forall (x,y)
$$

* $(a,d)$: $\mu_{R_3}(a,d)=1 \le \mu_{R_1}(a,d)=1$ ✅

So:

$$
R_3 \subseteq R_1 \quad \text{True}
$$

Similarly:

* $(a,d)$: $\mu_{R_3}(a,d)=1 \le \mu_{R_2}(a,d)=1$ ✅

So:

$$
R_3 \subseteq R_2 \quad \text{True}
$$

---

### ✅ Summary

| Operation           | Result                           |
| ------------------- | -------------------------------- |
| $R_1 \cup R_2$      | ${ (a,c), (a,d), (a,e), (b,e) }$ |
| $R_1 \cap R_2$      | ${ (a,d), (b,e) }$               |
| $R_3 \subseteq R_1$ | True                             |
| $R_3 \subseteq R_2$ | True                             |

---
