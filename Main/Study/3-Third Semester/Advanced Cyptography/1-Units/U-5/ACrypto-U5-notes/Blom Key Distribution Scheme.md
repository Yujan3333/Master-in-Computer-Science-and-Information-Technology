#advanced-cryptography #third-semester 

# Blom Key Distribution Scheme

## Definition

**Blom Key Distribution Scheme** is a **symmetric key pre-distribution scheme** that allows **any two users in a network to compute a common secret key** without directly exchanging it.

It was proposed by **Rolf Blom (1985)**.

---

## Purpose

The scheme enables secure communication in networks (especially sensor or wireless networks) by allowing every pair of users to establish a **unique shared key**.

---

## Basic Idea

* A **Trusted Authority (TA)** generates secret information.
* Each user receives **private key information** from the TA.
* When two users want to communicate, they use their private information to **independently compute the same shared secret key**.
* The secret key is **never transmitted** over the network.

---

## Algorithm BOOK

![](../../../../../../../Images/Third_Sem_Images/Blom%20Key%20Distribution%20Scheme.png)
![](../../../../../../../Images/Third_Sem_Images/Blom%20Key%20Distribution%20Scheme-1.png)
![](../../../../../../../Images/Third_Sem_Images/Blom%20Key%20Distribution%20Scheme-2.png)
### Example
![](../../../../../../../Images/Third_Sem_Images/Blom%20Key%20Distribution%20Scheme-3.png)
![](../../../../../../../Images/Third_Sem_Images/Blom%20Key%20Distribution%20Scheme-4.png)
![](../../../../../../../Images/Third_Sem_Images/Blom%20Key%20Distribution%20Scheme-5.png)



## Steps of Blom Scheme

### Step 1: Trusted Authority Setup

The Trusted Authority creates:

* A **public matrix** (G)
* A **secret symmetric matrix** (D)

It then computes:

$$[
A = (D \times G)^T
]$$

where:

* (D) is secret.
* (G) is public.
* (A) is used to distribute private information.

---

### Step 2: Key Distribution

For each user:

* The user receives **one row** of matrix (A) (private information).
* The corresponding **column** of matrix (G) is public.

---

### Step 3: Shared Key Computation

Suppose **Alice (User i)** and **Bob (User j)** want to communicate.

Alice computes

$$[
K_{ij}=A_i \times G_j
]$$

Bob computes

$$[
K_{ji}=A_j \times G_i
]$$

Because of the properties of the matrices,

$$[
K_{ij}=K_{ji}
]$$

Thus, both obtain **the same secret key** independently.

---

## Communication Diagram

```text
          Trusted Authority
        -----------------------
        Creates D and G
              │
      Computes A=(DG)ᵀ
              │
     -------------------------
     │                       │
 Sends row Ai          Sends row Aj
 to Alice              to Bob
     │                       │
     │                       │
Alice computes          Bob computes
Kij = Ai × Gj          Kji = Aj × Gi
     │                       │
     └────── Same Secret Key ──────┘
```

---

## Advantages

* No need to send the secret key over the network.
* Every pair of users gets a **unique shared key**.
* Efficient for large networks.
* Suitable for wireless sensor networks.

---

## Disadvantages

* Requires a trusted authority during setup.
* If too many users' secret information is compromised (more than the scheme's security threshold), the security of the system can be broken.
* Matrix computations increase implementation complexity.

---

## Applications

* Wireless sensor networks
* Ad hoc networks
* IoT devices
* Secure group communication

---

## 5-Mark Exam Answer

**Blom Key Distribution Scheme** is a symmetric key pre-distribution scheme that allows any two users in a network to compute a common secret key without transmitting it. A **Trusted Authority** generates a public matrix (G) and a secret symmetric matrix (D), computes $(A=(DG)^T)$, and distributes one row of (A) to each user. When two users communicate, each combines their private row with the other user's public column from (G) to compute the shared key. Due to the construction of the matrices, both users obtain the same secret key.

**Advantages:**

* No direct transmission of the secret key
* Unique shared key for every pair of users
* Efficient for large networks

**Disadvantages:**

* Depends on a trusted authority
* Security is lost if enough users' secret information is compromised
* More complex than basic key-sharing methods
