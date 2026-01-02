![](../../../../../../../Images/Second_Sem_Images/Numerical%20TF-IDF-table.png)
==Here the difference is that Document 6 is different then the picture==

---
## New Test Document

```
Doc6 - very poor movie and acting
```

---

## Step 1: Preprocessing

Remove stop words: `very`, `and`

So the test document becomes:

```
poor movie acting
```

Total words in test document:

$$
|d| = 3
$$

---

## Step 2: Vocabulary Reminder (same as before)

$$
V = {\text{loved, movie, hated, great, good, poor, acting}}
$$

Corpus size:

$$
N = 5
$$

---

## Step 3: Document Frequency and IDF (unchanged)

| Term   | $df(t)$ | $IDF(t)$                       |
| ------ | ------- | ------------------------------ |
| poor   | 1       | $\log(5)$                      |
| movie  | 4       | $\log\left(\frac{5}{4}\right)$ |
| acting | 2       | $\log\left(\frac{5}{2}\right)$ |

---

## Step 4: Term Frequency (TF) in Test Document

Each word appears **once** in the test document.

$$
TF(\text{poor}) = \frac{1}{3}
$$

$$
TF(\text{movie}) = \frac{1}{3}
$$

$$
TF(\text{acting}) = \frac{1}{3}
$$

---

## Step 5: TF-IDF Values for Test Document

$$
TF\text{-}IDF(\text{poor}) = \frac{1}{3}\log(5)
$$

$$
TF\text{-}IDF(\text{movie}) = \frac{1}{3}\log\left(\frac{5}{4}\right)
$$

$$
TF\text{-}IDF(\text{acting}) = \frac{1}{3}\log\left(\frac{5}{2}\right)
$$

---

## Step 6: Class Prior Probabilities

$$
P(+) = \frac{3}{5}
$$

$$
P(-) = \frac{2}{5}
$$

---

## Step 7: Class-wise TF-IDF Contributions

### Positive Class (+)

Which words exist in **positive training documents**?

* `poor` → ❌ not present
* `movie` → ✅ present
* `acting` → ✅ present

So only **movie** and **acting** contribute.

$$
\text{Sum}_{+}
==============

\frac{1}{3}\log\left(\frac{5}{4}\right)
+
\frac{1}{3}\log\left(\frac{5}{2}\right)
$$

---

### Negative Class (−)

All three words exist in **negative training documents**:

* `poor` → ✅
* `movie` → ✅
* `acting` → ✅

So all contribute.

$$
\text{Sum}_{-}
==============

\frac{1}{3}\log(5)
+
\frac{1}{3}\log\left(\frac{5}{4}\right)
+
\frac{1}{3}\log\left(\frac{5}{2}\right)
$$

---

## Step 8: Naïve Bayes Posterior (Proportional)

### Positive Class

$$
P(+ \mid d) \propto
\frac{3}{5}
\left[
\frac{1}{3}\log\left(\frac{5}{4}\right)
+
\frac{1}{3}\log\left(\frac{5}{2}\right)
\right]
$$

---

### Negative Class

$$
P(- \mid d) \propto
\frac{2}{5}
\left[
\frac{1}{3}\log(5)
+
\frac{1}{3}\log\left(\frac{5}{4}\right)
+
\frac{1}{3}\log\left(\frac{5}{2}\right)
\right]
$$

---

## Step 9: Final Comparison (Key Insight ⭐)

* $\log(5)$ is **large**
* `poor` is **strongly associated with negative class**
* Negative class gets **one extra high-IDF term**

Therefore:

$$
P(- \mid d) > P(+ \mid d)
$$

---

## ✅ Final Prediction

### **Predicted class for**

`very poor movie and acting` **is:**

$$
\boxed{- \text{ (Negative)}}
$$

---

## 🔑 One-Line Exam Rule (Very Important)

> **In TF-IDF, every word in the test document contributes proportionally to its frequency; words absent from the document contribute nothing, and rare words (high IDF) dominate the decision.**

---

