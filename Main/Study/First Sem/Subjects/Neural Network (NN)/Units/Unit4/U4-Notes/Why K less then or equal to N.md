- **Each hidden unit represents a “prototype” or “center”** 

If you have **1000** training examples:
- ✅ K = 50: You select 50 “centers” using clustering (like K-means). Model generalizes well.
    
- ⚠️ K = 1000: You use every training example as a center. Model may overfit.
    
- ❌ K = 1200: Invalid — how can you have more reference points than actual data?
    

---

## 🧠 So in short:

> **K ≤ N** is needed because:
> 
> - Hidden neurons are based on training data.
>     
> - You can't have more "reference centers" than actual examples.
>     
> - More neurons than data = overfitting and wasted computation.
>