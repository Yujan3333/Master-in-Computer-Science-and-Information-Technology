#PPL #third-semester 

# Unit 2.1 : Elementary Data Types (Exam-Focused Summary)

This unit mainly covers **Data Objects, Variables, Data Types, Type Checking, Type Conversion, Assignment, and Declarations**.

---

# 1. Introduction

A program consists of three basic elements:

1. **Data** – What information is stored.
2. **Operations** – What actions are performed on the data.
3. **Control** – In what order the operations execute.

Programming languages differ in:

* Types of data they support.
* Operations they provide.
* Control structures (if, loop, etc.).

---

# 2. Data Object

## Definition

A **Data Object** is a **run-time container that stores one or more data values** in memory.

Simply:

> Data Object = Container that stores data.

Example

```c
int age = 25;
```

Here,

* Data Object = `age`
* Data Value = `25`

---

## Types of Data Objects

### A. Programmer-defined Data Objects

Created directly by the programmer.

Examples:

* Variables
* Constants
* Arrays
* Files

Example:

```c
int age;
```

---

### B. System-defined Data Objects

Created automatically by the system.

Examples:

* Runtime stack
* Activation records
* File buffers
* Free-space lists

The programmer cannot directly access them.

---

## Difference Between Data Object and Data Value

| Data Object           | Data Value                  |
| --------------------- | --------------------------- |
| Container             | Actual information          |
| Stored in memory      | Represented as bit patterns |
| Example: Variable `x` | Example: `10`               |

---

## Elementary vs Data Structure

### Elementary Data Object

Contains **only one value**.

Example:

```c
int x;
```

---

### Data Structure

Contains **multiple data objects**.

Example:

```c
int arr[10];
```

---

## Important Attributes of a Data Object

1. **Type** – Integer, Float, Character, etc.
2. **Location** – Memory address.
3. **Value** – Current stored value.
4. **Name** – Identifier used by the programmer.
5. **Component** – Relationship with other data objects.

---

# 3. Variables and Constants

## Variable

A named data object whose value **can change**.

Example:

```c
int age = 20;
age = 25;
```

---

## Constant

A named data object whose value **cannot change**.

Example:

```c
const int MAX = 100;
```

---

## Literal Constant

The value itself.

Examples:

```text
10
3.14
'A'
```

---

## Manifest (Programmer-defined) Constant

Programmer gives a name.

Example:

```c
const float PI = 3.14159;
```

---

## Case Sensitive vs Case Insensitive

### Case Sensitive

```text
Age
age
AGE
```

All are different.

Example: C, C++, Java, Python.

---

### Case Insensitive

```text
Age = age = AGE
```

All mean the same.

---

# 4. Persistence

Persistence refers to **how long data exists**.

---

## Transient Data Objects

Exist only while the program is running.

Example:

Local variables.

---

## Persistent Data Objects

Continue to exist after the program ends.

Examples:

* Files
* Database records

---

## Persistent Language

A language that supports persistent data directly.

---

# 5. Data Type

## Definition

A **Data Type** is a class of data objects together with the operations that can be performed on them.

Examples:

* Integer
* Float
* Character
* Array
* File

---

## Data Type Specification

Contains three parts:

### 1. Attributes

Describe characteristics.

Example (Array):

* Dimensions
* Size
* Index range

---

### 2. Values

Possible values the type can hold.

Example:

Integer:

```text
..., -2, -1, 0, 1, 2, ...
```

---

### 3. Operations

Operations allowed.

Example:

Integer:

* Addition
* Subtraction
* Multiplication
* Division

---

## Data Type Implementation

Contains:

### Storage Representation

How data is stored in memory.

Example:

Integer occupies 4 bytes.

---

### Algorithms

How operations are implemented.

Example:

Addition uses CPU arithmetic instructions.

---

# 6. Elementary Data Types

Elementary data objects contain only **one value**.

Examples:

* Integer
* Float (Real)
* Character
* Boolean

---

## Specification

### Attributes

Type and Name.

---

### Values

All legal values of that type.

Example:

Boolean:

```text
True
False
```

---

### Operations

Operations allowed.

Example:

Boolean:

```text
AND
OR
NOT
```

---

# Operations

An operation is a mathematical function.

Example:

```text
+
-
*
/
```

---

## Signature

General form:

```text
Operation : Input Types → Result Type
```

Example:

```text
Add : int × int → int
```

Meaning:

Takes two integers and returns one integer.

---

## Unary Operation

One input.

Example:

```text
-x
```

---

## Binary Operation

Two inputs.

Example:

```text
a + b
```

---

## Arity

Number of arguments.

Examples:

* Unary → 1
* Binary → 2

---

## Problems in Defining Operations

### 1. Undefined Operations

Example:

```text
10 / 0
```

Undefined.

---

### 2. Implicit Arguments

Uses global variables.

---

### 3. Side Effects

Operation changes something outside itself.

Example:

```cpp
void add(int &x)
{
    x++;
}
```

`x` changes outside the function.

---

### 4. History Sensitivity (Self-modification)

Result depends on previous executions.

Example:

A function maintaining an internal counter.

---

## Subtype

A subtype is a smaller category within a larger type.

Example:

```text
Vehicle
   |
 Car
```

Car is a subtype of Vehicle.

Vehicle is the supertype.

---

# 7. Implementation of Elementary Data Types

Two parts:

## Storage Representation

How data is stored.

Example:

Integer:

```text
Memory

10101010
```

---

## Implementation of Operations

Three methods:

### Hardware Implementation

CPU performs operation directly.

Example:

Addition.

---

### Procedure/Function

Implemented using functions.

Example:

Square root.

---

### Inline Code

Compiler inserts operation code directly instead of calling a function.

---

# 8. Declarations

## Definition

A declaration tells the compiler about:

* Name
* Type
* Lifetime
* Initial value (optional)

Example:

```c
int age;
```

---

## Explicit Declaration

Programmer specifies type.

Example:

```c
int x;
```

---

## Implicit Declaration

Type is automatically inferred.

Example (Perl):

```perl
$x = 5;
```

---

## Declaration of Operations

Function prototype tells compiler argument types.

Example:

```c
float Sub(int x, float y);
```

Signature:

```text
Sub : int × float → float
```

---

## Purposes of Declarations

1. Select proper storage.
2. Manage memory efficiently.
3. Resolve overloaded functions at compile time.
4. Enable static type checking.

---

# 9. Type Checking

## Definition

Ensures every operation receives the **correct number and type of arguments**.

---

## Dynamic Type Checking

Performed **during execution**.

Example:

Python.

### Advantages

* Flexible.
* No declarations required.
* Variable type may change.

### Disadvantages

* Slower.
* More memory.
* Some errors appear only at runtime.

---

## Static Type Checking

Performed **during compilation**.

Example:

C, C++, Java.

Needs:

* Function signatures.
* Variable types.
* Constant types.

---

## Strong Typing

A language is **strongly typed** if **all type errors can be detected** and operations cannot produce values outside their declared result type.

Examples include languages such as Java and ML.

---

## Type Inference

Compiler determines missing types automatically.

Example:

```ml
fun area(length:int,width)=length*width
```

Compiler infers the type of `width`.

---

# 10. Type Conversion and Coercion

## Type Conversion

**Explicit** conversion by programmer.

Example:

```c
(int)x
```

---

## Coercion

**Implicit** conversion by compiler.

Example:

```c
5 + 3.5
```

Compiler converts:

```text
5 → 5.0
```

before addition.

---

## Widening

Safe conversion.

Example:

```text
int → float
```

No information lost.

---

## Narrowing

Unsafe conversion.

Example:

```text
float → int
```

May lose the decimal part.

---

# 11. Assignment and Initialization

## Assignment

Changes the value stored in a variable.

Example:

```c
x = 10;
```

---

## l-value and r-value

Example:

```c
A = B;
```

* **l-value** = Memory location of `A` (where the value will be stored).
* **r-value** = Current value of `B` (what is being copied).

Steps:

1. Find `A`'s location (l-value).
2. Read `B`'s value (r-value).
3. Store `B`'s value into `A`.
4. Return the assigned value (in languages where assignment is an expression).

---

## Uninitialized Variable

A variable that has been allocated memory but has **not been given an initial value**.

Example:

```c
int x;
printf("%d", x);
```

`x` contains a **random (garbage) value**.

---

## Initialization

Giving a variable its first value.

Example:

```c
int x = 0;
```

Initialization helps avoid errors caused by uninitialized variables.

---

# One-Page Exam Revision

| Topic                  | Key Point                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------- |
| Data Object            | Runtime container for data values.                                                                      |
| Programmer-defined     | Variables, constants, arrays, files.                                                                    |
| System-defined         | Stack, activation records, buffers.                                                                     |
| Variable               | Value can change.                                                                                       |
| Constant               | Value cannot change.                                                                                    |
| Literal Constant       | Value written directly (e.g., `21`).                                                                    |
| Manifest Constant      | Named constant defined by programmer (e.g., `const int MAX = 100;`).                                    |
| Persistence            | **Transient:** exists only during execution. **Persistent:** survives after program ends (e.g., files). |
| Data Type              | Defines attributes, values, and operations.                                                             |
| Elementary Data Type   | Single-value types such as integer, real, character, Boolean.                                           |
| Unary Operation        | One operand.                                                                                            |
| Binary Operation       | Two operands.                                                                                           |
| Declaration            | Gives compiler information about names, types, and lifetimes.                                           |
| Dynamic Type Checking  | Runtime checking; flexible but slower.                                                                  |
| Static Type Checking   | Compile-time checking; faster and catches errors early.                                                 |
| Strong Typing          | Prevents invalid type operations through type-safe rules.                                               |
| Type Conversion        | Explicit conversion by programmer.                                                                      |
| Coercion               | Implicit conversion by compiler.                                                                        |
| Widening               | Safe conversion (e.g., `int → float`).                                                                  |
| Narrowing              | May lose information (e.g., `float → int`).                                                             |
| Assignment             | Changes the value bound to a variable.                                                                  |
| l-value                | Memory location of an object.                                                                           |
| r-value                | Actual value stored in the object.                                                                      |
| Uninitialized Variable | Allocated but not assigned a valid value; contains garbage data.                                        |
