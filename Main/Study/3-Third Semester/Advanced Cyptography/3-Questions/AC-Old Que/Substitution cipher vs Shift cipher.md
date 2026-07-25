#advanced-cryptography #third-semester #exam-paper-answer 

# Q. Define a substitution cipher and explain how it differs from the Shift cipher in terms of the key used. **[3+2]**

---

# Answer

## (a) Substitution Cipher (3 Marks)

A **Substitution Cipher** is a classical encryption technique in which each plaintext letter is replaced by another letter according to a **substitution key**. The order of the letters remains unchanged; only the letters themselves are substituted.

### Example

Plaintext:

```text
HELLO
```

Substitution Key:

```text
A → Q
B → W
C → E
...
```

Ciphertext (example):

```text
ITSSG
```

---

### Characteristics

* Replaces each character with another character.
* Uses a substitution table (permutation of the alphabet).
* Preserves the order of characters.
* More secure than the simple Shift (Caesar) cipher because there are many more possible keys.

---

## (b) Difference Between Substitution Cipher and Shift Cipher (2 Marks)

| Substitution Cipher                                                       | Shift Cipher                                                  |
| ------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Uses a **random permutation (mapping)** of the alphabet as the key.       | Uses a **single shift value** (e.g., 3) as the key.           |
| Key space is very large (approximately $$26!$$ for the English alphabet). | Key space is only **25** possible shifts (excluding shift 0). |
| More secure.                                                              | Less secure and easy to break by brute force.                 |
| Example: A→Q, B→M, C→X, ...                                               | Example: Shift every letter by 3 (A→D, B→E, C→F).             |

---

# Exam Conclusion

> A **substitution cipher** replaces each plaintext letter with another letter using a substitution key (a permutation of the alphabet). In contrast, a **shift cipher** is a special type of substitution cipher that uses only a **single numeric shift** as its key, making it much simpler and less secure.
