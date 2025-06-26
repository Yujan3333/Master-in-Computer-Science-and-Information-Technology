### 🧮 Expression:

$x = a^d \pmod n$

This is a core step in the **Miller–Rabin Primality Test**.



---

### ✅ 1. **a** – Base

- A **random number** chosen between 2 and $n−2$
    
- It is used to test whether n might be prime
    

---

### ✅ 2. **d** – Exponent

- From $n-1 = 2^s \cdot d$
    
- d is an **odd number**
    
- It’s the part of n−1 that is **not divisible by 2**
    

---

### ✅ 3. Mod n – Modulo Operation

- Means “**remainder when divided by n**”
    
- For example:  
    - 17(mod5)=2.  
	    - Because 17 ÷ 5 = 3 remainder **2**