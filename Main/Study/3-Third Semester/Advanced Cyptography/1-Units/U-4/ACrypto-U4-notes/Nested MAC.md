#advanced-cryptography #third-semester 

# Nested MAC (Nested Message Authentication Code)

> **Exam Importance:** ⭐⭐⭐ (5 Marks)

---

# Q. What is Nested MAC? Explain its working with a neat diagram.

---

# Answer

## Definition

A **Nested MAC** is a Message Authentication Code (MAC) construction in which the MAC algorithm is **applied twice (nested)** using one or more secret keys to provide stronger security than a single MAC.

Instead of computing the MAC only once, the output of the first MAC is used as the input to a second MAC computation.

---

# Why is Nested MAC Needed?

A single MAC may be vulnerable to certain attacks depending on the underlying algorithm.

Nested MAC improves security by:

* Providing stronger authentication.
* Making forgery attacks more difficult.
* Reducing weaknesses of a single MAC computation.

---

# Working of Nested MAC

Assume:

* $M$ = Message
* $K_1$ = First secret key
* $K_2$ = Second secret key

### Step 1

Generate the first MAC.

$$
T_1 = \text{MAC}(K_1, M)
$$

---

### Step 2

Apply the MAC algorithm again to the first MAC.

$$
T = \text{MAC}(K_2, T_1)
$$

where:

* $T$ = Final Nested MAC

The sender sends:

* Message ($M$)
* Nested MAC ($T$)

---

### Step 3

The receiver performs the same two MAC computations using the shared keys.

If the computed Nested MAC matches the received Nested MAC, the message is accepted; otherwise, it is rejected.

---

# Diagram

```text id="f5kvgx"
              Sender

 Message (M)
      │
      ▼
 MAC using K1
      │
      ▼
 First MAC (T1)
      │
      ▼
 MAC using K2
      │
      ▼
 Nested MAC (T)
      │
      ├───────────────┐
      ▼               ▼
 Message (M)     Nested MAC
      (Sent Together)

====================================

             Receiver

 Message (M)
      │
      ▼
 MAC using K1
      │
      ▼
 First MAC
      │
      ▼
 MAC using K2
      │
      ▼
 Computed Nested MAC

Compare with Received Nested MAC

Equal → Accept

Not Equal → Reject
```

---

# Advantages

* Stronger security than a single MAC.
* Better resistance against forgery attacks.
* Provides authentication and integrity.
* Improves reliability of message verification.

---

# Limitations

* Requires more computation than a single MAC.
* Uses additional keys or multiple MAC operations.
* Does not provide confidentiality.
* Does not provide non-repudiation.

---

# Applications

* High-security communication systems.
* Banking and financial transactions.
* Secure network protocols.
* Military and government communication.

---

# Nested MAC vs Simple MAC

| Simple MAC                            | Nested MAC                                     |
| ------------------------------------- | ---------------------------------------------- |
| One MAC computation                   | Two MAC computations                           |
| Lower computational cost              | Higher computational cost                      |
| Provides authentication and integrity | Provides stronger authentication and integrity |
| Less resistant to some attacks        | More resistant to forgery attacks              |

---

# Key Points to Remember

* **Nested MAC = MAC applied twice.**
* The **output of the first MAC becomes the input to the second MAC.**
* Provides **authentication** and **integrity**.
* Does **not** provide **confidentiality** or **non-repudiation**.

---

# Possible TU Exam Questions

### Short Questions (2–5 Marks)

1. Define Nested MAC.
2. Why is Nested MAC more secure than a simple MAC?
3. What security services does Nested MAC provide?
4. Differentiate between a simple MAC and a Nested MAC.

---

### Memory Trick

Remember the sequence:

```text id="y7cnzi"
Message
   │
   ▼
MAC (K1)
   │
   ▼
First MAC
   │
   ▼
MAC (K2)
   │
   ▼
Final Nested MAC
```

The main idea is:

$$
T = \text{MAC}(K_2,; \text{MAC}(K_1,; M))
$$

This is why it is called a **Nested MAC**—one MAC is **nested inside another MAC**.
