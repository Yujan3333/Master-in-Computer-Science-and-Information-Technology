#ippr #third-semester #exam-paper-answer 

Let's calculate the **CDF step by step** for **this exact numerical**.

The CDF is just the **running (cumulative) sum** of the probabilities.

The formula is

$$
CDF(r_k)=\sum_{j=0}^{k}p(r_j)
$$

---

### Given PDF

| $r_k$ | $p(r_k)$ |
| ----: | -------: |
|     0 |    0.125 |
|     1 |    0.094 |
|     2 |    0.156 |
|     3 |    0.219 |
|     4 |    0.188 |
|     5 |    0.125 |
|     6 |    0.063 |
|     7 |    0.031 |

---

# Gray level 0

The first CDF is always equal to the first probability.

$$
CDF(0)=0.125
$$

---

# Gray level 1

Add the previous CDF and the current PDF.

$$
CDF(1)=CDF(0)+p(1)
$$

$$
=0.125+0.094
$$

$$
=0.219
$$

---

# Gray level 2

Again, add the current probability.

$$
CDF(2)=CDF(1)+p(2)
$$

$$
=0.219+0.156
$$

$$
=0.375
$$

---

# Gray level 3

$$
CDF(3)=0.375+0.219
$$

$$
=0.594
$$

---

# Gray level 4

$$
CDF(4)=0.594+0.188
$$

$$
=0.782
$$

The table writes **0.781** because of rounding. Using the exact fractions would give a value very close to this.

---

# Gray level 5

$$
CDF(5)=0.782+0.125
$$

$$
=0.907
$$

Rounded in the table to

$$
0.906
$$

---

# Gray level 6

$$
CDF(6)=0.907+0.063
$$

$$
=0.970
$$

Rounded in the table to

$$
0.969
$$

---

# Gray level 7

$$
CDF(7)=0.970+0.031
$$

$$
=1.001
$$

Because the probabilities are rounded to three decimal places, the total becomes **1.001** instead of **1.000**.

The actual probabilities before rounding are

$$
\frac{8}{64},
\frac{6}{64},
\frac{10}{64},
\frac{14}{64},
\frac{12}{64},
\frac{8}{64},
\frac{4}{64},
\frac{2}{64}
$$

Their exact sum is

$$
\frac{8+6+10+14+12+8+4+2}{64}
=\frac{64}{64}
=1
$$

So the final CDF is written as

$$
1.000
$$

---

## Complete Working

| Gray Level |   PDF | CDF Calculation |             CDF |
| ---------- | ----: | --------------- | --------------: |
| 0          | 0.125 | 0.125           |           0.125 |
| 1          | 0.094 | 0.125 + 0.094   |           0.219 |
| 2          | 0.156 | 0.219 + 0.156   |           0.375 |
| 3          | 0.219 | 0.375 + 0.219   |           0.594 |
| 4          | 0.188 | 0.594 + 0.188   | 0.782 (≈ 0.781) |
| 5          | 0.125 | 0.782 + 0.125   | 0.907 (≈ 0.906) |
| 6          | 0.063 | 0.907 + 0.063   | 0.970 (≈ 0.969) |
| 7          | 0.031 | 0.970 + 0.031   |   1.001 ≈ 1.000 |

---

### Why are the last values slightly different?

The PDF values in the question are **rounded**.

For example,

$$
\frac{6}{64}=0.09375
$$

but the table writes

$$
0.094
$$

Similarly,

$$
\frac{10}{64}=0.15625
$$

is written as

$$
0.156
$$

These small rounding errors accumulate, so the intermediate CDF values differ slightly (e.g., **0.782** vs. **0.781**). In exams, this is normal—follow the rounded values given or, if you're computing from frequencies, use the exact fractions first and round only at the end.
