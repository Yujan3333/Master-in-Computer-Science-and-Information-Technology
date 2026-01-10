- Text clustering is an unsupervised technique that groups documents into clusters such that documents in the same cluster are more similar to each other than to those in other clusters.
- [Text Clustering More](Text%20Clustering%20More.md)

Documents

D1: *Computer Science and Information Technology*
D2: *Computer Science and Engineering*
D3: *Humanities and Social Science*
D4: *Department of Social Science*
D5: *Applications of Computer Science*

---

1. Bag of Words (Vocabulary)

First collect all unique words from all documents:

```md
BW = {
Computer, Science, and, Information, Technology, Engineering,
Humanities, Social, Department, of, Applications
}
```

(We keep each word only once.)

---

2. Remove Stop Words

Common stop words: **and, of**

After removing them:

```md
BW = {
Computer, Science, Information, Technology, Engineering,
Humanities, Social, Department, Applications
}
```

This is our final vocabulary.

Let us index them:

| Index | Word         |
| ----- | ------------ |
| w1    | Computer     |
| w2    | Science      |
| w3    | Information  |
| w4    | Technology   |
| w5    | Engineering  |
| w6    | Humanities   |
| w7    | Social       |
| w8    | Department   |
| w9    | Applications |

Total documents (N = 5)

---

3. Word Stemming

In this example, words are already in base form, so no major changes:

Computer → computer
Science → science
Applications → application (optional)

For simplicity we continue without changing form.

---

4. Term Frequency (TF)

Count how many times each word appears in each document.

| Word \ Doc   | D1  | D2  | D3  | D4  | D5  |
| ------------ | --- | --- | --- | --- | --- |
| Computer     | 1   | 1   | 0   | 0   | 1   |
| Science      | 1   | 1   | 1   | 1   | 1   |
| Information  | 1   | 0   | 0   | 0   | 0   |
| Technology   | 1   | 0   | 0   | 0   | 0   |
| Engineering  | 0   | 1   | 0   | 0   | 0   |
| Humanities   | 0   | 0   | 1   | 0   | 0   |
| Social       | 0   | 0   | 1   | 1   | 0   |
| Department   | 0   | 0   | 0   | 1   | 0   |
| Applications | 0   | 0   | 0   | 0   | 1   |

These are TF values.

---

5. Inverse Document Frequency (IDF)


$$IDF = \log\left(\frac{N}{df}\right)
$$

where
(N = 5) (number of documents)
(df =) number of documents containing the word

| Word         | df  | IDF = log(5/df) |
| ------------ | --- | --------------- |
| Computer     | 3   | log(5/3) ≈ 0.22 |
| Science      | 5   | log(5/5) = 0    |
| Information  | 1   | log(5/1) ≈ 0.70 |
| Technology   | 1   | log(5/1) ≈ 0.70 |
| Engineering  | 1   | log(5/1) ≈ 0.70 |
| Humanities   | 1   | log(5/1) ≈ 0.70 |
| Social       | 2   | log(5/2) ≈ 0.40 |
| Department   | 1   | log(5/1) ≈ 0.70 |
| Applications | 1   | log(5/1) ≈ 0.70 |

(Using log base 10 or natural log is fine; values will just scale.)

---

6. TF–IDF Calculation


$$TF\text{-}IDF = TF \times IDF
$$

Example for **D1**:

D1 has: Computer, Science, Information, Technology

| Word        | TF  | IDF  | TF–IDF |
| ----------- | --- | ---- | ------ |
| Computer    | 1   | 0.22 | 0.22   |
| Science     | 1   | 0    | 0      |
| Information | 1   | 0.70 | 0.70   |
| Technology  | 1   | 0.70 | 0.70   |
| Others      | 0   | –    | 0      |

So vector for D1:

$$
D1 = [0.22,; 0,; 0.70,; 0.70,; 0,; 0,; 0,; 0,; 0]
$$

---

Similarly:

D2: *Computer Science Engineering*


$$D2 = [0.22,; 0,; 0,; 0,; 0.70,; 0,; 0,; 0,; 0]
$$

D3: *Humanities Social Science*

$$D3 = [0,; 0,; 0,; 0,; 0,; 0.70,; 0.40,; 0,; 0]
$$

D4: *Department Social Science*


$$D4 = [0,; 0,; 0,; 0,; 0,; 0,; 0.40,; 0.70,; 0]
$$

D5: *Applications Computer Science*

$$[
D5 = [0.22,; 0,; 0,; 0,; 0,; 0,; 0,; 0,; 0.70]
]$$

---

7. Final Result

Each document is now represented as a **TF-IDF vector**:

| Document | TF-IDF Vector                        |
| -------- | ------------------------------------ |
| D1       | [0.22, 0, 0.70, 0.70, 0, 0, 0, 0, 0] |
| D2       | [0.22, 0, 0, 0, 0.70, 0, 0, 0, 0]    |
| D3       | [0, 0, 0, 0, 0, 0.70, 0.40, 0, 0]    |
| D4       | [0, 0, 0, 0, 0, 0, 0.40, 0.70, 0]    |
| D5       | [0.22, 0, 0, 0, 0, 0, 0, 0, 0.70]    |

Now these vectors can be used directly for:

* Document clustering
* Document classification
* Similarity measurement

This is the complete pipeline:
**Bag of Words → Stop Word Removal → Stemming → TF → IDF → TF-IDF → Clustering**
