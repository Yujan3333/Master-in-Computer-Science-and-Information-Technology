**Text Preprocessing and Feature Vector Representation**

Text preprocessing is a vital step in preparing textual data for machine learning models. By cleaning the data, it enhances classifier performance and speeds up the classification process. Key techniques include **stop word removal**, **tokenization**, and the removal of symbols and numbers.

***

### Preprocessing Techniques

**1. Stop Word Removal**

Stop words are common, frequently occurring words like determiners, conjunctions, and postpositions that often lack significant meaning for information retrieval. While standard stop word lists are available for languages like English, a definitive list for the Nepali language is not. Examples of Nepali stop words include **यो** (this), **र** (and), and **हरु** (plural marker).

**2. Tokenization**

Tokenization is the process of breaking down a continuous string of text into smaller units called **tokens**. These tokens can be words, sentences, or other character sequences used for text analysis. In Nepali, word-level tokenization is common as words are typically separated by spaces.

**3. Symbol and Number Removal**

Symbols and numbers, while useful for text organization, are generally removed from documents before model training as they do not contribute to the text's semantic meaning. Examples of such characters in Nepali include **!**, **?**, **।**, and the numerals **०** to **९**.

***

### Feature Vector Representation

**Feature vector representation** converts text into a numerical format, which is essential for machine learning algorithms. This process improves model scalability, efficiency, and accuracy. Popular methods include **Bag of Words**, **Word2vec**, and **TF-IDF**.

**Term Frequency-Inverse Document Frequency (TF-IDF)**

**TF-IDF** is a widely used statistical method that quantifies the importance of a word within a document relative to a collection of documents. It's particularly useful for languages with complex word segmentation, like Nepali. TF-IDF is composed of two main parts:

* **Term Frequency (TF):** This measures how often a term appears in a document. A higher frequency indicates a greater importance of the term within that specific document. It is calculated as:
    $TF = \frac{\text{Number of times a term appears in a document}}{\text{Total number of words in the document}}$
* **Inverse Document Frequency (IDF):** This measures how rare or common a word is across all documents in a collection. Words that appear in many documents have a low IDF score, while rare words have a high IDF score, making them more significant. It is calculated as:
    $IDF = \log_e \left( \frac{\text{Total number of documents}}{\text{Number of documents containing the term}} \right)$

The final **TF-IDF** value for a word is the product of its TF and IDF scores:

$TF-IDF = TF \times IDF$

The process of TF-IDF vectorization involves identifying unique words in the entire dataset, creating a zero-filled vector for each sentence, and then updating each vector with the calculated TF-IDF value for each word.