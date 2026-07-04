#PPL 

# Overall Program–Subprogram Structure

## Definition

The **Overall Program–Subprogram Structure** describes **how a program and its subprograms (functions or procedures) are organized**.

A **subprogram** is a reusable block of code that performs a specific task.

Examples of subprograms:

* Function
* Procedure
* Method

---

# 1. Separate Subprogram Definition

## Definition

In this approach, **each subprogram is written as a separate unit**.

* Each function/procedure is compiled separately.
* Later, all compiled units are **linked together** to form the final program.

This approach is used in large software projects.

## Example

```c
// main.c
int main()
{
    add();
}
```

```c
// add.c
void add()
{
    // function body
}
```

The compiler compiles both files separately, and the **linker** combines them.

## Advantages

* Easy to maintain
* Easy to reuse code
* Supports team development

## Exam Definition

> **Separate subprogram definition means each function or procedure is defined and compiled separately, and the compiled units are linked together later.**

---

# 2. Separate Data Definition

## Definition

In this approach, **data and the operations that work on that data are grouped together**.

This is the idea behind **Object-Oriented Programming (OOP)**.

Languages like:

* Java
* C++
* Smalltalk

use this approach.

## Example

```cpp
class Student
{
    int age;

public:
    void display()
    {
    }
};
```

Here,

* `age` is the data.
* `display()` is the operation on that data.

Both are inside the same class.

## Advantages

* Better organization
* Information hiding
* Encapsulation
* Easier maintenance

## Exam Definition

> **Separate data definition groups data and the operations performed on that data into one unit, such as a class in object-oriented languages.**

---

# 3. Nested Subprogram Definitions

## Definition

A **nested subprogram** is a function defined **inside another function or program block**.

A subprogram can even contain other subprograms.

## Example (Conceptual)

```text
Main Program
    Function A
        Function B
```

Here,

* Function **B** is inside Function **A**.

This creates a hierarchical structure.

Languages like **Pascal** support nested functions.

## Advantages

* Better organization
* Limits visibility of inner functions
* Improves modularity

## Exam Definition

> **Nested subprogram definitions allow one subprogram to be declared inside another subprogram.**

---

# 4. Separate Interface

## Definition

Large programs often separate the **interface** from the **implementation**.

An **interface** tells other parts of the program:

* function names
* parameters
* return types

without showing the actual code.

Interfaces are created using:

* Modules
* Packages
* Header files

## Example (C)

Header file:

```c
// add.h
int add(int, int);
```

Implementation:

```c
// add.c
int add(int a, int b)
{
    return a + b;
}
```

The header file is the interface.

## Advantages

* Better modularity
* Easier maintenance
* Supports separate compilation

## Exam Definition

> **A separate interface provides the declarations of subprograms separately from their implementation using modules, packages, or header files.**

---

# 5. Data Descriptions Separated from Executable Statements

## Definition

In some programming languages, **data declarations** and **executable statements** are placed in different sections.

The program is divided into:

* Data Division (variable declarations)
* Procedure Division (program statements)

This style improves program organization.

## Example (Conceptual)

```text
DATA DIVISION
    int age;
    int marks;

PROCEDURE DIVISION
    age = 20;
    marks = 80;
```

Languages like **COBOL** use this approach.

## Advantages

* Clear program structure
* Easy to locate variables
* Improves readability

## Exam Definition

> **In this approach, variable declarations and executable statements are kept in separate sections of the program.**

---

# 6. Unseparated Subprogram Definitions

## Definition

In this approach, there is **no clear distinction between the main program and subprograms**.

The entire program is simply a list of statements.

Subprogram behavior is often created using **GOTO** statements instead of proper functions.

## Example (Conceptual)

```text
Statement 1
Statement 2

GOTO Label

Statement 3

Label:
Statement 4
Statement 5
```

There is no actual function definition.

Older programming styles often used this approach.

## Disadvantages

* Difficult to understand
* Difficult to debug
* Poor program structure
* Not modular

## Exam Definition

> **Unseparated subprogram definition means there is no syntactic distinction between the main program and subprograms, and control is often transferred using GOTO statements.**

---

# Summary Table

| Structure                                                  | Meaning                                                             | Example                                    |
| ---------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------ |
| **Separate Subprogram Definition**                         | Functions are written and compiled separately                       | Separate `.c` files in C                   |
| **Separate Data Definition**                               | Data and related operations are grouped together                    | Class in C++ or Java                       |
| **Nested Subprogram Definitions**                          | A function is defined inside another function                       | Pascal nested procedures                   |
| **Separate Interface**                                     | Function declarations are separate from implementations             | Header files (`.h`) in C                   |
| **Data Descriptions Separated from Executable Statements** | Variable declarations and executable code are in different sections | COBOL Data Division and Procedure Division |
| **Unseparated Subprogram Definitions**                     | No clear separation between main program and subprograms            | Programs using `GOTO` instead of functions |

---

# Quick Revision (2-Mark)

* **Separate Subprogram Definition:** Functions are defined and compiled separately, then linked together.
* **Separate Data Definition:** Data and related operations are grouped together in a class.
* **Nested Subprogram Definition:** A function is defined inside another function.
* **Separate Interface:** Function declarations are separated from their implementation.
* **Data Descriptions Separated from Executable Statements:** Variable declarations and executable code are kept in separate sections.
* **Unseparated Subprogram Definition:** No clear distinction between the main program and subprograms; often uses `GOTO`.
