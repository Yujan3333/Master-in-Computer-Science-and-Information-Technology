### **K-grams (Simple Explanation)**

**K-grams** are **substrings of length K** extracted from a string or text. They are used in **text processing, search engines, and spelling correction** to analyze sequences of characters or words.

---

### **How it works**

* Choose a value of **K** (e.g., 2, 3, 4)
* Break the text into **all possible consecutive substrings of length K**

---

### **Example (Character-level k-grams)**

Text: `"cat"`

* **2-grams (bigrams)**: `"ca", "at"`
* **3-grams (trigrams)**: `"cat"`

Text: `"hello"`

* 2-grams: `"he", "el", "ll", "lo"`
* 3-grams: `"hel", "ell", "llo"`

---

### **Applications**

1. **Spelling correction** – find words with similar k-grams
2. **Plagiarism detection** – compare documents based on overlapping k-grams
3. **Search engines** – index substrings for fast retrieval
4. **DNA sequencing** – k-grams represent sequences of nucleotides

---

### **Exam-friendly definition**

> K-grams are all contiguous substrings of length K extracted from a string, used to analyze patterns or similarity in text.

---
