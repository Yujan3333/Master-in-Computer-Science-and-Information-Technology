#PPL 

# FSA (Finite State Automaton / Finite State Machine)

A **Finite State Automaton (FSA)** is a mathematical model used to recognize patterns or strings in a language. It consists of a **finite number of states** and changes from one state to another based on the input symbols.

FSAs are widely used in **compiler design**, **lexical analysis**, **text processing**, **digital circuits**, and **communication protocols**.

---

# Definition

An **FSA** is a machine that:

* Starts from an **initial (start) state**.
* Reads one input symbol at a time.
* Moves to another state according to the transition rules.
* Accepts the input if it ends in an **accept (final) state**.

---

# Components of an FSA

An FSA consists of:

1. **States (Q)** – A finite set of states.
2. **Alphabet (Σ)** – The set of input symbols.
3. **Transition Function (δ)** – Rules for moving between states.
4. **Start State (q₀)** – The state where processing begins.
5. **Final State(s) (F)** – Accepting states.

Mathematically:

```text
FSA = (Q, Σ, δ, q₀, F)
```

---

# Diagram Example

![](../../../../../../../Images/Third_Sem_Images/Finite%20State%20Machine%20-%20FSA-diag.png)

Suppose we want to accept only the string **"ab"**.

```text
(Start)
   |
   v
 --> (q0) --a--> (q1) --b--> ((q2))
```

Where:

* `q0` = Start state
* `q1` = Intermediate state
* `q2` = Final (accepting) state (shown with a double circle)

Accepted:

```text
ab
```

Rejected:

```text
a
abc
ba
bb
```

---

# Example 1: Binary Numbers Ending in 1

Language:

```text
All binary strings ending with 1
```

Examples:

Accepted:

```text
1
101
111
1001
```

Rejected:

```text
0
10
1100
```

### FSA

```text
                0
             +------+
             |      |
             v      |
 --> (q0) ------0----+
      | \
      |  \1
      |   \
      |   ((q1))
      |     ^
      |     |
      +--0--+
            |
            1
```

Transition table:

| Current State | Input 0 | Input 1 |
| ------------- | ------- | ------- |
| q0            | q0      | q1      |
| q1            | q0      | q1      |

Final state:

```text
q1
```

---

# Example 2: Even Number of Zeros

States:

* q0 = Even number of 0s (Final)
* q1 = Odd number of 0s

Diagram:

```text
          0
 --> ((q0)) ------> (q1)
      ^             |
      |             |
      +------0------+
```

Every time a **0** is read, the machine switches between q0 and q1.

Accepted:

```text
ε (empty string)
11
00
1010
```

Rejected:

```text
0
100
1110
```

---

# Transition Table

For the first example:

| State | Input = 0 | Input = 1 |
| ----- | --------- | --------- |
| q0    | q0        | q1        |
| q1    | q0        | q1        |

This table tells us how the machine moves from one state to another.

---

# Types of Finite State Automata

## 1. DFA (Deterministic Finite Automaton)

* Exactly **one transition** for each input symbol from every state.
* No ambiguity.
* No ε (epsilon) transitions.

Example:
![](../../../../../../../Images/Third_Sem_Images/Finite%20State%20Machine%20-%20FSA-dfa.png)

```text
q0 --a--> q1
```

---

## 2. NFA (Non-Deterministic Finite Automaton)

* A state may have **multiple transitions** for the same input.
* May include **ε-transitions** (moves without consuming input).
* Easier to design than a DFA.
* Every NFA can be converted into an equivalent DFA.

Example:
![](../../../../../../../Images/Third_Sem_Images/Finite%20State%20Machine%20-%20FSA-nfa.png)


```text
           a
q0 ---------> q1
 \
  \
   a
    \
     > q2
```

Here, on input `a`, the machine can move to either `q1` or `q2`.

---

# Applications of FSA

* **Lexical analysis** in compilers (recognizing identifiers, keywords, numbers).
* Pattern matching.
* Regular expression processing.
* Network protocol design.
* Digital circuit design.
* Text searching.
* Spell checking.

---

# Advantages

* Simple and efficient.
* Fast pattern recognition.
* Easy to implement.
* Used in many real-world systems.

---

# Disadvantages

* Can recognize only **regular languages**.
* Cannot handle nested structures like balanced parentheses.
* Has limited memory (only the current state is remembered).

---

# Difference Between DFA and NFA

| DFA                             | NFA                           |
| ------------------------------- | ----------------------------- |
| One transition per input symbol | Multiple transitions possible |
| No ε-transitions                | ε-transitions allowed         |
| Easier to execute               | Easier to design              |
| Exactly one computation path    | Multiple possible paths       |

---

# Exam Answer (5 Marks)

A **Finite State Automaton (FSA)** is a mathematical model used to recognize patterns or strings in a language. It consists of a **finite set of states**, an **input alphabet**, **transition rules**, a **start state**, and one or more **accept (final) states**. The automaton reads one input symbol at a time, changes states according to the transition function, and accepts the input if it finishes in a final state.

**Components:**

* States (Q)
* Input alphabet (Σ)
* Transition function (δ)
* Start state (q₀)
* Final state(s) (F)

**Example:**

```text
 --> (q0) --a--> (q1) --b--> ((q2))
```

This FSA accepts only the string **`ab`**. Finite State Automata are widely used in compiler design for lexical analysis, pattern matching, regular expression processing, and the design of digital systems.
