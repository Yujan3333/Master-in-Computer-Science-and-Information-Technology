#advanced-cryptography #third-semester

# Fiat–Shamir Identification Protocol

The **Fiat–Shamir Identification Protocol** is a **zero-knowledge authentication protocol** that allows a user (the prover) to prove their identity to another user (the verifier) **without revealing the secret key**.

It is based on the **Integer Factorization Problem**, which means its security depends on the difficulty of factoring a large composite number.

---

# Main Idea

Suppose you want to log in to a secure system.

Normally, you send your password to the server.

However, if an attacker intercepts the password, your account can be compromised.

The Fiat–Shamir protocol allows you to prove:

> **"I know the secret key without revealing it."**

Thus, the verifier is convinced of your identity while the secret remains hidden.

---

# Real-Life Analogy

Imagine Alice owns a special key to a locker.

Bob wants to verify that Alice has the key.

Instead of showing the key, Alice:

1. Locks and unlocks the locker secretly.
2. Bob asks a random question.
3. Alice answers using the key.

If Alice answers correctly every time, Bob becomes convinced that Alice owns the key without ever seeing it.

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

Choose two large prime numbers

$$
p,;q
$$

Compute

$$
n=pq
$$

where

$$
n
$$

is made public.

---

Alice chooses a secret number

$$
s
$$

such that

$$
\gcd(s,n)=1
$$

She computes her public key

$$
v=s^{-2}\pmod n
$$

(Some books use

$$
v=s^2\pmod n
$$

instead. Follow your teacher's convention.)

---

# Protocol Steps

The protocol consists of **three message exchanges**.

---

## Step 1: Commitment

Alice chooses a random number

$$
r
$$

and computes

$$
x=r^2\pmod n
$$

She sends

$$
x
$$

to Bob.

---

## Step 2: Challenge

Bob generates a random challenge

$$
e
$$

where

$$
e\in{0,1}
$$

and sends it to Alice.

---

## Step 3: Response

If

$$
e=0,
$$

Alice sends

$$
y=r.
$$

If

$$
e=1,
$$

Alice sends

$$
y=rs\pmod n.
$$

---

## Step 4: Verification

Bob checks:

### Case 1

If

$$
e=0,
$$

verify

$$
y^2\equiv x\pmod n.
$$

---

### Case 2

If

$$
e=1,
$$

verify

$$
y^2\cdot v\equiv x\pmod n.
$$

If the equation is true, Alice is authenticated.

---

# Why Does It Work?

### When

$$
e=0
$$

Alice sends

$$
y=r.
$$

Therefore,

$$
y^2=r^2=x.
$$

Verification succeeds.

---

### When

$$
e=1
$$

Alice sends

$$
y=rs.
$$

Then

$$
y^2=(rs)^2=r^2s^2.
$$

Since

$$
v=s^{-2},
$$

we get

$$
y^2v=r^2s^2s^{-2}=r^2=x.
$$

Hence the verifier accepts Alice.

---

# Protocol Flow Diagram

```text
           Alice (Prover)                  Bob (Verifier)

Private Key = s
Public Key  = v

Choose random r
Compute x = r² mod n
-------------------------------> x

                       Generate challenge e (0 or 1)

<------------------------------- e

If e = 0
      y = r

If e = 1
      y = rs mod n

-------------------------------> y

Verify

If e = 0:
y² ≡ x (mod n)

If e = 1:
y²v ≡ x (mod n)

True  → Authentication Successful

False → Authentication Failed
```

---

# Simple Numerical Example

Choose

$$
p=3,\qquad q=7
$$

Then

$$
n=21.
$$

Choose private key

$$
s=5.
$$

Since

$$
\gcd(5,21)=1,
$$

it is valid.

Compute

$$
v=s^{-2}\pmod{21}.
$$

(For exams, many teachers provide $$v$$ directly instead of asking you to compute the modular inverse.)

Choose

$$
r=2.
$$

Compute

$$
x=2^2=4.
$$

Suppose Bob chooses

$$
e=0.
$$

Alice sends

$$
y=2.
$$

Verification:

$$
2^2=4=x.
$$

Hence, authentication succeeds.

---

# Why Is It Secure?

An attacker only sees:

* $$x$$
* $$e$$
* $$y$$

The private key

$$
s
$$

is never transmitted.

Recovering $$s$$ requires factoring

$$
n=pq,
$$

which is computationally infeasible when large primes are used.

---

# Advantages

* Zero-knowledge authentication
* Secret key is never revealed
* Based on the hard Integer Factorization Problem
* Resistant to replay attacks due to the random challenge

---

# Disadvantages

* Slower than Schnorr because it uses modular squaring.
* Requires generation of large prime numbers.
* More communication rounds than some modern protocols.

---

# Difference Between Fiat–Shamir and Schnorr

| Feature      | Fiat–Shamir                                                     | Schnorr                         |
| ------------ | --------------------------------------------------------------- | ------------------------------- |
| Based on     | Integer Factorization                                           | Discrete Logarithm              |
| Private Key  | $$s$$                                                           | $$x$$                           |
| Public Key   | $$v=s^{-2}\pmod n$$ (or $$s^2\pmod n$$ depending on convention) | $$y=g^x\pmod p$$                |
| Challenge    | $$e\in{0,1}$$                                                   | Random value $$c$$              |
| Verification | $$y^2v\equiv x\pmod n$$                                         | $$g^s\equiv t\cdot y^c\pmod p$$ |
| Speed        | Slower                                                          | Faster                          |

---

# Exam Answer (5 Marks)

### Definition

The **Fiat–Shamir Identification Protocol** is a **zero-knowledge authentication protocol** based on the **Integer Factorization Problem**. It allows a prover to prove knowledge of a secret key without revealing it.

### Steps

1. Choose large primes $$p$$ and $$q$$ and compute

   $$
   n=pq.
   $$

2. The prover chooses a private key $$s$$ and computes the public key $$v$$.

3. The prover selects a random number $$r$$ and computes

   $$
   x=r^2\pmod n.
   $$

4. The verifier sends a random challenge $$e$$.

5. The prover sends the response $$y$$.

6. The verifier checks the appropriate verification equation. If it is satisfied, the prover is authenticated.

### Advantages

* Zero-knowledge authentication
* Secret key is never revealed
* Based on the Integer Factorization Problem
* Resistant to replay attacks
