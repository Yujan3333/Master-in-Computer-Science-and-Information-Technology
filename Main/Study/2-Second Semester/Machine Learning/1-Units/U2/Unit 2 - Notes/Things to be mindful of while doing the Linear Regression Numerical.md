
# ✅ **1. What students usually get confused about in SGD (exam problems)**

### **(1) Mixing up Gradient Descent vs. SGD**

* **GD uses all data at once** (mean error).
* **SGD uses one data point at a time** (sample-by-sample update).
* Exam questions usually want **SGD** if they say:

  * “one epoch”
  * “update after each example”
  * “using first data point”, etc.

---

### **(2) Wrong sign in the update rule**

Students often confuse:

❌ Wrong:
$w \leftarrow w + \alpha \frac{\partial E}{\partial w}$

✔ Correct (Gradient Descent):
$w \leftarrow w - \alpha \frac{\partial E}{\partial w}$

But for squared error:
$\frac{\partial E}{\partial w_0} = -e,\quad \frac{\partial E}{\partial w_1} = -ex$

So the update becomes:
$w_0 \leftarrow w_0 + \alpha e$
$w_1 \leftarrow w_1 + \alpha e x$
**Students panic because they think it should be minus, but after derivative it becomes plus.**

---

### **(3) Forgetting to compute prediction first**

Many students directly do:

❌ Using $y$ instead of $\hat{y}$
❌ Using wrong error

Correct order:

1. Compute $\hat{y} = w_0 + w_1 x$
2. Compute $e = y - \hat{y}$
3. Plug into update rules

---

### **(4) Using updated weights too early**

Example mistake:

* Compute $w_0$ new
* Use that **new** $w_0$ to compute $w_1$ update

That is **wrong**, because BOTH should use OLD weights.

Correct:

* Compute both updates using old weights
* THEN update the weights.

---

### **(5) Wrong learning rate**

Some exams specify:

* $\alpha = 0.1$
* $\alpha = 0.01$

Students forget it and use their own value.

---

### **(6) Forgetting that it is Stochastic**

SGD updates **after each** of these:

```md
[
(1,3), (2,5), (3,7), (4,9)
]
```

Don't wait until the end to update.

---

### **(7) Rounding mistakes**

Small errors accumulate:

* Rounding too early causes bad results
* Best: keep **3–4 decimal places**

Exam will not require exact machine precision.

---

# ✅ **2. How many iterations should you do in exam?**

### **If the question says “one epoch”**

👉 You **must** do **one update per data point**.

Example dataset (4 points):

* One epoch = **4 updates**
* First epoch → update for (1,3), then (2,5), then (3,7), then (4,9)

---

### **If they say “show one iteration”**

* Do **only the first data point**
* One update only

---

### **If nothing is written**

Most teachers expect:

👉 **One epoch**
or
👉 **Show updates for the first 2–3 points**

But the safest general rule:

✔ If dataset is small (like 3–5 points) → do **all points**
✔ If dataset is big (like 10–20 points) → do **first 2 or 3 only**

---

# ✅ **3. What matters most for exam marks**

You will get full marks if you show clearly:

1. $\hat{y}$
2. $e$
3. Updated $w_0$
4. Updated $w_1$

For each example in the epoch.

### Format your answer like this (easy marks):

**Step i:**
$\hat{y} = w_0 + w_1 x$
$e = y - \hat{y}$
$w_0 = w_0 + \alpha e$
$w_1 = w_1 + \alpha e x$

Show numeric substitution → done.

---
