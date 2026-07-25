
#advanced-cryptography #third-semester #exam-paper-answer 
# Q. Explain the importance of the probabilities of occurrence of the letters, digrams and trigrams with suitable examples. **[10 Marks]**

## Answer

In any natural language, letters and groups of letters do **not occur with equal probability**. Some letters, pairs of letters (**digrams/bigrams**), and three-letter groups (**trigrams**) appear much more frequently than others. These statistical patterns are used in **frequency analysis** to break classical ciphers.

---

## 1. Probability of Letters (Monograms)

The probability of occurrence of a single letter is called **monogram frequency**.

For example, in English:

* High-frequency letters: **E, T, A, O, I, N**
* Low-frequency letters: **Q, X, Z, J**

### Importance

* Helps identify the plaintext letters in **monoalphabetic substitution** and **Caesar ciphers**.
* Reduces the number of possible key guesses.

### Example

If the ciphertext contains the letter **X** most frequently, it is likely to represent **E**, since **E** is the most common letter in English.

---

## 2. Probability of Digrams (Bigrams)

A **digram** is a pair of consecutive letters.

Common English digrams are:

* TH
* HE
* IN
* ER
* AN

### Importance

* Helps confirm guessed letter substitutions.
* Useful in breaking **Playfair** and **Vigenère** ciphers.
* Reveals common letter combinations.

### Example

If a ciphertext repeatedly contains **QR**, and analysis suggests **Q → T**, then **R** is likely **H**, forming the common digram **TH**.

---

## 3. Probability of Trigrams

A **trigram** is a sequence of three consecutive letters.

Common English trigrams are:

* THE
* AND
* ING
* ENT
* ION

### Importance

* Helps recognize complete words or parts of words.
* Confirms whether the decrypted text is meaningful.
* Increases the accuracy of frequency analysis.

### Example

If a repeated ciphertext pattern is believed to decrypt to **THE**, it becomes easier to determine the surrounding letters and recover the remaining plaintext.

---

## Summary

| Probability             | Examples      | Importance                                                       |
| ----------------------- | ------------- | ---------------------------------------------------------------- |
| **Letters (Monograms)** | E, T, A       | Breaks Caesar and substitution ciphers                           |
| **Digrams**             | TH, HE, IN    | Identifies common letter pairs and helps break Playfair/Vigenère |
| **Trigrams**            | THE, AND, ING | Recognizes words and validates decrypted text                    |

---

## Conclusion

The probabilities of **letters, digrams, and trigrams** provide statistical information about a language. These patterns are the basis of **frequency analysis**, making them extremely important in the cryptanalysis of classical encryption techniques.
