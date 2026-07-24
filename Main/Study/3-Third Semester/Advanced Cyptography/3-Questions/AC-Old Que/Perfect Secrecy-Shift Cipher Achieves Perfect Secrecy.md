#advanced-cryptography #third-semester #exam-paper-answer 

# Q. Define Perfect Secrecy. Prove that the Shift cipher achieves perfect secrecy for any plaintext probability distribution. **[4+6]**

## Answer

### (a) Perfect Secrecy (4 Marks)

A cryptosystem has **perfect secrecy** if observing the ciphertext gives **no information** about the plaintext.

Mathematically,

$$
P(M=m \mid C=c)=P(M=m)
$$

for every plaintext (m) and ciphertext (c).

This means the probability distribution of the plaintext remains unchanged even after seeing the ciphertext.

### Conditions for Perfect Secrecy

* The ciphertext reveals no information about the plaintext.
* Every plaintext is equally likely for a given ciphertext.
* The key is chosen uniformly at random and used only once.

---

## (b) Proof that the Shift Cipher Achieves Perfect Secrecy (6 Marks)

### Given

Plaintext space:

$$
M={0,1,\ldots,25}
$$

Key space:

$$
K={0,1,\ldots,25}
$$

Each key is chosen uniformly:

$$
P(K=k)=\frac{1}{26}
$$

Encryption rule:

$$
C=(M+K)\bmod 26
$$

---

### Step 1: Find the Required Key

For any plaintext (m) and ciphertext (c), the required key is

$$
k=(c-m)\bmod 26
$$

There is **exactly one** key that converts (m) into (c).

---

### Step 2: Probability of Producing the Ciphertext

Since every key is equally likely,

$$
P(C=c \mid M=m)=\frac{1}{26}
$$

This probability is the same for **every plaintext**.

---

### Step 3: Apply Bayes' Theorem

Using Bayes' theorem,

$$
P(M=m \mid C=c)
===============

\frac{P(C=c \mid M=m),P(M=m)}
{P(C=c)}
$$

Since

$$
P(C=c \mid M=m)=\frac{1}{26}
$$

and

$$
P(C=c)
======

\sum_m P(C=c \mid M=m),P(M=m)
$$

Substitute the value:

$$
P(C=c)
======

\frac{1}{26}\sum_m P(M=m)
$$

Since

$$
\sum_m P(M=m)=1
$$

we get

$$
P(C=c)=\frac{1}{26}
$$

Now,

$$
P(M=m \mid C=c)
===============

\frac{\frac{1}{26}P(M=m)}
{\frac{1}{26}}
==============

P(M=m)
$$

---

## Conclusion

Since

$$
P(M=m \mid C=c)=P(M=m)
$$

for **every plaintext probability distribution**, the ciphertext reveals no information about the plaintext.

Hence, **the Shift cipher achieves perfect secrecy**, **provided the key is chosen uniformly at random from all 26 possible shifts and is used only once (one-time use).**

---

## Exam Conclusion

* Perfect secrecy means

$$
P(M \mid C)=P(M)
$$

* In the Shift cipher, each plaintext–ciphertext pair corresponds to exactly one equally likely key.
* Therefore,

$$
P(M=m \mid C=c)=P(M=m)
$$

which proves that the Shift cipher achieves perfect secrecy under the given assumptions.
