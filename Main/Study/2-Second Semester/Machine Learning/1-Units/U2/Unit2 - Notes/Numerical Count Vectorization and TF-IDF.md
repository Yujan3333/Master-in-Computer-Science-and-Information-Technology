Example: Consider the following training set. Train the Naïve Bayes classifier and predict class label of the last one. (use Count Vectorization).
![](../../../../../../../Images/Second_Sem_Images/Numerical%20TF-IDF-table.png)

---
# 💡ANSWER using Count Vectorizer

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

---
---
# 💡ANSWER Using TF-IDF

## Given Training Set

| Doc | Text                           | Class |
| --- | ------------------------------ | ----- |
| 1   | I loved the movie              | +     |
| 2   | I hated the movie              | −     |
| 3   | A great movie. Very good movie | +     |
| 4   | Poor acting                    | −     |
| 5   | Great acting. Good movie       | +     |
| 6   | Very poor acting               | ?     |

Goal: **Predict the class of Document 6 using TF-IDF + Naïve Bayes**

---

## Step 1: Text Preprocessing (Assumed)

* Lowercase conversion
* Stop-word removal: *i, the, a, very*
* No stemming

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

$$
V = {\text{loved, movie, hated, great, good, poor, acting}}
$$

$$
|V| = 7
$$

---

## Step 4: TF-IDF Formula

### Term Frequency (TF)

$$
TF(t,d) = \frac{\text{count of } t \text{ in } d}{\text{total words in } d}
$$

---

### Inverse Document Frequency (IDF)

Total documents $N = 5$

$$
IDF(t) = \log\left(\frac{N}{df(t)}\right)
$$

---

## Step 5: Document Frequency and IDF

| Term   | $df(t)$ | $IDF(t)$    |
| ------ | ------- | ----------- |
| loved  | 1       | $\log(5)$   |
| hated  | 1       | $\log(5)$   |
| great  | 2       | $\log(5/2)$ |
| good   | 2       | $\log(5/2)$ |
| poor   | 1       | $\log(5)$   |
| acting | 2       | $\log(5/2)$ |
| movie  | 4       | $\log(5/4)$ |

---

## Step 6: TF-IDF of Test Document

Test document: `poor acting`
Total words $= 2$

$$
TF(\text{poor}) = \frac{1}{2}
$$

$$
TF(\text{acting}) = \frac{1}{2}
$$

---

### TF-IDF Values

$$
TF\text{-}IDF(\text{poor}) = \frac{1}{2} \log(5)
$$

$$
TF\text{-}IDF(\text{acting}) = \frac{1}{2} \log\left(\frac{5}{2}\right)
$$

---

## Step 7: Class Prior Probabilities

$$
P(+) = \frac{3}{5}
$$

$$
P(-) = \frac{2}{5}
$$

---

## Step 8: Class-wise TF-IDF Sums
- [Why is the poor removed and what happens if there are multiple occurence of the same word in the likelihood finding](Why%20is%20the%20poor%20removed%20and%20what%20happens%20if%20there%20are%20multiple%20occurence%20of%20the%20same%20word%20in%20the%20likelihood%20finding.md)

### Positive Class (+)

TF-IDF contributions:

* `poor` → not present → $0$
* `acting` → appears once

$$
\text{Sum}_{+} = \frac{1}{2} \log\left(\frac{5}{2}\right)
$$

---

### Negative Class (−)

Both words present:

$$
\text{Sum}_{-} = \frac{1}{2} \log(5) + \frac{1}{2} \log\left(\frac{5}{2}\right)
$$

---

## Step 9: Naïve Bayes Posterior (Proportional)

### Positive Class (+)

$$
P(+ \mid d) \propto P(+) \times \text{Sum}_{+}
$$

$$
= \frac{3}{5} \times \frac{1}{2} \log\left(\frac{5}{2}\right)
$$

---

### Negative Class (−)

$$
P(- \mid d) \propto P(-) \times \text{Sum}_{-}
$$

$$
= \frac{2}{5} \times \left[\frac{1}{2} \log(5) + \frac{1}{2} \log\left(\frac{5}{2}\right)\right]
$$

---

## Step 10: Comparison

Since:

$$
\log(5) + \log\left(\frac{5}{2}\right) > \log\left(\frac{5}{2}\right)
$$

and both have comparable priors,

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

## ⭐ Exam Note (Very Important)

* TF-IDF gives **higher weight to rare informative words**
* `poor` appears **only in negative class**
* Hence TF-IDF strengthens the **negative prediction**
* Multinomial Naïve Bayes works well even with **fractional TF-IDF values**

---
