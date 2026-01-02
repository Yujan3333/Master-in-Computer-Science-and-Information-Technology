## First: What does “TF-IDF contribution” mean here?

For **Naïve Bayes with TF-IDF**, each term contributes according to **its TF-IDF value in the document**.

General rule:

For a document $d$ with terms $t_1, t_2, \dots, t_k$,

$$
\text{Score}(C \mid d) \propto P(C) \times \prod_{t \in d} TF\text{-}IDF(t,d)
$$

(or sum of logs in practice).

👉 **Only terms that appear in the document contribute**.

---

## Case 1: Word does NOT occur in the document

Example: `poor` in Positive class

If a word **does not appear in the document**, then:

$$
TF(t,d) = 0
$$

So:

$$
TF\text{-}IDF(t,d) = 0 \times IDF(t) = 0
$$

### ✔ Exam interpretation

* That word contributes **nothing**
* So that term is **ignored**
* That is why we **removed the term completely**

✅ This is why we wrote:

```
poor → not present → 0 (ignored)
```

---

## Case 2: Word occurs ONCE in the document

Example: `acting` appears once in `poor acting`

Total words in document = 2

$$
TF(\text{acting}) = \frac{1}{2}
$$

So:

$$
TF\text{-}IDF(\text{acting}) = \frac{1}{2} \log\left(\frac{5}{2}\right)
$$

This term **contributes once**.

---

## Case 3: Word occurs MULTIPLE times in the document (THIS is your doubt 🔥)

### Suppose test document was:

```
poor acting acting
```

Total words = 3

Occurrences:

* `acting` = 2 times
* `poor` = 1 time

---

### TF calculation

$$
TF(\text{acting}) = \frac{2}{3}
$$

$$
TF(\text{poor}) = \frac{1}{3}
$$

---

### TF-IDF values

$$
TF\text{-}IDF(\text{acting}) = \frac{2}{3} \log\left(\frac{5}{2}\right)
$$

$$
TF\text{-}IDF(\text{poor}) = \frac{1}{3} \log(5)
$$

---

### 🔹 Class-wise sum (Negative class)

Now **both words contribute**, weighted by frequency:

$$
\text{Sum}_{-} =
\frac{2}{3} \log\left(\frac{5}{2}\right)
+
\frac{1}{3} \log(5)
$$

👉 **More occurrences ⇒ higher TF ⇒ larger contribution**

---

## Case 4: Word occurs MULTIPLE times in training but ONCE in test

⚠️ Important exam point:

* TF is computed **from the test document**
* NOT from how many times the word appears in the class

So even if:

* `acting` appears many times in training
* but once in test document

Its contribution is still:

$$
TF(\text{acting}) = \frac{1}{\text{total words in test doc}}
$$

---

## Why we “removed” terms in Positive class?

In **Step 8**, we were NOT saying:

> “The word doesn’t exist in positive class”

We were saying:

> **The word does not appear in the test document**

So:

* No TF
* No TF-IDF
* No contribution

That’s why:

$$
\text{Sum}_{+} = \frac{1}{2} \log\left(\frac{5}{2}\right)
$$

and **not**

$$
\frac{1}{2} \log(5) + \frac{1}{2} \log\left(\frac{5}{2}\right)
$$

---

## One-line exam rule ⭐

> **In TF-IDF, a term contributes only if it appears in the document.
> Multiple occurrences increase TF proportionally; zero occurrence removes the term completely.**

---

