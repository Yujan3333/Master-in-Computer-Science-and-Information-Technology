#PPL #third-semester 

# Unit 7- U3: Sequence Control

**Sequence Control** is one of the easiest units if you understand the concepts instead of memorizing.

---

# 1. Introduction

## What is Sequence Control?

**Sequence Control** is the mechanism that controls **the order in which program statements and operations are executed**.

Simply,

> **Sequence Control = Who executes first? Who executes next?**

Example

```c
a = 5;
b = 10;
c = a + b;
printf("%d", c);
```

Execution order:

```text
a=5
 ↓
b=10
 ↓
c=a+b
 ↓
print(c)
```

This order is called **sequence control**.

---

# Four Types of Sequence Control

The book divides sequence control into four parts.

```text
Sequence Control
│
├── Expressions
├── Statements
├── Declarative Programming
└── Subprograms
```

---

## 1. Expressions

Controls execution order inside expressions.

Example

```c
a + b * c
```

Which executes first?

```
+
*
```

Multiplication executes first because it has higher precedence.

---

## 2. Statements

Controls execution of statements.

Example

```c
if(age>=18)
    vote();

else
    wait();
```

Only one block executes.

---

## 3. Declarative Programming

Programmer specifies **what** should be done, not **how**.

Example

SQL

```sql
SELECT * FROM Student;
```

You don't specify how rows are searched.

---

## 4. Subprograms

Control transfers from one function to another.

Example

```c
main()

↓

add()

↓

return

↓

main()
```

---

# Implicit vs Explicit Sequence Control

## Implicit Sequence Control

Order is decided automatically by the language.

Example

```c
a=5;
b=6;
c=a+b;
```

Runs from top to bottom.

Another example

```c
a+b*c
```

Compiler automatically performs

```
b*c

then

a+
```

because of precedence.

---

## Explicit Sequence Control

Programmer changes the default order.

Example

```c
(a+b)*c
```

Parentheses change evaluation order.

Another example

```c
if

while

for

goto
```

These explicitly control execution.

---

# 2. Sequence Control in Arithmetic Expressions

This topic asks:

> **How does the compiler know which operator executes first?**

Two rules are used.

---

# A. Precedence

Precedence tells **which operator has higher priority.**

Example

```c
5+4*3
```

```
*

higher priority
```

So

```
4×3=12

12+5=17
```

---

Example

```c
8-3+2
```

Both have same precedence.

Need associativity.

---

# B. Associativity

Associativity tells

> Which operator is evaluated first if operators have the same precedence.

Example

```c
8-3+2
```

Addition and subtraction have same precedence.

Associativity is Left → Right

```
8-3=5

5+2=7
```

---

Easy Trick

```
Precedence

↓

Different operators

Associativity

↓

Same operators
```

---

# Expression Tree

An arithmetic expression can be represented as a tree.

Example

```
A+B*C
```

Expression Tree

```text
        +
      /   \
     A     *
          / \
         B   C
```

Leaves

```
A

B

C
```

Root

```
+
```

Evaluation order

```
B

C

↓

*

↓

+

```

Children execute before parent.

---

# Expression Notations

There are three notations.

---

## Infix

Operator between operands.

```
A+B
```

Most common.

---

## Prefix (Polish)

Operator first.

```
+AB
```

Example

```
(A+B)*C
```

Prefix

```
*+ABC
```

---

## Postfix (Reverse Polish)

Operator last.

```
AB+
```

Example

```
(A+B)*C
```

Postfix

```
AB+C*
```

---

Memory Trick

```
Prefix

Operator First

+AB

Infix

Operator Middle

A+B

Postfix

Operator Last

AB+
```

---

# Prefix Evaluation

Uses Stack.

General steps

1 Push operator.

2 Push operands.

3 When enough operands exist

Apply operator.

Replace by result.

---

Example

```
+34
```

```
3

4

↓

+

↓

7
```

---

# Postfix Evaluation

Also uses Stack.

Example

```
34+
```

```
Push 3

Push 4

+

↓

7
```

Very common interview question.

---

# Problems During Expression Evaluation

Book gives four problems.

---

## 1. Eager vs Lazy Evaluation

### Eager Evaluation

Evaluate operands first.

Example

```
a+b
```

Compute

```
a

b

↓

+
```

Most programming languages use eager evaluation.

---

### Lazy Evaluation

Don't evaluate immediately.

Evaluate only if needed.

Used in languages like Haskell.

---

Easy Memory

```
Eager

Evaluate Now

Lazy

Evaluate Later
```

---

## 2. Side Effects

A function changes something outside itself.

Example

```c
c/func(y)+c
```

Suppose

```
func(y)
```

changes c.

Then

```
Old c

or

New c
```

depends on evaluation order.

This makes the result different.

---

## 3. Error Conditions

Example

```c
10/0
```

Division by zero.

Or

```
Overflow
```

Must be handled.

---

## 4. Short Circuit Evaluation

Most important exam topic.

Example

```c
if(x==0 || y/x>5)
```

Suppose

```
x=0
```

First condition

```
x==0

True
```

Whole OR becomes True.

Compiler **does not evaluate**

```
y/x
```

Division by zero is avoided.

This is

```
Short Circuit Evaluation
```

---

For AND

```c
if(x!=0 && y/x>5)
```

If

```
x!=0

False
```

Second condition isn't evaluated.

---

Memory Trick

OR

```
True

↓

Stop
```

AND

```
False

↓

Stop
```

---

# 3. Sequence Control Between Statements

Instead of operators,

this controls statements.

---

Basic Statements

Examples

Assignment

```c
a=5;
```

Input

```c
scanf()
```

Output

```c
printf()
```

Subprogram Call

```c
add();
```

---

# Three Statement-Level Controls

---

## Composition

Statements execute one after another.

Example

```c
a=5;
b=6;
c=a+b;
```

```
1

↓

2

↓

3
```

---

## Alternation

Choose one path.

Example

```c
if

else
```

or

```c
switch
```

---

## Iteration

Repeat statements.

Example

```c
for

while

do while
```

---

Easy Table

| Control     | Meaning              |
| ----------- | -------------------- |
| Composition | Sequential execution |
| Alternation | Choose one path      |
| Iteration   | Repeat               |

---

# Explicit Sequence Control

Programmer forces execution.

Example

```
goto
```

Two types

Unconditional

```
goto END;
```

Always jumps.

Conditional

```
if(x==0)

goto END;
```

Jumps only if condition is true.

---

Break

Immediately exits loop.

Example

```c
while(1)
{
   break;
}
```

---

Continue

Skips remaining statements.

Starts next iteration.

---

Memory Trick

```
Break

Exit Loop

Continue

Next Iteration
```

---

# Structured Sequence Control

Modern programming avoids goto.

Uses

```
Compound Statements

Conditional Statements

Iteration Statements
```

---

## Compound Statement

Group multiple statements.

Example

```c
{
    a++;
    b++;
}
```

Acts like one statement.

---

## Conditional Statement

Makes decisions.

Examples

```
if

if-else

switch
```

---

## Iteration Statement

Repeats statements.

Examples

```
for

while

do-while

foreach
```

---

# Hardware Support

Conditional statements and loops are implemented using

```
Branch Instructions

Jump Instructions
```

---

# One-Page Exam Revision

| Topic                     | Key Point                                                                                |   |                                        |
| ------------------------- | ---------------------------------------------------------------------------------------- | - | -------------------------------------- |
| Sequence Control          | Controls the order of execution of operations and statements.                            |   |                                        |
| Expressions               | Controlled by precedence and associativity.                                              |   |                                        |
| Statements                | Controlled by conditionals and loops.                                                    |   |                                        |
| Declarative Programming   | Specifies *what* to do, not *how*.                                                       |   |                                        |
| Subprograms               | Transfer control between functions.                                                      |   |                                        |
| Implicit Sequence Control | Default order defined by the language (e.g., statement order, operator precedence).      |   |                                        |
| Explicit Sequence Control | Programmer changes the order (e.g., `if`, `for`, `goto`, parentheses).                   |   |                                        |
| Precedence                | Determines which operator executes first.                                                |   |                                        |
| Associativity             | Resolves the order for operators with the same precedence.                               |   |                                        |
| Expression Tree           | Leaves are operands, root is the main operator; evaluation proceeds from leaves to root. |   |                                        |
| Prefix Notation           | Operator before operands (e.g., `+AB`).                                                  |   |                                        |
| Infix Notation            | Operator between operands (e.g., `A+B`).                                                 |   |                                        |
| Postfix Notation          | Operator after operands (e.g., `AB+`).                                                   |   |                                        |
| Eager Evaluation          | Operands are evaluated before the operation.                                             |   |                                        |
| Lazy Evaluation           | Operands are evaluated only when needed.                                                 |   |                                        |
| Side Effects              | An operation changes state outside its local scope.                                      |   |                                        |
| Short-Circuit Evaluation  | Stops evaluating once the result is already known (`                                     |   | `stops on`true`, `&&`stops on`false`). |
| Composition               | Sequential execution of statements.                                                      |   |                                        |
| Alternation               | Selection using `if`/`switch`.                                                           |   |                                        |
| Iteration                 | Repetition using loops.                                                                  |   |                                        |
| `goto`                    | Unstructured jump to a labeled statement.                                                |   |                                        |
| `break`                   | Exits the nearest loop or `switch`.                                                      |   |                                        |
| `continue`                | Skips the rest of the current loop iteration and proceeds to the next one.               |   |                                        |

### Quick Memory Tricks

* **Precedence** → Different operators → **Who has higher priority?**
* **Associativity** → Same precedence → **Left-to-right or right-to-left?**
* **Prefix** → Operator **before** operands.
* **Infix** → Operator **between** operands.
* **Postfix** → Operator **after** operands.
* **OR (`||`)** → If the left side is **true**, stop evaluating.
* **AND (`&&`)** → If the left side is **false**, stop evaluating.
* **Composition** → Sequence.
* **Alternation** → Decision.
* **Iteration** → Repetition.
