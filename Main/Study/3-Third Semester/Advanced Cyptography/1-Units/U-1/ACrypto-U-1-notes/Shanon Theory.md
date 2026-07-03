#advanced-cryptography 

 **Shannon's Information Theory** and **Shannon's Cryptography Theory** are related, but they focus on different things.

| Information Theory                                              | Cryptography                                                            |
| --------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Focuses on **sending information efficiently**.                 | Focuses on **keeping information secret**.                              |
| Main problem: How to send data accurately over a noisy channel. | Main problem: How to prevent unauthorized people from reading the data. |
| Deals with communication channels and noise.                    | Deals with encryption, decryption, keys, and attackers.                 |

 ---

### Shannon's Theory in Cryptography

- *Entropy Included to?*

In **cryptography**, Claude Shannon introduced two important principles that make ciphers secure:

### 1. Confusion

* **Purpose:** Hide the relationship between the **key** and the **ciphertext**.
* Makes it difficult for an attacker to figure out the encryption key.

**Example:** Modern algorithms like **AES** use multiple substitutions to create confusion.

![](../../../../../../../Images/Third_Sem_Images/Shanon%20Theory-confusion.png)


---

### 2. Diffusion

* **Purpose:** Spread the influence of one plaintext bit over many ciphertext bits.
* A small change in the plaintext should change many bits in the ciphertext.

**Example:**

* Plaintext: `HELLO`
* Change one letter to `JELLO`
* The ciphertext changes completely.

This is called the **avalanche effect**.

![](../../../../../../../Images/Third_Sem_Images/Shanon%20Theory-Diffusion.png)

---

## Shannon's Goal in Cryptography

Shannon wanted encryption systems to:

* ✔️ Keep the message **confidential**.
* ✔️ Make it hard to discover the **key**.
* ✔️ Resist statistical attacks such as frequency analysis.

---

## Easy Way to Remember

* **Information Theory:** **Send data correctly.**
* **Cryptography Theory:** **Hide data securely.**

### Exam Point (Very Important)

**Shannon's two principles of cryptography are:**

1. **Confusion** – Hides the relationship between the key and the ciphertext.
2. **Diffusion** – Spreads the effect of each plaintext bit across many ciphertext bits.

These two principles are the foundation of many modern encryption algorithms, including **AES**.
