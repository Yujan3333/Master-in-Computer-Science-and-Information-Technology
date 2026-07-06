#PPL 

# Regular Grammar

A **Regular Grammar (RG)** is a type of grammar that generates **regular languages**. It is the **simplest type of grammar** in the Chomsky Hierarchy and is equivalent in power to a **Finite State Automaton (FSA)** and **regular expressions**.

Regular grammars are mainly used in **compiler design** for **lexical analysis (token recognition)**.

---

# Definition

A **Regular Grammar** is a grammar in which every production rule follows a restricted form.

It contains:

* **Non-terminals (Variables):** `S`, `A`, `B`
* **Terminals:** `a`, `b`, `0`, `1`
* **Production Rules**
* **Start Symbol**

General form:

```text
G = (V, T, P, S)
```

Where:

* **V** = Set of non-terminals
* **T** = Set of terminals
* **P** = Set of production rules
* **S** = Start symbol

---

# Types of Regular Grammar

There are **two types**:

## 1. Right Linear Grammar (RLG)

The non-terminal appears at the **right end**.

General form:

```text
A → aB

A → a

A → ε
```

Example:

```text
S → aA

A → bB

B → c
```

Generation:

```text
S
↓

aA
↓

abB
↓

abc
```

Generated string:

```text
abc
```

---

## 2. Left Linear Grammar (LLG)

The non-terminal appears at the **left end**.

General form:

```text
A → Ba

A → a

A → ε
```

Example:

```text
S → Ab

A → Ba

B → c
```

Here the non-terminal is on the **left side** of the terminals.

---

# Production Rules

A regular grammar allows productions like:

```text
A → aB

A → a

A → ε
```

Not allowed:

```text
A → aBb

A → ABa

A → aBC
```


> [!info]+ 
because more than one non-terminal or a non-terminal in the middle is not permitted.


---
# Example 1

Grammar:

```text
S → aA

A → bB

B → c
```

Derivation:

```text
S

↓

aA

↓

abB

↓

abc
```

Generated string:

```text
abc
```

---

# Example 2

Grammar:

```text
S → 0S

S → 1S

S → ε
```

This grammar generates all binary strings.

Examples:

```text
ε

0

1

00

01

101

11010
```

---

# Example 3

Grammar

```text
S → aS

S → b
```

Possible strings:

```text
b

ab

aab

aaab

aaaab
```

Notice that every string ends with **b**.

---

# Relationship with Finite State Automata (FSA)

Every **Regular Grammar** can be converted into an **FSA**, and every **FSA** can be converted back into an equivalent **Regular Grammar**.

Example:

Grammar:

```text
S → aA

A → b
```

Equivalent FSA:

```text
 --> (S) --a--> (A) --b--> ((Final))
```

Both accept:

```text
ab
```

---

# Relationship with Regular Expressions

These three are **equivalent**:

| Regular Grammar | Regular Expression | FSA                       |
| --------------- | ------------------ | ------------------------- |
| `S → aS \| b`   | `a*b`              | Automaton accepting `a*b` |

They all describe the **same regular language**.

---

# Applications

* Lexical analysis in compilers.
* Pattern matching.
* Token recognition.
* Text processing.
* String validation.
* Regular expression implementation.

---

# Advantages

* Simple and easy to understand.
* Efficient for recognizing regular languages.
* Easy to convert into an FSA.
* Widely used in compiler lexical analysis.

---

# Disadvantages

* Can generate only **regular languages**.
* Cannot represent nested structures like balanced parentheses.
* Less powerful than context-free grammars.

---

# Regular Grammar vs Context-Free Grammar

| Regular Grammar                      | Context-Free Grammar             |
| ------------------------------------ | -------------------------------- |
| Generates regular languages          | Generates context-free languages |
| One non-terminal at most, at one end | More flexible production rules   |
| Equivalent to FSA                    | Equivalent to Pushdown Automata  |
| Simpler                              | More powerful                    |

---

# Exam Answer (5 Marks)

A **Regular Grammar (RG)** is a grammar that generates **regular languages**. It is the simplest type of grammar in the **Chomsky Hierarchy** and is equivalent to **Finite State Automata (FSA)** and **regular expressions**. A regular grammar consists of **non-terminals, terminals, production rules, and a start symbol**.

Regular grammar production rules are of the form:

```text
A → aB

A → a

A → ε
```

where `A` and `B` are non-terminals, `a` is a terminal, and `ε` represents the empty string.

**Example:**

```text
S → aA

A → bB

B → c
```

Derivation:

```text
S ⇒ aA ⇒ abB ⇒ abc
```

Regular grammars are widely used in compiler design for lexical analysis, token recognition, and pattern matching.
