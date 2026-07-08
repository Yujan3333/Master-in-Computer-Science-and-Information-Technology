#advanced-cryptography #third-semester 

Here's a **correct, exam-friendly, copy-friendly example** of **Kasiski Examination** that you can write directly in your notes.

---

# Cryptanalysis of Vigenère Cipher – Kasiski Examination (Correct Example)

### Step 1: Find Repeated Groups

Suppose the ciphertext is:

```text
ABCDWXYZABCDQRSTABCD
```

The repeated group is:

```text
ABCD
```

It appears **3 times**.

Starting positions:

```text
First  ABCD → Position 0
Second ABCD → Position 8
Third  ABCD → Position 16
```

---

### Step 2: Measure the Distance

Calculate the distance between the repeated groups.

```text
0 → 8  = 8 letters

8 → 16 = 8 letters
```

Distance = **8**

---

### Step 3: Find the Factors

Find all factors of **8**.

```text
Factors of 8

1, 2, 4, 8
```

One of these is likely the **keyword length**.

Suppose after further analysis, **4** produces meaningful plaintext.

Therefore,

```text
Keyword Length = 4
```

---

# Why Does This Work?

Suppose the keyword is

```text
LION
```

Length = **4**

The keyword repeats like this:

```text
LIONLIONLIONLION...
```

Every **4 letters**, the same key letters repeat.

Therefore, repeated plaintext may produce repeated ciphertext at distances such as:

```text
4
8
12
16
20
```

These are all multiples of **4**.

So, by finding the distance between repeated ciphertext patterns and calculating their common factors, we can estimate the keyword length.

---

# Short Exam Answer (5 Marks)

```text
1. Find repeated groups in the ciphertext.

Example:
ABCDWXYZABCDQRSTABCD

Repeated group: ABCD

2. Measure the distance between repetitions.

0 → 8 = 8 letters
8 → 16 = 8 letters

3. Find the factors of the distance.

Factors of 8:
1, 2, 4, 8

4. One of these factors is likely the keyword length.

After further analysis, keyword length = 4.
```

### Memory Trick ⭐⭐⭐⭐⭐

```text
Repeated Pattern
        ↓
Measure Distance
        ↓
Find Factors (or GCD)
        ↓
Guess Keyword Length
        ↓
Use Frequency Analysis
        ↓
Recover the Keyword
```

