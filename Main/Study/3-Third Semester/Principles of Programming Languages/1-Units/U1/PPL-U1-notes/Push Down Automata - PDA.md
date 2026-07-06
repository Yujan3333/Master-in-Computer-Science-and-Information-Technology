#PPL 

# Pushdown Automata (PDA)

A **Pushdown Automata (PDA)** is a finite automaton (FSA) with an **additional memory called a stack**. The stack allows the PDA to recognize **Context-Free Languages (CFLs)**, which cannot be recognized by a normal FSA.

PDAs are widely used in **compiler design**, especially during **syntax analysis (parsing)**.

---

# Definition

A **Pushdown Automata (PDA)** is a computational model that:

* Reads one input symbol at a time.
* Changes from one state to another.
* Uses a **stack** to store and remove symbols.
* Accepts the input if it reaches an accepting state (or an empty stack, depending on the PDA).

---

# Why Do We Need a PDA?

A **Finite State Automaton (FSA)** has **no memory**, so it cannot recognize languages that require matching symbols.

Example:

```text
L = { aⁿbⁿ | n ≥ 1 }
```

Valid strings:

```text
ab
aabb
aaabbb
aaaabbbb
```

The machine must remember **how many `a`s** it has seen to compare them with the number of `b`s`.

An FSA cannot do this.

A PDA can do this using its **stack**.

---

# Components of a PDA

A PDA consists of:

1. **States (Q)** – Finite set of states.
2. **Input Alphabet (Σ)** – Input symbols.
3. **Stack Alphabet (Γ)** – Symbols that can be stored in the stack.
4. **Transition Function (δ)** – Rules for moving between states.
5. **Start State (q₀)** – Initial state.
6. **Start Stack Symbol (Z₀)** – Initial stack symbol.
7. **Final State(s) (F)** – Accepting states.

Mathematically:

```text
PDA = (Q, Σ, Γ, δ, q₀, Z₀, F)
```

---

# Basic Stack Operations

A PDA performs three basic stack operations:

### 1. Push

Adds an item to the top of the stack.

Example:

```text
Stack before

Top
----
A
B

Push X

Top
----
X
A
B
```

---

### 2. Pop

Removes the top item.

Example:

```text
Before

Top
----
X
A
B

Pop

Top
----
A
B
```

---

### 3. No Operation

Leaves the stack unchanged.

---

# Example: Language aⁿbⁿ

Language:

```text
L = { aⁿbⁿ | n ≥ 1 }
```

Examples:

Accepted:

```text
ab
aabb
aaabbb
```

Rejected:

```text
abb
aab
aaabb
```

---

## PDA Working

For every `a`:

* Push one symbol (`A`) onto the stack.

For every `b`:

* Pop one `A` from the stack.

If:

* All input is read, **and**
* The stack returns to its initial state,

then the string is accepted.

---

### Example: Input = `aabb`

| Input | Action  | Stack |
| ----- | ------- | ----- |
| Start | Initial | Z     |
| a     | Push A  | AZ    |
| a     | Push A  | AAZ   |
| b     | Pop A   | AZ    |
| b     | Pop A   | Z     |
| End   | Accept  | Z     |

The number of pushes equals the number of pops, so the string is accepted.

---

# PDA State Diagram

```text
                a / Push A
           +------------------+
           |                  |
           v                  |
 --> (q0) ---------> (q1)
       |               |
       |               |
       | b / Pop A     |
       +-------------> ((q2))
```

Conceptually:

* `q0` = Start.
* `q1` = Reading `a`s and pushing onto the stack.
* `q2` = Reading `b`s and popping from the stack. Accept when the input is finished and the stack is balanced.

---

# PDA vs FSA

| FSA                          | PDA                               |
| ---------------------------- | --------------------------------- |
| No memory                    | Has a stack                       |
| Recognizes regular languages | Recognizes context-free languages |
| Cannot count                 | Can match/count using the stack   |
| Simpler                      | More powerful                     |

---

# Applications of PDA

* Syntax analysis (parsing) in compilers.
* Checking balanced parentheses.
* Matching opening and closing brackets.
* Expression parsing.
* XML and HTML tag matching (conceptually).
* Processing context-free languages.

---

# Advantages

* Has stack memory.
* Recognizes context-free languages.
* Can handle nested structures.
* Used in compiler parsers.

---

# Disadvantages

* More complex than an FSA.
* Cannot recognize all context-sensitive languages.
* Limited to one stack (standard PDA).

---

# FSA vs PDA vs Turing Machine

| Feature               | FSA     | PDA          | Turing Machine         |
| --------------------- | ------- | ------------ | ---------------------- |
| Memory                | None    | Stack        | Unlimited tape         |
| Language              | Regular | Context-Free | Recursively Enumerable |
| Can recognize `aⁿbⁿ`? | ❌ No    | ✅ Yes        | ✅ Yes                  |
| Power                 | Lowest  | Medium       | Highest                |

---

# Exam Answer (5 Marks)

A **Pushdown Automata (PDA)** is a finite automaton with an additional **stack memory**, making it capable of recognizing **context-free languages**. A PDA reads the input one symbol at a time, changes states according to transition rules, and performs **push** and **pop** operations on the stack. It is widely used in compiler design for **syntax analysis (parsing)**.

The components of a PDA are:

* States (Q)
* Input alphabet (Σ)
* Stack alphabet (Γ)
* Transition function (δ)
* Start state (q₀)
* Initial stack symbol (Z₀)
* Final state(s) (F)

A PDA is represented as:

```text
PDA = (Q, Σ, Γ, δ, q₀, Z₀, F)
```

**Example:**

For the language:

```text
L = { aⁿbⁿ | n ≥ 1 }
```

the PDA pushes one symbol onto the stack for each `a` and pops one symbol for each `b`. If all input is processed and the stack returns to its initial state, the string is accepted.

Examples:

* ✅ `ab`, `aabb`, `aaabbb`
* ❌ `abb`, `aab`, `aaabb`

**Key Point for Exams:**

* **FSA → Regular Languages**
* **PDA → Context-Free Languages (uses a stack)**
* **Turing Machine → Recursively Enumerable Languages (uses unlimited tape)**
