
## 🔁 **What does "update our model online" mean?**

Updating a model **online** means you can **immediately adjust the model** whenever a **new piece of data** arrives — without needing to retrain it from scratch on all data.

This is useful in cases like:

* Live recommendation systems (e.g., YouTube, Netflix recommending in real time)
* Stock price prediction where data keeps changing
* Sensor data in IoT systems

---

## ❌ **Why Batch Gradient Descent can't do this**

Batch Gradient Descent works by:

* Looking at **all the data at once**
* Calculating the **average gradient over the entire dataset**
* Making a **single update** after processing the full dataset

So when **new data comes in**, the model can't process and learn from it **until the next full training cycle** — which requires loading **all old + new data again**.

That means:

* You can’t dynamically add new examples and learn right away.
* The model can't improve continuously based on **real-time data**.

---

### 📝 Example

Say you train a model on 1,000 examples using batch gradient descent.
Now you get 1 new training example.

With batch gradient descent, to use this new example:

* You **must retrain the whole model** with **all 1,001 examples**.
* You **cannot** just update the model with the new example alone.

---

## ✅ **So what allows online updates?**

Other versions like:

* **Stochastic Gradient Descent (SGD)**: updates the model **one example at a time**
* **Mini-batch Gradient Descent**: updates the model using **small batches of data (e.g., 32 samples)**

These allow the model to be updated **gradually and continuously** as new data comes in.

---

### ✅ Quick takeaway:

> **Batch Gradient Descent** = model learns **offline** in large chunks
> **SGD/Mini-batch** = model can learn **online**, adapting to new data as it comes
