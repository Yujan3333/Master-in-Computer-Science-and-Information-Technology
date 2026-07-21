#PPL #third-semester 


This is one of the **most important topics** in Unit 2. It explains **how a high-level language (like C, Java, Python) is executed on a computer**.

There are **two ways**:

1. **Translation**
2. **Software Simulation (Interpretation)**

---

# Translators and Virtual Architectures

## Problem

Computers understand only **machine language (0s and 1s)**.

But programmers write programs in **high-level languages**.

Example

```cpp
int sum = a + b;
```

The computer **cannot execute this directly**.

So we need a way to convert or execute it.

There are **two solutions**:

1. Translator
2. Software Simulation (Interpreter)

---

# 1. Translator

## Definition

A **translator** is a program that converts a program written in one language (**source language**) into an equivalent program in another language (**object language**).

### General Flow

```text
Source Program
       │
       ▼
   Translator
       │
       ▼
 Object Program
```

Example

```cpp
int a = 10;
```

↓

Machine Code

```text
101011001101...
```

---

# Types of Translators

There are **four important translators**.

---

## 1. Assembler

### Definition

An assembler converts

**Assembly Language → Machine Language**

### Flow

```text
Assembly Program
        │
        ▼
    Assembler
        │
        ▼
 Machine Language
```

### Example

Assembly

```assembly
MOV AX,5
ADD AX,10
```

↓

Machine code

```text
1010101010
```

---

## 2. Compiler

### Definition

A compiler converts

**High-Level Language → Assembly Language or Machine Language**

### Flow

```text
C Program
      │
      ▼
 Compiler
      │
      ▼
Machine Code
```

### Example

```cpp
int x = 10;
```

↓

Machine language.

### Examples of Compiled Languages

* C
* C++
* Pascal
* FORTRAN
* Ada

---

## 3. Loader (Link Editor)

### Definition

A loader (or linker) combines several compiled object files into **one executable program**.

### Example

Suppose a project has

```text
main.o
math.o
student.o
```

The loader links them into

```text
program.exe
```

### Purpose

* Combines object files.
* Resolves references between modules.
* Produces the executable program.

---

## 4. Preprocessor (Macroprocessor)

### Definition

A preprocessor processes the source program **before compilation**.

It handles:

* `#include`
* `#define`
* Macros
* Conditional compilation

### Example

Before preprocessing

```cpp
#define PI 3.14
```

After preprocessing

```cpp
3.14
```

Then the compiler compiles the modified program.

---

# Translation may occur in multiple steps

High-level programs are often translated in several stages.

Example

```text
High-Level Program
        │
        ▼
 Preprocessor
        │
        ▼
 Compiler
        │
        ▼
 Assembly Code
        │
        ▼
 Assembler
        │
        ▼
 Object Code
        │
        ▼
 Loader
        │
        ▼
 Executable Program
```

---

# 2. Software Simulation (Software Interpretation)

Instead of translating the program into machine language,

the interpreter **executes the source program directly**.

---

## Definition

An **interpreter** reads the program **line by line**, translates it internally, and immediately executes it.

### Flow

```text
Source Program
       │
       ▼
 Interpreter
       │
       ▼
 Execute Directly
```

---

### Example

Python

```python
a = 10
print(a)
```

The interpreter executes these statements directly.

No executable file is produced.

---

# Virtual Machine

The interpreter creates a **Virtual Machine**.

The virtual machine behaves like an imaginary computer that understands the high-level language.

Example

Java

```text
Java Program
      │
      ▼
Java Compiler
      │
      ▼
Bytecode
      │
      ▼
Java Virtual Machine (JVM)
      │
      ▼
Actual Hardware
```

The JVM acts as a **virtual computer**.

---

# Combination of Translation and Interpretation

Many languages use **both**.

Example

Java

```text
Java Source
      │
      ▼
Compiler
      │
      ▼
Bytecode
      │
      ▼
JVM (Interpreter)
      │
      ▼
Machine Code
```

This gives portability while maintaining good performance.

---

# Compiled vs Interpreted Languages

| Compiled Languages                             | Interpreted Languages                                                               |
| ---------------------------------------------- | ----------------------------------------------------------------------------------- |
| Entire program is translated before execution. | Program is executed line by line.                                                   |
| Produces machine code/executable.              | Produces intermediate code or executes directly.                                    |
| Faster execution.                              | Slower execution.                                                                   |
| Errors are reported after compilation.         | Errors are reported during execution.                                               |
| Example: C, C++, Pascal, FORTRAN, Ada          | Example: Python, JavaScript (traditional model). Java uses a hybrid model with JVM. |

---

# Memory Trick

Remember the translators as **ACLP**:

* **A** = Assembler → Assembly → Machine
* **C** = Compiler → High-level → Machine/Assembly
* **L** = Loader → Object files → Executable
* **P** = Preprocessor → Processes source before compilation

---

# Important Questions

## Q1. What is a translator?

**Ans:**
A **translator** is a software program that converts a program written in one language (source language) into an equivalent program in another language (object language).

---

## Q2. Name the types of translators.

**Ans:**

1. Assembler
2. Compiler
3. Loader (Link Editor)
4. Preprocessor (Macroprocessor)

---

## Q3. What is an assembler?

**Ans:**
An **assembler** converts an assembly language program into machine language.

---

## Q4. What is a compiler?

**Ans:**
A **compiler** translates a high-level language program into assembly language or machine language before execution.

---

## Q5. What is a loader?

**Ans:**
A **loader (link editor)** combines multiple object files into a single executable program and resolves references among them.

---

## Q6. What is a preprocessor?

**Ans:**
A **preprocessor** processes directives such as `#include` and `#define` before compilation, producing a standard source program for the compiler.

---

## Q7. What is software simulation (interpretation)?

**Ans:**
Software simulation (interpretation) executes a high-level language program directly without first generating machine code. The interpreter acts as a **virtual machine**.

---

## Q8. Differentiate compiled and interpreted languages. (5 Marks)

**Ans:**

| Compiled                                        | Interpreted                                                                              |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Translates the entire program before execution. | Executes the program line by line.                                                       |
| Produces machine code/executable.               | Does not produce a native executable before execution.                                   |
| Faster execution.                               | Slower execution.                                                                        |
| Examples: C, C++, Pascal                        | Examples: Python, JavaScript (traditional model); Java is hybrid using bytecode and JVM. |


