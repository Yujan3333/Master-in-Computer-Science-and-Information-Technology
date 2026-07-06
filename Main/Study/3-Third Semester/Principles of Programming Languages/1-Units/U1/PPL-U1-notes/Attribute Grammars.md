#PPL 

# Attribute Grammars (Detailed and Easy-to-Understand)

After the **parser** checks that the program is syntactically correct and builds a **parse tree**, the compiler must determine the **meaning (semantics)** of the program.

This is where **Attribute Grammars** are used.

---

# What is an Attribute Grammar?

An **Attribute Grammar** is an extension of a **Context-Free Grammar (CFG)** that adds **attributes** and **semantic rules** to grammar productions.

* **CFG** defines the **syntax (structure)** of a language.
* **Attribute Grammar** defines the **semantics (meaning)** of that syntax.

### Simple Definition (Exam)

> **Attribute Grammar** is a context-free grammar augmented with attributes and semantic rules to define the meaning of a program by passing semantic information through the parse tree.

---

# Why Do We Need Attribute Grammars?

A parser can verify that a statement is grammatically correct, but it cannot determine whether it is **meaningful**.

For example:

```c
int x;
x = 10;
```

This is both syntactically and semantically correct.

But consider:

```c
int x;
x = "Hello";
```

The parser accepts it because the syntax is valid.

However, assigning a **string** to an **integer** is a **semantic error**.

Attribute grammars help detect such errors.

---

# Main Purpose

Attribute grammars are used to

* Define the semantics (meaning) of programs.
* Pass information through the parse tree.
* Perform semantic analysis.
* Check type compatibility.
* Check variable declarations.
* Compute expression values.
* Generate intermediate code.

---

# Basic Idea

Each node in the parse tree stores additional information called an **attribute**.

Instead of only knowing

```text
Expression
```

the compiler can also know

```text
Expression
Type = Integer
Value = 15
```

These extra pieces of information are the **attributes**.

---

# Parse Tree with Attributes

Suppose the expression is

```text
5 + 3
```

Grammar

```text
E → E + T
T → number
```

Without attributes

```text
        E
      / | \
     E  +  T
     |     |
     T     3
     |
     5
```

With attributes

```text
                E
            value = 8
           /    |    \
      value=5   +   value=3
```

The parser builds the tree.

The attribute grammar computes the value **8**.

---

# What is an Attribute?

An **attribute** is extra information associated with a grammar symbol.

Examples

```text
Type
Value
Memory Address
Scope
Data Size
Variable Name
```

---

## Example

Suppose

```c
int a;
```

The node

```text
a
```

may contain attributes

```text
Name = a
Type = Integer
Size = 4 bytes
Scope = Global
```

---

# Semantic Rules

Each grammar rule has semantic rules that compute attribute values.

Example

Grammar

```text
E → E1 + T
```

Semantic rule

```text
E.value = E1.value + T.value
```

Meaning

The value of the parent node equals the sum of its children.

---

# Example

Expression

```text
4 + 6
```

Attributes

```text
Left child value = 4

Right child value = 6
```

Semantic rule

```text
E.value = 4 + 6
```

Result

```text
E.value = 10
```

---

# Types of Attributes

There are **two types** of attributes.

```text
Attributes
     |
 -------------------
 |                 |
Inherited     Synthesized
```

---

# 1. Synthesized Attributes

## Definition

A **synthesized attribute** is computed **from the attributes of a node's children** and passed **upward** toward the parent.

### Easy Definition

Information flows

```text
Children
   ↑
 Parent
```

or

```text
Bottom
↑
Top
```

---

## Example

Grammar

```text
E → E1 + T
```

Semantic rule

```text
E.value = E1.value + T.value
```

Suppose

```text
E1.value = 8

T.value = 5
```

Then

```text
E.value = 13
```

The parent gets information from its children.

This is a **synthesized attribute**.

---

## Diagram

```text
      E(value=13)
      /        \
8                5
```

Information moves upward.

```text
8 ↑

5 ↑

Parent = 13
```

---

## Example 2

Expression

```text
2 * 4
```

Grammar

```text
E → E1 * T
```

Semantic rule

```text
E.value = E1.value × T.value
```

Children

```text
2

4
```

Parent

```text
8
```

---

# Characteristics of Synthesized Attributes

* Computed from children.
* Passed upward.
* Used to evaluate expressions.
* Common in bottom-up parsing.

---

# 2. Inherited Attributes

## Definition

An **inherited attribute** is computed from the **parent node** and/or **siblings** and passed **downward** (or sideways) to a child.

### Easy Definition

Information flows

```text
Parent
 ↓
Children
```

or

```text
Top
↓
Bottom
```

---

## Example

Suppose

```c
int a, b, c;
```

Grammar

```text
Declaration → Type VariableList
```

The **Type** node has

```text
Integer
```

The variables

```text
a

b

c
```

inherit the type

```text
Integer
```

Information flows from the parent to the children.

---

## Diagram

```text
Declaration
Type=Integer
      |
      ↓
  VariableList
   /   |    \
  a    b     c
```

All variables inherit

```text
Type = Integer
```

---

## Another Example

Suppose

```text
float x, y;
```

Type node

```text
float
```

Inherited by

```text
x

y
```

Both become

```text
Type = float
```

---

# Characteristics of Inherited Attributes

* Computed from parent or siblings.
* Passed downward.
* Used for declarations.
* Used in scope checking.
* Common in top-down parsing.

---

# Difference Between Synthesized and Inherited Attributes

| Feature                | Synthesized Attribute                   | Inherited Attribute                            |
| ---------------------- | --------------------------------------- | ---------------------------------------------- |
| Information comes from | Children                                | Parent and/or siblings                         |
| Direction of flow      | Bottom → Top                            | Top → Bottom (or sideways from siblings)       |
| Computed by            | Children                                | Parent or sibling                              |
| Used for               | Expression evaluation, type calculation | Declarations, scopes, passing type information |
| Common in              | Bottom-up parsing                       | Top-down parsing                               |

---

# Complete Example

Grammar

```text
Declaration → Type Variable
```

Input

```text
int x;
```

Parse tree

```text
Declaration
   /      \
Type      Variable
(int)        (x)
```

### Inherited Attribute

The `Type` information is passed to the variable.

```text
Variable.type = Type.type
```

Result

```text
x.type = Integer
```

---

Now consider

```text
5 + 8
```

Grammar

```text
E → E1 + T
```

Semantic rule

```text
E.value = E1.value + T.value
```

Children

```text
5

8
```

Parent

```text
13
```

This is a **synthesized attribute** because the value is computed from the children and passed upward.

---

# Real Compiler Uses of Attribute Grammars

Attribute grammars help the compiler to:

* Check variable declarations.
* Verify data types.
* Detect semantic errors.
* Evaluate constant expressions.
* Build symbol table information.
* Generate intermediate code.
* Perform type checking.

---

# Memory Trick

Imagine a family tree:

### Synthesized Attribute

Children give information to their parent.

```text
Child
  ↑
Parent
```

Think: **Children → Parent** (Bottom → Top)

---

### Inherited Attribute

Parent gives information to the children.

```text
Parent
  ↓
Child
```

Think: **Parent → Children** (Top → Bottom)

---

# Exam Tip (2–5 Marks)

* **Attribute Grammar** extends a context-free grammar by attaching **attributes** and **semantic rules** to grammar productions, allowing the compiler to define the **meaning (semantics)** of programs.
* It is mainly used during **semantic analysis** to perform tasks such as **type checking**, **variable declaration checking**, **expression evaluation**, and **passing semantic information** through the parse tree.
* **Synthesized attributes** are computed from a node's children and flow **upward** (bottom to top).
* **Inherited attributes** are obtained from a node's parent and/or siblings and flow **downward** (or sideways) to the children.
