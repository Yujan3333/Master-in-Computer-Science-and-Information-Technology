#PPL 

**BNF (Backus–Naur Form)** is a **formal notation used to describe the grammar (syntax) of a programming language or any language with a defined structure.**

It tells us **what combinations of symbols are valid** in a language.

---

## Why is BNF used?

BNF is used to:

* Define the syntax of programming languages
* Design compilers and parsers
* Remove ambiguity in language rules
* Describe how statements and expressions are formed

For example, languages like **C, Java, Python, SQL** all have grammars that can be represented using BNF or its extended versions.

---

## Basic BNF Symbols

| Symbol   | Meaning                        | Example                     |
| -------- | ------------------------------ | --------------------------- |
| `< >`    | Non-terminal (can be expanded) | `<expression>`              |
| `::=`    | "is defined as"                | `<digit> ::= 0 \| 1 \| ...` |
| `\|`     | OR (choose one alternative)    | `A \| B`                    |
| Terminal | Actual symbol or keyword       | `if`, `+`, `a`, `5`         |

---

## Example 1: Digits

Suppose we want to define digits.

```bnf
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

Meaning:

A `<digit>` can be

* 0
* or 1
* or 2
* ...
* or 9

Examples

Valid:

```
5
9
0
```

Invalid

```
12
A
%
```

because they are not a single digit.

---

## Example 2: Integer

```bnf
<integer> ::= <digit>
            | <digit><integer>
```

Meaning

An integer can be

* one digit

or

* one digit followed by another integer.

### How does 573 get generated?

Start

```
<integer>
```

↓

```
<digit><integer>
```

↓

```
5<integer>
```

↓

```
5<digit><integer>
```

↓

```
57<integer>
```

↓

```
573
```

---

## Example 3: Identifier

Programming languages allow identifiers like

```
age
count
student1
```

BNF:

```bnf
<identifier> ::= <letter>
               | <letter><identifier>
               | <identifier><digit>
```

where

```bnf
<letter> ::= A | B | C | ... | Z
           | a | b | c | ... | z
```

Examples

Valid

```
sum
age
x1
student25
```

Invalid

```
1abc
%
a-b
```

---

## Example 4: Arithmetic Expression

BNF

```bnf
<expression> ::= <expression> + <term>
               | <term>

<term> ::= <term> * <factor>
         | <factor>

<factor> ::= (<expression>)
           | <number>

<number> ::= <digit>
           | <digit><number>
```

This grammar allows expressions like

```
5+3

7*4

(2+5)

8*(3+2)
```

---

## Example 5: If Statement

```bnf
<if-statement> ::= if (<condition>) <statement>
```

Example

```java
if (x > 5)
    y = 10;
```

---

# How to Read BNF

Suppose

```bnf
<statement> ::= if
              | while
              | for
```

Read it as

> A **statement** can be **if**, **while**, or **for**.

---

## Terminal vs Non-terminal

### Non-terminal

Needs further expansion.

Example

```bnf
<expression>

<digit>

<identifier>
```

---

### Terminal

Cannot be expanded.

Example

```
if

+

3

(
)

while
```

These are actual symbols that appear in the program.

---

## Small Example

Grammar

```bnf
<animal> ::= cat | dog
```

Possible outputs

```
cat

dog
```

Not

```
cow
```

because it is not defined.

---

## Another Example

```bnf
<greeting> ::= Hello <name>

<name> ::= Ram
         | Sita
```

Possible sentences

```
Hello Ram

Hello Sita
```

---

# Advantages of BNF

* Clearly defines language syntax.
* Easy for humans and compilers to understand.
* Eliminates ambiguity in grammar.
* Widely used in compiler design and language specification.

---

# Limitations of BNF

* Describes **syntax only**, not meaning (semantics).
* Can become lengthy for complex languages.
* Often replaced by **Extended BNF (EBNF)** for more concise grammar descriptions.

---

# Exam Answer (5 Marks)

**Backus–Naur Form (BNF)** is a formal notation used to define the **syntax (grammar)** of programming languages. It consists of **non-terminals** (written inside `< >`), **terminals** (actual symbols or keywords), the definition operator `::=` (meaning "is defined as"), and the OR operator `|` (meaning "choose one"). BNF is widely used in compiler design to specify valid language structures.

Example:

```bnf
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

<number> ::= <digit>
           | <digit><number>
```

This grammar defines digits and numbers. For example, `573` is a valid `<number>`, while `A5` is not according to these rules.
