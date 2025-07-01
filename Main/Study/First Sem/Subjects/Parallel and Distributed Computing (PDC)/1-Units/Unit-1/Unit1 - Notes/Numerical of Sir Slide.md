
## ✅ Example 1

```
{ x = 5 }     
x = x + 1     
{ x = 6 }
```

- `P` (Pre-condition): `x = 5`
    
- `S` (Statement): `x = x + 1`
    
- `Q` (Post-condition): `x = 6`
    

✅ Since 5 + 1 = 6, this triple is **valid**.

---

## ✅ Example 2

```
{ j = 3 AND k = 4 }     
j = j + k     
{ j = 7 AND k = 4 }
```

- `P`: `j = 3 ∧ k = 4`
    
- `S`: `j = j + k`
    
- `Q`: `j = 7 ∧ k = 4`
    

Explanation:

- Before execution: `j = 3`, `k = 4`
    
- After: `j = 3 + 4 = 7`, `k` remains `4`
    

✅ So, this Hoare Triple is **also valid**.

---

## 🔁 Loop Example 1

```
{ x ≥ 0 }     
while (x ≠ 0) do x = x – 1     
{ x = 0 }
```

Let’s break this:

- Precondition: `x` is **greater than or equal to 0**
    
- Loop condition: `x ≠ 0`
    
- Body: `x = x - 1`
    
- Postcondition: `x = 0`
    

✅ This loop **terminates** because `x` decreases by 1 in each step and will eventually reach 0.

**Example:**  
If `x = 3` → becomes `2`, then `1`, then `0`, then loop stops.

✅ So this Hoare triple is **valid** — it satisfies the condition:  
**If `P` is true and loop terminates, then `Q` is true.**

---

## ♾️ Loop Example 2 — Infinite Loop

```
{ x < 0 }     
while (x ≠ 0) do x = x – 1     
{ x = 0 }
```

Let’s analyze:

- Precondition: `x < 0`
    
- `x = x - 1` makes `x` even **more negative**, never reaching 0.
    
- So the loop condition `x ≠ 0` is **always true**
    
- ❌ The loop **never ends** → **does not terminate**
    

So the **postcondition `x = 0` is never reached**.

⚠️ This Hoare triple is **invalid** **because termination fails.**

---

## 🔁 Rule Summary

You wrote:

```
P ∧ S terminates → Q
```

This means:

- If:
    
    - `P` is true (before execution)
        
    - `S` (the statement or loop) **terminates**
        
- Then:
    
    - `Q` will be true **after execution**
        

✅ This is **exactly what Hoare logic says**.

---

### 🔄 Summary Table of Your Examples

|#|Statement|Terminates?|Postcondition Holds?|Valid?|
|---|---|---|---|---|
|1|`{x=5} x = x+1 {x=6}`|✅ Yes|✅ Yes|✅ Yes|
|2|`{j=3 ∧ k=4} j = j+k {j=7 ∧ k=4}`|✅ Yes|✅ Yes|✅ Yes|
|3|`{x≥0} while(x≠0) x-- {x=0}`|✅ Yes|✅ Yes|✅ Yes|
|4|`{x<0} while(x≠0) x-- {x=0}`|❌ No|❌ No|❌ No|

---
### [Last Numerical](Last%20Numerical.md)