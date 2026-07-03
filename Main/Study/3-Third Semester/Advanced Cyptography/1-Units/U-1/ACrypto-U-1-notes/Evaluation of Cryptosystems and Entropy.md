

### Unit 1

1. **Crypto Systems**
2. **Shannon Theory**
3. **Evaluation of Cryptosystems**

   * Computational Security
   * Provable Security
   * Unconditional Security
4. **Entropy**
5. **Classical Cryptosystems**

   * Shift Cipher
   * Affine Cipher
   * Vigenère Cipher
   * Hill Cipher
   * Permutation Cipher
6. **Cryptanalysis**

   * Shift Cipher
   * Affine Cipher
   * Vigenère Cipher
   * Hill Cipher
   * Permutation Cipher

### So, does "Evaluation of Cryptosystems" include Entropy?

**No.**

From the way the syllabus is written:

* **Evaluation of Cryptosystems** includes only:

  * Computational Security
  * Provable Security
  * Unconditional Security

Then **Entropy** is listed separately, meaning it is its **own topic**.

### Why is Entropy separate?

Entropy is a concept from **Shannon's Information Theory**. It measures the **uncertainty or randomness** of information.

Although entropy is used to analyze the strength of cryptographic systems (for example, measuring the randomness of keys or passwords), it is **not itself one of the three security evaluation methods**.

### What you should study

For **Evaluation of Cryptosystems**, prepare these three:

1. **Computational Security**

   * Secure because breaking it requires an impractical amount of time or computing power.
   * Example: AES, RSA.

2. **Provable Security**

   * Security is supported by a mathematical proof based on a hard problem.
   * Example: RSA security is related to the difficulty of factoring large numbers.

3. **Unconditional (Information-Theoretic) Security**

   * Cannot be broken even if the attacker has unlimited computing power.
   * Example: One-Time Pad (when used correctly).

For **Entropy**, study separately:

* Definition
* Formula: $$(H(X) = -\sum p(x)\log_2 p(x))$$
* Meaning of entropy (measure of uncertainty/randomness)
* Examples and its importance in cryptography

### Exam Tip

If your professor asks:

> **"Explain the evaluation of cryptosystems."**

**Do not include entropy** unless the question specifically mentions it.

If the question is:

> **"Explain Shannon Theory."**

Then you can discuss **entropy**, because entropy is one of the key concepts introduced by Shannon.
