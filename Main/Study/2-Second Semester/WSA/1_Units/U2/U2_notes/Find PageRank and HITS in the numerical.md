![](../../../../../../../Images/Second_Sem_Images/Find%20PageRank%20and%20HITS%20in%20the%20numerical-que2.png)
The graph in the image has **six nodes**: A, B, C, D, E, and F.


---

## 1. 🌐 PageRank Algorithm (Iteration 2)

PageRank uses a single score for each node, representing its importance. We will use the standard **damping factor $d = 0.85$** and $N=6$.

### A. Setup: Links and Initial Ranks

* **Total Pages ($N$):** 6 (A, B, C, D, E, F)
* **Initial PageRank ($\mathbf{r}_0$):** $1/N = 1/6 \approx 0.1667$ for all pages.
* **Teleportation Component:** $\frac{1-d}{N} = \frac{1-0.85}{6} = \frac{0.15}{6} = \mathbf{0.025}$
* **Outbound Links ($L(P)$):**
    * $L(A)=2$ (to B, E)
    * $L(B)=1$ (to E)
    * $L(C)=2$ (to B, E)
    * $L(D)=2$ (to C, E)
    * $L(E)=2$ (to B, C)
    * $L(F)=2$ (to B, E)

The PageRank formula for the next iteration is:
$$PR_{k+1}(P_i) = 0.025 + 0.85 \sum_{P_j \in B_{P_i}} \frac{PR_k(P_j)}{L(P_j)}$$

### B. Iteration 1 ($\mathbf{r}_1$)

Use $PR_0 = 0.1667$ for all source pages.

| Page | In-links ($B_{P_i}$) | PageRank Calculation | $PR_1$ Value |
| :--- | :--- | :--- | :--- |
| **A** | None | $0.025 + 0.85 \times (0)$ | **0.0250** |
| **B** | A, C, E, F | $0.025 + 0.85 \times (\frac{0.1667}{2} + \frac{0.1667}{2} + \frac{0.1667}{2} + \frac{0.1667}{2})$ | $0.025 + 0.85 \times (4 \times 0.08335) \approx \mathbf{0.3072}$ |
| **C** | D, E | $0.025 + 0.85 \times (\frac{0.1667}{2} + \frac{0.1667}{2})$ | $0.025 + 0.85 \times (2 \times 0.08335) \approx \mathbf{0.1667}$ |
| **D** | None | $0.025 + 0.85 \times (0)$ | **0.0250** |
| **E** | A, B, C, D, F | $0.025 + 0.85 \times (\frac{0.1667}{2} + \frac{0.1667}{1} + \frac{0.1667}{2} + \frac{0.1667}{2} + \frac{0.1667}{2})$ | $0.025 + 0.85 \times (0.08335 + 0.1667 + 3 \times 0.08335) \approx \mathbf{0.4496}$ |
| **F** | None | $0.025 + 0.85 \times (0)$ | **0.0250** |
| **Sum** | | | $\mathbf{1.0085}$ (Slight deviation from 1.0 due to rounding) |

$$\mathbf{r}_1 \approx [0.0250, 0.3072, 0.1667, 0.0250, 0.4496, 0.0250]^T$$

### C. Iteration 2 ($\mathbf{r}_2$)

Use the $PR_1$ values from the table above for the source pages.

| Page | In-links ($B_{P_i}$) | PageRank Calculation | $PR_2$ Value |
| :--- | :--- | :--- | :--- |
| **A** | None | $0.025$ | **0.0250** |
| **B** | A, C, E, F | $0.025 + 0.85 \times (\frac{0.0250}{2} + \frac{0.1667}{2} + \frac{0.4496}{2} + \frac{0.0250}{2})$ | $0.025 + 0.85 \times (0.0125 + 0.08335 + 0.2248 + 0.0125) \approx \mathbf{0.3129}$ |
| **C** | D, E | $0.025 + 0.85 \times (\frac{0.0250}{2} + \frac{0.4496}{2})$ | $0.025 + 0.85 \times (0.0125 + 0.2248) \approx \mathbf{0.2245}$ |
| **D** | None | $0.025$ | **0.0250** |
| **E** | A, B, C, D, F | $0.025 + 0.85 \times (\frac{0.0250}{2} + \frac{0.3072}{1} + \frac{0.1667}{2} + \frac{0.0250}{2} + \frac{0.0250}{2})$ | $0.025 + 0.85 \times (0.0125 + 0.3072 + 0.08335 + 0.0125 + 0.0125) \approx \mathbf{0.3957}$ |
| **F** | None | $0.025$ | **0.0250** |

$$\mathbf{r}_2 \approx [0.0250, 0.3129, 0.2245, 0.0250, 0.3957, 0.0250]^T$$

---

## 2. 🔗 HITS Algorithm (Iteration 2)

HITS (Hyperlink-Induced Topic Search) assigns two scores: **Authority (Au)** and **Hub (H)**. We normalize the scores after each step.

### A. Setup: Initial Ranks

* **Initial Hub & Authority Scores:** $\mathbf{h}_0 = \mathbf{a}_0 = [1, 1, 1, 1, 1, 1]^T$.

### B. Iteration 1

#### 1. Authority Update ($\mathbf{a}_1$)
Authority is the sum of the **Hub scores** of all pages that link *to* the current page.

$$Au(P_i) = \sum_{P_j \to P_i} H(P_j)$$

| Page | In-links | Sum of $\mathbf{h}_0$ (1's) | $\mathbf{a}_1$ Value |
| :--- | :--- | :--- | :--- |
| **A** | None | 0 | 0 |
| **B** | A, C, E, F | $H(A)+H(C)+H(E)+H(F)$ | 4 |
| **C** | D, E | $H(D)+H(E)$ | 2 |
| **D** | None | 0 | 0 |
| **E** | A, B, C, D, F | $H(A)+H(B)+H(C)+H(D)+H(F)$ | 5 |
| **F** | None | 0 | 0 |
| **Sum** | | | $\mathbf{11}$ |

**Normalization:** Divide each $\mathbf{a}_1$ value by the square root of the sum of squares of the $\mathbf{a}_1$ vector:
$\sqrt{0^2 + 4^2 + 2^2 + 0^2 + 5^2 + 0^2} = \sqrt{16+4+25} = \sqrt{45} \approx 6.708$

$$\mathbf{a}_1 \approx [\mathbf{0}, \mathbf{0.596}, \mathbf{0.298}, \mathbf{0}, \mathbf{0.745}, \mathbf{0}]^T$$

#### 2. Hub Update ($\mathbf{h}_1$)
Hub is the sum of the **Authority scores** of all pages that the current page links *to*.

$$H(P_i) = \sum_{P_i \to P_j} Au(P_j)$$

| Page | Out-links | Sum of $\mathbf{a}_1$ | $\mathbf{h}_1$ Value |
| :--- | :--- | :--- | :--- |
| **A** | B, E | $Au(B)+Au(E)$ | $0.596 + 0.745 = 1.341$ |
| **B** | E | $Au(E)$ | $0.745$ |
| **C** | B, E | $Au(B)+Au(E)$ | $0.596 + 0.745 = 1.341$ |
| **D** | C, E | $Au(C)+Au(E)$ | $0.298 + 0.745 = 1.043$ |
| **E** | B, C | $Au(B)+Au(C)$ | $0.596 + 0.298 = 0.894$ |
| **F** | B, E | $Au(B)+Au(E)$ | $0.596 + 0.745 = 1.341$ |
| **Sum** | | | $\mathbf{6.705}$ |

**Normalization:** $\sqrt{1.341^2 + 0.745^2 + 1.341^2 + 1.043^2 + 0.894^2 + 1.341^2} = \sqrt{6.703} \approx 2.589$

$$\mathbf{h}_1 \approx [\mathbf{0.518}, \mathbf{0.288}, \mathbf{0.518}, \mathbf{0.403}, \mathbf{0.345}, \mathbf{0.518}]^T$$

### C. Iteration 2

#### 1. Authority Update ($\mathbf{a}_2$)
Use the $\mathbf{h}_1$ scores from above.

| Page | In-links | Sum of $\mathbf{h}_1$ | $\mathbf{a}_2$ Value |
| :--- | :--- | :--- | :--- |
| **A** | None | 0 | 0 |
| **B** | A, C, E, F | $0.518 + 0.518 + 0.345 + 0.518$ | 1.899 |
| **C** | D, E | $0.403 + 0.345$ | 0.748 |
| **D** | None | 0 | 0 |
| **E** | A, B, C, D, F | $0.518 + 0.288 + 0.518 + 0.403 + 0.518$ | 2.245 |
| **F** | None | 0 | 0 |
| **Sum** | | | $\mathbf{4.892}$ |

**Normalization:** $\sqrt{0^2 + 1.899^2 + 0.748^2 + 0^2 + 2.245^2 + 0^2} = \sqrt{3.606 + 0.559 + 5.040} = \sqrt{9.205} \approx 3.034$

$$\mathbf{a}_2 \approx [\mathbf{0}, \mathbf{0.626}, \mathbf{0.247}, \mathbf{0}, \mathbf{0.739}, \mathbf{0}]^T$$

#### 2. Hub Update ($\mathbf{h}_2$)
Use the $\mathbf{a}_2$ scores from above.

| Page | Out-links | Sum of $\mathbf{a}_2$ | $\mathbf{h}_2$ Value |
| :--- | :--- | :--- | :--- |
| **A** | B, E | $0.626 + 0.739$ | 1.365 |
| **B** | E | $0.739$ | 0.739 |
| **C** | B, E | $0.626 + 0.739$ | 1.365 |
| **D** | C, E | $0.247 + 0.739$ | 0.986 |
| **E** | B, C | $0.626 + 0.247$ | 0.873 |
| **F** | B, E | $0.626 + 0.739$ | 1.365 |
| **Sum** | | | $\mathbf{6.693}$ |

**Normalization:** $\sqrt{1.365^2 + 0.739^2 + 1.365^2 + 0.986^2 + 0.873^2 + 1.365^2} = \sqrt{6.691} \approx 2.587$

$$\mathbf{h}_2 \approx [\mathbf{0.528}, \mathbf{0.286}, \mathbf{0.528}, \mathbf{0.381}, \mathbf{0.337}, \mathbf{0.528}]^T$$

---

## 📊 Summary of Results after Iteration 2

| Page | PageRank ($\mathbf{r}_2$) | HITS Authority ($\mathbf{a}_2$) | HITS Hub ($\mathbf{h}_2$) |
| :--- | :--- | :--- | :--- |
| **A** | 0.0250 | 0 | 0.528 |
| **B** | **0.3129** | 0.626 | 0.286 |
| **C** | 0.2245 | 0.247 | 0.528 |
| **D** | 0.0250 | 0 | 0.381 |
| **E** | **0.3957** | **0.739** | 0.337 |
| **F** | 0.0250 | 0 | 0.528 |

**Interpretation:**
* **PageRank:** **E** is the most important page, followed by B. This is because E receives a link from every page *except* itself (which is fine), and B receives links from A, C, E, and F.
* **HITS Authority:** **E** is the strongest authority, as it is pointed to by 5 out of 6 nodes (A, B, C, D, F).
* **HITS Hub:** Pages **A, C, and F** are the strongest hubs, as they link to the strongest authority (E) and to B, which is also a strong authority.