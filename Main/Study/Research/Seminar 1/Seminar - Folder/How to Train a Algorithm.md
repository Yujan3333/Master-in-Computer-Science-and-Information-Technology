 **"Nepali News Classification using Multinomial Naïve Bayes"**.

---

### 🧠 **What Does It Mean to Train an Algorithm?**

It means **teaching a machine** to recognize patterns by giving it examples (data) and the correct answers (labels).

---

### ✅ **Step-by-Step: How to Train an Algorithm**

Let’s train a **Multinomial Naïve Bayes** classifier to **classify Nepali news into categories** like politics, sports, entertainment, etc.

---

### 🔹 **Step 1: Collect the Dataset (Corpus)**

You need many Nepali news articles and their **labels** (category of the news).

| News Text (Nepali)      | Label         |
| ----------------------- | ------------- |
| "प्रधानमन्त्रीले..."    | Politics      |
| "नेपालले मलेसियालाई..." | Sports        |
| "नयाँ चलचित्र..."       | Entertainment |

👉 You can collect data from **online news sites** or use a **pre-collected dataset**.

---

### 🔹 **Step 2: Preprocess the Data**

Clean and prepare the text so the algorithm can understand it.

Common preprocessing:

* Remove punctuation and numbers
* Lowercase the text
* [Tokenize](Tokenization-Stemming-Lemmatization.md) (split into words)
* Remove stopwords (like "को", "ले", etc.)
* (Optional) Use [Stemming or Lemmatization](Tokenization-Stemming-Lemmatization.md)

In Python (simplified):

```python
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(news_texts)  # Convert text to numbers
```

---

### 🔹 **Step 3: Split the Data**

Split your dataset into:

* **Training data** (80%): used to teach the model
* **Testing data** (20%): used to evaluate the model

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2)
```

---

### 🔹 **Step 4: Train the Model**

Now you train the algorithm (Multinomial Naïve Bayes):

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train, y_train)
```

🔁 This is the training step: the model **learns patterns** between the news and their categories.

---

### 🔹 **Step 5: Test the Model**

Use test data to see how well your model performs:

```python
y_pred = model.predict(X_test)
```

---

### 🔹 **Step 6: Evaluate the Model**

Check accuracy and performance:

```python
from sklearn.metrics import accuracy_score, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

---

### 🎯 Summary

| Step         | What You Do                                     |
| ------------ | ----------------------------------------------- |
| 1. Dataset   | Collect and label Nepali news                   |
| 2. Clean     | Preprocess: clean, tokenize, remove stopwords   |
| 3. Vectorize | Convert text to numbers using `CountVectorizer` |
| 4. Train     | Use `.fit()` to train Naïve Bayes model         |
| 5. Test      | Use `.predict()` to predict on new data         |
| 6. Evaluate  | Use `accuracy_score` or `classification_report` |

---
