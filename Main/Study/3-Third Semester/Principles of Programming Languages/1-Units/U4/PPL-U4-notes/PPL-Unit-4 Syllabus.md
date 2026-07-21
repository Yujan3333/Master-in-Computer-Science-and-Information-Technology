#third-semester #PPL 

From this syllabus, **TU repeatedly asks conceptual questions**. Here's what you should prepare.

---

# 4.1 Distributed Processing (4 Hours)

## Important Topics

### 1. Exceptions ⭐⭐⭐⭐⭐ (Very Important)

Possible Questions:

**2 Marks**

* What is an exception?
* What is exception handling?

**5 Marks**

* Explain exception handling with an example.
* Explain the exception handling mechanism.

**Short Answer**

* An **exception** is a runtime error or abnormal event that interrupts the normal flow of a program.
* **Exception handling** is a mechanism to detect and handle exceptions using constructs like `try`, `catch`, `throw`, and `finally`.

---

### 2. Exception Propagation ⭐⭐⭐⭐

Possible Questions:

* What is exception propagation?
* Explain exception propagation with an example.

**Short Answer**

Exception propagation is the process of **passing an exception from the function where it occurs to its caller** until it is handled.

Example:

```text
main()
   ↓
fun1()
   ↓
fun2()
 Exception occurs
   ↓
fun1()
   ↓
main()
```

If `fun2()` does not handle it, it propagates upward.

---

### 3. Exception Handler ⭐⭐⭐

Possible Questions

* What is an exception handler?
* Differentiate exception and exception handler.

**Short Answer**

An **exception handler** is a block of code that catches and processes an exception.

Example

```java
try{
   ...
}
catch(Exception e){
   ...
}
```

---

### 4. Coroutines ⭐⭐⭐⭐⭐ (Very Important)

Possible Questions

* What is a coroutine?
* Differentiate coroutine and subprogram.
* Explain coroutine with diagram.

**Short Answer**

A **coroutine** is a special type of subprogram where execution can **pause (yield)** and later **resume from the same point**.

Unlike functions, coroutines transfer control **back and forth** without restarting.

---

### Coroutine vs Subprogram

| Subprogram                        | Coroutine                               |
| --------------------------------- | --------------------------------------- |
| Starts from beginning every call. | Resumes from previous suspension point. |
| Uses call-return mechanism.       | Uses suspend-resume mechanism.          |
| One active routine.               | Multiple routines cooperate.            |
| No state preserved after return.  | State is preserved after suspension.    |

---

### 5. Parallel Programming ⭐⭐⭐⭐⭐

Possible Questions

* What is parallel programming?
* Advantages of parallel programming.
* Parallel vs Sequential programming.

**Short Answer**

Parallel programming executes **multiple tasks simultaneously** using multiple processors or cores to improve performance.

---

### Parallel vs Sequential

| Sequential         | Parallel                      |
| ------------------ | ----------------------------- |
| One task at a time | Multiple tasks simultaneously |
| Slower             | Faster                        |
| Single CPU/Core    | Multiple CPUs/Cores           |

---

# 4.2 Paradigms and Languages

---

## 1. Procedural Programming (FORTRAN & C) ⭐⭐⭐⭐⭐

Possible Questions

* What is procedural programming?
* Characteristics of procedural programming.

**Answer**

Procedural programming organizes programs into **procedures/functions** that execute step-by-step instructions.

Examples:

* FORTRAN
* C

Features

* Function-based
* Top-down approach
* Uses procedures
* Focuses on algorithms

---

## 2. Block Structured Programming (PASCAL) ⭐⭐⭐⭐

Possible Questions

* What is block structured programming?
* Features of Pascal.

**Answer**

Block-structured programming organizes code into **nested blocks**, each having its own local variables and scope.

Example

Pascal

Features

* Nested blocks
* Lexical scope
* Better modularity

---

## 3. Object-Oriented Programming (C++, Smalltalk) ⭐⭐⭐⭐⭐

Possible Questions

* Explain object-oriented programming.
* What are the principles of OOP?

**Answer**

Object-oriented programming organizes software using **objects and classes**.

Main principles

* Class
* Object
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction

Examples

* C++
* Smalltalk

---

## 4. Functional Programming (LISP) ⭐⭐⭐⭐

Possible Questions

* What is functional programming?
* Features of functional programming.

**Answer**

Functional programming solves problems using **mathematical functions**.

Features

* Functions are first-class
* No global state
* Recursion
* Immutable data

Example

* LISP

---

## 5. Logic Programming (PROLOG) ⭐⭐⭐⭐

Possible Questions

* What is logic programming?
* Features of Prolog.

**Answer**

Logic programming is based on **facts, rules, and logical inference**.

Instead of writing algorithms, the programmer specifies **what is true**, and the language determines **how** to solve the problem.

Example

* PROLOG

---

# Very Important Difference Questions (5 Marks)

### Procedural vs Object-Oriented

| Procedural                      | Object-Oriented               |
| ------------------------------- | ----------------------------- |
| Function-based                  | Object-based                  |
| Top-down                        | Bottom-up                     |
| Data and functions are separate | Data and methods are together |
| Example: C                      | Example: C++                  |

---

### Functional vs Logic Programming

| Functional         | Logic                    |
| ------------------ | ------------------------ |
| Based on functions | Based on facts and rules |
| Uses recursion     | Uses inference engine    |
| Example: LISP      | Example: PROLOG          |

---

### Coroutine vs Subprogram

| Subprogram                        | Coroutine                 |
| --------------------------------- | ------------------------- |
| Call-return                       | Suspend-resume            |
| Starts from beginning             | Resumes execution         |
| Does not preserve execution point | Preserves execution point |

---

### Parallel vs Sequential Programming

| Sequential            | Parallel                  |
| --------------------- | ------------------------- |
| One task              | Multiple tasks            |
| Slower                | Faster                    |
| Single processor/core | Multiple processors/cores |

---

# ⭐ Most Expected Exam Questions

## 10 Marks

1. Explain exception handling and exception propagation.
2. Explain different programming paradigms with examples.
3. Compare procedural, object-oriented, functional, and logic programming.

## 5 Marks

1. Explain coroutine.
2. Explain parallel programming.
3. Explain procedural programming.
4. Explain object-oriented programming.
5. Explain functional programming.
6. Explain logic programming.
7. Explain block-structured programming.
8. Differentiate coroutine and subprogram.
9. Differentiate procedural and object-oriented programming.
10. Differentiate functional and logic programming.

These are the **highest-probability questions** from Unit **4.1 and 4.2** for TU PPL exams.
