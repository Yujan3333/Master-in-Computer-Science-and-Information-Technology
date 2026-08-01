#ippr #third-semester 

# 1. Given a 6-symbol image segment with probabilities: 0.5, 0.3, 0.16, 0.1, 0.1, 0.06 — Compute the Huffman code, average length, compression ratio. **[5+5=10]**


---

# What is Huffman Coding?

**Huffman Coding** is a **lossless compression technique** that assigns:

* **Shorter binary codes** to symbols that occur **more frequently**.
* **Longer binary codes** to symbols that occur **less frequently**.

Thus, the average number of bits required to represent data is reduced.

**Example:**

Suppose six symbols have probabilities

| Symbol | Probability |
| ------ | ----------: |
| A      |        0.50 |
| B      |        0.30 |
| C      |        0.16 |
| D      |        0.10 |
| E      |        0.10 |
| F      |        0.06 |

(Notice these probabilities sum to **1.22**, not **1.00**. In a proper Huffman coding problem, probabilities should sum to **1**. In many exam questions, the table actually contains **frequencies** or there may be a printing error. The Huffman tree construction is the same whether you use probabilities or frequencies.)

---

# Huffman Coding Algorithm

1. Arrange symbols in ascending order of probability.
2. Select the two symbols with the smallest probabilities.
3. Merge them into a new node whose probability is the sum of the two.
4. Insert the new node back into the list.
5. Repeat until only one node remains.
6. Assign:

   * Left branch = 0
   * Right branch = 1
7. Read the code for each symbol from the root to the leaf.

---

# Step 1: Arrange in Ascending Order

| Symbol | Probability |
| ------ | ----------: |
| F      |        0.06 |
| D      |        0.10 |
| E      |        0.10 |
| C      |        0.16 |
| B      |        0.30 |
| A      |        0.50 |

---

# Step 2: Merge the Two Smallest

Merge

$$
0.06+0.10=0.16
$$

Now we have

| Node | Probability |
| ---- | ----------: |
| E    |        0.10 |
| C    |        0.16 |
| FD   |        0.16 |
| B    |        0.30 |
| A    |        0.50 |

---

# Step 3: Merge Again

Merge

$$
0.10+0.16=0.26
$$

Now

| Node | Probability |
| ---- | ----------: |
| C    |        0.16 |
| EDF  |        0.26 |
| B    |        0.30 |
| A    |        0.50 |

---

# Step 4

Merge

$$
0.16+0.26=0.42
$$

Now

| Node | Probability |
| ---- | ----------: |
| B    |        0.30 |
| FDEC |        0.42 |
| A    |        0.50 |

---

# Step 5

Merge

$$
0.30+0.42=0.72
$$

Now

| Node  | Probability |
| ----- | ----------: |
| A     |        0.50 |
| BFDEC |        0.72 |

---

# Step 6

Merge

$$
0.50+0.72=1.22
$$

Tree completed.

---

# Huffman Tree

One valid Huffman tree is

```text
					                    (1.22)
                                      /      \
                                 A(0.50)    (0.72)
                                            /      \
                                       B(0.30)    (0.42)
                                                  /      \
                                             C(0.16)    (0.26)
                                                        /      \
                                                  E(0.10)    (0.16)
                                                              /     \
                                                         F(0.06)  D(0.10)
```

Assign

* Left = 0
* Right = 1

---

# Huffman Codes

| Symbol | Code | Length |
| ------ | ---- | -----: |
| A      | 0    |      1 |
| B      | 10   |      2 |
| F      | 1100 |      4 |
| D      | 1101 |      4 |
| E      | 1110 |      4 |
| C      | 1111 |      4 |

**Note:** Huffman codes are **not unique**. Different left/right assignments can produce different binary codes, but the **code lengths and average length remain the same**.

---

# Average Code Length

Formula

$$
L=\sum p_i l_i
$$

where

* $p_i$ = probability
* $l_i$ = code length

Substitute the values:

$$
L=(0.50)(1)
+(0.30)(2)
+(0.16)(4)
+(0.10)(4)
+(0.10)(4)
+(0.06)(4)
$$

$$
L=0.50+0.60+0.64+0.40+0.40+0.24
$$

$$
L=2.78\text{ bits/symbol}
$$

---

# Compression Ratio

Assume the original image uses **3-bit fixed-length coding** (since there are up to 8 symbols).

Formula

$$
CR=\frac{\text{Original bits/symbol}}{\text{Average bits/symbol}}
$$

$$
CR=\frac{3}{2.78}
$$

$$
CR\approx1.08:1
$$

This means the compressed data is about **1.08 times smaller** than the original.

---

# Entropy

Entropy is the theoretical minimum average number of bits required to represent a symbol.

Formula

$$
H=-\sum p_i\log_2 p_i
$$

You substitute each probability into the formula and add the results.

*(If the given probabilities do not sum to 1, normalize them first or use the corrected values provided in the exam.)*

---

# Coding Efficiency

Formula

$$
\eta=\frac{H}{L}\times100%
$$

where

* $H$ = entropy
* $L$ = average code length

The closer the efficiency is to **100%**, the better the Huffman code.

---

# Relative Data Redundancy

Formula

$$
R_D=1-\frac{1}{CR}
$$

If

$$
CR=1.08
$$

then

$$
R_D
===

1-\frac{1}{1.08}
\approx0.074
$$

or

$$
R_D\approx7.4%
$$

---

# Algorithm for Huffman Coding

1. List all symbols with their probabilities or frequencies.

2. Sort them in ascending order.

3. Merge the two least probable nodes.

4. Reinsert the merged node into the sorted list.

5. Repeat until only one node remains.

6. Assign **0** to the left branch and **1** to the right branch.

7. Read the binary code for each symbol from the root to its leaf.

8. Compute the average code length using

   $$
   L=\sum p_i l_i
   $$

9. Compute the compression ratio and coding efficiency if required.

---

# Important Exam Notes

* If the question gives **frequencies** instead of probabilities, first compute the probabilities:

  $$
  p_i=\frac{f_i}{\sum f_i}
  $$

* Huffman codes are **not unique**. Different valid trees may produce different binary codes, but the **average code length is the same**.

* Always show:

  1. Sorted table
  2. Tree construction
  3. Final codes
  4. Average code length
  5. Compression ratio (and entropy/efficiency if asked)

This complete workflow is the standard approach expected in TU examinations.
