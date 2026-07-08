#permutation-cipher #advanced-cryptography #third-semester 

This table is **very important in the Hill Cipher**, but it's actually very simple.

The table is:

| $x$           | 1 | 2 | 3 | 4 | 5 | 6 |
| ------------- | - | - | - | - | - | - |
| $\pi^{-1}(x)$ | 3 | 6 | 1 | 5 | 2 | 4 |

Here:

* $\pi$ (pi) = **permutation (shuffle)**
* $\pi^{-1}$ = **inverse permutation (undo the shuffle)**

---

## Step 1: Think of 6 boxes

```
Original positions

1  2  3  4  5  6
A  B  C  D  E  F
```

Suppose someone shuffled them.

---

## Step 2: Inverse permutation tells us

The table says

```
Position 1 came from position 3
Position 2 came from position 6
Position 3 came from position 1
Position 4 came from position 5
Position 5 came from position 2
Position 6 came from position 4
```

That's exactly what the table means.

For example,

```
π⁻¹(1) = 3
```

means

> The value now at position **1** originally came from **position 3**.

Similarly,

```
π⁻¹(2) = 6
```

means

> Position **2** gets the value from original position **6**.

---

## Step 3: Example

Original block

```
Position : 1 2 3 4 5 6
Letters  : A B C D E F
```

Using the table

| New Position | Takes letter from |
| ------------ | ----------------- |
| 1            | 3                 |
| 2            | 6                 |
| 3            | 1                 |
| 4            | 5                 |
| 5            | 2                 |
| 6            | 4                 |

So the new block becomes

```
Position : 1 2 3 4 5 6
Letters  : C F A E B D
```

---

## Easy way to remember

The table

| $x$           | 1 | 2 | 3 | 4 | 5 | 6 |
| ------------- | - | - | - | - | - | - |
| $\pi^{-1}(x)$ | 3 | 6 | 1 | 5 | 2 | 4 |

simply means:

```
New Position ← Old Position

1 ← 3
2 ← 6
3 ← 1
4 ← 5
5 ← 2
6 ← 4
```

So whenever you see $\pi^{-1}(x)$, read it as:

> **"For each new position, which old position should I copy from?"**

That's all this table is doing—it tells you how to **rearrange (permute) the letters or numbers** during encryption or decryption.
