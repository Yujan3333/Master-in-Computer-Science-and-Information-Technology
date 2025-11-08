
## ✅ **What is Batch Gradient Descent?**

Batch Gradient Descent is a type of **gradient descent optimization** where we **use the entire training dataset** to compute the gradient of the cost (or loss) function and update the model parameters.

---

## 🔁 **How It Works**

1. **Compute the gradient** of the cost function using **all training samples**.
2. **Update the parameters (weights)** only once per iteration (epoch), using the full dataset’s gradient.
3. **Repeat** for a number of iterations (epochs) until the model improves enough.

---

## 🔢 **Pseudocode for Batch Gradient Descent**

```python
for i in range(#epochs): 
    grad = evaluate_gradient(data, para) 
    para = para – learning_rate * grad
```

* `#epochs`: number of full passes over the data
* `evaluate_gradient(data, para)`: calculates how wrong the model is for the **entire dataset**
* `learning_rate`: step size to adjust parameters

---

## ⚖️ **Advantages**

* ✅ **Converges smoothly** toward the minimum because it uses **all the data**.
* ✅ Works well for **convex cost functions** (like linear regression) – guaranteed to find the **global minimum**
* ✅ For **non-convex functions**, it can get stuck in a **local minimum** but still finds a useful solution.

---

## ⚠️ **Disadvantages**

* ❌ Can be **very slow and memory-intensive** for large datasets since it needs to load and process the **entire dataset at once**.
* ❌ Can't update model parameters **in real-time** as new data comes in (no online learning).
* ❌ Doesn’t work when dataset doesn’t fit into computer memory.

---

## 📌 Summary

| Feature          | Batch Gradient Descent              |
| ---------------- | ----------------------------------- |
| Update frequency | Once per epoch (full dataset)       |
| Speed per update | Slow (computes on all data)         |
| Memory           | High (needs full dataset)           |
| Convergence      | Smooth and stable                   |
| Best for         | Smaller datasets or convex problems |

---

### Batch gradient descent also doesn't allow us to update our model online, i.e. with new examples on-the-fly
[Batch gradient doesnot allow to update model online](Batch%20gradient%20doesnot%20allow%20to%20update%20model%20online.md)
[Why are we needed to retrain everything in batch gradient to accumulate new data](Why%20are%20we%20needed%20to%20retrain%20everything%20in%20batch%20gradient%20to%20accumulate%20new%20data.md)
