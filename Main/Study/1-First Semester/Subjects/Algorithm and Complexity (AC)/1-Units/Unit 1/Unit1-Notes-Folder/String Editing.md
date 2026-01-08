## What is String Editing?

String editing refers to **transforming one string into another** using a set of allowed operations. The goal is usually to find the **minimum number of operations** needed.

## Common String Editing Problems

### 1. Edit Distance (Levenshtein Distance) - Most Important

**Problem**: Transform string A into string B using minimum operations.

**Allowed Operations**:

- **Insert** a character
- **Delete** a character
- **Replace** a character
![](../../../../../../../../Images/Second_Sem_Images/String%20Editing-rules.png)
- IN substitution no change =0
---
## Numerical
![](../../../../../../../../Images/First_Sem_Images/String%20Editing-que.png)

### 🧾 **Given:**

- **Source string**: `a a b a b` → length = 5
    
- **Destination string**: `b a b b` → length = 4

### ✅ Final Edit Distance = **3**

To convert `"a a b a b"` → `"b a b b"`, we need **3 operations** (using only insert, delete, copy):

### 🔁 Possible Sequence of Operations (not unique):

1. **Delete a₁** (`a`)
    
2. **Copy a₂** (`a`)
    
3. **Copy b₃** (`b`)
	    
4. **Insert b** at the end