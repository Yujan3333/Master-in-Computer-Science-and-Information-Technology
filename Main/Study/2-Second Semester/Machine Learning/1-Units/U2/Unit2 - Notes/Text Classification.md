## Text Classification
**Text classification** is a **machine learning approach** that automatically assigns open-ended text documents to one of a set of **predefined classes**.

Let

* $D = {d_1, d_2, \dots, d_N}$ be a collection of documents
* $C = {C_1, C_2, \dots, C_m}$ be the set of predefined classes

The objective of text classification is to learn a function
$f : D \rightarrow C$
that assigns each document to the most appropriate class.

---

## Multinomial Naive Bayes for Text Classification

The **Multinomial Naive Bayes (MNB)** classifier is widely used for text classification because:

* It works well with **high-dimensional sparse data**
* It assumes features represent **term frequencies**
* It is computationally efficient

Although the multinomial model assumes **integer counts**, in practice it also works well with **fractional values such as TF-IDF weights**.

### Classification Rule

Given a document $d$, the predicted class is:

$$
\hat{C} = \arg\max_{C_i} P(C_i \mid d)
$$

Using Bayes’ theorem:

$$
P(C_i \mid d) = \frac{P(d \mid C_i),P(C_i)}{P(d)}
$$

Since $P(d)$ is the same for all classes, we maximize:

$$
\hat{C} = \arg\max_{C_i} P(d \mid C_i),P(C_i)
$$

---

## General Steps in Text Classification

### 1. Stop Word Removal

Stop words are commonly occurring words such as *the, is, and, of*.
These words appear frequently in almost all documents and provide **little discriminatory power**, so they are removed to reduce noise and dimensionality.

---

### 2. Stemming

Stemming reduces words to their **root or base form**.

Examples:

* *playing → play*
* *studies → studi*

This helps:

* Reduce vocabulary size
* Treat related words as the same feature

---

### 3. Document Vector Creation

Text documents must be converted into **numerical vectors** before applying machine learning algorithms.

Two commonly used methods are:

1. **Bag-of-Words (Count Vectorization)**
2. **TF-IDF Vectorization**

---

## Bag-of-Words (BoW) / Count Vectorization

The **bag-of-words model** represents each document as a vector of word counts.

Let:

* $V = {w_1, w_2, \dots, w_k}$ be the vocabulary
* $tf_{i,j}$ be the number of times word $w_j$ appears in document $d_i$

Then the document vector is:

$$
d_i = (tf_{i,1}, tf_{i,2}, \dots, tf_{i,k})
$$

### Characteristics

* Word order is ignored
* Only word frequency matters
* Simple and effective for many tasks

---

## Term Frequency – Inverse Document Frequency (TF-IDF)

**TF-IDF** assigns weights to words based on:

* Their importance in a document
* Their rarity across the corpus

It improves over bag-of-words by **down-weighting common words** and **emphasizing informative words**.

---

## Term Frequency (TF)

Term Frequency measures how frequently a term occurs in a document.

For term $t$ in document $d$:

$$
TF(t,d) = \frac{\text{Number of times term } t \text{ appears in } d}
{\text{Total number of terms in } d}
$$

TF reflects the **local importance** of a word within a document.

---

## Inverse Document Frequency (IDF)

Inverse Document Frequency measures how important a term is across the entire corpus.

Let:

* $N$ = total number of documents
* $df(t)$ = number of documents containing term $t$

Then:

$$
IDF(t) = \log\left(\frac{N}{df(t)}\right)
$$

### Interpretation

* Rare words → high IDF
* Common words → low IDF

---

## TF-IDF Weight

The final TF-IDF weight of term $t$ in document $d$ is:

$$
TF\text{-}IDF(t,d) = TF(t,d) \times IDF(t)
$$

Each document is represented as a vector of TF-IDF weights:

$$
d = (TF\text{-}IDF(w_1,d), \dots, TF\text{-}IDF(w_k,d))
$$

---

## Use of TF-IDF with Multinomial Naive Bayes

Although Multinomial Naive Bayes theoretically assumes **integer word counts**, TF-IDF values are commonly used in practice because:

* They improve classification accuracy
* They reduce the impact of very frequent but uninformative words
* The Naive Bayes assumption still holds approximately

---

## Summary (Exam-Friendly)

* Text classification assigns documents to predefined classes
* Multinomial Naive Bayes is suitable for text data
* Preprocessing includes stop word removal and stemming
* Documents are converted into vectors using BoW or TF-IDF
* TF-IDF combines local importance (TF) and global importance (IDF)
* TF-IDF often improves classification performance over raw word counts

---