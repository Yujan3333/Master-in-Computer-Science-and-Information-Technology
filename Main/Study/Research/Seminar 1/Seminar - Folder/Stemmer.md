
## What is **stemming**?

**Stemming** is a **text preprocessing technique** in **Natural Language Processing (NLP)** where you **reduce words to their base or root form**.

✅ **Example in English:**

* “running”, “runs”, “runner” → “run”
* “studies”, “studying”, “studied” → “studi”

✅ **Example in Nepali:**

* “गरेको”, “गर्छ”, “गरिरहेका” → “गर”
* “सकिरहेको”, “सकियो”, “सकिने” → “सक”

---

### Why is stemming important?

🔹 It **reduces different forms of a word to a common base**, so the algorithm **treats them as the same feature**.
🔹 Helps **reduce vocabulary size**, making models faster and generalize better.
🔹 Useful in **sentiment analysis** so that words like “गरेको”, “गर्छ”, “गरे” are treated as the same, capturing context without duplication.

---

### How is it different from lemmatization?

| **Stemming**                         | **Lemmatization**                   |
| ------------------------------------ | ----------------------------------- |
| Chops off word endings using rules   | Uses vocabulary and grammar rules   |
| May produce non-real words (“studi”) | Produces valid root words (“study”) |
| Faster and simpler                   | Slower but more accurate            |
| E.g., “studying” → “studi”           | E.g., “studying” → “study”          |

---

### In my **Nepali Sentiment Analysis pipeline**:

✅ I used:

```python
from snowballstemmer import NepaliStemmer
```

to **stem Nepali words before vectorization**, reducing inflectional variations in your dataset.

### [NepaliStemmer](https://github.com/SushilShrestha/NepaliStemmer?tab=readme-ov-file)
---

## Summary:

> **Stemming = Cutting words to their root form to reduce vocabulary size and treat similar words as the same during NLP tasks like sentiment analysis.**

---
