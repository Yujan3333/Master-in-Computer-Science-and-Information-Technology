#PPL 

# Regular Expression (Regex)

A **Regular Expression (RE or Regex)** is a sequence of symbols used to describe or represent a **pattern of strings** in a **regular language**.

In compiler design, regular expressions are mainly used in **lexical analysis** to identify **tokens** such as identifiers, keywords, numbers, and operators.

---

# Definition

A **Regular Expression** is a notation used to represent a set of strings using **characters and special operators**.

For example:

```text
a*
```

means:

> **Zero or more occurrences of `a`**

Possible strings:

```text
ε
a
aa
aaa
aaaa
```

where **ε (epsilon)** means the **empty string**.

---

# Basic Symbols in Regular Expressions

| Symbol               | Meaning                     | Example    |          |
| -------------------- | --------------------------- | ---------- | -------- |
| `a`                  | Character                   | `a`        |          |
| `b`                  | Character                   | `b`        |          |
| `                    | `                           | OR (Union) | `a \| b` |
| `.` or Concatenation | Followed by                 | `ab`       |          |
| `*`                  | Zero or more times          | `a*`       |          |
| `+`                  | One or more times           | `a+`       |          |
| `?`                  | Zero or one time (optional) | `a?`       |          |
| `( )`                | Grouping                    | `(ab)*`    |          |
| `ε`                  | Empty string                | `ε`        |          |

---

# Regular Expression Operators
![](../../../../../../../Images/Third_Sem_Images/Regular%20Expressions-fig.png)


## 1. Union (`|`)

Means **either this or that**.

Example:

```text
a|b
```

Accepted strings:

```text
a
b
```

Not accepted:

```text
ab
ba
```

---

## 2. Concatenation

Means one symbol followed by another.

Example:

```text
ab
```

Accepted:

```text
ab
```

Not accepted:

```text
a

b

ba
```

---

## 3. Kleene Star (`*`)

Means **zero or more repetitions**.

Example:

```text
a*
```

Accepted:

```text
ε

a

aa

aaa

aaaa
```

---

## 4. Plus (`+`)

Means **one or more repetitions**.

Example:

```text
a+
```

Accepted:

```text
a

aa

aaa
```

Not accepted:

```text
ε
```

because at least one `a` is required.

---

## 5. Optional (`?`)

Means **zero or one occurrence**.

Example:

```text
a?
```

Accepted:

```text
ε

a
```

Not accepted:

```text
aa
```

---

# Examples

## Example 1

Regular Expression:

```text
ab
```

Accepted:

```text
ab
```

Rejected:

```text
a

b

abc
```

---

## Example 2

Regular Expression:

```text
a*
```

Accepted:

```text
ε

a

aa

aaa
```

---

## Example 3

Regular Expression:

```text
(a|b)
```

Accepted:

```text
a

b
```

---

## Example 4

Regular Expression:

```text
(a|b)*
```

Accepted:

```text
ε

a

b

ab

ba

abab

bbbaaa
```

This means:

> Any combination of **a** and **b**, including the empty string.

---

## Example 5

Regular Expression:

```text
a*b
```

Meaning:

* Zero or more `a`
* Followed by one `b`

Accepted:

```text
b

ab

aab

aaab

aaaab
```

Rejected:

```text
a

bb

aba
```

---

# Identifier Example

A programming language identifier can be represented as:

```text
[A-Za-z][A-Za-z0-9]*
```

Meaning:

* First character must be a letter.
* Remaining characters can be letters or digits.

Valid:

```text
count

student1

ABC123

x
```

Invalid:

```text
1count

@abc

-name
```

---

# Number Example

Integers:

```text
[0-9]+
```

Accepted:

```text
5

123

45678
```

---

Signed integers:

```text
[-+]?[0-9]+
```

Accepted:

```text
10

-20

+35
```

---

# Relationship with Regular Grammar and FSA

All three are **equivalent**.

| Regular Expression | Regular Grammar | FSA                       |
| ------------------ | --------------- | ------------------------- |
| `a*b`              | `S → aS \| b`   | Automaton accepting `a*b` |

They all represent the same **regular language**.

---

# Applications

* Lexical analysis in compilers.
* Pattern matching.
* Search and replace in text editors.
* Input validation (email, phone number, password).
* Log file analysis.
* Web form validation.

---

# Advantages

* Short and concise notation.
* Easy pattern matching.
* Fast searching.
* Widely supported in programming languages.

---

# Disadvantages

* Difficult to read for complex patterns.
* Cannot recognize nested structures (e.g., balanced parentheses).
* Limited to regular languages.

---

# Difference Between Regular Expression and Regular Grammar

| Regular Expression                     | Regular Grammar              |
| -------------------------------------- | ---------------------------- |
| Pattern notation                       | Grammar rules                |
| Compact                                | More detailed                |
| Used for searching and matching        | Used for language generation |
| Equivalent in power to regular grammar | Equivalent in power to regex |

---

# Exam Answer (5 Marks)

A **Regular Expression (RE)** is a sequence of characters and operators used to represent a **pattern of strings** in a regular language. It is widely used in compiler design during **lexical analysis** to recognize tokens such as identifiers, numbers, and keywords.

The main operators are:

* `|` (union or OR)
* Concatenation (placing symbols together)
* `*` (Kleene star: zero or more repetitions)
* `+` (one or more repetitions)
* `?` (optional occurrence)

**Example:**

```text
a*b
```

This regular expression represents **zero or more `a` characters followed by one `b`**.

Accepted strings:

```text
b
ab
aab
aaab
```

Regular expressions are equivalent in expressive power to **Regular Grammars** and **Finite State Automata (FSA)** and are widely used for pattern matching, lexical analysis, text processing, and input validation.
