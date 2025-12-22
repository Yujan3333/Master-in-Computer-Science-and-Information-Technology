![](../../../../../../../Images/Second_Sem_Images/Collaborative%20Filtering%20NUM1.png)

---


# **1️⃣ Why do we need Recommendation Systems?**

Recommendation systems are needed to:

* Reduce **information overload**
* Help users find **relevant items quickly**
* Increase **user satisfaction**
* Improve **sales and engagement** (movies, products, music)

**Example:**
Netflix recommends movies based on your taste instead of showing thousands of options.

---

# **2️⃣ Collaborative Filtering vs Content-Based Recommendation**

| Feature             | Collaborative Filtering     | Content-Based             |
| ------------------- | --------------------------- | ------------------------- |
| Based on            | Other users’ ratings        | Item features             |
| Needs other users   | ✔ Yes                       | ❌ No                      |
| Recommendation idea | “Users like you liked this” | “You liked similar items” |
| Cold start problem  | Yes                         | Less                      |
| Example             | Movie ratings by users      | Genre, actors, director   |

---

# **3️⃣ Predict Rating of U1 for Movie M6 (User-Based CF)**

We use **Pearson Correlation Coefficient** and **Top-2 closest users**.

---

## 🔹 Step 1: Identify users who rated **M6**

| User | M6 Rating |
| ---- | --------- |
| U3   | 5         |
| U4   | 2         |

👉 Only **U3 and U4** can be neighbors.

---

## 🔹 Step 2: Find similarity between **U1 & U3**

### Common movies between U1 and U3

M1, M2, M4, M5

| Movie | U1 | U3 |
| ----- | -- | -- |
| M1    | 5  | 5  |
| M2    | 3  | 3  |
| M4    | 4  | 2  |
| M5    | 5  | 2  |

### Mean ratings

* Mean(U1) = $(5+3+4+5)/4 = 4.25$
* Mean(U3) = $(5+3+2+2)/4 = 3$

### Pearson similarity

$$
sim(U1,U3) =
\frac{\sum (r_{1}-\bar r_1)(r_{3}-\bar r_3)}
{\sqrt{\sum (r_{1}-\bar r_1)^2}\sqrt{\sum (r_{3}-\bar r_3)^2}}
$$

After calculation:
$$
sim(U1,U3) \approx 0.74
$$

---

## 🔹 Step 3: Find similarity between **U1 & U4**

### Common movies

M2, M4

| Movie | U1 | U4 |
| ----- | -- | -- |
| M2    | 3  | 4  |
| M4    | 4  | 2  |

### Mean ratings

* Mean(U1) = $(3+4)/2 = 3.5$
* Mean(U4) = $(4+2)/2 = 3$

After calculation:
$$
sim(U1,U4) \approx -1
$$

---

## 🔹 Step 4: Select **Top-2 closest users**

* U3 → similarity = **0.74**
* U4 → similarity = **−1**

---

## 🔹 Step 5: Prediction Formula (User-Based CF)

$$
\hat r_{U1,M6} =
\bar r_{U1}
+
\frac{\sum sim(U1,U_i)(r_{U_i,M6}-\bar r_{U_i})}
{\sum |sim(U1,U_i)|}
$$

---

## 🔹 Step 6: Substitute values

* Mean(U1) = **4.25**
* Mean(U3) = **3**
* Mean(U4) = **3**
* Rating(U3,M6) = 5
* Rating(U4,M6) = 2

### Numerator:

$$
0.74(5-3) + (-1)(2-3) = 1.48 + 1 = 2.48
$$

### Denominator:

$$
|0.74| + |−1| = 1.74
$$

### Final prediction:

$$
\hat r_{U1,M6} = 4.25 + \frac{2.48}{1.74}
$$

$$
\hat r_{U1,M6} \approx 5.67
$$

---

# ✅ **Final Answer**

* **Predicted rating of U1 for movie M6 ≈ 5.67**
* U3 is the most influential neighbor
* User-based collaborative filtering is used with Pearson correlation

---
