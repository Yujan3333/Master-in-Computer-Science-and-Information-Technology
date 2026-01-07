![](../../../../../../../Images/Second_Sem_Images/Content%20Based%20Recommendation-que.png)

---
![](../../../../../../../Images/Second_Sem_Images/Content%20Based%20Recommendation---2.png)


---
![](../../../../../../../Images/Second_Sem_Images/Content%20Based%20Recommendation-1.png)


---

## 🔹 Given: Rating & Genre Table

| Movie | U1    | U2  | U3    | U4  | U5  | U6    | Genre    |
| ----- | ----- | --- | ----- | --- | --- | ----- | -------- |
| M1    | 1     | 1   | **?** | 1   | 1   | **?** | Romance  |
| M2    | 1     | 1   | 1     | 1   | 1   | ?     | Thriller |
| M3    | 1     | 1   | 1     | 1   | 1   | 1     | Action   |
| M4    | **?** | 1   | 1     | 1   | 1   | 1     | Romance  |
| M5    | 1     | 1   | 1     | 1   | 1   | **?** | Crime    |
| M6    | 1     | 1   | 1     | 1   | 1   | 1     | Crime    |

👉 We must **predict rating of Movie M4 for User U1**
👉 Use **Content-Based Recommendation**


---
---

## 🔹 Original Given Data (simplified)

Genres available:

* Romance
* Thriller
* Action
* Crime

Each movie belongs to **one genre** and ratings are **binary (1 = liked)**.

---

## 🔹 Step 1: Build **User Profile vectors**

A **user profile** =

> fraction of movies liked by the user in each genre

### 👉 Formula used

For a user $U$:

$\text{Genre weight} = \dfrac{\text{Number of movies liked by } U \text{ in that genre}}{\text{Total movies liked by } U}$

---

## 🔹 Step 2: Calculate **U1’s profile**

From the table, **U1 rated (liked)**:

| Movie | Genre    |
| ----- | -------- |
| M1    | Romance  |
| M2    | Thriller |
| M3    | Action   |
| M5    | Crime    |
| M6    | Crime    |

👉 Total movies liked by U1 = **5**

Now count per genre:

| Genre    | Count | Weight      |
| -------- | ----- | ----------- |
| Romance  | 1     | $1/5 = 0.2$ |
| Thriller | 1     | $1/5 = 0.2$ |
| Action   | 1     | $1/5 = 0.2$ |
| Crime    | 2     | $2/5 = 0.4$ |

✅ That gives the row:

$U1 = (0.2,;0.2,;0.2,;0.4)$

---

## 🔹 Step 3: Why other users have similar fractions

Example **U2**:

U2 liked:

* Romance (1)
* Thriller (1)
* Action (1)
* Crime (1)

Total = 4

So:

$U2 = \left(\dfrac{1}{3},;\dfrac{1}{6},;\dfrac{1}{6},;\dfrac{1}{3}\right) \approx (0.33,;0.17,;0.17,;0.33)$

Same logic applies to U3–U6.

---

## 🔹 Step 4: Represent **Movie M4 as a vector**

Movie M4 genre = **Romance**

So its genre vector is:

$M4 = (1,;0,;0,;0)$

Romance = 1, others = 0

---

## 🔹 Step 5: Cosine Similarity between **M4 and U1**

### Cosine Similarity formula

$\cos(\theta) = \dfrac{A \cdot B}{|A||B|}$

Where:

* $A = M4 = (1,0,0,0)$
* $B = U1 = (0.2,0.2,0.2,0.4)$

---

### 🔹 Dot product

$A \cdot B = (1)(0.2) = 0.2$

---

### 🔹 Magnitudes

$|M4| = \sqrt{1^2} = 1$

$|U1| = \sqrt{0.2^2 + 0.2^2 + 0.2^2 + 0.4^2} = \sqrt{0.28} \approx 0.529$

---

### 🔹 Final similarity

$\cos(M4,U1) = \dfrac{0.2}{1 \times 0.529} \approx 0.38$

✅ **Matches the image result**

---

## ✅ Final Interpretation (Exam-friendly)

* User U1 has **20% preference for Romance**
* Movie M4 is **pure Romance**
* Cosine similarity between U1 profile and M4 = **0.38**
* Hence, **M4 is moderately suitable for U1**

---

## 🔹 One-Line Exam Explanation ✍️

> The user profile is created by normalizing genre preferences, and cosine similarity is used to measure how close the movie genre vector is to the user profile.

---
