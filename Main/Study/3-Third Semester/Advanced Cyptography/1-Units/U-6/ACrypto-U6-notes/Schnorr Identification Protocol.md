
#advanced-cryptography #third-semester

# Schnorr Identification Protocol

The **Schnorr Identification Protocol** is a **zero-knowledge authentication protocol** that enables a user (the prover) to prove possession of a **secret key** without revealing the key itself.

It is based on the **Discrete Logarithm Problem (DLP)** and is considered an improvement over the Fiat–Shamir Identification Protocol because it is simpler, more efficient, and requires less communication.

---

# Main Idea

Suppose you want to log in to your bank account.

Normally, you enter your password, and the bank verifies it.

However, transmitting the password may expose it to attackers.

The Schnorr Identification Protocol allows you to prove:

> **"I know my secret key without revealing it."**

The verifier becomes convinced that you know the secret, but never learns the secret itself.

This property is called **Zero-Knowledge Authentication**.

---

# Real-Life Analogy

Imagine Alice owns a treasure chest that can only be opened with a special key.

Bob wants proof that Alice possesses the key.

Instead of showing the key, Alice:

```md
1. Performs a temporary action using the key.
2. Bob sends a random challenge.
3. Alice answers the challenge using the key.
```


If Alice consistently answers correctly, Bob is convinced she owns the key, even though he never sees it.

---

# Participants

## Prover (P)

* Claims to know the secret.
* Wants to prove their identity.

**Example:** Alice

---

## Verifier (V)

* Verifies whether the prover actually knows the secret.

**Example:** Bob

---

# Mathematical Setup

Choose:

* A large prime number **$$p$$**
* A prime number **$$q$$** such that *here is (p-1) divided by q should be satisfied* 

$$
q \mid (p-1)
$$
* [Schnorr Maths q div (p-1)](Schnorr%20Maths%20q%20div%20(p-1).md)

Choose a generator

$$
g
$$

of the subgroup.

---

Alice chooses a secret number

$$
x
$$

This is her **private key**.

She computes the corresponding **public key** as

$$
y = g^x \pmod p
$$

Therefore,

* **Private Key:** $$x$$
* **Public Key:** $$y$$

---

# Protocol Steps

The Schnorr Identification Protocol consists of **three message exchanges**.
![](../../../../../../../Images/Third_Sem_Images/Schnorr%20Identification%20Protocol.png)

---

## Step 1: Commitment

Alice chooses a random number

$$
r
$$

She computes

$$
t = g^r \pmod p
$$

and sends

$$
t
$$

to Bob.

### Meaning

The value $$t$$ is a temporary commitment. It does **not** reveal Alice's private key.

---

## Step 2: Challenge

Bob generates a random challenge

$$
c
$$

and sends it to Alice.

The random challenge ensures that old messages cannot be reused, preventing replay attacks.

---

## Step 3: Response

Alice computes

$$
s = r + cx \pmod q
$$

and sends

$$
s
$$

to Bob.

---

## Step 4: Verification

Bob verifies whether

$$
g^s \equiv t \cdot y^c \pmod p
$$

If the equation is true, Alice is authenticated.

Otherwise, the authentication fails.

---

# Why Does the Verification Work?

Alice computes

$$
s = r + cx
$$

Substituting this into the verification equation:

$$
g^s = g^{r+cx}
$$

Using the exponent rule,

$$
g^{r+cx}=g^r \cdot g^{cx}
$$

Since

$$
t=g^r
$$

and

$$
y=g^x
$$

we have

$$
g^{cx}=(g^x)^c=y^c
$$

Therefore,

$$
g^s=t \cdot y^c
$$

Hence, Bob's verification equation is satisfied.

---

# Protocol Flow Diagram

```text
          Alice (Prover)                     Bob (Verifier)

Private Key = x
Public Key  = y = g^x mod p

Choose random r
Compute t = g^r
-------------------------------> t

                         Generate random challenge c

<------------------------------- c

Compute

s = r + cx

-------------------------------> s

                    Verify

          g^s ≡ t · y^c (mod p)

          True  → Authentication Successful

          False → Authentication Failed
```

---

# Numerical Example

Suppose

$$
p = 23
$$

Generator

$$
g = 5
$$

Private key

$$
x = 4
$$

Public key

$$
y = 5^4 \equiv 4 \pmod{23}
$$

---

### Step 1

Choose

$$
r = 3
$$

Compute

$$
t = 5^3 = 125 \equiv 10 \pmod{23}
$$

Send

$$
t = 10
$$

---

### Step 2

Bob chooses

$$
c = 2
$$

---

### Step 3

Compute

$$
s = 3 + (2 \times 4)=11
$$

Send

$$
s = 11
$$

---

### Verification

Left-hand side

$$
g^{11}=5^{11}\equiv22 \pmod{23}
$$

Right-hand side

$$
t \cdot y^c
=10 \times 4^2
=10 \times 16
=160
\equiv22 \pmod{23}
$$

Since

$$
22=22
$$

the verification succeeds, and Bob accepts Alice's identity.

---

# Why Is It Secure?

An attacker can only observe:

* $$t$$
* $$c$$
* $$s$$

The private key

$$
x
$$

is never transmitted.

Recovering $$x$$ from the public key

$$
y=g^x \pmod p
$$

requires solving the **Discrete Logarithm Problem**, which is computationally infeasible for sufficiently large parameters.

---

# Advantages

* Zero-knowledge authentication
* Fast and computationally efficient
* Low communication overhead
* Based on the hard Discrete Logarithm Problem
* Resistant to replay attacks because a new random challenge is generated for every authentication

---

# Disadvantages

* Requires carefully selected large prime numbers.
* Security depends on the difficulty of the Discrete Logarithm Problem.
* Requires a secure source of randomness for generating challenges.

---

# Difference Between Fiat–Shamir and Schnorr

| Feature            | Fiat–Shamir               | Schnorr                               |
| ------------------ | ------------------------- | ------------------------------------- |
| Mathematical Basis | Integer Factorization     | Discrete Logarithm                    |
| Secret             | Square root modulo $$n$$  | Private exponent $$x$$                |
| Public Key         | $$v=s^2 \pmod n$$         | $$y=g^x \pmod p$$                     |
| Verification       | Modular squaring relation | $$g^s \equiv t \cdot y^c \pmod p$$    |
| Efficiency         | Good                      | Faster and more efficient             |
| Applications       | Identification            | Identification and Digital Signatures |

---

# Exam Answer (5 Marks)

### Definition

The **Schnorr Identification Protocol** is a **zero-knowledge authentication protocol** based on the **Discrete Logarithm Problem**. It enables a prover to prove knowledge of a secret key without revealing the key.

### Steps

1. The prover selects a random number $$r$$ and computes

   $$
   t = g^r \pmod p
   $$

   Then sends $$t$$ to the verifier.

2. The verifier generates a random challenge $$c$$ and sends it to the prover.

3. The prover computes

   $$
   s = r + cx \pmod q
   $$

   and sends $$s$$ to the verifier.

4. The verifier checks whether

   $$
   g^s \equiv t \cdot y^c \pmod p
   $$

   If the equation holds, the prover is authenticated.

### Advantages

* Zero-knowledge authentication
* Fast and efficient
* Based on the Discrete Logarithm Problem
* Resistant to replay attacks due to the use of a fresh random challenge each time
