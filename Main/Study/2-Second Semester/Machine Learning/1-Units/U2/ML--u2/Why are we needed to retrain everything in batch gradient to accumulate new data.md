
### 🧠 Why Batch Gradient Descent Requires All Data Every Time

Suppose you're training a model with many data points. To update the model's parameters (like weights), Batch Gradient Descent:

1. **Calculates the gradient** of the loss function w.r.t. each parameter.
2. That gradient is based on the **average error** across **all data points**.
3. Only **after** looking at the whole dataset does it decide how to adjust the parameters.

So if **new data arrives**, you can't just tweak your already-trained model a little; you'd have to:

* Add that new data to your dataset
* Recalculate the **gradient using all data again**
* Update the parameters

This means even **one new example requires re-processing the entire dataset** — which is slow and inefficient for real-time or streaming scenarios.

---

### 🛑 Why Can't It Be Done in Real Time?

Because:

* You need the **full dataset** in memory to compute a single gradient update.
* You **can't update after just one example** — you need to collect all data first.
* If you're constantly getting new data (like in a live system), you’d have to **retrain from scratch or keep pausing** everything to do full-batch updates.

This is why **Batch GD is not “online” or real-time friendly**.

---

### ✅ Real-Time Alternative

**Stochastic Gradient Descent (SGD)** solves this:

* It updates parameters **one sample at a time**.
* New data can immediately trigger an update.
* Much faster for streaming data or constantly changing environments.
