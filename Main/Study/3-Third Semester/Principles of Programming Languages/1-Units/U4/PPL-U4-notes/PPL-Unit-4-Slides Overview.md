#PPL  #third-semester 

This is the **second half of Unit 7**. It mainly covers **Subprogram Sequence Control**, **Recursion**, **Exception Handling**, **Coroutines**, and **Subprogram Scheduling**. These topics are often asked as **3–8 mark questions**. Here's an exam-focused, easy-to-understand summary.

---

# Unit 7 (Part 2)- U4: Subprogram Sequence Control

## 1. What is Subprogram Sequence Control?

### Definition

**Subprogram Sequence Control** is the mechanism that controls:

* How one subprogram (function/procedure) **calls another**, and
* How the called subprogram **returns control** back to the caller.

Simply,

> **Subprogram Sequence Control = Function Calling + Returning**

Example:

```c
main()
{
    add();
    printf("Finished");
}

void add()
{
    printf("Adding");
}
```

Execution order:

```text
main()

↓

call add()

↓

execute add()

↓

return to main()

↓

print "Finished"
```

---

# Simple Call-Return Subprogram

This is the normal function calling mechanism used in languages like **C, C++, Java**.

Example

```c
main()
{
    display();

    printf("End");
}

display()
{
    printf("Hello");
}
```

Execution

```text
main

↓

display()

↓

Hello

↓

return

↓

End
```

Notice:

* `main()` pauses while `display()` runs.
* After `display()` finishes, control returns to the next statement in `main()`.

---

## Characteristics

* Program starts from **main()**.
* Main calls subprograms.
* Subprograms may call other subprograms.
* After completion, control returns to the caller.
* Caller resumes execution from the next statement.

---

# Copy Rule

### Definition

The **effect of a function call** is the same as if the function body were copied and pasted at the call location (with parameters substituted).

Example

```c
square(5);
```

Suppose

```c
square(x)
{
    return x*x;
}
```

According to the Copy Rule:

```c
square(5);
```

behaves like

```c
5*5;
```

Of course, the compiler **does not literally copy** the code—it is only a way to understand function calls.

### Why use subprograms?

Instead of writing

```c
a=a*a;
```

many times,

we write

```c
square(a);
```

This improves:

* Code reuse
* Readability
* Maintenance

---

# Assumptions of Simple Call-Return

The book lists five assumptions.

| Assumption                | Meaning                                                      |
| ------------------------- | ------------------------------------------------------------ |
| No recursion              | A function cannot call itself.                               |
| Explicit calls            | Functions must be called using a call statement.             |
| Complete execution        | The function finishes before returning.                      |
| Immediate transfer        | Control immediately moves to the called function and back.   |
| Single execution sequence | Only one active execution of that function exists at a time. |

---

# Implementation

Understanding these four concepts is enough for exams.

---

## 1. Subprogram Definition

This is the **actual written function**.

Example

```c
void add()
{
    ...
}
```

It is stored only once.

---

## 2. Subprogram Activation

Every time the function is called,

a new execution begins.

Example

```c
add();

add();

add();
```

There is

* One definition
* Three activations

---

# Code Segment

The **Code Segment** stores

* Program instructions
* Constants

Example

```text
Code Segment

----------------

add()

display()

main()

----------------
```

It never changes during execution.

Only **one copy** exists.

---

# Activation Record

Also called the **Stack Frame**.

Contains

* Local variables
* Parameters
* Return address
* Other execution information

Example

```c
void add(int x)
{
    int y;
}
```

Activation Record contains

```text
Activation Record

------------------

Parameter x

Local variable y

Return address

------------------
```

Each function call gets its own activation record.

When the function returns,

the activation record is destroyed.

---

# CIP (Current Instruction Pointer)

### Definition

CIP points to

> **the instruction currently being executed.**

Example

```c
a=5;

b=10;

c=a+b;
```

Suppose the program is executing

```c
b=10;
```

CIP points to

```text
b=10;
```

---

# CEP (Current Environment Pointer)

### Definition

CEP points to

> **the current activation record.**

Since the activation record contains local variables,

CEP tells the processor

where the current function's variables are located.

---

# During Function Call

Suppose

```text
main()

↓

add()
```

Steps

1. Save old CIP
2. Save old CEP
3. Create new activation record
4. CEP → new activation record
5. CIP → first instruction of `add()`

When returning

1. Destroy activation record
2. Restore old CIP
3. Restore old CEP
4. Continue execution in `main()`

---

# Recursive Subprogram

## Definition

A **Recursive Subprogram** is a function that **calls itself**, directly or indirectly.

Example

```c
factorial(n)
{
    if(n==1)

        return 1;

    return n*factorial(n-1);
}
```

---

## Two Conditions for Recursion

### 1. Base Condition

Stops recursion.

Example

```c
if(n==1)

return 1;
```

---

### 2. Progress Toward Base Case

Every recursive call should move closer to the base case.

Example

```text
5

↓

4

↓

3

↓

2

↓

1
```

Eventually stops.

Without this,

the recursion never ends.

---

## Recursive Activation

Suppose

```text
factorial(3)
```

Execution

```text
factorial(3)

↓

factorial(2)

↓

factorial(1)

↓

Return

↓

Return

↓

Return
```

There are **three activation records** on the stack.

Each recursive call gets its own activation record.

Both **CIP and CEP** are used to manage these calls.

---

# Exception Handling

## What is an Exception?

An **Exception** is a **runtime error or unusual condition** that occurs while a program is executing.

Examples:

* Divide by zero
* Array index out of bounds
* File not found
* Out of memory

---

# Types of Errors

### Logic Error

Wrong algorithm.

Program runs but gives incorrect output.

---

### Syntax Error

Grammar mistakes.

Detected by the compiler.

Example

```c
if(x>0

missing )
```

---

### Exception

Occurs during execution.

Example

```c
10/0
```

---

# Exception Handling Process

```text
Problem Occurs

↓

Throw Exception

↓

Catch Exception

↓

Handle Exception
```

---

# Keywords

## try

Contains statements that may produce an exception.

```cpp
try
{
    ...
}
```

---

## throw

Generates an exception.

```cpp
throw x;
```

---

## catch

Receives and handles the exception.

```cpp
catch(int i)
{
    ...
}
```

---

# Flow

```text
try

↓

Error

↓

throw

↓

catch

↓

Handle Error
```

---

# Multiple Catch Blocks

One try block can throw different exceptions.

```cpp
try
{
    ...
}

catch(int)
{
}

catch(float)
{
}

catch(char)
{
}
```

Each catch handles a different type.

---

# Catch All Exceptions

```cpp
catch(...)
{
}
```

Handles any exception.

---

# Exception Propagation

Suppose

```text
main()

↓

A()

↓

B()

↓

Error
```

If B cannot handle it,

the exception goes to A.

If A cannot handle it,

it goes to main.

If no one handles it,

the program terminates.

This is called **Exception Propagation**.

---

# Coroutines

## Definition

A **Coroutine** is a special type of subprogram that can:

* Pause execution (**yield**),
* Return control to another coroutine,
* Later resume execution from the same point.

Unlike normal functions, coroutines do **not** need to finish before giving up control.

---

## Difference from Subroutines

| Subroutine                                | Coroutine                       |
| ----------------------------------------- | ------------------------------- |
| One entry point                           | Multiple entry/resume points    |
| Must finish before returning              | Can pause and resume            |
| Uses Last-In, First-Out (LIFO) call stack | Execution resumes based on need |

---

## Producer–Consumer Example

```text
Producer

↓

Creates Items

↓

Yield

↓

Consumer

↓

Uses Items

↓

Yield

↓

Producer resumes
```

They take turns instead of one finishing completely before the other starts.

---

# Subprogram Scheduling

Normally,

when you call a function,

it executes **immediately**.

Scheduling delays or controls **when** it executes.

### Scheduling Techniques

1. **After another subprogram**

```text
Call B after A
```

2. **When a condition becomes true**

```text
Call X when Y == 7
```

3. **At a specific time**

```text
Call B at time = CurrentTime + 50
```

4. **Based on priority**

```text
Call B with priority 5
```

Higher-priority tasks execute before lower-priority ones.

---

# One-Page Exam Revision

| Topic                           | Key Point                                                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Subprogram Sequence Control     | Controls function calls and returns.                                                                    |
| Simple Call-Return              | Caller pauses, callee executes, then returns.                                                           |
| Copy Rule                       | Function call behaves as if the function body were inserted at the call site (conceptually).            |
| Subprogram Definition           | The written function code, stored once.                                                                 |
| Subprogram Activation           | One execution instance of a function; created on each call.                                             |
| Code Segment                    | Stores executable instructions; shared by all activations.                                              |
| Activation Record (Stack Frame) | Stores parameters, local variables, return address, etc.                                                |
| CIP                             | Current Instruction Pointer; points to the instruction currently executing.                             |
| CEP                             | Current Environment Pointer; points to the current activation record.                                   |
| Recursive Subprogram            | A function that calls itself.                                                                           |
| Base Condition                  | Stops recursion.                                                                                        |
| Exception                       | A runtime abnormal condition (e.g., divide by zero).                                                    |
| `try`                           | Contains code that may generate an exception.                                                           |
| `throw`                         | Raises an exception.                                                                                    |
| `catch`                         | Handles the exception.                                                                                  |
| Exception Propagation           | Exception moves to the caller if not handled locally.                                                   |
| Coroutine                       | A subprogram that can suspend (`yield`) and later resume execution.                                     |
| Subprogram Scheduling           | Controls when a subprogram is executed (after another task, on a condition, at a time, or by priority). |

## Memory Tricks

* **Code Segment** → *Program instructions (shared, never changes).*
* **Activation Record** → *Function's temporary workspace (created on call, destroyed on return).*
* **CIP** → *Which instruction is executing?*
* **CEP** → *Where are the current function's local variables?*
* **Recursion** → *Function calls itself + must have a base case.*
* **Exception Handling** → **Try → Throw → Catch → Handle**.
* **Coroutine** → *Pause now, resume later.*
* **Scheduling** → *Decide **when** a subprogram should run.*
