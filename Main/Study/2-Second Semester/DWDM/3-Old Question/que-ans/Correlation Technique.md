## 1️⃣ List of Correlation Techniques

Correlation measures the strength and direction of the relationship between two variables. Common techniques include:

Got it! You want a **compact, exam-friendly version with formulas only**, no extra text. Here’s the **essential correlation techniques with formulas**:
   
   ---
   
   ### **1️⃣ Pearson Correlation (r)** – Linear relationship
   
   $$
   r = \frac{\sum_{i=1}^{n} (X_i - \bar X)(Y_i - \bar Y)}{\sqrt{\sum_{i=1}^{n} (X_i - \bar X)^2} \sqrt{\sum_{i=1}^{n} (Y_i - \bar Y)^2}}
   $$
   
   * Range: $-1 \le r \le 1$
   
   ---
   
   ### **2️⃣ Spearman Rank Correlation (ρ)** – Monotonic relationship
   
   $$
   \rho = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2-1)}
   $$
   
   * $d_i$ = difference between ranks of $X_i$ and $Y_i$
   * $n$ = number of observations
   
   ---
   
   ### **3️⃣ Kendall’s Tau (τ)** – Ranked association
   
   $$
   \tau = \frac{(C - D)}{\frac{1}{2} n (n-1)}
   $$
   
   * $C$ = number of concordant pairs
   * $D$ = number of discordant pairs
   * $n$ = number of observations
   
   ---
   
   ### **4️⃣ Point-Biserial Correlation (r_pb)** – Continuous vs binary
   
   $$
   r_{pb} = \frac{\bar X_1 - \bar X_0}{s_X} \sqrt{\frac{n_1 n_0}{n^2}}
   $$`
   
   * $\bar X_1, \bar X_0$ = means of continuous variable for groups 1 and 0
   * $s_X$ = standard deviation of continuous variable
   * $n_1, n_0$ = size of each group
   * $n = n_1 + n_0$
   
   ---
   
   ### **5️⃣ Cramér’s V** – Categorical variables
   
   $$
   V = \sqrt{\frac{\chi^2}{n \cdot \min(k-1, r-1)}}
   $$
   
   * $\chi^2$ = chi-square statistic
   * $n$ = total observations
   * $k$ = number of columns, $r$ = number of rows
   
   ---
---

## 2️⃣ Why Correlation is Required

Correlation is important to:

1. **Understand relationships** – Know if two variables move together (positively or negatively).
2. **Feature selection in ML** – Remove redundant or highly correlated features to avoid multicollinearity.
3. **Prediction** – Strong correlations can improve predictive models.
4. **Data exploration** – Identify hidden patterns in the dataset.

---

## 3️⃣ Which Correlation Technique is Better and Why

| Technique          | When to Use                             | Pros/Why Better                                                |
| ------------------ | --------------------------------------- | -------------------------------------------------------------- |
| **Pearson**        | Linear, continuous data                 | Most widely used, simple, interpretable                        |
| **Spearman**       | Non-linear monotonic, ordinal or ranked | Handles non-linear monotonic relationships; robust to outliers |
| **Kendall’s Tau**  | Ranked data, small sample               | More accurate for small datasets, less sensitive to ties       |
| **Point-Biserial** | Binary vs continuous                    | Best for binary-continuous association                         |
| **Cramér’s V**     | Categorical variables                   | Suitable for nominal data                                      |

**✅ Bottom line:**

* If variables are **continuous and linearly related**, **Pearson correlation** is preferred.
* If relationship is **non-linear but monotonic**, use **Spearman**.
* Kendall’s Tau is more reliable for small datasets or many tied ranks.

---