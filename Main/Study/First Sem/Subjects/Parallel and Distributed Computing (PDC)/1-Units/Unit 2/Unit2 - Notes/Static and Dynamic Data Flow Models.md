
## 🧠 **What is Data Flow Architecture?**

**Data Flow Architecture** is a type of computer architecture where **program execution is driven by the availability of data**, not by a fixed sequence of instructions (as in control flow/von Neumann models).

* Computation happens **when data arrives** at an operator.
* Each **node (operator)** in the graph performs a computation.
* **Tokens** (representing data) flow through **edges** (arcs).

---

## 🧱 Types of Data Flow Models

### 1️⃣ **Static Data Flow Model**

> 📌 One token per arc per instruction — **single-use tokens only**.

#### 🔧 Characteristics:

* A **node can only fire once** per input combination.
* Each **arc (edge)** holds at most **one token** at a time.
* **Instructions are uniquely labeled** and executed **once**.
* Less flexible but **simpler** and easier to implement.

#### 🧪 Example:

```c
z = a + b
```

* This operation is represented **once**, and it executes when **a and b tokens** arrive.

#### ⚠️ Limitations:

* Cannot handle **iteration or recursion** easily.
* Reuse of operations requires **manual duplication of nodes**.

---

### 2️⃣ **Dynamic Data Flow Model**

> 📌 Multiple tokens and multiple activations allowed — **supports loops, recursion, and concurrency**.

#### 🔧 Characteristics:

* Allows **multiple tokens on the same arc**, distinguished by **tags or contexts** (e.g., loop iteration index).
* Same instruction (node) can be executed **many times** with **different data tokens**.
* Enables **dynamic control flow**, such as **if-else, recursion, and loops**.
* More complex to implement due to **token management and tagging**.

#### 🧪 Example:

```c
for (i = 0; i < n; i++) {
  sum = sum + a[i];
}
```

* The **same addition node** is used multiple times with **different inputs**.
* Each iteration’s data is tagged uniquely to avoid conflict.

---

## 📊 Comparison Table

| Feature                  | Static Model          | Dynamic Model                |
| ------------------------ | --------------------- | ---------------------------- |
| Tokens per arc           | One                   | Multiple (tagged)            |
| Supports loops/recursion | ❌ No                  | ✅ Yes                        |
| Flexibility              | Low                   | High                         |
| Complexity               | Low                   | High                         |
| Node firing control      | Simple                | Needs token matching         |
| Use cases                | Simple data pipelines | Complex, real-world programs |

---

## ✅ Summary

* **Static data flow**: Good for simple, linear computations.
* **Dynamic data flow**: Needed for realistic programming with conditionals and loops.
* **Data flow architecture** enables natural **parallelism** and **asynchronous** execution.

---
