#advanced-cryptography #third-semester #el-gamal

# ElGamal Digital Signature Scheme (5 Marks)

**Definition:**

The **ElGamal Digital Signature Scheme** is a public-key digital signature algorithm based on the **Discrete Logarithm Problem (DLP)**. It provides **authentication, integrity, and non-repudiation**.

---

## 1. Key Generation

Choose:

* Prime number $$p$$
* Primitive root $$g$$
* Private key $$x$$

Compute the public key:

$$
y=g^x \bmod p
$$

* **Public Key:** $$(p,;g,;y)$$
* **Private Key:** $$x$$

---

## 2. Signature Generation

For message $$M$$:

1. Compute the hash:

$$
m=H(M)
$$

2. Choose a random integer $$k$$ such that

$$
\gcd(k,p-1)=1
$$

3. Compute

$$
r=g^k \bmod p
$$

4. Compute

$$
s=k^{-1}(m-xr)\bmod(p-1)
$$

5. Signature is

$$
(r,s)
$$

---

## 3. Signature Verification

1. Compute

$$
m=H(M)
$$

2. Verify whether

$$
g^m \equiv y^r r^s \pmod p
$$

* If true → **Valid Signature**
* Otherwise → **Invalid Signature**

---

## Advantages

* Provides authentication, integrity, and non-repudiation.
* Security is based on the Discrete Logarithm Problem.

---

### Exam Tip

**Remember these three formulas:**

**Public Key**

$$
y=g^x \bmod p
$$

**Signature**

$$
r=g^k \bmod p
$$

$$
s=k^{-1}(m-xr)\bmod(p-1)
$$

**Verification**

$$
g^m \equiv y^r r^s \pmod p
$$


