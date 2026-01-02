Example: Consider the following training set. Train the Naïve Bayes classifier and predict class label of the last one. (use Count Vectorization).
![](../../../../../../../Images/Second_Sem_Images/Numerical%20TF-IDF-table.png)

---
## Given Training Set

| Doc ID | Text                           | Class |
| ------ | ------------------------------ | ----- |
| 1      | I loved the movie              | +     |
| 2      | I hated the movie              | −     |
| 3      | A great movie. Very good movie | +     |
| 4      | Poor acting                    | −     |
| 5      | Great acting. Good movie       | +     |
| 6      | Very poor acting               | ?     |

Goal: **Train Naïve Bayes and predict the class of Document 6** using **Count Vectorization**.

---

## Step 1: Text Preprocessing (Assumed)

* Convert to lowercase
* Remove stop words: *i, the, a, very*
* No stemming (not specified)

---

## Step 2: Preprocessed Documents

### Positive Class (+)

Doc 1: `loved movie`
Doc 3: `great movie good movie`
Doc 5: `great acting good movie`

---

### Negative Class (−)

Doc 2: `hated movie`
Doc 4: `poor acting`

---

### Test Document

Doc 6: `poor acting`

---

## Step 3: Vocabulary Construction

Unique words from training data:

$$
V = {\text{loved, movie, hated, great, good, poor, acting}}
$$

Vocabulary size:

$$
|V| = 7
$$

---

## Step 4: Class Prior Probabilities

Total training documents $= 5$

Positive documents $= 3$
Negative documents $= 2$

$$
P(+) = \frac{3}{5}
$$

$$
P(-) = \frac{2}{5}
$$

---

## Step 5: Count Vectorization (Word Frequencies)

### Word Counts in Positive Class (+)

| Word   | Count |
| ------ | ----- |
| loved  | 1     |
| movie  | 3     |
| great  | 2     |
| good   | 2     |
| acting | 1     |

Total words in positive class:

$$
N_+ = 1 + 3 + 2 + 2 + 1 = 9
$$

---

### Word Counts in Negative Class (−)

| Word   | Count |
| ------ | ----- |
| hated  | 1     |
| movie  | 1     |
| poor   | 1     |
| acting | 1     |

Total words in negative class:

$$
N_- = 4
$$

---

## Step 6: Likelihood Calculation (Laplace Smoothing)

Formula:

$$
P(w \mid C) = \frac{\text{count}(w,C) + 1}{N_+ + |V|}
$$

---

## Step 7: Likelihoods for Test Document Words

Test document words:

$$
d = {\text{poor, acting}}
$$

---

### Likelihoods for Positive Class (+)

$$
P(\text{poor} \mid +) = \frac{0 + 1}{9 + 7} = \frac{1}{16}
$$

$$
P(\text{acting} \mid +) = \frac{1 + 1}{9 + 7} = \frac{2}{16}
$$

---

### Likelihoods for Negative Class (−)

$$
P(\text{poor} \mid -) = \frac{1 + 1}{4 + 7} = \frac{2}{11}
$$

$$
P(\text{acting} \mid -) = \frac{1 + 1}{4 + 7} = \frac{2}{11}
$$

---

## Step 8: Posterior Probability Calculation

### Positive Class (+)

$$
P(+ \mid d) \propto P(+) \times P(\text{poor} \mid +) \times P(\text{acting} \mid +)
$$

$$
= \frac{3}{5} \times \frac{1}{16} \times \frac{2}{16}
$$

$$
= \frac{6}{1280}
$$

---

### Negative Class (−)

$$
P(- \mid d) \propto P(-) \times P(\text{poor} \mid -) \times P(\text{acting} \mid -)
$$

$$
= \frac{2}{5} \times \frac{2}{11} \times \frac{2}{11}
$$

$$
= \frac{8}{605}
$$

---

## Step 9: Comparison

$$
\frac{6}{1280} \approx 0.00469
$$

$$
\frac{8}{605} \approx 0.01322
$$

Since:

$$
P(- \mid d) > P(+ \mid d)
$$

---

## ✅ Final Prediction

### **The predicted class label for Document 6 is:**

$$
\boxed{- \text{ (Negative)}}
$$

---

## ⭐ Exam Checklist (Very Important)

Always include:

* Vocabulary size
* Prior probabilities
* Laplace smoothing formula
* Likelihood and posterior calculations
* Final comparison and conclusion
