#PPL 


---

# Unit 1.3 Overview — Translation Issues: Syntax and Semantics

## What is Translation?

A computer **cannot directly understand high-level programming languages** like C, Java, or Python.

Programs written by programmers must first be **translated** into machine language.

Translation is performed by language processors such as:

* Compiler
* Interpreter
* Assembler

Example

```c
int x = 10;
```

The compiler translates this into machine instructions that the CPU can execute.

So this unit begins with understanding **how translation works**.

---

# Syntax

After translation, the compiler must determine whether the program is **written correctly**.

This is called checking the **syntax**.

Syntax refers to the **grammar or structure of a programming language**.

Example

Correct

```c
int x = 10;
```

Incorrect

```c
int = x 10;
```

The second statement violates the syntax rules.

This unit explains how syntax is formally described so that computers can understand programming languages.

---

# Syntactic Criteria

These are the rules that determine whether a program is syntactically valid.

Examples include

* keywords
* identifiers
* operators
* punctuation
* statement structure

Example

```c
if(x > 5)
```

is syntactically correct.

But

```c
if > x 5
```

is not.

---

# Syntactic Elements

Every programming language is built from smaller components.

Examples include

* identifiers
* constants
* keywords
* operators
* expressions
* statements
* blocks

Example

```c
x = a + b;
```

Contains

* identifier → x
* operator → =
* identifiers → a, b
* arithmetic operator → +
* statement → whole line

---

# Formal Methods of Describing Syntax

Instead of writing grammar in English, language designers use **formal mathematical notation**.

This unit studies three common methods.

---

## 1. BNF (Backus-Naur Form)

A grammar notation used to describe programming language syntax.

Example

```
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

BNF is widely used in compiler design.

---

## 2. Regular Grammar (RG)

Regular grammar is a simpler grammar used mainly for describing

* identifiers
* numbers
* tokens

Lexical analyzers commonly use Regular Grammar.

---

## 3. Parse Tree

Once grammar rules are defined, the compiler builds a tree showing how a statement is derived.

Example

```
a + b * c
```

The parse tree shows multiplication happening before addition.

Parse trees help verify that syntax is correct.

---

# Ambiguity

Sometimes a grammar can produce **more than one parse tree** for the same statement.

This is called ambiguity.

Example

```
a + b * c
```

Could mean

```
(a+b)*c
```

or

```
a+(b*c)
```

Programming languages avoid ambiguity using precedence and associativity rules.

---

# Parsing Algorithm

Once grammar is defined, the compiler must actually **check whether the program follows it**.

This process is called parsing.

Common parsing methods include

* Top-down parsing
* Bottom-up parsing

Parsing converts program text into a parse tree.

---

# Semantics

Even if syntax is correct, the statement must also **have meaning**.

Semantics refers to the meaning of a program.

Example

```c
int x;
x = 5;
```

Both syntax and semantics are correct.

But

```c
int x;
x = "Hello";
```

Syntax may be correct, but semantics is incorrect because a string cannot be assigned to an integer (in C).

---

# Semantic Modeling

Programming languages also need a formal way to describe meaning.

Two important methods are covered.

---

## Attribute Grammar

Attribute Grammar extends BNF by attaching additional information (attributes) to grammar rules.

It helps describe

* type checking
* scope checking
* declaration checking

Example

```
int x = 5;
```

The compiler verifies that

* x is declared
* x is integer
* 5 is integer

---

## Denotational Semantics

Denotational semantics describes the meaning of a program using mathematical functions.

Instead of explaining **how** the program runs, it specifies **what** the program means mathematically.

It is widely used in programming language theory.

---

# Flow of Unit 1.3

```text
Program
      │
      ▼
Translation
      │
      ▼
Syntax Checking
      │
      ├── Syntactic Criteria
      ├── Syntactic Elements
      ├── BNF
      ├── Regular Grammar
      ├── Parse Tree
      ├── Ambiguity
      └── Parsing Algorithm
      │
      ▼
Semantic Checking
      │
      ├── Attribute Grammar
      └── Denotational Semantics
      │
      ▼
Correct Program
```

---

# Exam Weight and Learning Focus

From this unit, university exams commonly ask questions such as:

* Define translation, compiler, and interpreter.
* What is syntax? Differentiate syntax and semantics.
* Explain syntactic criteria and syntactic elements.
* Write grammar using BNF.
* Construct a parse tree for a given expression.
* Explain ambiguity in grammar with an example.
* Describe parsing algorithms (top-down and bottom-up).
* Explain attribute grammar.
* Explain denotational semantics.
* Differentiate syntax and semantics with examples.

---

# Summary

Unit 1.3 explains **how programming languages are formally defined and understood by a compiler**. It starts with **translation**, then covers **syntax** (the grammatical structure of programs) through concepts such as **BNF**, **Regular Grammar**, **Parse Trees**, **Ambiguity**, and **Parsing Algorithms**. Finally, it introduces **semantics**, which defines the meaning of syntactically correct programs using **Attribute Grammar** and **Denotational Semantics**. Together, these concepts form the theoretical foundation of compiler design and programming language implementation.
