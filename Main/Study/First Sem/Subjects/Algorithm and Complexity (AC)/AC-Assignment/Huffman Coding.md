 - compression techniques that handles the data compression of ASCII characters.
- Developed by David Huffman in 1952

- Based on top-down approach. In this algorithm, a **binary tree** is created in a top−down manner to produce a minimal sequence.

- It translates the characters contained in a *data file into a binary code*.

- The Huffman coding is a **lossless text compression** method because in this method, the compressed data can be restored to its *original format*.

- Huffman coding uses a *variable−length encoding scheme*, where each symbol in the input data is assigned a *binary code based on its frequency of occurrence*. This allows for efficient compression of the data, as symbols that occur more frequently in the input will be assigned shorter codes, reducing the overall size of the encoded data.

#### Example

| Symbol | Frequency |
| ------ | --------- |
| A      | 10        |
| B      | 7         |
| C      | 5         |
| D      | 3         |
| E      | 2         |

 ##### **Step-by-Step Process of Huffman Coding**
 **Step 1: Create a Priority Queue**
- Start with all symbols as separate **nodes** in a priority queue, where the least frequent symbols have the highest priority.

**Step 2: Build the Huffman Tree**
- **Merge the two least frequent symbols** into a new node.
- Assign **0** to the left branch and **1** to the right branch.
- Repeat the merging process until only **one root node** remains.

**Step 3: Assign Huffman Codes**
- Traverse the tree from the root and assign binary codes to each symbol based on the path.

 ###### Building the Huffman Tree

1. **Merge D (3) and E (2) → New Node (5)**
```md
   (D,E) - 5
   /     \
 D(3)   E(2)
```

2. **Merge C (5) and (D,E) (5) → New Node (10)**
```md
      (C,D,E) - 10
      /        \
    C(5)     (D,E) - 5
            /     \
          D(3)   E(2)
```

3. **Merge B (7) and (C,D,E) (10) → New Node (17)**
```md
       (B,C,D,E) - 17
       /         \
     B(7)      (C,D,E) - 10
             /        \
           C(5)     (D,E) - 5
                   /     \
                 D(3)   E(2)
```

4. **Merge A (10) and (B,C,D,E) (17) → New Node (27) (Final Tree)**
```md
          (A,B,C,D,E) - 27
          /           \
        A(10)     (B,C,D,E) - 17
                  /         \
                B(7)      (C,D,E) - 10
                        /        \
                      C(5)     (D,E) - 5
                              /     \
                            D(3)   E(2)
```

**Step 4: Generate Huffman Codes**
Now, we assign **0** to the left branches and **1** to the right branches:

| Symbol | Huffman Code |
| ------ | ------------ |
| A      | **0**        |
| B      | **10**       |
| C      | **110**      |
| D      | **1110**     |
| E      | **1111**     |

==NOTE==
- More frequent symbols (A, B) get **shorter** codes.
- Less frequent symbols (D, E) get **longer** codes.

##### Final Encoded Message
Input- `ABCADE`
```md
A  B  C  A  D  E
0  10 110 0 1110 1111 (11bits)
```

---
#### Comparison with Fixed Length Coding
f we used **fixed-length encoding**, we'd need at least **3 bits per symbol** (since we have 5 symbols, and (2^3 = 8) covers all symbols):

|Symbol|Fixed-Length Code|
|---|---|
|A|000|
|B|001|
|C|010|
|D|011|
|E|100|

Encoding `"ABCADE"` in fixed-length:
```md
000 001 010 000 011 100  (18 bits)
```

