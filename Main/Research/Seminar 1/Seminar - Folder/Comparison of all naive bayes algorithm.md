
### 🔎 Types of Naïve Bayes

1. **MultinomialNB**

   * Best for **word counts / TF-IDF** features.
   * Commonly used for **text classification** (like your Nepali sentiment analysis).

2. **BernoulliNB**

   * Works with **binary features** (word present = 1, absent = 0).
   * Useful if you want to see how performance changes when treating words as "present/absent" instead of frequencies.

3. **GaussianNB**

   * Assumes features are **continuous** and normally distributed.
   * Rarely used for raw text data (TF-IDF doesn’t follow Gaussian distribution).

---

### ✅ Recommendation 

* Definitely **compare with BernoulliNB** → because it’s another NB variant suited for text data.
* You **can also include GaussianNB** for completeness, but don’t expect it to perform as well (since your features are sparse and not continuous).
* If your supervisor just wants a *solid academic comparison*, doing **MultinomialNB vs BernoulliNB** is enough.
* If you want to show **thoroughness**, include all 3 (and then explain why GaussianNB is weaker in text tasks).

---

* *“Since this is a text classification task with TF-IDF features, MultinomialNB is the most suitable. However, for comparison, BernoulliNB was also tested to evaluate performance when features are treated as binary. GaussianNB was included for completeness, although it is less appropriate for sparse text features.”*

---
