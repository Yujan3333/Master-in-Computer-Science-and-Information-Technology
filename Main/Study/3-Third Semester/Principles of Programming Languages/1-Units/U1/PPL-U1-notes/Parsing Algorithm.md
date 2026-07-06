#PPL 

# Parsing Algorithms (Detailed and Easy-to-Understand)

After **lexical analysis** converts the source code into **tokens**, the **parser (syntax analyzer)** checks whether these tokens follow the grammar (syntax rules) of the programming language.

The parser also **constructs a Parse Tree (Syntax Tree)** that shows how the program is derived from the grammar.

---

# What is Parsing?

**Parsing** is the process of analyzing a sequence of tokens according to the grammar of a programming language.

Its main jobs are:

* Check whether the program follows grammar rules.
* Report syntax errors.
* Build a parse tree.
* Pass the parse tree to later compiler phases.

---

## Example

Suppose the source code is

```c
a = b + c;
```

After lexical analysis, the parser receives tokens like

```text
id = id + id ;
```

The parser checks whether this token sequence is valid according to the language grammar.

If valid, it builds a parse tree.

---

# What is a Parse Tree?

A **Parse Tree** (Syntax Tree) is a tree representation showing how a sentence is generated using grammar rules.

Example grammar

```text
E → E + T
E → T
T → id
```

For

```text
a + b
```

Parse Tree

```text
          E
        / | \
       E  +  T
       |     |
       T     id(b)
       |
     id(a)
```

The parser constructs this tree.

---

# Types of Parsing Algorithms

There are **three general types** of parsing algorithms.

```text
                 Parsing Algorithms
                 /       |        \
         Universal   Top-Down   Bottom-Up
```

---

# 1. Universal Parsing

## Definition

Universal parsing algorithms can parse **almost any context-free grammar**.

They are called "universal" because they are not limited to a special kind of grammar.

Examples include

* CYK Algorithm
* Earley Parser

---

## How it works

Instead of using specialized rules, they examine many grammar possibilities to determine whether the input belongs to the grammar.

---

## Example

Suppose grammar

```text
S → AB
A → a
B → b
```

Input

```text
ab
```

Universal parser checks all grammar possibilities until it confirms

```text
S
├──A
│  └──a
└──B
   └──b
```

---

## Advantages

* Can parse almost any grammar.
* Very flexible.

---

## Disadvantages

* Very slow.
* Requires more memory.
* Not suitable for production compilers.

---

## Exam Point

> Universal parsing works for almost every grammar but is too inefficient for practical compiler implementation.

---

# 2. Top-Down Parsing

## Definition

Top-down parsing starts from the **start symbol (root)** and tries to generate the input string step by step until it reaches the terminal symbols (leaves).

It builds the parse tree

```text
Root
 ↓
Children
 ↓
Leaves
```

---

## Simple Idea

Imagine growing a tree from the trunk to the leaves.

Parser starts with

```text
Program
```

and gradually expands grammar rules.

---

## Example Grammar

```text
E → T + E
E → T
T → id
```

Input

```text
a + b
```

The parser starts with

```text
E
```

Expands

```text
E
↓
T + E
↓
id + E
↓
id + T
↓
id + id
```

which matches

```text
a + b
```

---

# Parse Tree Construction

Step 1

```text
E
```

Step 2

```text
      E
    / | \
   T  +  E
```

Step 3

```text
      E
    / | \
   T  +  T
   |     |
 id(a) id(b)
```

Notice that construction starts from the **top**.

---

# Types of Top-Down Parsing

There are two important methods.

---

## A. Recursive Descent Parsing

This parser uses recursive procedures.

Each non-terminal has its own function.

Example

```text
E()
T()
F()
```

When parser wants to parse

```text
E
```

it calls

```text
E()
```

which calls

```text
T()
```

and so on.

---

### Problem: Backtracking

Sometimes parser guesses the wrong production.

Then it must return and try another rule.

This is called **backtracking**.

---

### Example

Grammar

```text
S → aA
S → aB
```

Input

```text
ab
```

Parser first guesses

```text
S → aA
```

Later it discovers the remaining input doesn't match.

So it returns and tries

```text
S → aB
```

This returning process is called **backtracking**.

---

### Disadvantages

* Slower.
* May repeat work.
* Inefficient.

---

# B. Predictive Parsing

Predictive parsing is an improved version of recursive descent parsing.

The parser predicts the correct production using a lookahead token.

---

## Lookahead

Usually the parser examines **one upcoming token**.

Example

Current token

```text
id
```

Parser predicts immediately which production to use.

---

## No Backtracking

This is the biggest advantage.

Parser never goes back.

It always chooses the correct rule.

---

### Example

Grammar

```text
E → T E'

E' → + T E'
E' → ε

T → id
```

Input

```text
a+b
```

Parser sees

```text
id
```

Immediately chooses

```text
T → id
```

Then sees

```text
+
```

Chooses

```text
E' → +TE'
```

No wrong guesses occur.

---

## Advantages

* Very fast.
* No backtracking.
* Easy to implement.
* Used in LL(1) parsers.

---

## Disadvantages

* Grammar must satisfy certain conditions (e.g., left recursion must be removed and the grammar often needs left factoring).

---

# Top-Down Parsing Summary

```text
Start Symbol
      |
      V
Expand productions
      |
      V
Generate terminals
      |
      V
Match input
```

Tree grows

```text
Top
 ↓
Bottom
```

---

# 3. Bottom-Up Parsing

## Definition

Bottom-up parsing starts from the **input symbols (leaves)** and gradually combines them until the **start symbol (root)** is obtained.

Tree grows

```text
Leaves
 ↑
Root
```

---

## Simple Idea

Imagine building a house.

You first place the bricks.

Then walls.

Then roof.

Similarly,

Parser starts from

```text
id
+
id
```

and combines them step by step.

---

## Example Grammar

```text
E → E + T
E → T
T → id
```

Input

```text
id + id
```

Bottom-up parser does

```text
id
↓

T
↓

E
```

Second

```text
id
↓

T
```

Then

```text
E + T
↓

E
```

Finished.

---

## Parse Tree

```text
        E
      / | \
     E  +  T
     |     |
     T     id
     |
    id
```

Notice that parser built this from the bottom upward.

---

# Shift-Reduce Parsing

The most common bottom-up parser is **Shift-Reduce Parsing**.

It performs only two main actions.

---

## Shift

Take one input symbol and push it onto the stack.

Example

Input

```text
id + id
```

Stack

```text
(empty)
```

Shift

```text
Stack
id
```

---

## Reduce

Replace symbols on the stack using grammar rules.

Example

Grammar

```text
T → id
```

Stack

```text
id
```

Reduce

```text
T
```

Later

```text
E → T
```

Stack

```text
E
```

---

## Shift-Reduce Example

Input

```text
id + id
```

Grammar

```text
E → E + T
E → T
T → id
```

| Step | Stack | Input | Action       |
| ---- | ----- | ----- | ------------ |
| 1    |       | id+id | Shift        |
| 2    | id    | +id   | Reduce T→id  |
| 3    | T     | +id   | Reduce E→T   |
| 4    | E     | +id   | Shift +      |
| 5    | E+    | id    | Shift id     |
| 6    | E+id  |       | Reduce T→id  |
| 7    | E+T   |       | Reduce E→E+T |
| 8    | E     |       | Accept       |

---

## Advantages

* Can handle a larger class of grammars than top-down parsing.
* More powerful.
* Used in many real compilers.
* Basis for LR, SLR, CLR, and LALR parsers.

---

## Disadvantages

* More difficult to implement manually.
* Parsing tables can be large.

---

# Comparison of Parsing Methods

| Feature                       | Universal Parsing       | Top-Down Parsing                                               | Bottom-Up Parsing                                   |
| ----------------------------- | ----------------------- | -------------------------------------------------------------- | --------------------------------------------------- |
| Starts from                   | Can analyze any grammar | Start symbol (root)                                            | Input symbols (leaves)                              |
| Builds tree                   | General methods         | Top → Bottom                                                   | Bottom → Top                                        |
| Speed                         | Slow                    | Fast                                                           | Very fast                                           |
| Backtracking                  | May occur               | Recursive descent may require it; predictive parsing avoids it | No backtracking in standard shift-reduce/LR parsing |
| Ease of implementation        | Difficult               | Easy                                                           | More complex                                        |
| Common methods                | CYK, Earley             | Recursive Descent, Predictive (LL)                             | Shift-Reduce, LR, SLR, CLR, LALR                    |
| Used in production compilers? | Rarely                  | Yes (for suitable grammars)                                    | Very commonly                                       |

---

# Easy Way to Remember

```text
Universal Parsing
-----------------
Can parse almost any grammar
↓
Very slow
↓
Rarely used in compilers

Top-Down Parsing
----------------
Starts from Start Symbol
Root → Leaves
Expand grammar
Recursive Descent
Predictive Parsing (No Backtracking)

Bottom-Up Parsing
-----------------
Starts from Input
Leaves → Root
Combine symbols
Shift-Reduce Parsing
```

## Exam Tip (2–5 Marks)

* **Universal Parsing:** Can parse almost any context-free grammar but is too slow for production compilers.
* **Top-Down Parsing:** Begins from the start symbol and builds the parse tree from root to leaves. Includes **Recursive Descent** (may require backtracking) and **Predictive Parsing** (uses lookahead, no backtracking).
* **Bottom-Up Parsing:** Begins from the input symbols and builds the parse tree from leaves to root. The most common method is **Shift-Reduce Parsing**, which repeatedly shifts input symbols onto a stack and reduces them using grammar rules until the start symbol is produced.
