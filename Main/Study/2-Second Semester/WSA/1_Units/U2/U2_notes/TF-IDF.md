## 1️⃣ Why TF-IDF is needed (intuition)

* Some words appear **very often** (e.g., *the, is, and*)
* Frequent words alone are **not useful**
* A word is important if:

  * it appears **often in one document**
  * but **not in many other documents**

TF-IDF captures this idea mathematically.

---

## 2️⃣ Components of TF-IDF

### **A. Term Frequency (TF)**

Measures how frequently a term appears in a document.

[
TF(t, d) = \frac{\text{Number of times term } t \text{ appears in document } d}{\text{Total terms in document } d}
]

👉 Higher TF = term is important in that document.

---

### **B. Inverse Document Frequency (IDF)**

Measures how rare a term is across all documents.

[
IDF(t) = \log\left(\frac{N}{df(t)}\right)
]

Where:

* (N) = total number of documents
* (df(t)) = number of documents containing term (t)

👉 Rare terms get **higher IDF**.

---

## 3️⃣ TF-IDF Formula

[
TF\text{-}IDF(t, d) = TF(t, d) \times IDF(t)
]

---

## 4️⃣ Simple Example

Corpus:

1. Doc1: *"data mining techniques"*
2. Doc2: *"data science and mining"*

Word: **"data"**

* TF is high
* Appears in **both documents**
* IDF is low → TF-IDF is **low**

Word: **"techniques"**

* Appears in only one document
* IDF is high → TF-IDF is **high**

---

## 5️⃣ Key Properties

| Word Type           | TF   | IDF      | TF-IDF |
| ------------------- | ---- | -------- | ------ |
| Common word (*the*) | High | Very Low | Near 0 |
| Important keyword   | High | High     | High   |

---

## 6️⃣ Where TF-IDF is Used

* Search engines
* Document similarity
* Text classification
* Keyword extraction
* Plagiarism detection

---

## 7️⃣ Advantages

✔ Simple and effective
✔ No training required
✔ Works well for small & medium text datasets

---

## 8️⃣ Limitations

❌ Ignores word order
❌ Cannot capture meaning (semantics)
❌ Poor with synonyms & polysemy

---

### **One-line exam definition**

> **TF-IDF is a weighting scheme that assigns higher weight to terms that occur frequently in a document but rarely across the document collection.**
