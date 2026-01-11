KMO (Kaiser–Meyer–Olkin) test tells us **how suitable our data is for factor analysis**.
That is why it is called a test of **sampling adequacy**.

Sampling adequacy means:

> Do the variables share enough common information (correlation) to form factors?

KMO compares:

* Correlation between variables
  with
* Partial correlation between variables

If:

* Correlations are high
* Partial correlations are low

→ Good for factor analysis
→ KMO value will be high

If:

* Correlations are weak
* Partial correlations are high

→ Not good for factor analysis
→ KMO value will be low

---

Intuition:

* Factor analysis works when variables are **related because of common factors**.
* KMO checks whether correlations are caused by **common factors** or are just random.

So KMO answers:

> Are my variables connected enough to extract meaningful factors?

---

KMO value ranges from **0 to 1**:

| KMO Value   | Meaning                      |
| ----------- | ---------------------------- |
| < 0.50      | Unacceptable (do not use FA) |
| 0.50 – 0.59 | Poor                         |
| 0.60 – 0.69 | Acceptable                   |
| 0.70 – 0.79 | Good                         |
| 0.80 – 0.89 | Very Good                    |
| ≥ 0.90      | Excellent                    |

Most exams say:

> **KMO ≥ 0.6 → data is adequate for factor analysis**

---

Simple example:

Suppose you have variables:

* Math, Physics, Chemistry marks

They are strongly correlated.
KMO will be high → Factor analysis is suitable.

But if you have:

* Height, Favorite color, Internet speed

They are unrelated.
KMO will be low → Factor analysis is not suitable.

---

One-line exam definition:

> KMO test measures the proportion of common variance among variables and indicates whether the data is adequate for applying factor analysis.

Even shorter:

> KMO checks whether correlations among variables are strong enough to extract meaningful factors.
