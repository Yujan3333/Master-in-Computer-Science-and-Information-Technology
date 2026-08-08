#third-semester #advanced-cryptography #assignment 
# Shift Cipher has perfect Secrecy
Based on **Cryptography: Theory and Practice**, the answer is clear and more *formal*.

---

## ❌ Does Shift Cipher Have Perfect Secrecy?

**No, the shift cipher does NOT have perfect secrecy.**

---

## 🔐 Definition (Stinson / Shannon model)

A cryptosystem has perfect secrecy if:

$$P(M=m \mid C=c) = P(M=m) \quad \forall m,c$$

👉 Meaning: observing ciphertext **does not change** the probability of any plaintext.

---

## 📌 Condition for Perfect Secrecy (from Stinson)

For perfect secrecy, it is required that:

1. $$|K| \ge |M|$$
   (Number of keys ≥ number of possible messages)

2. Keys are chosen **uniformly at random**

---

## 🔤 Apply to Shift Cipher

* Key space: $$|K| = 26$$
* Message space: $$|M| = 26^n$$ (for messages of length $n$)

👉 Clearly:
$$26 < 26^n \quad (\text{for } n \ge 2)$$

❌ So the condition $$|K| \ge |M|$$ is violated.

---

## 🚫 Conclusion from Stinson

Since the key space is **much smaller** than the message space:

* Different plaintexts can map to the same ciphertext under different keys
* Ciphertext **does leak information about plaintext**

👉 Therefore, **perfect secrecy is not achieved**

---

## 📖 Extra Insight (as emphasized in book)

* Shift cipher is **deterministic and small-key**
* It can be broken by:

  * Exhaustive search (26 keys)
  * Frequency analysis

---

## ✅ Final Exam Answer (Stinson-style)

> According to Stinson, a cryptosystem achieves perfect secrecy only if the number of keys is at least as large as the number of possible messages. In a shift cipher, the key space has only 26 elements, while the message space grows exponentially with message length. Hence, the condition for perfect secrecy is violated, and therefore, the shift cipher does not provide perfect secrecy.

---
