
![](../../../../../../../Images/Second_Sem_Images/Numerical%20-%20ID3-fig.png)

Construct decision tree from above data using information gain.
Predict class level of the tuple: 

*X = (age = youth, income = medium, student = yes, credit_rating = fair)*

[Completing the ID3 Numerical](Completing%20the%20ID3%20Numerical.md)

---
## Given Training Data (Class: *Buys_Computer*)

| ID | Age         | Income | Student | Credit_rating | Class |
| -- | ----------- | ------ | ------- | ------------- | ----- |
| 1  | youth       | high   | no      | fair          | no    |
| 2  | youth       | high   | no      | excellent     | no    |
| 3  | middle_aged | high   | no      | fair          | yes   |
| 4  | senior      | medium | no      | fair          | yes   |
| 5  | senior      | low    | yes     | fair          | yes   |
| 6  | senior      | low    | yes     | excellent     | no    |
| 7  | middle_aged | low    | yes     | excellent     | yes   |
| 8  | youth       | medium | no      | fair          | no    |
| 9  | youth       | low    | yes     | fair          | yes   |
| 10 | senior      | medium | yes     | fair          | yes   |
| 11 | youth       | medium | yes     | excellent     | yes   |
| 12 | middle_aged | medium | no      | excellent     | yes   |
| 13 | middle_aged | high   | yes     | fair          | yes   |
| 14 | senior      | medium | no      | excellent     | no    |

---

## Step 1: Entropy of Dataset $D$

Number of tuples = 14
Yes = 9, No = 5

$$
Entropy(D) = -\frac{9}{14}\log_2\frac{9}{14} - \frac{5}{14}\log_2\frac{5}{14}
$$

$$
Entropy(D) = 0.940
$$

---

## Step 2: Information Gain of Attributes

### 1️⃣ Attribute: **Age**

Partitions:

* **Youth** → (Yes=2, No=3)
* **Middle_aged** → (Yes=4, No=0)
* **Senior** → (Yes=3, No=2)

- [Expanding in the Information Gain of Attributes Part](Expanding%20in%20the%20Information%20Gain%20of%20Attributes%20Part.md)

Entropy calculations:

$$
Entropy(Youth) = 0.971
$$

$$
Entropy(Middle_aged) = 0
$$

$$
Entropy(Senior) = 0.971
$$

Expected entropy:

$$
Entropy_{Age}(D) = \frac{5}{14}(0.971) + \frac{4}{14}(0) + \frac{5}{14}(0.971)
$$

$$
Entropy_{Age}(D) = 0.694
$$

Information Gain:

$$
Gain(Age) = 0.940 - 0.694 = 0.246
$$

---

### 2️⃣ Attribute: **Income**

$$
Gain(Income) = 0.029
$$

---

### 3️⃣ Attribute: **Student**

$$
Gain(Student) = 0.151
$$

---

### 4️⃣ Attribute: **Credit_rating**

$$
Gain(Credit_rating) = 0.048
$$

---

## Step 3: Root Node Selection

Maximum Information Gain:

$$
Gain(Age) = 0.246 \quad \text{(Highest)}
$$

✅ **Root Node = Age**

---

## Step 4: Final Decision Tree (HERE NOT COMPLETE ONLY ROOT IS DONE)
 - [Completing the ID3 Numerical](Completing%20the%20ID3%20Numerical.md)

```
            Age
          /   |     \
      Youth Middle_aged Senior
        |        |        |
     Student    Yes   Credit_rating
     /    \           /        \
   Yes    No        Fair     Excellent
   |       |          |          |
  Yes     No         Yes        No
```

---

## Step 5: Prediction for Given Tuple

### Given Tuple:

$$
X = (age = youth,\ income = medium,\ student = yes,\ credit\_rating = fair)
$$

### Tree Traversal:

1. **Age = youth**
2. Go to **Student**
3. **Student = yes**
4. Leaf node → **Yes**

---

## ✅ Final Prediction

$$
\boxed{\text{Class = Yes}}
$$

---

### 🔹 Exam-Friendly Conclusion

> Using ID3 and Information Gain, the constructed decision tree predicts that the tuple
> $(age=youth, income=medium, student=yes, credit_rating=fair)$
> belongs to class **Yes**.

---

