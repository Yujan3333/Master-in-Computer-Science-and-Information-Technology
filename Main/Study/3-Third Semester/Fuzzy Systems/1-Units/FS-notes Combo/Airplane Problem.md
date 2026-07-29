#fuzzy-system #third-semester 

With decrease in velocity height also decrease, we need to evaluate the applied force to stop the Aircraft.

We use Mamdani inference for this problem.

**Given**

### 1) Membership values of height:

| Height (ft) | 0 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 1000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Large (L)** | 0 | 0 | 0 | 0 | 0 | 0 | 0.2 | 0.4 | 0.6 | 0.8 | 1 |
| **Medium (M)** | 0 | 0 | 0 | 0 | 0.2 | 0.4 | 0.6 | 0.8 | 1 | 0.8 | 0.6 |
| **Small (S)** | 0.4 | 0.6 | 0.8 | 1 | 0.8 | 0.6 | 0.4 | 0.2 | 0 | 0 | 0 |
| **Near Zero (NZ)** | 1 | 0.8 | 0.6 | 0.4 | 0.2 | 0 | 0 | 0 | 0 | 0 | 0 |


---

# Membership Values for Vertical Velocity

| Vertical Velocity (ft/s) | -30 | -25 | -20 | -15 | -10 |  -5 |  0  |  5  |  10 |  15 |  20 |  25 |  30 |
| -----------------------: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|  **Positive Large (PL)** |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  | 0.5 |  1  |  1  |
|  **Positive Small (PS)** |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  | 0.5 |  1  | 0.5 |  0  |  0  |
|             **Zero (Z)** |  0  |  0  |  0  |  0  |  0  |  0  | 0.5 |  1  | 0.5 |  0  |  0  |  0  |  0  |
|  **Negative Small (NS)** |  0  |  0  |  0  | 0.5 |  1  | 0.5 |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
|  **Negative Large (NL)** |  1  |  1  |  1  | 0.5 |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |

---

# Membership Values for Control Force

|      Control Force (ft) | -30 | -25 | -20 | -15 | -10 |  -5 |  0  |  5  |  10 |  15 |  20 |  25 |  30 |
| ----------------------: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **Positive Large (PL)** |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  | 0.5 |  1  |  1  |
| **Positive Small (PS)** |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  | 0.5 |  1  | 0.5 |  0  |  0  |
|            **Zero (Z)** |  0  |  0  |  0  |  0  |  0  |  0  | 0.5 |  1  | 0.5 |  0  |  0  |  0  |  0  |
| **Negative Small (NS)** |  0  |  0  |  0  | 0.5 |  1  | 0.5 |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
| **Negative Large (NL)** |  1  |  1  |  1  | 0.5 |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |

---

# Fuzzy Rule Base

| **Height** ↓ / **Velocity** → | **PL** | **PS** | **Z** | **NS** | **NL** |
| :---------------------------: | :----: | :----: | :---: | :----: | :----: |
|         **L (Large)**         |   PL   |   PS   |   Z   |   NS   |   NL   |
|         **M (Medium)**        |   PS   |    Z   |   NS  |   NL   |   NL   |
|         **S (Small)**         |    Z   |   NS   |   Z   |   NS   |   NL   |
|      **VS (Very Small)**      |    Z   |    Z   |   Z   |   NS   |   NS   |

### Linguistic Terms

* **PL** = Positive Large
* **PS** = Positive Small
* **Z** = Zero
* **NS** = Negative Small
* **NL** = Negative Large
__________

### Given

* Initial height:

$$
h_0 = 1000\ \text{ft}
$$

* Initial velocity:

$$
v_0 = -20\ \text{ft s}^{-1}
$$

* Control force:

$$
f_0 ; ? \quad \text{to be computed}
$$


---
[Airplane Problem Soln](Airplane%20Problem%20Soln.md)