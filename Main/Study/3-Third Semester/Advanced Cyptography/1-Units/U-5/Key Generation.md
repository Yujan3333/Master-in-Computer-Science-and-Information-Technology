#advanced-cryptography #third-semester 

---

# 1. Key Generation

## Definition

**Key generation** is the process of creating cryptographic keys that are used for encryption, decryption, authentication, and digital signatures.

A good key should be:

* Random
* Unpredictable
* Sufficiently long
* Securely generated

---

## Types of Keys Generated

### Symmetric Key

One key is used for both encryption and decryption.

Example:

* AES
* DES

---

### Asymmetric Key Pair

Two keys are generated.

* Public Key
* Private Key

Example:

* RSA
* ECC

---

## Methods of Key Generation

### 1. Random Number Generator (RNG)

Uses random values.

Example:

```text id="r9zd4y"
Random bits

101011010110101...
```

---

### 2. Pseudo Random Number Generator (PRNG)

Produces numbers that appear random using a mathematical algorithm.

Needs a **seed** value.

---

### 3. Hardware Random Number Generator (HRNG)

Generates randomness from physical events.

Examples:

* Thermal noise
* Clock jitter
* Radioactive decay

More secure than software-based generators.

---

## Characteristics of a Good Key

* Random
* Unique
* Difficult to guess
* Appropriate key length
* Generated securely

---

## Advantages

* Stronger encryption
* Prevents brute-force attacks
* Increases overall security

---

