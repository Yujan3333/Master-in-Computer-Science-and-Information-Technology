#third-semester #PPL 

# 3.2 Subprogram Control

## 1. Introduction

A **subprogram** is a self-contained block of code that performs a specific task. It can be called whenever needed, improving code reuse and modularity.

Examples:

* Function
* Procedure
* Method

**Advantages**

* Code reusability
* Easy maintenance
* Modular programming
* Reduces code duplication

---

# 2. Subprogram Sequence Control

Subprogram sequence control determines **how control is transferred between the calling program and the called subprogram**.

### Steps

1. The calling program invokes the subprogram.
2. Control transfers to the subprogram.
3. Parameters are passed.
4. The subprogram executes.
5. The result is returned.
6. Control returns to the calling program.

**Example**

```c
int sum(int a, int b)
{
    return a + b;
}

int main()
{
    int x = sum(5, 3);
}
```

Flow:

```text
main()
   ↓
sum()
   ↓
return
   ↓
main()
```

---

# 3. Parameter Transmission (Parameter Passing)

Parameter transmission is the **process of passing values between the calling function and the called function**.

There are several methods.

### a) Pass by Value

* A copy of the actual parameter is passed.
* Changes inside the function do not affect the original variable.

```c
void fun(int x)
{
    x = 20;
}

int a = 10;
fun(a);
```

Result:

```text
a = 10
```

---

### b) Pass by Reference

* The address (reference) of the variable is passed.
* Changes inside the function affect the original variable.

```c
void fun(int *x)
{
    *x = 20;
}

int a = 10;
fun(&a);
```

Result:

```text
a = 20
```

---

### Difference

| Pass by Value            | Pass by Reference             |
| ------------------------ | ----------------------------- |
| Copy is passed           | Address/reference is passed   |
| Original value unchanged | Original value changes        |
| Safer                    | More efficient for large data |

---

# 4. Scope

**Scope** is the region of a program where a variable can be accessed.

---

## a) Static (Lexical) Scope

* Scope is determined by the **program structure**.
* The compiler determines scope before execution.
* Used by C, C++, Java, Python.

Example

```c
int x = 10;

void fun()
{
    printf("%d", x);
}
```

`fun()` accesses the global variable `x`.

---

## b) Dynamic Scope

* Scope depends on the **calling sequence** of functions.
* Determined during program execution.
* Used in languages such as Lisp, APL, and Snobol.

---

### Difference

| Static Scope               | Dynamic Scope                     |
| -------------------------- | --------------------------------- |
| Determined at compile time | Determined at run time            |
| Based on program structure | Based on calling sequence         |
| Easier to understand       | More flexible but harder to trace |

---

# 5. Lifetime

**Lifetime** is the period during which a variable exists in memory.

### Types

### Static Lifetime

* Exists throughout program execution.

Example

```c
static int x;
```

---

### Stack (Automatic) Lifetime

* Created when a function starts.
* Destroyed when the function ends.

```c
void fun()
{
    int x;
}
```

---

### Heap Lifetime

* Allocated dynamically.
* Exists until explicitly deallocated.

Example

```c
int *p = malloc(sizeof(int));
free(p);
```

---

# 6. Block Structure

A **block** is a group of statements enclosed within `{ }`.

Variables declared inside a block are accessible only within that block.

Example

```c
{
    int x = 10;
}
```

`x` cannot be accessed outside the block.

### Advantages

* Organizes code.
* Limits variable visibility.
* Prevents name conflicts.

---

# 7. Local Referencing Environment

The **local referencing environment** is the set of all variables that a subprogram can access during its execution.

It includes:

* Local variables
* Parameters
* Global variables (if visible)
* Variables from enclosing blocks (depending on the language)

Example

```c
int g = 5;

void fun(int a)
{
    int b = 10;
}
```

Inside `fun()`, the local referencing environment includes:

* `a` (parameter)
* `b` (local variable)
* `g` (global variable)

---

# Exam-Oriented Short Notes

**Q. What is a subprogram?**
**Ans:** A subprogram is a reusable block of code (function or procedure) that performs a specific task.

**Q. What is subprogram sequence control?**
**Ans:** It controls the transfer of execution from the calling program to the called subprogram and back after execution.

**Q. What is parameter transmission?**
**Ans:** It is the process of passing data between the calling function and the called function. Common methods are **pass by value** and **pass by reference**.

**Q. What is scope?**
**Ans:** Scope is the region of a program where a variable is accessible. It can be **static (lexical)** or **dynamic**.

**Q. What is lifetime?**
**Ans:** Lifetime is the duration for which a variable exists in memory.

**Q. What is a block structure?**
**Ans:** A block structure is a group of statements enclosed in braces `{ }` that defines the scope of local variables.

**Q. What is the local referencing environment?**
**Ans:** It is the collection of variables that are accessible within a subprogram during its execution, including local variables, parameters, and any visible global variables.
