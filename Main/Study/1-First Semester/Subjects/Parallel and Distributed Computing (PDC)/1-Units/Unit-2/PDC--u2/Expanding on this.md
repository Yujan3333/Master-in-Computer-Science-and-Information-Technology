
## 🧠 GOAL

Given:

$$
\text{Input array } a = [a_1, a_2, \dots, a_n]
$$

We want:

$$
\text{Output: } [a_1, a_1 + a_2, a_1 + a_2 + a_3, \dots, a_1 + a_2 + \dots + a_n]
$$

But **using parallel processors** to **speed up** the computation.

---

## 🔁 LOOP OVER LOG n LEVELS

Each level $j$ performs additions over **increasing distances** of $2^j$:

| j | Distance | Meaning                       |
| - | -------- | ----------------------------- |
| 0 | 1        | Add previous element          |
| 1 | 2        | Add value two positions back  |
| 2 | 4        | Add value four positions back |
| … | …        | …                             |

At each level, you update many elements **in parallel**, using:

$$
a[i] = a[i - 2^j] + a[i]
$$

This adds in **more and more of the past values**, step by step, to build up the full prefix.

---

## 🔢 LET’S SEE A FULL EXAMPLE

### Input:

$$
a = [3, 1, 4, 2]
$$

We’ll number elements from index 1 to match your notation.

---

### 🟢 Initial:

```
Index:   1   2   3   4
Value:   3   1   4   2
```

---

### 🔁 j = 0 → Distance $2^0 = 1$

We update all $i \geq 2$:

$$
a[i] = a[i - 1] + a[i]
$$

| i | a\[i - 1] | a\[i] before | a\[i] after |
| - | --------- | ------------ | ----------- |
| 2 | a\[1] = 3 | 1            | 3 + 1 = 4   |
| 3 | a\[2] = 1 | 4            | 1 + 4 = 5   |
| 4 | a\[3] = 4 | 2            | 4 + 2 = 6   |

🔹 Updated array:

```
[3, 4, 5, 6]
```

We’ve added the **previous element** at each step.

---

### 🔁 j = 1 → Distance $2^1 = 2$

We update all $i \geq 3$:

$$
a[i] = a[i - 2] + a[i]
$$

| i | a\[i - 2] | a\[i] before | a\[i] after |
| - | --------- | ------------ | ----------- |
| 3 | a\[1] = 3 | 5            | 3 + 5 = 8   |
| 4 | a\[2] = 4 | 6            | 4 + 6 = 10  |

🔹 Updated array:

```
[3, 4, 8, 10]
```

Now:

* a\[1] = a₁
* a\[2] = a₁ + a₂
* a\[3] = a₁ + a₂ + a₃
* a\[4] = a₁ + a₂ + a₃ + a₄

✅ **Prefix sum complete!**

---

## 🔄 SO WHAT'S HAPPENING AT EACH STAGE?

At level $j$, you’re **adding to each element the value that’s $2^j$ places behind it** — this way:

* Stage 0 adds the **immediate previous value**
* Stage 1 adds the **value 2 places back**
* Stage 2 adds the **value 4 places back**
* etc.

As a result, each element keeps **accumulating the sum of more elements** before it — eventually all the way back to index 1.

---

## ⚙️ INTUITION:

* Think of it like **doubling the history window** at each step.
* First you add the last 1 element, then the last 2, then the last 4, and so on.
* After $\log_2(n)$ steps, you’ve added everything before each position.

---

## ⏱️ Why It’s Fast?

* In a **sequential loop**, you’d need $O(n)$ time.
* Here, because all additions at each stage run **in parallel**, it only takes $O(\log n)$ time!

---
