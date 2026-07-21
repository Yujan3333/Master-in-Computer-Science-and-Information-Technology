#PPL #third-semester 

# Unit 2.2: Abstract Data Types (ADT) – Exam-Focused Summary

This unit mainly covers:

1. Abstraction
2. Abstract Data Types (ADT)
3. Information Hiding
4. Encapsulation
5. Type Equivalence
6. Storage Management

---

# 1. Abstraction

## Definition

**Abstraction** means showing **only the important features** of an object while **hiding unnecessary implementation details**.

Simply,

> **Abstraction = Show what an object does, hide how it does it.**

---

## Why is abstraction needed?

Programming becomes complex as programs grow.

Abstraction helps programmers:

* Focus on important details.
* Ignore unnecessary implementation.
* Make programs easier to understand and maintain.

---

## Types of Abstraction

### A. Process Abstraction

Hides **how a task is performed**.

You only know what the function does.

Example:

```c
sort(array);
```

You know it sorts the array.

You don't need to know:

* Bubble Sort
* Merge Sort
* Quick Sort

---

### B. Data Abstraction

Hides **how data is stored or represented**.

Example:

```cpp
stack.push(10);
```

You don't know whether Stack uses:

* Array
* Linked List

Only the operations matter.

---

# 2. Abstract Data Type (ADT)

## Definition

An **Abstract Data Type (ADT)** is a data type that **hides its internal data representation** and allows access **only through predefined operations (methods/functions)**.

Simply,

> **ADT = Data + Allowed Operations + Hidden Implementation**

---

## Characteristics of ADT

* Data representation is hidden.
* User accesses data only through provided operations.
* Interface is visible.
* Implementation is hidden.
* Provides security and modularity.

---

## Example

### Stack ADT

Visible operations:

```text
Push()
Pop()
Top()
IsEmpty()
```

Hidden implementation:

* Array
* Linked List

The user doesn't know which one is used.

---

# 3. Built-in Types as ADT

Built-in types are also ADTs.

Example:

```cpp
float x = 3.5;
```

You can perform

```text
+
-
*
/
```

But you cannot access:

* Sign bit
* Exponent
* Mantissa

Their representation is hidden.

---

# 4. User-defined ADT

Programmers can also create ADTs.

Example:

```cpp
class BankAccount
{
private:
    int balance;

public:
    void deposit();
    void withdraw();
};
```

User can only use

```text
deposit()

withdraw()
```

Cannot directly modify

```text
balance
```

---

## Properties of User-defined ADT

* Internal representation hidden.
* Only defined operations available.
* Interface independent of implementation.
* Variables of that type can be created.

---

# 5. Information Hiding

## Definition

Information hiding means **hiding internal data and implementation details** and allowing access only through approved operations.

Simply,

> Hide the data, expose only the operations.

---

## Example

```cpp
private:
    int salary;
```

Access only through

```cpp
setSalary()
getSalary()
```

---

## Benefits

### 1. Protects Data

Prevents accidental or unauthorized modification.

---

### 2. Easier Maintenance

Only a small part of the code can modify the data.

Finding bugs becomes easier.

---

### 3. Reduces Complexity

Programmer doesn't need to understand the entire system.

---

### 4. Avoids Name Conflicts

Hidden variables have smaller scope.

---

# 6. Encapsulation

## Definition

Encapsulation means **grouping related data and methods into a single unit (module/class/package)**.

Simply,

> **Encapsulation = Wrap data + functions together.**

---

## Why is Encapsulation Needed?

Large programs become difficult to manage.

Problems:

* Difficult organization.
* Large recompilation time.

Solution:

Encapsulation.

---

## Benefits
- [More Benefits of Encapsulation](More%20Benefits%20of%20Encapsulation.md)

### Better organization

Related code stays together.

---

### Separate compilation

Only changed modules are recompiled.

---

### Reusability

Modules can be stored in libraries.

---

### Easier maintenance

Only affected modules need changes.

---

# Difference Between Abstraction and Encapsulation

| **Abstraction**                                                                     | **Encapsulation**                                                                                          |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 1. Hides **implementation details**.                                                | Hides **data (internal state)**.                                                                           |
| 2. Focuses on **what** an object does.                                              | Focuses on **how** data is protected.                                                                      |
| 3. Provides only the **essential features** to the user.                            | Restricts **direct access** to data.                                                                       |
| 4. Achieved using **Abstract Data Types (ADTs), abstract classes, and interfaces**. | Achieved using **classes** and **access modifiers** (`private`, `protected`, `public`).                    |
| 5. Reduces the **complexity** of a system.                                          | Improves **security** and data integrity.                                                                  |
| 6. Concerned with **design level** (interface).                                     | Concerned with **implementation level** (data protection).                                                 |
| 7. Users know **what operations are available**, not how they work internally.      | Users access data only through **public methods** such as getters, setters, or other member functions.     |
| 8. Example: A driver uses a car without knowing how the engine works.               | Example: A bank account's balance is private and can only be modified through `deposit()` or `withdraw()`. |



### **Easy Memory Trick**

| **Abstraction**         | **Encapsulation**     |
| ----------------------- | --------------------- |
| **What**                | **How**               |
| Hide **implementation** | Hide **data**         |
| Reduce **complexity**   | Increase **security** |
| Interface               | Access control        |



---

# 7. Type Equivalence

## Definition

Two types are **equivalent** if one can replace the other **without type conversion (coercion).**

---

## Two Approaches

### A. Name Type Equivalence

Two types are equivalent only if they have the **same type name**.

Example

```cpp
typedef int age;
typedef int roll_no;

age a;
roll_no r;
```

Although both are integers,

they have different names.

Therefore,

```text
Not Name Equivalent
```

---

#### Advantages

* Easy to implement.
* Strong type safety.

---

#### Disadvantages

* Very restrictive.
* Even similar structures may not be equivalent.

---

### B. Structure Type Equivalence

Two types are equivalent if their structures are identical.

Example

```cpp
typedef int age;
typedef int roll_no;
```

Both store integers.

Therefore,

```text
Structure Equivalent
```

---

#### Advantages

* More flexible.
* Easier to reuse similar structures.

---

#### Disadvantages

* Harder for compiler.
* Entire structure must be compared.

---

## Comparison

| Name Equivalence    | Structure Equivalence    |
| ------------------- | ------------------------ |
| Compare names       | Compare structure        |
| Easy implementation | Difficult implementation |
| Restrictive         | Flexible                 |
| Strong safety       | Easier reuse             |

---

# Example

```cpp
typedef int age;
typedef int roll_no;

age a1,a2;
roll_no r1,r2;
```

Name equivalence:

```text
a1 ↔ a2 ✔

a1 ↔ r1 ✘
```

Structure equivalence:

```text
a1 ↔ r1 ✔
```

---

# 8. Storage Management

## Definition

Storage management is the process of **allocating and managing memory** for variables, arrays, objects, and other data structures.

The compiler and operating system decide **where and how data is stored in memory**.

---

## Types of Storage Allocation

### A. Static Allocation

Memory allocated **before execution (compile time)**.

---

#### Characteristics

* Address never changes.
* Exists throughout execution.
* Fast.
* Not flexible.

---

#### Example

```c
int global;
```

Global variables.

---

#### Advantages

* Simple.
* Fast.

---

#### Disadvantages

* Wastes memory.
* Cannot create dynamic objects.

---

### B. Stack Allocation

Memory allocated **during execution** using the stack.

Used for:

* Local variables
* Function parameters

---

#### Characteristics

* Memory allocated when function starts.
* Automatically removed when function ends.

---

#### Example

```cpp
void fun()
{
    int x;
}
```

`x` exists only while `fun()` executes.

---

#### Advantages

* Fast.
* Automatic memory management.

---

#### Disadvantages

* Cannot store long-lived dynamic objects.
* Limited stack size.

---

### C. Heap Allocation

Memory allocated dynamically at runtime.

---

#### Characteristics

* Allocated when needed.
* Freed manually (C/C++) or by Garbage Collector (Java).

---

#### C/C++ Example

```cpp
int *p = new int;
```

or

```c
malloc()
calloc()
realloc()
```

---

#### Java Example

```java
Student s = new Student();
```

---

#### Advantages

* Flexible.
* Supports dynamic data structures.

---

#### Disadvantages

* Slower than stack allocation.
* May cause memory leaks (especially in C/C++).

---

# Comparison of Storage Allocation

| Feature         | Static           | Stack               | Heap                                   |
| --------------- | ---------------- | ------------------- | -------------------------------------- |
| Allocation Time | Compile time     | Runtime             | Runtime                                |
| Memory Released | Program ends     | Function/block ends | Manually or Garbage Collector          |
| Speed           | Fastest          | Fast                | Slower                                 |
| Flexibility     | Low              | Medium              | High                                   |
| Example         | Global variables | Local variables     | Objects created with `new`, `malloc()` |

---

# One-Page Exam Revision

| Topic                          | Key Point                                                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Abstraction                    | Shows essential features and hides unnecessary implementation details.                                        |
| Process Abstraction            | Hides how a task is performed (e.g., calling `sort()`).                                                       |
| Data Abstraction               | Hides data representation while exposing operations.                                                          |
| Abstract Data Type (ADT)       | Combines data with operations and hides internal representation.                                              |
| Built-in ADT                   | Types like `int` and `float`; users use operations but cannot access internal representation.                 |
| User-defined ADT               | Programmer-created types with hidden data and public operations (e.g., classes).                              |
| Information Hiding             | Restricts direct access to internal data; only approved operations can modify it.                             |
| Benefits of Information Hiding | Protects data, reduces complexity, simplifies maintenance, avoids name conflicts.                             |
| Encapsulation                  | Groups related data and methods into a single module or class.                                                |
| Benefits of Encapsulation      | Better organization, separate compilation, reuse, easier maintenance.                                         |
| Type Equivalence               | Determines whether two types can be used interchangeably without coercion.                                    |
| Name Type Equivalence          | Types are equivalent only if they share the same type name.                                                   |
| Structure Type Equivalence     | Types are equivalent if their structures are identical.                                                       |
| Static Allocation              | Memory allocated at compile time; used for global/static variables.                                           |
| Stack Allocation               | Runtime memory for local variables; automatically freed when the function returns.                            |
| Heap Allocation                | Runtime dynamic memory; allocated with `new`, `malloc()`, etc., and freed manually or by a garbage collector. |

## Memory Trick

* **Abstraction** → *Hide details.*
* **Information Hiding** → *Hide data.*
* **Encapsulation** → *Wrap data + methods together.*
* **ADT** → *Data + Operations + Hidden Representation.*
* **Name Equivalence** → *Same name.*
* **Structure Equivalence** → *Same structure.*
* **Static → Global**, **Stack → Local**, **Heap → Dynamic**.
