#advanced-cryptography #third-semester 

# Index of Coincidence (IC) in Vigenère Cipher ⭐⭐⭐⭐⭐ (Exam-Focused)

The **Index of Coincidence (IC)** is another method used to **break the Vigenère cipher**. It helps us **estimate the keyword length**.

> **Note:** Both **Kasiski Examination** and **Index of Coincidence (IC)** are used to find the **keyword length**.

---

# What is the Index of Coincidence?

### Definition (2 Marks)

> **The Index of Coincidence (IC) is a statistical measure that calculates the probability that two randomly selected letters from a ciphertext are the same. It is used to estimate the keyword length in the Vigenère cipher.**

---

# Simple Idea ⭐⭐⭐⭐⭐

Think of IC like this:

Suppose you have a bag of letters.

```text
A A A B C D E E E E F G
```

If you pick two letters randomly,

there is a **high chance** they are the same because there are many repeated **A's** and **E's**.

➡️ **High repetition = High IC**

---

Now another bag:

```text
A B C D E F G H I J K L
```

Every letter appears only once.

The chance of picking the same letter twice is **very low**.

➡️ **Low repetition = Low IC**

---

# Why is IC Used in Vigenère Cipher?

Suppose you don't know the keyword.

You try different keyword lengths.

Example:

```text
Guess 1 → Keyword Length = 2

Guess 2 → Keyword Length = 3

Guess 3 → Keyword Length = 5
```

For each guess,

* Split the ciphertext into groups.
* Calculate the IC for each group.

The correct keyword length usually gives IC values **close to normal English text**.

---

# English IC Value ⭐⭐⭐⭐⭐

Remember these values:

| Text Type    |    IC Value |
| ------------ | ----------: |
| Random text  | ≈ **0.038** |
| English text | ≈ **0.065** |

### Memory Trick

```text
Random letters → 0.038

English text → 0.065
```

---

# How IC is Used

Suppose ciphertext is

```text
LXFOPVEFRNHR...
```

### Guess Keyword Length = 2

Split into 2 groups.

Calculate IC.

Suppose

```text
IC = 0.040
```

This is close to random text.

Probably **wrong**.

---

### Guess Keyword Length = 5

Split into 5 groups.

Calculate IC.

Suppose

```text
Group 1 = 0.064
Group 2 = 0.067
Group 3 = 0.066
Group 4 = 0.065
Group 5 = 0.063
```

Average IC

```text
≈ 0.065
```

This is close to English.

Therefore

```text
Keyword Length = 5 ✅
```

---

# Steps of Index of Coincidence ⭐⭐⭐⭐⭐

### Step 1

Obtain the ciphertext.

↓

### Step 2

Guess a keyword length.

Example

```text
2

3

4

5
```

↓

### Step 3

Split the ciphertext into groups.

↓

### Step 4

Calculate the IC for each group.

↓

### Step 5

Find the average IC.

↓

### Step 6

If the average IC is close to **0.065**, the guessed keyword length is probably correct.

---

# Diagram

```text
Ciphertext
      │
      ▼
Guess Keyword Length
      │
      ▼
Split into Groups
      │
      ▼
Calculate IC
      │
      ▼
Average IC
      │
      ▼
≈ 0.065 ?
      │
      ▼
Correct Keyword Length
```

---

# IC Formula (For Theory)

If your teacher asks for the formula, write:

$$
IC=\frac{\sum f_i(f_i-1)}{N(N-1)}
$$

Where:

* $f_i$ = Frequency of the $i^{\text{th}}$ letter
* $N$ = Total number of letters

**For most theory exams, you usually don't have to calculate it unless specifically asked.**

---

# IC vs Kasiski Examination ⭐⭐⭐⭐⭐

| Kasiski Examination                  | Index of Coincidence            |
| ------------------------------------ | ------------------------------- |
| Looks for repeated patterns          | Uses letter frequencies         |
| Estimates keyword length             | Estimates keyword length        |
| Easier manually                      | Uses statistical analysis       |
| Works better with repeated sequences | Works well with long ciphertext |

---

# Example (Exam Style)

Suppose ciphertext:

```text
LXFOPVEFRNHR...
```

Try

```text
Keyword Length = 5
```

Split into 5 groups.

Calculate IC.

```text
Group 1 = 0.064

Group 2 = 0.066

Group 3 = 0.065

Group 4 = 0.067

Group 5 = 0.063
```

Average

```text
≈0.065
```

Therefore,

```text
Keyword Length = 5
```

Now perform **frequency analysis** to recover the keyword.

---

# Advantages

* Helps estimate the keyword length.
* More reliable for long ciphertext.
* Complements the Kasiski examination.

---

# Limitations

* Requires a sufficiently long ciphertext.
* Very short ciphertexts may produce inaccurate IC values.

---

# Exam Definition ⭐⭐⭐⭐⭐

> **The Index of Coincidence is a statistical technique used in the cryptanalysis of the Vigenère cipher to estimate the keyword length by measuring how closely the letter frequencies resemble normal English text.**

---

# Frequently Asked Exam Questions ⭐⭐⭐⭐⭐

### 2 Marks

1. Define the Index of Coincidence.
2. What is the purpose of IC in the Vigenère cipher?
3. What are the approximate IC values for English and random text?

### 5 Marks

1. Explain the Index of Coincidence with steps.
2. Differentiate Kasiski Examination and Index of Coincidence.
3. Explain how IC helps determine the keyword length.

---

# One-Minute Revision ⭐⭐⭐⭐⭐

```text
Index of Coincidence (IC)

Purpose:
Find the keyword length of a Vigenère cipher.

Steps:
1. Guess keyword length.
2. Split ciphertext into groups.
3. Calculate IC for each group.
4. Find average IC.
5. If average ≈ 0.065 → Correct keyword length.

Important Values:
English text ≈ 0.065
Random text ≈ 0.038

After finding the keyword length:
→ Apply frequency analysis to recover the keyword.
```

## Easy Memory Trick

Imagine you're guessing the number of boxes that contain letters.

* **Wrong number of boxes** → letters look random → **IC ≈ 0.038**.
* **Correct number of boxes** → each box behaves like normal English → **IC ≈ 0.065**.

So remember:

* **IC ≈ 0.065** → likely the **correct keyword length**.
* **IC ≈ 0.038** → likely an **incorrect keyword length**.
