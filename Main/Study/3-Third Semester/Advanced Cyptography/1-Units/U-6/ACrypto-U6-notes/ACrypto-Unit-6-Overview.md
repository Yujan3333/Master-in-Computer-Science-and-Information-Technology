#advanced-cryptography #third-semester 

# Unit 6: Secret Sharing Scheme (4 Hours) – Summary

This unit focuses on **identification protocols and secret sharing techniques**, which allow secure authentication and secure distribution of confidential information among multiple participants.

---

# Unit 6 Summary

## 1. Fiat–Shamir Protocol ⭐⭐⭐⭐

Study:

* What is the Fiat–Shamir Protocol?
* Identification protocol
* Working
* Challenge-response mechanism
* Zero-Knowledge Proof (basic idea)
* Advantages
* Applications

---

## 2. Schnorr's Identification Protocol ⭐⭐⭐⭐⭐

Very important topic.

Study:

* What is Schnorr's Identification Protocol?
* Working
* Challenge-response steps
* Security
* Advantages
* Applications

Know the difference between Fiat–Shamir and Schnorr protocols.

---

## 3. Threshold Schemes ⭐⭐⭐⭐⭐

One of the most important topics.

Study:

* What is a Threshold Scheme?
* Secret sharing
* $(t,n)$ Threshold Scheme
* Working
* Advantages
* Applications

Example:

```text
(3,5) Threshold Scheme

5 people share a secret.

Any 3 people can reconstruct it.

2 or fewer cannot.
```

---

## 4. Threshold Schemes with Liars ⭐⭐⭐⭐

Study:

* What are dishonest participants (liars)?
* Detecting incorrect shares
* Error correction
* Security against cheating

---

## 5. Access Structures and General Secret Sharing ⭐⭐⭐⭐

Study:

* Access Structure
* Authorized sets
* Unauthorized sets
* General Secret Sharing Scheme
* Monotone Access Structure

Example:

```text
Manager + Accountant

can open the safe.

Accountant alone

cannot.
```

---

## 6. Visual Secret Sharing Schemes ⭐⭐⭐⭐⭐

Very important topic.

Study:

* What is Visual Secret Sharing (VSS)?
* Image-based secret sharing
* Share generation
* Share reconstruction
* Advantages
* Applications

Example:

```text
Secret Image

↓

Share 1

+

Share 2

↓

Original Image
```

Each share individually reveals **no information**.

---

# Most Important Topics (Very Likely in Exams)

⭐⭐⭐⭐⭐

* Threshold Schemes
* Visual Secret Sharing
* Schnorr Identification Protocol

---

# Medium Priority

⭐⭐⭐⭐

* Fiat–Shamir Protocol
* Threshold Schemes with Liars
* Access Structures

---

# Expected Exam Questions

## 2 Marks

* Define Secret Sharing.
* What is a Threshold Scheme?
* What is Visual Secret Sharing?
* Define Fiat–Shamir Protocol.
* Define Schnorr Identification Protocol.
* What is an Access Structure?

---

## 5 Marks

* Explain Threshold Schemes with an example.
* Explain Visual Secret Sharing Scheme.
* Explain Schnorr Identification Protocol.
* Explain Fiat–Shamir Protocol.
* Explain Access Structures and General Secret Sharing.
* Explain Threshold Schemes with Liars.

---

# Most Important Definitions

### Secret Sharing

> **Secret Sharing is a cryptographic technique in which a secret is divided into multiple shares and distributed among participants. The original secret can only be reconstructed when a required number of shares are combined.**

---

### Threshold Scheme

> **A Threshold Scheme is a secret sharing method in which at least $t$ out of $n$ participants are required to reconstruct the secret. It is denoted as a $(t,n)$ threshold scheme.**

---

### Visual Secret Sharing

> **Visual Secret Sharing is a cryptographic technique that divides an image into multiple shares such that the original image is revealed only when the required shares are stacked together.**

---

# One-Minute Revision

```text
Unit 6

1. Fiat–Shamir Protocol
2. Schnorr Identification Protocol
3. Threshold Schemes
4. Threshold Schemes with Liars
5. Access Structures
6. General Secret Sharing
7. Visual Secret Sharing
```

---

# Study Order (Recommended)

1. **Threshold Schemes** ⭐⭐⭐⭐⭐
2. **Visual Secret Sharing** ⭐⭐⭐⭐⭐
3. **Schnorr Identification Protocol** ⭐⭐⭐⭐⭐
4. **Fiat–Shamir Protocol**
5. **Access Structures & General Secret Sharing**
6. **Threshold Schemes with Liars**

This order covers the most frequently examined topics first and builds from basic secret sharing concepts to advanced identification protocols.
