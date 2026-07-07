#PPL #third-semester 

# Binding and Binding Time (Detailed, Easy-to-Understand & Exam-Focused)

This is one of the most important theory topics in **Programming Language**. The main idea is simple:

* **Binding** = *What property is associated with a program element?*
* **Binding Time** = *When is that association made?*

---

# What is Binding?

## Definition (Exam)

> **Binding** is the process of associating a program element (such as a variable, function, or data type) with one of its properties or characteristics.

In simple words:

**Binding means connecting something with its property.**

---

## Simple Analogy

Imagine a student.

```text
Student
```

The student has many properties:

* Name
* Roll Number
* Class
* Address

When we assign

```text
Student → Roll No = 25
```

we have **bound** the student to Roll No. 25.

Similarly, in programming,

```c
int age;
```

the variable

```text
age
```

is bound to

```text
Type = int
```

---

# Examples of Binding

## Example 1 – Variable to Type

```c
int x;
```

Binding:

```text
Variable x
      ↓
Type int
```

---

## Example 2 – Variable to Value

```c
x = 10;
```

Binding:

```text
Variable x
      ↓
Value 10
```

---

## Example 3 – Variable to Memory Location

```c
int x;
```

Compiler allocates memory:

```text
Variable x
      ↓
Memory Address 2000
```

---

## Example 4 – Function Call

```c
sum(5,10);
```

Binding:

```text
Formal Parameter a
↓

Actual Value 5
```

---

# What is Binding Time?

## Definition (Exam)

> **Binding Time** is the time during program creation or execution when a binding is established.

Simply:

It answers the question:

> **"When does the binding happen?"**

---

## Example

```c
int x;
```

Question:

When was

```text
x → int
```

decided?

Answer:

During **compile time**.

So,

```text
Binding = x → int

Binding Time = Compile Time
```

---

# Classes of Binding Time

There are **four major binding times**:

```text
Binding Time
      │
 ┌────┼───────────┬──────────────┬────────────────────┐
 │    │           │              │
Language   Language      Translation      Execution
Definition Implementation   (Compile/Load)     (Run Time)
Time        Time           Time               Time
```

Let's study each.

---

# 1. Language Definition Time

## Definition

Some properties are fixed **when the programming language is designed**.

The programmer cannot change them.

---

## Examples

The language designer decides:

* Keywords
* Operators
* Basic data types
* Grammar rules

Example in C:

```c
int
char
float
if
while
```

These keywords are fixed when C was designed.

You cannot change

```c
if
```

into

```c
when
```

---

## Example

In C

```c
int
```

is always an integer type.

This decision was made when C was created.

---

## Easy Diagram

```text
Language Created

↓

Keywords

↓

Operators

↓

Grammar

↓

Basic Types
```

---

## Exam Point

> Language definition time is when the language designer fixes the syntax, keywords, operators, grammar, and basic data types of the language.

---

# 2. Language Implementation Time

## Definition

Some decisions are made when the language compiler/interpreter is implemented for a specific computer.

These decisions may differ between implementations.

---

## Example

How should the integer

```text
10
```

be stored?

One compiler may use

```text
32 bits
```

Another may use

```text
64 bits
```

This depends on the compiler implementation.

---

Another example

```text
Size of int
```

may differ on different systems.

---

## Easy Diagram

```text
Language

↓

Compiler

↓

Machine Representation
```

---

## Exam Point

> Language implementation time refers to decisions made by the compiler or language implementation, such as internal data representation and storage format.

---

# 3. Translation Time (Compile Time)

Translation time is when the source code is translated into machine code.

Three subcategories are important.

---

## (a) Bindings Chosen by the Programmer

The programmer makes certain decisions while writing the program.

Examples

```c
int age;
```

The programmer chooses

* Variable name
* Variable type

Another example

```c
float salary;
```

The programmer selected

```text
float
```

---

## Examples of Programmer Bindings

* Variable names
* Function names
* Data types
* Statement structure

---

## (b) Bindings Chosen by the Compiler (Translator)

The compiler makes decisions automatically.

The programmer does not know them.

Example

Compiler decides

```text
age

↓

Memory Offset = 16 bytes
```

The programmer never specifies this.

---

Examples

* Memory layout
* Relative addresses
* Register allocation
* Optimization

---

## (c) Bindings Chosen by the Loader

After compilation,

multiple object files must be combined.

Example

```text
Student.obj

Teacher.obj

Library.obj
```

↓

Loader combines them.

↓

Executable Program

The loader assigns the **actual memory addresses** where the program will be loaded.

---

## Easy Diagram

```text
Compile

↓

Object Files

↓

Loader

↓

Executable Program
```

---

## Exam Point

Translation time includes:

* Programmer-selected bindings
* Compiler-selected bindings
* Loader-selected bindings

---

# 4. Execution Time (Run Time)

## Definition

Bindings made **while the program is running**.

These are dynamic bindings.

Examples

* Variable values
* Memory allocation
* Parameter passing

---

Execution time has **two subcategories**.

---

# (a) On Entry to a Subprogram or Block

Bindings occur when a function starts.

Example

```c
void add(int a, int b)
{
}
```

Call

```c
add(5,10);
```

At function entry

Binding occurs:

```text
a

↓

5
```

```text
b

↓

10
```

This is called

**Binding of formal parameters to actual parameters.**

Memory is also allocated for local variables when entering the function.

---

Diagram

```text
Function Call

↓

Enter Function

↓

Bind Parameters

↓

Allocate Local Variables
```

---

# (b) At Arbitrary Points During Execution

Some bindings can occur anywhere while the program runs.

The most common example is **assignment**.

Example

```c
x = 5;

x = 10;

x = 20;
```

Bindings become

```text
x → 5

↓

x →10

↓

x →20
```

These bindings occur whenever the assignment statement executes.

Languages like

* LISP
* Smalltalk
* ML

allow many such dynamic bindings.

---

## Easy Diagram

```text
Program Running

↓

Assignment

↓

Variable Gets New Value
```

---

# Complete Summary Table

| Binding Time                     | Who Makes the Binding?           | Examples                                                            |
| -------------------------------- | -------------------------------- | ------------------------------------------------------------------- |
| **Language Definition Time**     | Language designer                | Keywords (`if`, `while`), operators, grammar, basic data types      |
| **Language Implementation Time** | Compiler/implementation designer | Internal representation of data, size/bit pattern of data types     |
| **Translation (Compile) Time**   | Programmer, compiler, and loader | Variable names, variable types, memory layout, linking object files |
| **Execution (Run) Time**         | Program while executing          | Variable values, memory allocation, parameter binding               |

---

# Memory Trick

Think of the program's life cycle:

```text
Language Designed
        │
        ▼
Language Definition Time
        │
        ▼
Compiler Built
        │
        ▼
Language Implementation Time
        │
        ▼
Program Compiled
        │
        ▼
Translation Time
        │
        ▼
Program Runs
        │
        ▼
Execution Time
```

So the order is:

```text
Language Definition
        ↓
Language Implementation
        ↓
Translation (Compile/Load)
        ↓
Execution (Run Time)
```

---

# Frequently Asked Examples

| Binding                                              | Binding Time                           |
| ---------------------------------------------------- | -------------------------------------- |
| `int`, `float`, `if`, `while` keywords               | **Language Definition Time**           |
| Bit representation or internal storage of integers   | **Language Implementation Time**       |
| Variable type (`int x;`)                             | **Translation (Compile) Time**         |
| Variable name chosen by programmer                   | **Translation (Compile) Time**         |
| Linking object files into an executable              | **Loader (Translation Time)**          |
| Function parameters bound to arguments (`add(5,10)`) | **Execution Time (on function entry)** |
| `x = 10;` (variable gets a new value)                | **Execution Time (during execution)**  |

---

# Exam Tip (5 Marks)

**Binding** is the association of a program element with one of its properties, such as a variable with its type, value, or memory location. **Binding Time** is the stage at which this association is established.

The main classes of binding time are:

1. **Language Definition Time** – Language designers define keywords, grammar, operators, and basic data types.
2. **Language Implementation Time** – Compiler or implementation designers determine internal representations and storage formats.
3. **Translation (Compile) Time** – Bindings are made during compilation. The programmer chooses names and types, the compiler decides memory layout, and the loader assigns actual addresses when linking.
4. **Execution (Run) Time** – Dynamic bindings occur while the program executes, such as parameter binding when entering a function and variable-value binding during assignment statements.

**Quick Memory Rule:**

* **Definition Time** → Language designer
* **Implementation Time** → Compiler implementation
* **Translation Time** → Compiler + Loader
* **Execution Time** → Running program
