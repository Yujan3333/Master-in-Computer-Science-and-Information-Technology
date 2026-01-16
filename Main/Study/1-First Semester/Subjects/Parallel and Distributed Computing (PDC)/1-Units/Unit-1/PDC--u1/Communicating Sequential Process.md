
---

## 💬 **Communicating Sequential Processes (CSP)**

### ✅ **Definition:**

CSP is a **formal model** used to describe the behavior of **concurrent systems** through **interacting processes**.

* Each **process** is defined as a sequence of **events**.
* The basic unit of interaction is an **event**.
* The **behavior** of a process is described as:

  $$
  x \rightarrow Q
  $$

  Where:

  * `x` is an **event**,
  * `Q` is the **next process** after event `x` occurs.

---

### 🔤 **Notation:**

* **Lowercase letters**: Events (e.g., `coin`, `candy`, `note`)
* **Uppercase letters**: Processes (e.g., `VM₀`, `VM₁`)
* **Alphabet**: The set of events a process can perform.
  A process cannot engage in an event outside its alphabet.

---

### 🚧 **Example: Simple Vending Machine**

#### 🟢 **Single-use vending machine (serve one customer):**

$$
VM_0 \equiv \text{coin} \rightarrow (\text{candy} \rightarrow \text{stop})
$$

* Accept a coin, then give candy, then **stop**.

#### 🔁 **Repeating vending machine (serve multiple customers):**

$$
VM_1 \equiv \text{coin} \rightarrow (\text{candy} \rightarrow VM_1)
$$

* Accept a coin, give candy, then **restart**.

---

### 🔀 **Parallel Processes:**

CSP also supports **parallel composition** using `||`, where processes run concurrently and may interact.

#### Example: Vending machine with two payment options

$$
\begin{align*}
VM_2 &\equiv (\text{coin} \rightarrow (\text{candy} \rightarrow VM_2)) \\
     &\quad ||\ (\text{notebill} \rightarrow (\text{toffee} \rightarrow VM_2))
\end{align*}
$$

* Two processes running **in parallel**:

  * One handles `coin → candy`
  * The other handles `notebill → toffee`
* The system can serve **both types of customers** indefinitely.

---

### 📝 **Summary (Exam-ready):**

> **CSP (Communicating Sequential Processes)** is a formal model for describing concurrent systems as collections of processes engaging in events.
> A process is written as:
> $x \rightarrow Q$, meaning it performs event `x` then behaves as process `Q`.
> Processes can be combined using parallel composition (`||`).
> Example:
> A vending machine:
>
> $$
> VM_1 \equiv \text{coin} \rightarrow (\text{candy} \rightarrow VM_1)
> $$
>
> This model allows reasoning about system behaviors like **deadlock**, **synchronization**, and **event sequencing**.

---

