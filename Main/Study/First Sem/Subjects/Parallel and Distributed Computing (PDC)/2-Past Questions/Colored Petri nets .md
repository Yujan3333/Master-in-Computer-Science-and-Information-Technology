
## ✳️ **Definition of Petri Net:**

A **Petri Net** is a **mathematical modeling tool** used to describe and analyze the **flow of information and control** in systems, especially those that are **concurrent**, **distributed**, **parallel**, or **asynchronous**.

### 🔹 **Formally**, a Petri Net is a **5-tuple**:

$$
PN = (P, T, F, M_0, W)
$$

Where:

* $P$: Finite set of **places**
* $T$: Finite set of **transitions**
* $F \subseteq (P \times T) \cup (T \times P)$: **Flow relation**
* $M_0$: **Initial marking** (distribution of tokens)
* $W$: **Weight function** (optional)

### 🔹 **Purpose:**

* Used to model **system behavior**
* Analyze properties like **reachability**, **boundedness**, **liveness**, and **deadlocks**

---

## 🎨 **Colored Petri Net (CPN) and Its Purpose:**

### ✅ **Definition:**

A **Colored Petri Net** is an **extension of the basic Petri Net** where **tokens carry data values** (called **colors**).
This allows modeling of **complex systems** in a more compact and expressive way.

* Places can hold tokens of different types (colors)
* Transitions can have **guard conditions** and **data-manipulating actions**
* Enables **parameterized modeling**

---

### 🎯 **Purposes of Colored Petri Nets:**

1. ✅ **Compact Modeling:**

   * Avoids repetition by using token values instead of creating multiple places/transitions

2. ✅ **Data Handling:**

   * Supports **data operations** directly in transitions using variables and expressions

3. ✅ **Modeling Complex Systems:**

   * Suitable for **communication protocols**, **manufacturing systems**, **workflow systems**

4. ✅ **Simulation and Verification:**

   * Used for **state space analysis**, **performance evaluation**, and **formal verification**

5. ✅ **Tool Support:**

   * Supported by tools like **CPN Tools** for modeling, simulation, and analysis

---

### 📝 **Full Answer Example (to write in exam):**

> A **Petri Net** is a graphical and mathematical modeling tool used to describe and analyze the behavior of concurrent and distributed systems. It consists of places, transitions, and tokens that move according to firing rules. Petri Nets help in verifying properties like deadlocks, liveness, boundedness, and reachability.
>
> A **Colored Petri Net (CPN)** extends the basic Petri Net by allowing tokens to carry data values (colors). This enhances the modeling power and allows compact representation of systems with similar behavior. CPNs are used for modeling real-life complex systems, enabling data manipulation, simulation, and formal analysis using tools like CPN Tools.

---
