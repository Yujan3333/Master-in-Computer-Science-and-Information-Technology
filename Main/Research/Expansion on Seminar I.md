## 💡 Master's Thesis Roadmap: Nepali Sentiment Analysis

Your overall goal for the thesis should be to **significantly advance the state-of-the-art for Nepali sentiment analysis** by moving beyond traditional machine learning models (like Naïve Bayes) and applying modern deep learning techniques.

### Semester 2: Deep Dive & Advanced Traditional Methods

The focus of this semester should be on improving your baseline results and comparing them with more robust traditional machine learning models.

#### **1. Enhanced Data Preprocessing**
* **Negation Handling:** Implement a rule to detect negation words (e.g., "not," "cannot") and modify the features to account for them (e.g., adding a "NOT\_" prefix to the next few words). This significantly boosts Naïve Bayes and other models.
* [cite_start]**Handling Code-Switching/Slang:** Nepali text often mixes with English (code-switching)[cite: 464, 465]. Develop techniques (like using a combined Nepali-English stop-word list or separate processing for English words) to better handle mixed-language text. [cite_start]You could also include a dictionary of common Nepali social media slang/informal text, as suggested in future recommendations[cite: 595].

#### **2. New Feature Engineering**
* **N-grams:** Currently, you use unigrams (single words). [cite_start]Experiment with **bigrams** (two-word phrases) and **trigrams** (three-word phrases) with your TF-IDF and Count Vectorizer features[cite: 551, 553]. Phrases like "धेरै राम्रो" (very good) have a stronger sentiment than the words alone.
* **Sentiment Lexicons:** Try building or finding a small Nepali sentiment lexicon (a list of words pre-scored as positive or negative) and use it as an additional feature in your models.

#### **3. Advanced Traditional Algorithms**
* **Implement and Evaluate:** Implement more powerful traditional machine learning classifiers, such as:
    * [cite_start]**Support Vector Machine (SVM)** [cite: 450, 460, 470]
    * [cite_start]**Logistic Regression (LR)** [cite: 470]
* **Comparative Analysis:** Compare the performance of MNB, BNB, SVM, and LR using your enhanced feature sets and preprocessing techniques.

| Semester Goal | Deliverable |
| :--- | :--- |
| Establish an improved baseline using advanced feature engineering and superior traditional models. | Seminar Report (or Project Report) detailing: 1. Enhanced Preprocessing (Negation, Slang). 2. Comparative results of MNB, BNB, SVM, and LR with N-gram features. |

### Semester 3: Deep Learning and State-of-the-Art Models

This is where you transition to modern, high-impact research, which is essential for a Master's thesis. You will move from traditional models to deep learning.

#### **1. Recurrent Neural Networks (RNNs)**
* [cite_start]**Long Short-Term Memory (LSTM):** Implement an LSTM model [cite: 390, 457, 594] to classify Nepali text. [cite_start]Unlike Naïve Bayes, LSTMs can understand the **sequence and context** of words, which is crucial for capturing subtle sentiment[cite: 458].
* [cite_start]**Bidirectional LSTM (BiLSTM):** Implement a BiLSTM[cite: 384, 467]. This model reads the sentence both forward and backward, capturing the full context, which usually leads to better performance than a standard LSTM.

#### **2. Advanced Deep Learning Models**
* [cite_start]**Convolutional Neural Network (CNN):** Implement a 1D CNN model for text classification[cite: 388, 457, 459]. CNNs are effective at automatically identifying important local n-gram patterns in the text.
* **Transfer Learning with BERT:** This is a key part of modern NLP. [cite_start]Since Nepali is a low-resource language [cite: 409, 436][cite_start], you can use **pre-trained BERT models** (specifically, those pre-trained on Indic languages, which include Devanagari script) and **fine-tune** them for your sentiment task[cite: 383, 594]. This is highly recommended for achieving state-of-the-art results.

#### **3. Comparison and Proposal**
* **Comprehensive Evaluation:** Evaluate all deep learning models against your best performing traditional model (likely SVM or MNB).
* **Thesis Proposal:** Develop a formal thesis proposal detailing your best-performing model (likely BiLSTM or Fine-tuned BERT) as the core contribution, and outline the remaining work.

| Semester Goal | Deliverable |
| :--- | :--- |
| Implement and evaluate deep learning architectures (LSTM, CNN, BERT) to significantly outperform the traditional baseline. | Thesis Proposal & Seminar/Project Report detailing: 1. Implementation of BiLSTM and CNN. 2. Implementation of a fine-tuned Indic/Nepali BERT model. 3. Final comparative results showing the deep learning model's superiority. |

### Semester 4: Final Thesis & Documentation

This final semester is dedicated to perfecting your best model, writing the final document, and ensuring all steps are complete.

#### **1. Optimization and Final Model**
* [cite_start]**Hyperparameter Tuning:** Fine-tune the hyperparameters of your best deep learning model (e.g., learning rate, number of layers, batch size) to squeeze out the maximum performance[cite: 594].
* [cite_start]**Model Analysis:** Conduct a deep analysis of your best model's misclassifications (e.g., looking at the confusion matrix to see where the errors lie [cite: 564, 576]) to explain *why* the model performs the way it does.

#### **2. The Final Thesis Document**
* **Refine Chapters:** Expand your existing report chapters (Introduction, Literature Review, Methodology, Implementation/Results, Conclusion, Future Recommendations) into a full-fledged thesis document.
* **Systematic Write-up:** Ensure your problem statement, objectives, and conclusions are tightly aligned with the original work and the new deep learning contributions.
* [cite_start]**Future Work:** Your current future recommendations are excellent and should be expanded upon (e.g., multi-level sentiment analysis, multi-aspect analysis, comparison with more algorithms)[cite: 471, 592, 595].

| Semester Goal | Deliverable |
| :--- | :--- |
| Complete the Master's thesis by optimizing the final model and writing the full, comprehensive document. | Final Master's Thesis Document with Defense/Presentation. |

