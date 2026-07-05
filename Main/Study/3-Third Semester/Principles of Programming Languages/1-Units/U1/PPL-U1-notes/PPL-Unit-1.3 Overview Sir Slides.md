#PPL 

Here's an **exam-focused summary** of **Unit 3: Language Translation Issues** based on your notes. I have highlighted the **most important definitions, comparisons, compiler phases, grammars, automata, and likely exam questions**. 

---

# UNIT 3 – LANGUAGE TRANSLATION ISSUES (Exam Notes)

---

# 1. Programming Language Syntax ⭐⭐⭐

## Definition

**Syntax** is the set of rules that define **how programs are written** in a programming language.

It tells:

* How statements are written
* How declarations are written
* How expressions are written

Example

```text
X = 2.45 + 3.67
```

Syntax only says this statement is **correctly written**.

It **cannot tell**

* whether X is declared
* whether X is integer or float

That is the job of **semantics**.

---

## Syntax vs Semantics ⭐⭐⭐⭐⭐ (Very Important)

| Syntax                   | Semantics                     |
| ------------------------ | ----------------------------- |
| Deals with grammar       | Deals with meaning            |
| Checks program structure | Checks program correctness    |
| Done during parsing      | Done during semantic analysis |
| Example: Missing ;       | Example: Type mismatch        |

Example

```java
int x;
x = "Hello";
```

Syntax ✔

Semantics ✖ (int cannot store String)

---

# 2. General Syntactic Criteria ⭐⭐⭐⭐

There are **5 criteria**

---

## 1. Readability

How easily humans understand a program.

Improved by

* meaningful identifiers
* keywords
* comments
* structured statements
* indentation

Example

```java
totalMarks
```

better than

```java
a
```

---

## 2. Writability

How easy it is to write programs.

Improved by

* simple syntax
* regular syntax
* meaningful operators

---

## 3. Ease of Verifiability

Easy to mathematically prove correctness.

Readable + simple programs are easier to verify.

---

## 4. Ease of Translation

Easy for compiler to translate.

Simple syntax → easier compiler

Complex syntax → harder compiler

---

## 5. Lack of Ambiguity ⭐⭐⭐⭐⭐

Every statement should have only **one meaning**.

---

Example

```text
if A
    if B
       S1
    else
       S2
```

Question:

Does else belong to first if?

or second if?

This is called

## Dangling Else Problem ⭐⭐⭐⭐⭐

---

Solutions

### ALGOL

Uses

```
begin
...
end
```

---

### Ada

Uses

```
end if
```

---

### C and Pascal

Else always matches the **nearest if**

---

# 3. Syntactic Elements ⭐⭐⭐⭐

Know these.

---

### Character Set

Characters used in language

Examples

* ASCII
* Unicode
* EBCDIC

---

### Identifier

Names of variables/functions/classes.

Example

```
sum
totalMarks
studentName
```

Rules

* starts with letter
* letters + digits

---

### Operators

```
+
-
*
/
%
```

---

### Keywords

Reserved words.

Cannot be variable names.

Examples

```
if
while
for
int
float
```

---

### Noise Words

Words only for readability.

Example

```
GO TO
```

TO is optional.

---

### Comments

Improve readability.

Example

```java
// single line

/* multi line */
```

---

### Blanks (Spaces)

C ignores most spaces.

---

### Delimiters

Used to mark beginning/end.

Examples

```
()
{}
[]
;
```

---

### Free Field Format

Write anywhere.

Example

C

Java

Python

---

### Fixed Field Format

Position matters.

Example

FORTRAN

---

### Expressions

Return a value.

Example

```java
a+b*c
```

---

### Statements

Perform action.

Example

```java
x=5;
```

---

# 4. Program Structure ⭐⭐⭐

Ways subprograms are organized.

Know these names:

* Separate subprogram
* Separate data definition
* Nested subprogram
* Separate interface
* Separate data declarations
* Unseparated subprogram

Examples

Java

Uses classes.

C

Uses header files.

---

# 5. Stages of Translation ⭐⭐⭐⭐⭐ (Most Important)

Compiler has two major parts

```
Analysis

↓

Synthesis
```

---

# Analysis Phase

Compiler understands source program.

Contains

### 1. Lexical Analysis ⭐⭐⭐⭐⭐

Input

Characters

Output

Tokens

Example

```java
int x=5;
```

Tokens

```
int

identifier

=

number

;
```

Also

* removes spaces
* stores identifiers in symbol table

Uses

## Finite State Automata (FSA)

---

### 2. Syntax Analysis (Parsing) ⭐⭐⭐⭐⭐

Input

Tokens

Output

Parse Tree

Checks grammar.

Example

```
a = b + c
```

Correct syntax?

Yes

---

### 3. Semantic Analysis ⭐⭐⭐⭐⭐

Checks meaning.

Detects

* undeclared variable
* type mismatch
* wrong function arguments

Example

```java
int x;

x="hello";
```

Semantic Error

---

# Synthesis Phase

Produces executable program.

Contains

---

### Optimization

Makes code faster.

Removes

* unnecessary calculations
* dead code

---

### Code Generation

Converts intermediate code into

* Assembly
* Machine code

---

### Linking and Loading ⭐⭐⭐⭐

Combines multiple object files.

Produces executable (.exe)

---

# Compiler Passes ⭐⭐⭐

### One-pass Compiler

Fast compilation

Little optimization

---

### Two-pass Compiler

Most common

```md
Pass 1 → Analyze

Pass 2 → Generate Code

```

---

### Three-pass Compiler

```md
Pass 1

Analyze

↓

Pass 2

Optimize

↓

Pass 3

Generate code
```

---

# Compiler Flow ⭐⭐⭐⭐⭐

```
Source Program

↓

Lexical Analysis

↓

Syntax Analysis

↓

Semantic Analysis

↓

Optimization

↓

Code Generation

↓

Linking & Loading

↓

Executable Program
```

---

# 6. Bootstrapping ⭐⭐⭐⭐

Definition

Using a compiler to compile itself.

Called

Self-hosting compiler

Example

C compiler compiling newer C compiler.

---

# 7. Formal Translation Models ⭐⭐⭐⭐⭐

Grammar defines syntax.

Compiler mainly uses

1. BNF Grammar

2. Regular Grammar

---

# 8. BNF (Backus-Naur Form) ⭐⭐⭐⭐⭐

Used to describe language syntax.

Developed by

John Backus

Peter Naur

Equivalent to

CFG (Context Free Grammar)

---

Symbols

```
::=

means

is defined as
```

```
|

means

OR
```

Example

```
<digit>

::=

0|1|2|3...
```

---

Example Identifier

```
<identifier>

::=

<letter>

|

<identifier><digit>
```

---

# Parse Tree ⭐⭐⭐⭐

Shows derivation of sentence.

If parse tree exists

↓

Syntax correct

Otherwise

↓

Syntax Error

---

# Ambiguous Grammar ⭐⭐⭐⭐⭐

Definition

One string has **two different parse trees.**

This is called

Grammar Ambiguity.

---

# Extension to BNF (EBNF) ⭐⭐⭐⭐

New symbols

```
[]

optional
```

```
{}

repetition
```

```
|

alternative
```

Example

```
[+|-]

means optional sign
```

---

# Syntax Chart

Also called

Railroad Diagram

Graphical version of EBNF.

---

# 9. Finite State Automata (FSA) ⭐⭐⭐⭐⭐

Used in

Lexical Analysis

Recognizes

Tokens

---

Components

* Start state
* Final state
* Transitions

---

### Deterministic FSA (DFA)

One transition per input.

---

### Non-deterministic FSA (NFA)

Multiple possible transitions.

Accepted if **any path reaches final state.**

---

# DFA vs NFA ⭐⭐⭐⭐

| DFA            | NFA                  |
| -------------- | -------------------- |
| One transition | Multiple transitions |
| Faster         | Easier to design     |
| One path       | Many paths           |

---

# 10. Regular Grammar ⭐⭐⭐⭐

Equivalent to

FSA

Right side contains

Terminal

or

Terminal + Nonterminal

Example

```
A→0A|1A|0
```

---

# 11. Regular Expression ⭐⭐⭐⭐⭐

Equivalent to

Regular Grammar

Equivalent to

FSA

Symbols

```
|

OR
```

```
*

Kleene Closure

(0 or more)
```

```
ab

concatenation
```

Example

```
letter(letter|digit)*
```

Identifier

---

# 12. Pushdown Automata (PDA) ⭐⭐⭐⭐⭐

FSA + Stack

Used for

Context Free Grammar

BNF Grammar

---

Difference

```
FSA

No stack

PDA

Has stack
```

---

PDA recognizes

```
aⁿbⁿ
```

FSA cannot.

---

# FSA vs PDA ⭐⭐⭐⭐⭐

| FSA              | PDA                  |
| ---------------- | -------------------- |
| No Stack         | Has Stack            |
| Regular Grammar  | Context Free Grammar |
| Lexical Analysis | Parsing              |

---

# 13. Parsing Algorithms ⭐⭐⭐⭐⭐

Purpose

Construct Parse Tree.

---

Three Types

### Universal Parser

Very slow

Any grammar

---

### Top Down Parser ⭐⭐⭐⭐

Starts

```
Root

↓

Leaves
```

Examples

* Recursive Descent
* Predictive Parser

Predictive parser

No backtracking

---

### Bottom Up Parser ⭐⭐⭐⭐

Starts

```
Leaves

↓

Root
```

Example

Shift Reduce Parser

---

# Top Down vs Bottom Up ⭐⭐⭐⭐⭐

| Top Down           | Bottom Up     |
| ------------------ | ------------- |
| Root → Leaves      | Leaves → Root |
| Predictive Parsing | Shift Reduce  |
| Easier             | Faster        |

---

# 14. Attribute Grammar ⭐⭐⭐⭐

Adds semantic information to grammar.

Two attributes

---

### Inherited Attribute

Information flows

```
Parent

↓

Child
```

---

### Synthesized Attribute

Information flows

```
Child

↓

Parent
```

---

# 15. Denotational Semantics ⭐⭐⭐⭐

Maps programming language constructs into **mathematical meaning.**

Contains

1. Syntax categories

2. BNF grammar

3. Value domains

4. Semantic functions

5. Semantic equations

---

# IMPORTANT COMPARISONS ⭐⭐⭐⭐⭐

## Syntax vs Semantics

| Syntax    | Semantics         |
| --------- | ----------------- |
| Structure | Meaning           |
| Parser    | Semantic Analyzer |

---

## Lexical vs Syntax vs Semantic Analysis

| Lexical             | Syntax              | Semantic       |
| ------------------- | ------------------- | -------------- |
| Characters → Tokens | Tokens → Parse Tree | Checks Meaning |
| FSA                 | Parser              | Symbol Table   |

---

## DFA vs NFA

| DFA               | NFA                  |
| ----------------- | -------------------- |
| Single transition | Multiple transitions |

---

## FSA vs PDA

| FSA             | PDA   |
| --------------- | ----- |
| No Stack        | Stack |
| Regular Grammar | CFG   |

---

## Top Down vs Bottom Up

| Top Down      | Bottom Up     |
| ------------- | ------------- |
| Root → Leaves | Leaves → Root |

---

## BNF vs EBNF

| BNF            | EBNF                             |    |
| -------------- | -------------------------------- | -- |
| Basic notation | Extended notation (`[]`, `{}`, ` | `) |

---

# Expected Exam Questions ⭐⭐⭐⭐⭐

### Very Likely (Long Questions)

1. Explain all stages of language translation with a neat diagram.
2. Differentiate syntax and semantics with examples.
3. Explain lexical, syntax, and semantic analysis.
4. Explain BNF grammar with examples.
5. Explain Finite State Automata (FSA).
6. Explain Pushdown Automata (PDA) and compare it with FSA.
7. Explain parsing techniques (Top-down vs Bottom-up).
8. Explain Regular Grammar and Regular Expressions.
9. Explain Attribute Grammar.
10. Explain Denotational Semantics.

### Frequently Asked Short Questions (2–5 marks)

* What is syntax?
* What is semantics?
* Define readability and writability.
* What is ambiguity?
* Explain the dangling else problem.
* What is a token?
* What is a lexeme?
* What is a parse tree?
* Define bootstrapping.
* What is a symbol table?
* What is optimization?
* What is code generation?
* What is linking and loading?
* Define BNF and EBNF.
* What is a regular expression?
* What is Kleene closure (`*`)?
* Differentiate DFA and NFA.
* Differentiate FSA and PDA.
* Define inherited and synthesized attributes.
* What is denotational semantics?

If you study the **⭐⭐⭐⭐⭐ sections first**, you'll cover the topics that are most commonly tested in compiler design and programming language translation exams. 
