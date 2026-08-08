#third-semester #advanced-cryptography #assignment 
# 🔐 RC4 (Rivest Cipher 4)

## ✅ Introduction

* Designed by Ron Rivest (1987)
* **Type:** Stream Cipher
* Encrypts data **one byte at a time**
* Very fast and simple → widely used in:

  * SSL (older versions)
  * WEP/WPA (Wi-Fi)

⚠️ **Important:** RC4 is now **deprecated** due to keystream biases and attacks.

---

## ⚙️ Working Principle

RC4 generates a **random-looking keystream**, which is XORed with plaintext.

$$
C = P \oplus K
$$
$$
P = C \oplus K
$$

---

## 🔹 1. Key Scheduling Algorithm (KSA)

**Goal:** Initialize and shuffle array $S$

### Steps:

1. Initialize array:
   $$
   S[i]=i \quad (0 \le i \le 255)
   $$

2. Repeat key to form $K[i]$

3. Shuffle using:
   $$
   j=(j+S[i]+K[i])\bmod256
   $$

4. Swap:
   $$
   S[i] \leftrightarrow S[j]
   $$

👉 After KSA → we get a **random permutation of S**

---

## 🔹 2. Pseudo-Random Generation Algorithm (PRGA)

**Goal:** Generate keystream

### Steps (for each byte):

$$
i=(i+1)\bmod256
$$
$$
j=(j+S[i])\bmod256
$$

Swap:
$$
S[i] \leftrightarrow S[j]
$$

Keystream byte:
$$
K=S[(S[i]+S[j])\bmod256]
$$

---

## 🔹 Encryption Process

$$
C_i = P_i \oplus K_i
$$

---

## 🧮 Detailed RC4 Example (Small Scale)

👉 For understanding, assume reduced size (not 256)

### Given:

* Key = [1,2,3]
* Initial $S = [0,1,2,3]$

---

### 🔸 KSA

| i | j calculation | Swap      | S           |
|---|---------------|----------|------------|
| 0 | $(0+0+1)\%4=1$ | swap(0,1) | [1,0,2,3] |
| 1 | $(1+0+2)\%4=3$ | swap(1,3) | [1,3,2,0] |
| 2 | $(3+2+3)\%4=0$ | swap(2,0) | [2,3,1,0] |
| 3 | $(0+0+1)\%4=1$ | swap(3,1) | [2,0,1,3] |



---

### 🔸 PRGA (1 step)

* $i=1$
* $j=(0+S[1])=0$

Swap → [0,2,1,3]

Keystream:
$$K=S[(2+0)\%4]=S[2]=1$$

---

### 🔸 Encryption

If plaintext = 2:
$$
C = 2 \oplus 1 = 3
$$

---

## ✅ Key Features of RC4

* Simple and fast
* Uses permutation + XOR
* Same process for encryption & decryption
* ❌ Weak security (not used today)

---

# 🔐 RC5 (Rivest Cipher 5)

## ✅ Introduction

* Designed by Ron Rivest (1994)
* **Type:** Block Cipher
* Uses:

  * XOR
  * Addition modulo $2^w$
  * Data-dependent rotations

---

## ⚙️ RC5 Parameters

$$
RC5(w,r,b)
$$

Where:

* $w$ = word size (16, 32, 64 bits)
* $r$ = number of rounds
* $b$ = key length (bytes)

---

## 🔹 Structure

* Input block → split into:
  $$
  A, B
  $$

---

## 🔹 1. Key Expansion

* Converts key into subkeys:
  $$
  S[0], S[1], ..., S[2r+1]
  $$

---

## 🔹 2. Encryption Algorithm

### Initial step:

$$
A = A + S[0]
$$
$$
B = B + S[1]
$$

---

### 🔁 For each round (i = 1 to r):

$$
A = ((A \oplus B) \lll B) + S[2i]
$$

$$
B = ((B \oplus A) \lll A) + S[2i+1]
$$

---

### 🔸 Rotation meaning

* $\lll$ = circular left shift
* Amount depends on data → increases security

---

## 🔹 3. Decryption

Reverse steps:

* Subtract subkeys
* Right rotate
* XOR

---

## 🧮 Detailed RC5 Example

### Given:

* $A=5$, $B=10$
* $S[0]=2$, $S[1]=3$
* Assume 1 round

---

### 🔸 Initial step:

$$
A = 5 + 2 = 7
$$
$$
B = 10 + 3 = 13
$$

---

### 🔸 Round 1:

1. XOR:
   $$
   A \oplus B = 7 \oplus 13 = 10
   $$

2. Rotate:

* Rotate 10 left by 13 → assume result = 20

3. Add:
   $$
   A = 20 + S[2]
   $$

---

Similarly for B:
$$
B = ((13 \oplus A) \lll A) + S[3]
$$

---

👉 Final output = encrypted block

---

## ✅ Key Features of RC5

* Block cipher
* Parameterized → flexible
* Strong security
* Uses:

  * XOR
  * Rotation
  * Addition

---

# ⚖️ RC4 vs RC5 (Detailed Comparison)

| Feature         | RC4           | RC5                       |
| --------------- | ------------- | ------------------------- |
| Type            | Stream cipher | Block cipher              |
| Data processing | Byte-by-byte  | Block-wise                |
| Operations      | XOR           | XOR + rotation + addition |
| Speed           | Very fast     | Fast                      |
| Security        | Weak          | Strong                    |
| Complexity      | Simple        | Moderate                  |

---

# ✅ Final Exam Summary

### 🔹 RC4

* Stream cipher
* Uses **KSA + PRGA**
* Keystream XOR encryption
* ❌ Not secure today

---

### 🔹 RC5

* Block cipher
* Uses **data-dependent rotations**
* Flexible parameters
* ✔️ More secure

---

If you want next:
👉 I can give **full 256-step RC4 table (important for exams)**
👉 Or **complete RC5 numerical with actual bit rotations (no assumptions)**
