#advanced-cryptography 

- [Playfair Cipher - Geeks](https://www.geeksforgeeks.org/dsa/playfair-cipher-with-examples/)

The **Playfair cipher** is a classical **symmetric substitution cipher** that encrypts **pairs of letters (digraphs)** instead of individual letters. It uses a **5 × 5 key matrix** built from a keyword, where the letters **I** and **J** share one cell.


1. Generate the key Square (5x5): 
	- The key square is a 5×5 grid of alphabets that acts as the key for encrypting the plaintext. Each of the 25 alphabets must be unique and one letter of the alphabet (usually J) is omitted from the table (as the table can hold only 25 alphabets). If the plaintext contains J, then it is replaced by I. 
	
	- The initial alphabets in the key square are the unique alphabets of the key in the order in which they appear followed by the remaining letters of the alphabet in order. 

2. Algorithm to encrypt the plain text: The plaintext is split into pairs of two letters (digraphs). If there is an odd number of letters, a Z is added to the last letter.  

### Step 1: Construct the key matrix

**Key:** `TANGODOWN`

Remove duplicate letters:

**T A N G O D W**

Fill the remaining letters of the alphabet (excluding J):

| T | A | N | G | O |
| - | - | - | - | - |
| D | W | B | C | E |
| F | H | I | K | L |
| M | P | Q | R | S |
| U | V | X | Y | Z |

---

### Step 2: Prepare the plaintext

**Plaintext:**
`THE WAS IS COMING`

Remove spaces:

`THEWASISCOMING`

Split into pairs:

**TH EW AS IS CO MI NG**

---

### Step 3: Encrypt each pair

| Pair | Rule      | Cipher Pair |
| ---- | --------- | ----------- |
| TH   | Rectangle | **AF**      |
| EW   | Same row  | **DB**      |
| AS   | Rectangle | **OP**      |
| IS   | Rectangle | **LQ**      |
| CO   | Rectangle | **EG**      |
| MI   | Rectangle | **QF**      |
| NG   | Same row  | **GO**      |

---

## Final Ciphertext

**AFDBOPLQEGQFGO**

So, using the **Playfair cipher** with the key **TANGODOWN**, the plaintext:

> **THE WAS IS COMING**

encrypts to:

> **🔐 AFDBOPLQEGQFGO**

---
## [Decipher Process](Decipher%20Process.md)
