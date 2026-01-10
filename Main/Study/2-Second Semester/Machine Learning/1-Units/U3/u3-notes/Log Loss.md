## **1️⃣ What is Log Loss?**

* Log loss, also called **logarithmic loss** or **cross-entropy loss**, is a metric for **classification models** that output probabilities between 0 and 1.
* Unlike accuracy, which only checks if the prediction is correct or wrong, log loss **penalizes predictions that are confident but wrong**.

---

## **2️⃣ How it works**

1. For each sample, the model predicts a probability of belonging to the positive class.
2. If the model predicts **correctly with high confidence**, the loss is small.
3. If the model predicts **wrongly with high confidence**, the loss is large.
4. The negative log is used so that the loss is **positive**, and **lower loss means a better model**.

---

## **3️⃣ Example**

Suppose we have **one sample**:

* Actual class = positive
* Model predicts 0.9 probability for positive → Loss is small (~0.1)
* Model predicts 0.1 probability for positive → Loss is large (~2.3)

✅ Key point: The more **confident and wrong** the prediction, the **higher the penalty**.

---

Log loss is very useful when your model gives **probabilities** instead of just class labels because it rewards models that are **accurate and confident**.

---