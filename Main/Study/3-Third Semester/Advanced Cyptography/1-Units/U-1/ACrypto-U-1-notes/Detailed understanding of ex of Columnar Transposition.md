#advanced-cryptography #example #permutation-cipher #third-semester 
- [Complete EX Columnar Transposition](Complete%20EX%20Columnar%20Transposition.md)

## Suppose the key is

```text
3 1 4 2
```

This key is written **above the columns**.


| Column  | 1     | 2     | 3     | 4     |
| ------- | ----- | ----- | ----- | ----- |
| **Key** | **3** | **1** | **4** | **2** |

This means:

* **Column 1 has key value 3**
* **Column 2 has key value 1**
* **Column 3 has key value 4**
* **Column 4 has key value 2**

---

## During Encryption

You **do NOT read Column 1, Column 2, Column 3, Column 4**.

Instead, you ask:

> **Where is key value 1?**

Look at the table:

| Column | 1 | 2     | 3 | 4 |
| ------ | - | ----- | - | - |
| Key    | 3 | **1** | 4 | 2 |

Key **1** is above **Column 2**.

So first read **Column 2**.

---

Next ask:

> **Where is key value 2?**

| Column | 1 | 2 | 3 | 4     |
| ------ | - | - | - | ----- |
| Key    | 3 | 1 | 4 | **2** |

Key **2** is above **Column 4**.

So second read **Column 4**.

---

Next:

Where is **key value 3**?

| Column | 1     | 2 | 3 | 4 |
| ------ | ----- | - | - | - |
| Key    | **3** | 1 | 4 | 2 |

Key **3** is above **Column 1**.

Read Column 1.

---

Finally:

Where is **key value 4**?

It is above **Column 3**.

Read Column 3.

---

So the reading order is:

```text
Key 1 → Column 2
Key 2 → Column 4
Key 3 → Column 1
Key 4 → Column 3
```

---

## Why you thought differently

You wrote:

> Key1 = Col3

That would mean:

```text
Key
3 1 4 2
↑
```

You are reading **the numbers themselves** as if they tell you **which column to read next**.

But in **columnar transposition**, they are **labels** attached to the columns.

Think of them like exam roll numbers.

Suppose four students stand in columns:

| Column | Student |
| ------ | ------- |
| 1      | Roll 3  |
| 2      | Roll 1  |
| 3      | Roll 4  |
| 4      | Roll 2  |

If the teacher says:

> "Call students in roll number order."

You don't call:

* Column 1
* Column 2
* Column 3
* Column 4

Instead you find:

* Roll 1 → Column 2
* Roll 2 → Column 4
* Roll 3 → Column 1
* Roll 4 → Column 3

Exactly the same idea!

---

## Quick Memory Trick

For a key:

```text
3 1 4 2
```

Think:

> **"Find where 1 is, then where 2 is, then where 3 is, then where 4 is."**

Not:

> "Go to column 3 first."

That second interpretation is **not** how the standard columnar transposition cipher works.

---

### One important note

There are **different conventions** in different textbooks. Some books define the key as a **reading order** (e.g., `3 1 4 2` means read columns 3, 1, 4, 2 directly), while the more common textbook convention labels the columns with key values and then reads them in ascending key order.

**Your textbook may be using the first convention.** If you can upload the page or screenshot showing this example, I can tell you **exactly which convention your professor/textbook is using**, so you won't lose marks in the exam.
