## 🎯 **Goal of the Code**

The code checks **where a third point $P$** lies in relation to a **directed line segment from point $P_0$ to $P_1$**.

The possible positions of point $P$ are:

* **Left** of the line
* **Right** of the line
* **Behind** (before $P_0$)
* **Beyond** (after $P_1$)
* **Origin** (coincides with $P_0$)
* **Terminus** (coincides with $P_1$)
* **Between** (on the segment between $P_0$ and $P_1$)

---

## 🔢 **Math Behind the Logic**

### Step 1: **Vector Setup**

We define the vectors:

* $\vec{A} = P_1 - P_0 = (x_1 - x_0, y_1 - y_0)$
* $\vec{B} = P - P_0 = (x - x_0, y - y_0)$

We use these two vectors to figure out where point $P$ is relative to the line from $P_0$ to $P_1$.

---

### Step 2: **Cross Product** — To check Left or Right

The 2D cross product (also called the **perpendicular dot product**) is:

$$
\vec{A} \times \vec{B} = (x_1 - x_0)(y - y_0) - (y_1 - y_0)(x - x_0)
$$

Interpretation:

* If the result is **positive**, $P$ is to the **left** of the vector $\vec{A}$
* If it's **negative**, $P$ is to the **right**
* If it's **zero**, $P$ is **colinear** (on the same line as $P_0 \rightarrow P_1$)

---

### Step 3: **Dot Product** — To check Behind, Between, Beyond

Only used **if the cross product is zero** (i.e. point is colinear):

We compute the **dot product**:

$$
\vec{A} \cdot \vec{B} = (x_1 - x_0)(x - x_0) + (y_1 - y_0)(y - y_0)
$$

Let:

* $\text{dot} = \vec{A} \cdot \vec{B}$
* $\text{len\_sq} = \vec{A} \cdot \vec{A}$ (squared length of the segment)

Interpretation:

* If `dot < 0` → point $P$ is **behind** $P_0$
* If `dot > len_sq` → point $P$ is **beyond** $P_1$
* If `dot == 0` → point $P = P_0$ → **Origin**
* If `dot == len_sq` → point $P = P_1$ → **Terminus**
* If $0 < \text{dot} < \text{len\_sq}$ → point lies **between** $P_0$ and $P_1$

---

## 📈 Plotting in the Code

To help visualize:

* It plots the **main line segment** $P_0 \rightarrow P_1$
* Adds **dotted extensions** for:

  * **Behind**: extension backward from $P_0$
  * **Beyond**: extension forward from $P_1$
* Marks the test point $P$ and labels it with its classification

---

## 🧠 Summary of Classifications

| Case     | Condition                    | Meaning                               |
| -------- | ---------------------------- | ------------------------------------- |
| Left     | $\vec{A} \times \vec{B} > 0$ | P is to the left of the line segment  |
| Right    | $\vec{A} \times \vec{B} < 0$ | P is to the right of the line segment |
| Behind   | Cross = 0 and Dot < 0        | P lies before the start               |
| Beyond   | Cross = 0 and Dot > len\_sq  | P lies after the end                  |
| Origin   | P == P0                      | P is the starting point               |
| Terminus | P == P1                      | P is the ending point                 |
| Between  | 0 < Dot < len\_sq            | P lies between start and end          |
