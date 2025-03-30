- encoding algorithm used to generate a uniquely decodable code.
- Developed By -> Claude Shannon and Robert Fano in 1949

- Shannon-Fano coding is a method of **data compression** that creates **binary codes** for symbols based on their probabilities (how often they appear in the data) but not always efficient.

#### **How Shannon-Fano Coding Works (Step by Step)**

1. **List symbols in decreasing order of frequency**
    - More frequent symbols appear **at the top**, and less frequent ones appear **at the bottom**.
        
2. **Divide the symbols into two groups**
    - The goal is to split the symbols into **two groups** where the total frequency in each group is **as close as possible**.
        
    - This is the key difference from **Huffman coding**, which merges the least frequent symbols first.
        
3. **Assign binary digits (0 or 1)**
    - One group gets a **0** as a prefix.
        
    - The other group gets a **1** as a prefix.
        
4. **Repeat the process** for each group
    - Continue dividing each group into two smaller groups and assign additional binary digits (0 or 1).
        
    - Repeat until each symbol has a unique binary code.        

---

#### **Example of Shannon-Fano Coding**

Let’s say we have the following symbols with their frequencies:

| Symbol | Frequency |
| ------ | --------- |
| A      | 10        |
| B      | 7         |
| C      | 5         |
| D      | 3         |
| E      | 2         |

##### **Step 1: Sort by Frequency**

| Symbol | Frequency |
| ------ | --------- |
| A      | 10        |
| B      | 7         |
| C      | 5         |
| D      | 3         |
| E      | 2         |

##### **Step 2: Divide into Two Groups (Balanced)**
We split the symbols into two groups such that their total frequencies are as balanced as possible.

**Group 1:** {A, B} → Total frequency = **10 + 7 = 17**  
**Group 2:** {C, D, E} → Total frequency = **5 + 3 + 2 = 10**

We assign:
- **"0"** to **Group 1**
    
- **"1"** to **Group 2**

##### **Step 3: Recursively Divide Each Group**
Now, we divide further:

- **Group 1 (A, B)** → Split into:
    
    - **A (10) → "00"**
        
    - **B (7) → "01"**
        
- **Group 2 (C, D, E)** → Split into:
    
    - **C (5) → "10"**
        
    - **D, E (3, 2)** → Split further:
        
        - **D (3) → "110"**
            
        - **E (2) → "111"**
            

##### **Final Shannon-Fano Codes**

|Symbol|Shannon-Fano Code|
|---|---|
|A|00|
|B|01|
|C|10|
|D|110|
|E|111|



