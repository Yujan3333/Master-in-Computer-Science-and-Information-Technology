A **convex** function is one where the line segment between any two points on the graph lies **above or on** the graph. A **non-convex** function is one where this isn't always true — the graph might bend up and down, creating multiple valleys and peaks.

---
### 🔷 Convex Function

* **Shape**: Looks like a bowl or cup — always curving upward.
* **Property**: Any line connecting two points on the curve stays **above or on** the curve.
* **Optimization**: Has **only one global minimum** — if you're going downhill, you're guaranteed to reach the lowest point.
* **Example**:
  [ f(x) = x^2 ]
  The curve is U-shaped.



---

### 🔶 Non-Convex Function

* **Shape**: Can have multiple bumps, hills, and valleys.
* **Property**: A line connecting two points might dip below the curve in places.
* **Optimization**: Can have **multiple minima** — you might get stuck in a **local minimum** that isn’t the absolute lowest.
* **Example**:
  [ f(x) = x^3 - 3x]
  The curve bends both up and down.

![](../../../../../../../Images/Second_Sem_Images/Convex%20Vs%20Non-Convex%20Functions-2.png)

---

### 🤖 Why It Matters in Machine Learning

* If the **loss function** is **convex**, gradient descent **always finds the best** (global) solution.
* If the function is **non-convex** (like most deep learning models), gradient descent might get stuck in a **local** minimum — but that's still often good enough!

---

### 🧠 Visual Summary

* ✅ **Convex**: One valley → easy to find the bottom.
* ❌ **Non-convex**: Many valleys → harder to know which is the lowest.

