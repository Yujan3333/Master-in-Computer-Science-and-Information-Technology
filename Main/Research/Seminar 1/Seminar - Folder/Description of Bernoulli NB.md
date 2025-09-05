
### Nepali Sentiment Analysis Using Bernoulli Naïve Bayes

A classifier is an algorithm that maps input data to a particular category. In this project, the **Bernoulli Naïve Bayes (BNB) Classifier** is used to classify Nepali text into two sentiment classes: positive and negative. BNB is a probabilistic learning method based on Bayes’ Theorem, but unlike Multinomial Naïve Bayes, it uses **binary word occurrence features** instead of word frequencies.

In the context of Nepali sentiment analysis, the input $X$ represents a preprocessed Nepali sentence. Each sentence, such as “राम्रो छ फिल्म।”, is tokenized, cleaned, and converted into a **binary feature vector** using Count Vectorizer. Here, each element $x_i$ in the vector indicates whether the $i$-th word in the vocabulary is **present (1)** or **absent (0)** in the sentence.

The model estimates the probability of a sentence belonging to each sentiment class. Words like “राम्रो” (good) increase the probability of the positive class, while words like “नराम्रो” (bad) increase the probability of the negative class. By combining the **prior probability** of each class with the **likelihood of word presence or absence**, the algorithm predicts whether a given Nepali sentence expresses positive or negative sentiment.

$$
P(C_k | X) \propto P(C_k) \prod_{i=1}^{n} P(x_i | C_k)^{x_i} (1 - P(x_i | C_k))^{1-x_i}
$$

Where:

* $x_i \in \{0,1\}$ indicates the presence or absence of the $i$-th word in the sentence.
* $P(x_i | C_k)$ is the probability that word $x_i$ occurs in class $C_k$ (Positive or Negative).
* $P(C_k)$ is the prior probability of class $C_k$.

The predicted class is the one with the **highest posterior probability**:

$$
\hat{C} = \arg\max_{C_k} P(C_k) \prod_{i=1}^{n} P(x_i | C_k)^{x_i} (1 - P(x_i | C_k))^{1-x_i}
$$

Where $\hat{C}$ is the predicted sentiment label (Positive or Negative).

---
