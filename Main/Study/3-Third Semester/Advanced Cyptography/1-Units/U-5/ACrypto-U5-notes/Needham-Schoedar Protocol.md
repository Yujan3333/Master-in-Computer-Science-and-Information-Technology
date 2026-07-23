#third-semester #advanced-cryptography #needham-schroeder 

- [Needham and Schroeder Protocol](https://www.youtube.com/watch?v=IqMptI99Eg8)
- [Needham-Schroeder In terms of Video](Needham-Schroeder%20In%20terms%20of%20Video.md)

---
# Needham–Schroeder Symmetric Key Distribution Scheme (SKDS)

The **Needham–Schroeder Symmetric Key Distribution Scheme (SKDS)** is a protocol that uses a **trusted Key Distribution Center (KDC)** to establish a **session key** between two users.

* Proposed by **Roger Needham** and **Michael Schroeder (1978)**.
* Used for **symmetric-key cryptography**.

---

## Purpose

To allow **Alice (A)** and **Bob (B)** to securely obtain a **shared session key** with the help of a **Key Distribution Center (KDC)**.

---

## Participants

* **A** = Alice (Initiator)
* **B** = Bob (Receiver)
* **KDC** = Trusted Key Distribution Center
* **KAB** = Session key
* **KA** = Secret key shared between Alice and KDC
* **KB** = Secret key shared between Bob and KDC

---

## Protocol Steps


### Step 1: Alice → KDC

Alice requests a session key to communicate with Bob.

```
A → KDC : A, B, NA
```

* A = Alice's identity
* B = Bob's identity
* NA = Nonce (random number)

---

### Step 2: KDC → Alice

The KDC generates a session key **KAB** and sends:

```
KDC → A :
EKA(KAB, B, NA, EKB(KAB, A))
```

Inside the encrypted message:

* Session key KAB
* Bob's identity
* Alice's nonce
* Ticket for Bob

The ticket is:

```
EKB(KAB, A)
```

Only Bob can open this ticket because it is encrypted with **KB**.

---

### Step 3: Alice → Bob

Alice forwards Bob's ticket.

```
A → B :
EKB(KAB, A)
```

Bob decrypts it and learns the session key.

---

### Step 4: Bob → Alice

Bob challenges Alice.

```
B → A :
EKAB(NB)
```

where **NB** is Bob's nonce.

---

### Step 5: Alice → Bob

Alice proves she knows the session key.

```
A → B :
EKAB(NB − 1)
```

Bob verifies the response.

Now both trust each other and use **KAB** for communication.

---

## Flow Diagram

```text
Alice                KDC                  Bob
 |                    |                    |
 |----A,B,NA--------->|                    |
 |                    |                    |
 |<--KAB,Ticket-------|                    |
 |                    |                    |
 |------Ticket---------------------------> |
 |                                         |
 |<------EKAB(NB)--------------------------|
 |                                         |
 |------EKAB(NB−1)------------------------>|
 |                                         |
Secure communication using KAB
```

---

## Advantages

* Uses a trusted KDC.
* Session keys are temporary, improving security.
* Mutual authentication between users.
* No need for users to share permanent keys with each other.

---

## Disadvantage

### Replay Attack

If an attacker steals an old **ticket** and an old session key, they may replay the ticket and impersonate Alice if the session key is still valid.

This weakness led to improvements such as the **Denning–Sacco Protocol**, which adds timestamps to prevent replay attacks.

---

# 5-Mark Exam Answer

**Needham–Schroeder Symmetric Key Distribution Scheme (SKDS)** is a protocol that uses a **Key Distribution Center (KDC)** to securely establish a temporary **session key** between two users. Alice sends a request to the KDC with a nonce. The KDC generates a session key and sends it to Alice along with a ticket encrypted for Bob. Alice forwards the ticket to Bob. Bob challenges Alice using a nonce encrypted with the session key, and Alice responds correctly to prove possession of the key. After successful authentication, both users communicate securely using the session key.

### Advantages

* Secure session key establishment
* Mutual authentication
* No permanent shared key required between users

### Disadvantage

* Vulnerable to **replay attacks** if an old session key is compromised, which is addressed by later protocols like **Denning–Sacco**.
