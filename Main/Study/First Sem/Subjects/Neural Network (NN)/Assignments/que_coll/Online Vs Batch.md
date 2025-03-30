### **Difference Between Online and Batch Gradient Descent**

Gradient Descent is an optimization algorithm used to update the weights of a neural network by minimizing the loss function. There are **three main types**:

1. **Batch Gradient Descent (BGD)**
    
2. **Stochastic (Online) Gradient Descent (SGD)**
    
3. **Mini-Batch Gradient Descent (MBGD)** _(a mix of both)_
    

Let's focus on **Online (SGD) vs. Batch (BGD)**:

---

### **1️⃣ Online Gradient Descent (Stochastic Gradient Descent - SGD)**

- Updates **weights after each training sample**.
    
- **Pros:**
    
    - Faster updates → useful for large datasets.
        
    - Can escape local minima due to noisy updates.
        
    - More suitable for real-time learning.
        
- **Cons:**
    
    - Noisy updates → may not converge smoothly.
        
    - Computationally inefficient for small datasets.
        

✅ **Example:**  
If we have 4 training samples in XOR:

1. Update weights using first sample.
    
2. Update again using second sample.
    
3. Continue for each sample individually.
    

---

### **2️⃣ Batch Gradient Descent (BGD)**

- Updates **weights after processing the entire dataset** (i.e., one update per epoch).
    
- **Pros:**
    
    - Smoother convergence (less noise).
        
    - Efficient for small datasets.
        
- **Cons:**
    
    - Slower for large datasets.
        
    - Requires more memory (holds entire dataset at once).
        
    - Might get stuck in local minima.
        

✅ **Example:**

1. Compute **average** gradient over all training samples.
    
2. Update weights only once per epoch.
    

---

### **Key Differences in a Table**

|Feature|Online (SGD)|Batch (BGD)|
|---|---|---|
|**Weight update**|After each sample|After all samples in dataset|
|**Computational cost**|Lower (per step)|Higher (per step)|
|**Speed**|Faster for large datasets|Slower for large datasets|
|**Memory usage**|Low (only one sample at a time)|High (entire dataset in memory)|
|**Convergence**|Noisy, but can escape local minima|Smoother, but might get stuck|

---

### **When to Use Which?**

- **Use Online (SGD) if:**
    
    - You have a **large dataset**.
        
    - You need real-time updates.
        
    - You want to escape local minima.
        
- **Use Batch (BGD) if:**
    
    - You have a **small dataset**.
        
    - You need stable convergence.
        
    - Memory is not a constraint.
        

---

### **Bonus: Mini-Batch Gradient Descent**

If you want a trade-off between speed and stability, use **Mini-Batch Gradient Descent**, which updates weights after processing a small batch (e.g., 32 samples at a time). 🚀