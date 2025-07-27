```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),       # unigrams + bigrams
    min_df=2,                 # ignore very rare words
    max_df=0.85,              # ignore overly common words
    max_features=10000        # limit feature space to reduce noise
)
X = vectorizer.fit_transform(df['cleaned'])

```

Increased the accuracy of Multinomial Naïve Bayes from `5%`.
