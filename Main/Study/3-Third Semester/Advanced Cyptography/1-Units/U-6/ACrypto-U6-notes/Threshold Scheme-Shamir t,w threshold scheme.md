#advanced-cryptography #third-semester

# Threshold Scheme (Shamir's ((t,w)) Threshold Scheme)

## What is a Threshold Scheme?

A **Threshold Scheme** is a method of **dividing a secret into multiple pieces (called shares)** so that only a minimum number of participants can reconstruct the secret.

It was proposed by **Adi Shamir in 1979**.

---

# Main Idea

Suppose a company has a secret password.

Giving the password to only one person is risky because:

* The person may lose it.
* The person may misuse it.

Instead, split the secret into several shares.

Example:

There are **5 managers**.

* Any **3 managers** together can recover the secret.
* Only **1 or 2 managers** cannot recover it.

This is called a **Threshold Scheme**.

---

# What does ((t,w)) mean?

In Shamir's scheme,

* $$w$$ = Total number of participants (or shares).
* $$t$$ = Minimum number of shares required to reconstruct the secret.

where

$$
t \le w
$$

---

### Example

$$
(3,5)
$$

means:

* Total shares = **5**
* Minimum shares needed = **3**

So,

| Number of Shares | Secret Recovered? |
| ---------------- | ----------------- |
| 1                | ❌ No              |
| 2                | ❌ No              |
| 3                | ✅ Yes             |
| 4                | ✅ Yes             |
| 5                | ✅ Yes             |

---

# Real-Life Example

Imagine a treasure chest with **5 keys**.

The lock is designed so that **any 3 keys** can open it.

* 1 key → Cannot open.
* 2 keys → Cannot open.
* 3 or more keys → Opens successfully.

This is exactly how a **(3,5) threshold scheme** works.

---

# Why is it Needed?

It provides:

* High security
* No single point of failure
* Protection against key loss
* Shared trust among participants

---

# Working Principle

Shamir's Threshold Scheme uses **Polynomial Interpolation**.

The secret is hidden as the **constant term** of a polynomial.

A polynomial of degree

$$
t-1
$$

is created.

The secret is

$$
S=f(0)
$$
# [Simpler Example of Threshold Scheme](Simpler%20Example%20of%20Threshold%20Scheme.md)
---

# Secret Sharing Phase

Suppose the secret is

$$
S=10
$$

Choose

$$
t=3,\qquad w=5
$$

Since

$$
t=3,
$$

construct a polynomial of degree

$$
2.
$$

Example:

$$
f(x)=10+4x+2x^2
$$

Here,

* Secret = 10
* Polynomial degree = 2

---

Now evaluate the polynomial at different values of $$x$$.

### Share 1

$$
f(1)=10+4+2=16
$$

Share:

$$
(1,16)
$$

---

### Share 2

$$
f(2)=10+8+8=26
$$

Share:

$$
(2,26)
$$

---

### Share 3

$$
f(3)=10+12+18=40
$$

Share:

$$
(3,40)
$$

---

### Share 4

$$
f(4)=10+16+32=58
$$

Share:

$$
(4,58)
$$

---

### Share 5

$$
f(5)=10+20+50=80
$$

Share:

$$
(5,80)
$$

Each participant receives only one share.

---

# Secret Reconstruction

Suppose participants 2, 3, and 5 come together.

Their shares are:

$$
(2,26),\quad(3,40),\quad(5,80)
$$

Using **Lagrange Interpolation**, they reconstruct the polynomial.

Finally,

$$
f(0)=10
$$

Therefore,

the original secret is

$$
10.
$$

---

# Why Can't Two Shares Recover the Secret?

Since

$$
t=3,
$$

the polynomial has degree

$$
2.
$$

A degree-2 polynomial requires **at least 3 points** to determine it uniquely.

With only 2 shares, there are infinitely many possible polynomials, so the secret cannot be determined.

---

# Flow Diagram

```text id="z5u9wu"
                 Secret

                   │
                   ▼
        Create Polynomial

                   │
                   ▼
      Generate w Different Shares

                   │
        ┌──────────┴──────────┐
        ▼          ▼          ▼
      Share1    Share2     Share3 ... Sharew

                   │
          Collect at least t Shares

                   ▼
      Lagrange Interpolation

                   ▼
        Recover Original Secret
```

---

# Advantages

* High security
* Secret is never stored in one place
* Any $$t$$ participants can recover the secret
* Fewer than $$t$$ participants learn nothing about the secret
* No single point of failure

---

# Disadvantages

* Requires secure distribution of shares.
* Reconstruction requires polynomial interpolation.
* If enough shares are lost (fewer than $$t$$ remain), the secret cannot be recovered.

---

# Applications

* Bank vault security
* Military launch codes
* Cryptocurrency wallet recovery
* Cloud key management
* Distributed authentication systems

---

# Exam Answer (5 Marks)

### Definition

Shamir's **((t,w)) Threshold Scheme** is a secret-sharing scheme in which a secret is divided into **$$w$$ shares**, and **any $$t$$ or more shares** can reconstruct the secret, while fewer than $$t$$ shares reveal no information about it.

### Working

1. Choose the threshold $$t$$ and total participants $$w$$
2. Construct a polynomial of degree $$t-1$$ with the secret as the constant term.
3. Generate $$w$$ shares by evaluating the polynomial at different values of $$x$$.
4. Distribute one share to each participant.
5. Any $$t$$ participants can reconstruct the polynomial using **Lagrange Interpolation** and recover the secret.

### Advantages

* High security
* No single point of failure
* Secret cannot be recovered with fewer than $t$ shares

---

### **Exam Tip**

Remember these two formulas:

* **Polynomial degree**

  $$
  \text{Degree} = t-1
  $$

* **Secret**

  $$
  S=f(0)
  $$

These are the two most important mathematical concepts in **Shamir's ((t,w)) Threshold Scheme**.
