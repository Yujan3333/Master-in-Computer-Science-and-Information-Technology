#PPL #third-semester 

# Unit 6(2.3): Inheritance (Exam-Focused Summary)

This unit mainly covers:

1. Inheritance
2. Derived Classes
3. Abstract Classes
4. Objects and Messages
5. Polymorphism

---

# 1. Inheritance

## Definition

**Inheritance** is the mechanism by which one class acquires the properties (data) and methods (functions) of another class.

Simply,

> **Inheritance = Child class gets properties and methods from Parent class.**

It promotes **code reuse** because you don't have to rewrite common code.

---

## General Idea

Suppose every student has:

* Name
* Age
* Address

Instead of writing these in every class, create a parent class.

```text
          Person
      ----------------
      Name
      Age
      Address
             ▲
      ----------------
      |              |
   Student        Teacher
```

Student and Teacher automatically inherit:

* Name
* Age
* Address

---

# Early Form of Inheritance (Scope Rules)

Before OOP, inheritance could be seen in **block-structured languages** like C through scope rules.

Example:

```c
{
    int i, j;

    {
        float j, k;
        k = i + j;
    }
}
```

Here:

* `i` is **not declared** in the inner block, so it is inherited from the outer block.
* `j` is declared again in the inner block (`float j`), so the outer `int j` is **hidden (shadowed)**.

Thus:

* `i` → inherited.
* Outer `j` → blocked by inner `j`.

---

# Parent and Child Class

If

```text
A → B
```

then

* **A = Parent (Superclass/Base Class)**
* **B = Child (Subclass/Derived Class)**

Example:

```cpp
class Animal      // Parent
{
};

class Dog : public Animal   // Child
{
};
```

Dog automatically inherits members of Animal (subject to access rules).

---

# Types of Inheritance

## A. Single Inheritance

One child has only one parent.

```text
Animal
   │
  Dog
```

Example:

```cpp
class Dog : public Animal
```

---

## B. Multiple Inheritance

One child has multiple parents.

```text
Teacher      Researcher
      \      /
       \    /
     Professor
```

Example:

```cpp
class Professor : public Teacher, public Researcher
```

* Supported in **C++**.
* **Not supported in Java** (Java uses interfaces instead).

---

# Family Relationships

```text
         A
       /   \
      B     C
       \
        D
```

* A = Ancestor of B, C, D
* B and C = Siblings
* B = Immediate descendant of A
* D = Descendant of A

---

# 2. Derived Class

## Definition

A **Derived Class** (or Child/Subclass) is a class created from an existing class (Base Class).

It inherits properties and methods of the base class.

Example:

```cpp
class Animal
{
public:
    void eat() {}
};

class Dog : public Animal
{
public:
    void bark() {}
};
```

Dog inherits `eat()` and adds its own `bark()`.

---

## Characteristics

* Reuses code from the base class.
* Can add new members.
* Can override inherited methods.
* Public inherited members remain accessible to users (depending on inheritance mode).

---

# Approaches to Inheritance

## A. Copy-Based Approach

Each object has its **own copy** of inherited data.

```text
Animal Object
-------------
name
age

Dog Object
-------------
name
age
breed
```

The inherited data is duplicated in each derived object.

---

## B. Delegation-Based Approach

Derived objects **share** the base object's data instead of copying it.

```text
Dog
 │
 ▼
Animal Data
```

Changes in the shared base data are reflected in derived objects.

---

# Difference

| Copy-Based              | Delegation-Based                   |
| ----------------------- | ---------------------------------- |
| Copies inherited data   | Shares inherited data              |
| More memory used        | Less memory used                   |
| Objects are independent | Objects depend on shared base data |

---

# 3. Abstract Class

## Definition

An **Abstract Class** is a class that **cannot be instantiated** (you cannot create objects directly from it).

It acts as a **template** for other classes.

Simply,

> **Abstract Class = Incomplete class used only for inheritance.**

---

## Example

```cpp
class Animal
{
public:
    virtual void sound() = 0;
};
```

You cannot write:

```cpp
Animal a;   // Error
```

Instead,

```cpp
class Dog : public Animal
{
public:
    void sound()
    {
        cout << "Bark";
    }
};
```

Now:

```cpp
Dog d;
```

is allowed.

---

## Java

Declared using:

```java
abstract class Animal
```

Can contain:

* Abstract methods (no body)
* Normal methods (with body)

---

## C++

An abstract class contains **at least one pure virtual function**.

Example:

```cpp
virtual void display() = 0;
```

---

# Why Use Abstract Classes?

* Define a common interface.
* Force child classes to implement required methods.
* Prevent creating incomplete objects.

---

# 4. Objects and Messages

## Object

An **Object** is an **instance of a class**.

Example:

```cpp
Student s;
```

Here:

* Class = Student
* Object = s

---

## Instantiation

The process of creating an object from a class.

Example:

```cpp
Student s;
```

Instantiation creates the object `s`.

---

## Message

A **Message** is a **request sent to an object to execute one of its methods**.

Example:

```cpp
s.display();
```

Message:

```text
display()
```

Receiver:

```text
s
```

---

## Message Contains

1. Method name
2. Arguments (if any)

Example:

```cpp
student.calculateMarks(80);
```

Message contains:

* Method: `calculateMarks`
* Argument: `80`

---

# 5. Polymorphism

## Definition

**Polymorphism** means **one interface, many forms**.

The same function or operator behaves differently depending on the object or arguments.

Simply,

> **Same name, different behavior.**

---

# Types of Polymorphism

```text
          Polymorphism
               │
     ┌─────────┴─────────┐
     │                   │
Compile-Time        Run-Time
```

---

# A. Compile-Time Polymorphism (Static Polymorphism)

The compiler decides **which function to call** during compilation.

Achieved by:

1. Function Overloading
2. Operator Overloading
3. Templates

---

## Function Overloading

```cpp
void show();
void show(int);
```

Compiler chooses the correct version based on the arguments.

---

## Operator Overloading

Operators gain new meanings for user-defined types.

Example:

```cpp
Complex c3 = c1 + c2;
```

The `+` operator is overloaded to add `Complex` objects.

---

## Templates

Templates let you write generic code.

Example:

```cpp
template<typename T>
T add(T a, T b)
{
    return a + b;
}
```

The same function works for `int`, `float`, `double`, etc.

---

# B. Run-Time Polymorphism (Dynamic Polymorphism)

The method to execute is determined **during program execution**.

Achieved by:

* Method Overriding
* Virtual Functions

---

## Method Overriding

The child class provides its own implementation of a parent method.

Example:

```cpp
class Animal
{
public:
    virtual void sound()
    {
        cout << "Animal";
    }
};

class Dog : public Animal
{
public:
    void sound()
    {
        cout << "Bark";
    }
};
```

At runtime:

```cpp
Animal* a = new Dog();
a->sound();
```

Output:

```text
Bark
```

The program decides at runtime that the object is a `Dog`.

---

# Comparison of Compile-Time and Run-Time Polymorphism

| Compile-Time Polymorphism | Run-Time Polymorphism   |
| ------------------------- | ----------------------- |
| Static (Early Binding)    | Dynamic (Late Binding)  |
| Decision at compile time  | Decision at runtime     |
| Function overloading      | Method overriding       |
| Operator overloading      | Virtual functions       |
| Templates                 | Dynamic method dispatch |
| Faster                    | Slightly slower         |

---

# One-Page Exam Revision

| Topic                        | Key Point                                                                           |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| Inheritance                  | Mechanism by which a child class acquires properties and methods of a parent class. |
| Parent/Superclass            | The class that provides inherited members.                                          |
| Child/Subclass/Derived Class | The class that inherits from the parent.                                            |
| Single Inheritance           | One parent and one child relationship.                                              |
| Multiple Inheritance         | One child inherits from multiple parents (supported in C++, not Java).              |
| Derived Class                | Reuses base class members and can add or override functionality.                    |
| Copy-Based Inheritance       | Each derived object stores its own copy of inherited data.                          |
| Delegation-Based Inheritance | Derived objects share the base object's data.                                       |
| Abstract Class               | A class that cannot be instantiated and is meant to be inherited.                   |
| Java Abstract Class          | Declared using the `abstract` keyword.                                              |
| C++ Abstract Class           | Contains at least one pure virtual function (`= 0`).                                |
| Object                       | An instance of a class.                                                             |
| Instantiation                | The process of creating an object.                                                  |
| Message                      | A request sent to an object to invoke one of its methods.                           |
| Polymorphism                 | One interface with many implementations or behaviors.                               |
| Compile-Time Polymorphism    | Achieved using function overloading, operator overloading, and templates.           |
| Run-Time Polymorphism        | Achieved using method overriding and virtual functions.                             |

## Memory Tricks

* **Inheritance** → *Child gets Parent's properties.*
* **Derived Class** → *New class built from an existing class.*
* **Abstract Class** → *Template class; no objects can be created directly.*
* **Object** → *Instance of a class.*
* **Message** → *Method call sent to an object.*
* **Compile-Time Polymorphism** → *Overloading + Templates (compiler decides).*
* **Run-Time Polymorphism** → *Overriding + Virtual Functions (runtime decides).*
