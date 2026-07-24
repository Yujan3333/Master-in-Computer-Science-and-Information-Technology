# Digital Signatures using ECC (ECDSA)

**ECDSA (Elliptic Curve Digital Signature Algorithm)** is a digital signature scheme based on **Elliptic Curve Cryptography (ECC)**. It provides:

* **Authentication**
* **Integrity**
* **Non-repudiation**

---

## 1. Key Generation

Choose:

* Elliptic curve $$E$$
* Base point $$G$$
* Private key $$d$$

Compute the public key:

$$
Q=dG
$$

* **Private Key:** $$d$$
* **Public Key:** $$Q$$

---

## 2. Signature Generation

For message $$M$$:

1. Compute the hash:

$$
e=H(M)
$$

2. Choose a random number $$k$$.

3. Compute

$$
P=kG=(x_1,y_1)
$$

4. Compute

$$
r=x_1 \bmod n
$$

5. Compute

$$
s=k^{-1}(e+dr)\bmod n
$$

The signature is

$$
(r,s)
$$

---

## 3. Signature Verification

1. Compute

$$
e=H(M)
$$

2. Compute

$$
w=s^{-1}\bmod n
$$

$$
u_1=ew\bmod n
$$

$$
u_2=rw\bmod n
$$

3. Compute

$$
X=u_1G+u_2Q
$$

4. Accept the signature if

$$
r\equiv x_1 \pmod n
$$

Otherwise, the signature is invalid.

---

## Advantages

* Smaller key size than RSA.
* Faster computation.
* Less memory and bandwidth.
* High security.

---

## Applications

* SSL/TLS
* Bitcoin and cryptocurrencies
* Digital certificates
* Smart cards
* Mobile banking

---

## Exam Summary (5 Marks)

**ECDSA** is a digital signature algorithm based on **ECC**. It generates a signature using the **private key** and verifies it using the **public key**. It provides **authentication, integrity, and non-repudiation** with **smaller key sizes and higher efficiency** than RSA.
