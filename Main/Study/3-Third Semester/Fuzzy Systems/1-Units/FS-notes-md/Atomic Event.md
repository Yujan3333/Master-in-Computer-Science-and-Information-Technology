#fuzzy-system #third-semester 

# Atomic Event (Exam Summary)

## Definition

An **Atomic Event** is a **complete specification of the state of the world** about which the agent is uncertain.

In other words, an atomic event gives the value of **every random variable** in the system. Once all random variables are assigned values, there is no uncertainty about that particular state. 

---

# Simple Explanation

Suppose our world has only **two Boolean random variables**:

* **Cavity** = {True, False}
* **Toothache** = {True, False}

Since each variable has **2 possible values**, the total number of atomic events is:

$$
2 \times 2 = 4
$$

Each atomic event is a **complete combination** of these values.

---

# The Four Atomic Events

The notes give one atomic event:

* **Cavity = False, Toothache = True**

The remaining three are:

| Atomic Event | Cavity | Toothache               |
| ------------ | ------ | ----------------------- |
| Event 1      | True   | True                    |
| Event 2      | True   | False                   |
| Event 3      | False  | True *(given in notes)* |
| Event 4      | False  | False                   |

These are **all possible complete states** of the world.

---

# Why is it Called "Atomic"?

The word **atomic** means **indivisible**.

An atomic event cannot be broken into smaller events because it already specifies **every random variable** completely.

For example:

* **Cavity = True** ❌ *(Not atomic, because Toothache is still unknown.)*
* **Cavity = True, Toothache = False** ✅ *(Atomic, because both variables are specified.)*

---

# General Rule

If there are:

* $n$ Boolean random variables,

then the total number of atomic events is:

$$
2^n
$$

For this example:

* Number of variables = 2

Therefore,

$$
2^2 = 4
$$

atomic events.

---

# Key Points

* An **atomic event** is a **complete assignment** of values to **all** random variables.
* It represents one possible state of the world.
* With two Boolean variables (**Cavity** and **Toothache**), there are **4 atomic events**.
* Every atomic event specifies **all variables**, leaving no uncertainty.

---

# 5-Mark Exam Answer

**Atomic Event:**
An **atomic event** is a complete specification of the state of the world about which an agent is uncertain. It assigns a value to **every random variable** in the system. In the notes, the world contains two Boolean random variables: **Cavity** and **Toothache**, each having the domain ${\text{True}, \text{False}}$. Therefore, there are four possible atomic events:

1. Cavity = True, Toothache = True
2. Cavity = True, Toothache = False
3. Cavity = False, Toothache = True
4. Cavity = False, Toothache = False

Each atomic event represents one complete and unique state of the world. 

---

## Exam Tip

Students often confuse **random variables** with **atomic events**.

| Random Variable                                | Atomic Event                                      |
| ---------------------------------------------- | ------------------------------------------------- |
| A single uncertain variable (e.g., **Cavity**) | A complete assignment of **all** random variables |
| Example: `Cavity`                              | Example: `(Cavity=True, Toothache=False)`         |
| Does **not** fully describe the world          | Fully describes one possible state of the world   |
