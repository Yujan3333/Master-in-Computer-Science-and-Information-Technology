#third-semester #advanced-cryptography 

# One-Time Pad (OTP)

The **One-Time Pad (OTP)** is a **symmetric encryption technique** that is considered **the only encryption method that is mathematically unbreakable**, **provided it is used correctly**.

It is a **special case of the Vernam Cipher**.

---

# Simple Definition (Exam)

> **A One-Time Pad is a symmetric encryption technique in which a random secret key, equal in length to the plaintext, is used only once for encryption and decryption.**

---

# How One-Time Pad Works

Encryption:

$$
C=P\oplus K
$$

Decryption:

$$
P=C\oplus K
$$

where:

* **$P$** = Plaintext
* **$K$** = Secret key
* **$C$** = Ciphertext
* **$\oplus$** = XOR operation

---

# Conditions for a One-Time Pad

For a cipher to be a **true One-Time Pad**, all **four conditions** must be satisfied:

1. ✅ The key must be **completely random**.
2. ✅ The key length must be **equal to the plaintext length**.
3. ✅ The key must be **used only once**.
4. ✅ The key must be **kept secret**.

If any one of these conditions is violated, it is **not a true One-Time Pad**.

---

# Simple Example

- [One Time Pad using Alphabets not XOR](One%20Time%20Pad%20using%20Alphabets%20not%20XOR.md)
- [One TIme Pad using XOR](One%20TIme%20Pad%20using%20XOR.md)
Plaintext:

```text
HELLO
```

Random key:

```text
BAXYC
```

Since:

* Both have 5 letters.
* The key is random.
* The key is used only once.

This is a **One-Time Pad**.

The plaintext and key are converted into binary (or numbers), XOR is performed, and the result is the ciphertext.

To decrypt:

```text
Ciphertext ⊕ Same Key = Plaintext
```

---

# Why is it Called "One-Time Pad"?

* **One-Time** → The key is used only once.
* **Pad** → Originally, random keys were printed on paper pads. After using one page (pad), it was destroyed.

---

# Advantages

* ✔️ Provides **perfect (unconditional) security**.
* ✔️ Impossible to break by brute force or cryptanalysis if used correctly.
* ✔️ Simple encryption and decryption using XOR.

---

# Disadvantages

* ❌ Key must be as long as the message.
* ❌ Securely sharing such a long key is difficult.
* ❌ The key can **never** be reused.
* ❌ Managing large random keys is impractical.

---

# Difference Between Vernam Cipher and One-Time Pad

| Vernam Cipher                     | One-Time Pad                                |
| --------------------------------- | ------------------------------------------- |
| Uses XOR for encryption.          | Uses XOR for encryption.                    |
| Key may be reused.                | Key is used only once.                      |
| Key may not be completely random. | Key must be truly random.                   |
| Not always perfectly secure.      | Perfectly secure if all conditions are met. |

---

# Applications

Although OTP is difficult to use in everyday communication, it has been used for:

* Military communications.
* Diplomatic communications.
* High-security government communications.

---

# Exam Definition (2 Marks)

> **A One-Time Pad (OTP) is a symmetric encryption method that uses a truly random secret key of the same length as the plaintext. The key is used only once and kept secret, making OTP the only cryptographic system with perfect (unconditional) security when implemented correctly.**

---

# Easy Memory Trick ⭐

Remember the **4 R's**:

* **R**andom key
* **R**ight length (same as the message)
* **R**un once (use only once)
* **R**emain secret

If these four conditions are met, the encryption is a **true One-Time Pad** and is **unbreakable**.
