#advanced-cryptography #third-semester 

# RC4 (Rivest Cipher 4) – Easy Exam Explanation

RC4 is one of the most important **stream ciphers** in cryptography. It was designed by **Ron Rivest** in **1987** for RSA Security.

Although it was widely used in the past, **RC4 is now considered insecure** and should not be used in new systems.

---

# Definition

**RC4 (Rivest Cipher 4)** is a **symmetric-key stream cipher** that encrypts data **one byte at a time** by generating a random-looking stream of bytes called the **keystream**.

Encryption and decryption use the **same secret key**.

---

# Key Features

* Symmetric key algorithm
* Stream cipher
* Variable key length (40–2048 bits, commonly 128 bits)
* Fast and simple
* Encrypts one byte at a time
* Uses XOR operation
* Same algorithm for encryption and decryption

---

# What is a Stream Cipher?

Instead of encrypting data in blocks (like AES),

a stream cipher encrypts data **character by character** or **byte by byte**.

Example

Plaintext

```text
HELLO
```

RC4 generates

```text
Keystream

52 91 17 200 43
```

Each plaintext byte is XORed with one keystream byte.

---

# RC4 Working

RC4 works in **two phases**.

```text
Secret Key
      │
      ▼
Key Scheduling Algorithm (KSA)
      │
Initial permutation of array S
      │
      ▼
Pseudo Random Generation Algorithm (PRGA)
      │
Generate keystream
      │
      ▼
Plaintext XOR Keystream
      │
      ▼
Ciphertext
```

---

# Step 1: Key Scheduling Algorithm (KSA)

### Purpose

KSA initializes and shuffles an array using the secret key.

Initially,

Create an array

```text
S = [0,1,2,3,...,255]
```

This array contains **256 values**.

Then,

Use the secret key to shuffle this array.

The shuffled array becomes the starting state for encryption.

---

### KSA Algorithm

Initialize

```text
for i = 0 to 255

S[i] = i
```

Then

```text
j = 0

for i = 0 to 255

j = (j + S[i] + Key[i mod keylength]) mod 256

Swap(S[i], S[j])
```

### Output

A randomly shuffled array **S**.

---

# Step 2: Pseudo Random Generation Algorithm (PRGA)

### Purpose

Generate one random byte (keystream byte) at a time.

Algorithm

```text
i = (i + 1) mod 256

j = (j + S[i]) mod 256

Swap(S[i], S[j])

t = (S[i] + S[j]) mod 256

KeyStreamByte = S[t]
```

Repeat this for every plaintext byte.

---

# Encryption

RC4 uses XOR.

Formula

```text
Ciphertext = Plaintext XOR Keystream
```

Example

Plaintext

```text
A
```

ASCII

```text
65
```

Keystream

```text
110
```

Encryption

```text
65 XOR 110 = 47
```

Ciphertext = 47

---

# Decryption

Exactly the same process.

Formula

```text
Plaintext = Ciphertext XOR Keystream
```

Example

Ciphertext

```text
47
```

Keystream

```text
110
```

```text
47 XOR 110 = 65
```

ASCII 65 = A

Original message recovered.

---

# Why Does the Same Algorithm Work?

Because XOR has a special property.

```text
A XOR B XOR B = A
```

Example

```text
Plaintext = 25

Key = 90

Cipher = 25 XOR 90

Decrypt

Cipher XOR 90

= 25
```

So encryption and decryption are identical.

---

# RC4 Internal State

RC4 maintains:

### 1. State array

```text
S[256]
```

Contains numbers

```text
0–255
```

---

### 2. Two pointers

```text
i

j
```

They move around inside the array while generating the keystream.

---

# Example Flow

Suppose

Key

```text
SECRET
```

Plaintext

```text
HELLO
```

### KSA

Creates shuffled array

```text
S
```

↓

### PRGA

Generates keystream

```text
22

81

43

190

77
```

↓

Encryption

```text
H XOR 22

E XOR 81

L XOR 43

L XOR 190

O XOR 77
```

↓

Ciphertext

---

# Advantages

* Very fast
* Simple implementation
* Small memory requirement
* Suitable for software implementation
* Encryption and decryption use the same algorithm

---

# Disadvantages

* Weak key scheduling
* Keystream is not truly random
* Vulnerable to statistical attacks
* Initial output bytes reveal information
* No longer considered secure
* Replaced by stronger algorithms like ChaCha20 and AES (used in stream modes like CTR or GCM)

---

# Applications (Historical)

RC4 was previously used in:

* SSL
* TLS (older versions)
* WEP
* WPA

Today, its use in these protocols has been discontinued because of known security weaknesses.

---

# RC4 Algorithm Summary

```text
                Secret Key
                     │
                     ▼
          Key Scheduling Algorithm
              (Initialize S[256])
                     │
                     ▼
          Shuffle S using the key
                     │
                     ▼
      Pseudo Random Generation Algorithm
                     │
                     ▼
        Generate Keystream Bytes
                     │
                     ▼
 Plaintext XOR Keystream = Ciphertext
                     │
                     ▼
 Ciphertext XOR Same Keystream = Plaintext
```

---

# Exam Points (2–5 Marks)

**Definition:**

> RC4 (Rivest Cipher 4) is a symmetric-key stream cipher that encrypts data one byte at a time by XORing the plaintext with a pseudorandom keystream generated from a secret key.

**Main Steps:**

1. Key Scheduling Algorithm (KSA)
2. Pseudo Random Generation Algorithm (PRGA)
3. Encrypt using XOR
4. Decrypt using the same XOR operation

**Remember:**

* **RC4 = Stream Cipher**
* **256-byte state array (`S`)**
* **Uses KSA and PRGA**
* **Encryption = Decryption (because of XOR)**
* **Fast, but no longer recommended due to security vulnerabilities**
