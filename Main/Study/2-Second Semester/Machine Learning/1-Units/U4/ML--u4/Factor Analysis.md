**Factor Analysis – Exam Friendly Summary**
- [Factor Analysis - Even Simpler](Factor%20Analysis%20-%20Even%20Simpler.md)

Factor Analysis is an **unsupervised dimensionality reduction technique**.
Its aim is to **reduce many observed variables into fewer unobserved variables called factors**, which represent the **common variance** (variance due to correlation).



It is based on a **linear model**:

$$[
X = LF + E
]$$

Where:

* (X) = observed variables
* (L) = factor loadings
* (F) = factors (latent variables)
* (E) = error (unique variance)

So each observed variable is:
$$[
x_i = l_{i1}F_1 + l_{i2}F_2 + \dots + l_{ik}F_k + e_i
]$$

---

### Why Factor Analysis?

* Reduce dimensionality
* Find hidden structure in data
* Simplify interpretation
* Group correlated variables under common factors

---

## Steps in Factor Analysis (Easy to Remember: **A-D-I**)

1. **A – Adequacy Test**
2. **D – Determine number of factors**
3. **I – Interpret factors**

---

## 1. Adequacy Test (Check if FA is possible)

Before applying FA, check **factorability**.

Two tests:

### (a) Bartlett’s Test

* Checks if correlation exists
* Null hypothesis (H_0): Correlation matrix is identity (no correlation)
* We want to **reject (H_0)**
* If **p < 0.05 → suitable for factor analysis**

### (b) KMO Test (Kaiser-Meyer-Olkin)
- [KMO - Expanding On it](KMO%20-%20Expanding%20On%20it.md)
* Measures sampling adequacy
* Range: 0 to 1

| KMO value | Interpretation |
| --------- | -------------- |
| < 0.6     | Not suitable   |
| 0.6–0.7   | Acceptable     |
| 0.7–0.8   | Good           |
| 0.8–0.9   | Great          |
| > 0.9     | Excellent      |

Higher KMO → better for factor analysis

---

## 2. Determining the Number of Factors

Initially, number of factors = number of variables
But we keep only the **important factors**.

Method:

* Use **Eigenvalues**
* Rule:
  [
$$  \text{Keep factors with Eigenvalue } > 1
  ]$$
  (They explain more variance than one variable)

Also visual method: **Scree Plot**

---

## 3. Interpreting the Factors

Use **Factor Loadings**:

* Range: (-1) to (+1)
* High loading (close to ±1) → strong influence
* Low loading (close to 0) → weak influence

Meaning:

* Variables with **high loadings on same factor belong together**
* That factor represents a **common concept**

Example:

| Factor   | High Loadings On   | Meaning                    |
| -------- | ------------------ | -------------------------- |
| Factor 1 | E1, E2, E3, E4, E5 | One personality/trait      |
| Factor 2 | N1, N2, N3, N4, N5 | Another trait              |
| Factor 3 | C1, C2, C3, C4, C5 | Another trait              |
| Factor 4 | O1, O2, O3, O4, O5 | Another trait              |
| Factor 5 | A1, A2, A3, A4, A5 | Another trait              |
| Factor 6 | No strong loadings | Ignore (not interpretable) |

So we keep **5 factors**, not 6.

---

## One-Page Memory Version (For Exams)

> Factor Analysis is an unsupervised linear dimensionality reduction technique that explains correlations among observed variables using fewer latent variables called factors.

Model:
[
X = LF + E
]

Steps:

1. **Adequacy Test**

   * Bartlett’s Test: p < 0.05 → correlation exists
   * KMO Test: KMO ≥ 0.6 → data suitable

2. **Determine number of factors**

   * Use Eigenvalues
   * Keep factors with Eigenvalue > 1

3. **Interpret factors**

   * Use factor loadings (−1 to 1)
   * High loading → strong relationship
   * Group variables with high loadings under one factor
   * Drop factors with no significant loadings

---

## Short 3-Line Answer (If Very Short Question)

> Factor Analysis reduces many correlated observed variables into fewer latent factors representing common variance. It first checks data adequacy using KMO and Bartlett’s test, then selects factors using eigenvalues > 1, and finally interprets factors using factor loadings.

---

Tip to remember:
**FA = Reduce → Check (KMO + Bartlett) → Choose (Eigenvalue > 1) → Interpret (Loadings)**
