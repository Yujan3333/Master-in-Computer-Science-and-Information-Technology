
### 🧩 **1. Tokenization** = Breaking a sentence into words

👉 Example:

```text
Sentence: "नेपालले मलेसियालाई हरायो।"
After Tokenization: ["नेपालले", "मलेसियालाई", "हरायो"]
```

---

### 🌱 **2. Stemming** = Cutting words to their root form (roughly)

👉 It removes suffixes (but not always grammatically correct)

Example:

* "सिकाइ" → "सिक"
* "गइरहेको" → "ग"

✅ Used to make words like “गइरहेको”, “गए”, “गइरहन्छ” → "ग"

---

### 📚 **3. Lemmatization** = Reducing words to their **dictionary root form**

👉 It's more accurate than stemming.

Example:

* "गइरहेको", "गए", "गइरहन्छ" → **"जानु"**

But lemmatization is **harder in Nepali**, as it needs grammar rules and dictionaries.

---

### 🟢 Summary:

| Task          | Meaning                     | Example Input  | Output               |
| ------------- | --------------------------- | -------------- | -------------------- |
| Tokenization  | Break into words            | "नेपाल जित्यो" | \["नेपाल", "जित्यो"] |
| Stemming      | Cut words to base (roughly) | "गइरहेको"      | "ग"                  |
| Lemmatization | Find root word (accurate)   | "गइरहेको"      | "जानु"               |

---
