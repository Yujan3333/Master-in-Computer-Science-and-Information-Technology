- Need to Add the part taking the dataset, performing the preprocessing on the data, vectorizing the data and finally training the model and testing it. [Link to Collab](https://colab.research.google.com/drive/12MbZCIygVUTb13gSqKmkO0wMSVGFBmaj?usp=sharing)
## Web App Using `streamlit`

### 📦 1. **Install the Dependencies**

- Here `scikit-learn` also should be installed its dependency is on the `model.pkl` file

- `streamlit` for creating a simple python web app
- `joblib` to load the trained `model.pkl` and `vectorize.pkl` file
- `snowballstemmer` is to import Nepali Stemmer for preprocessing of the input data

```bash
pip install streamlit
pip install joblib
pip install snowballstemmer
pip install scikit-learn

```

---

### 📁 2. **Main  file named** `app.py`

```python
import streamlit as st
   from preprocessing_module import preprocess_text, stop_words, punctuation_words
   
   # For the pkl file of model and vectorizer
   import joblib 
   
   # Load model and vectorizer
   model = joblib.load("model.pkl")
   vectorizer = joblib.load("vectorizer.pkl")
   
   
   # Mapping for prediction output
   label_map = {-1: "Negative", 0: "Neutral", 1: "Positive"}
   
   # Streamlit Web UI
   st.title("Nepali News Sentiment Analysis")
   st.write("Enter a Nepali sentence to predict its sentiment.")
   
   # Input from user
   user_input = st.text_area("Your Nepali sentence:")
   
   # Predict button
   if st.button("Predict"):
       if user_input.strip() == "":
           st.warning("Please enter a sentence.")
       else:
           # Preprocess and predict
           cleaned = preprocess_text([user_input], stop_words, punctuation_words)[0]
           vector = vectorizer.transform([cleaned])
           prediction = model.predict(vector)[0]
           
           # Show result
           st.subheader("Results:")
           st.write("**Original:**", user_input)
           st.write("**Cleaned:**", cleaned)
           st.success(f"**Predicted Sentiment:** {label_map[prediction]}")
```

---

### 📦 3. Folder Structure

```
my_project/
│
├── app.py
├── model.pkl              # Save your trained model
├── vectorizer.pkl         # Save your vectorizer
├── preprocessing_module.py  # Your preprocess_text stop_words, and punctuations, etc.
├── nepali_stopwords.txt
├── nepali_punctuation.txt
```


### 4. Here done to load the model and vectorizer
- I created the model and vectorizer `.pkl` file using google collab and downloaded from there and trying to use in this web app
```python
# Save model
import joblib
joblib.dump(model, "model.pkl")

# Save vectorizer
joblib.dump(vectorizer, "vectorizer.pkl")
```

In `app.py`, the following part is used :

```python
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
```

### 5. Preprocessing 
- the file for the preprocessing using the snowballstemmer to import NepaliStemmer
```python
# preprocessing_module.py

from snowballstemmer import NepaliStemmer




# 🔹 Load Nepali stop words from file
with open("nepali_stopwords.txt", encoding='utf-8') as f:
    stop_words = [line.strip() for line in f if line.strip()]

# 🔹 Load Nepali punctuation from file
with open("nepali_punctuation.txt", encoding='utf-8') as f:
    punctuation_words = [line.strip() for line in f if line.strip()]

# 🔹 Preprocessing Function
def preprocess_text(sentences, stop_words, punctuation_words):
    stemmer = NepaliStemmer()
    noise_digits = "1,2,3,4,5,6,7,8,9,0,०,१,२,३,४,५,६,७,८,९".split(",")
    
    cleaned_sentences = []

    for sentence in sentences:
        words = sentence.strip().split(" ")
        new_words = []

        for word in words:
            # Skip stop words and punctuation
            if word in stop_words or word in punctuation_words:
                continue

            # Skip words containing digits
            if any(d in word for d in noise_digits):
                continue

            # Stem and clean word
            word = stemmer.stemWord(word)
            word = word.replace("(", "").replace(")", "")

            if len(word) > 1:
                new_words.append(word)

        cleaned_sentence = " ".join(new_words)
        cleaned_sentences.append(cleaned_sentence.strip())

    return cleaned_sentences

```


---

### ▶️ 6. Run the App

In terminal, run:

```bash
streamlit run app.py
```

In Browser the App will open

### 7. Sample Output from the Browser
![](../../../../../Images/First_Sem_Images/Seminar%20Web%20App-%20Image.png)

---

## 🎉 Web App Will:

* Take a Nepali sentence as input
* Clean it using your custom logic
* Predict sentiment using your trained model
* Show the result (Negative, Neutral, Positive)

---
