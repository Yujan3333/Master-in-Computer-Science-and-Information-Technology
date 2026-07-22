#PPL #third-semester 


# Unit 2.3: Inheritance 

# 1. Inheritance

## Definition

**Inheritance** is the mechanism by which one class acquires the **properties (data members)** and **methods (functions)** of another class. It promotes **code reuse** and establishes an **"is-a" relationship** between classes.

According to your slides, inheritance means **receiving in one program component the properties or characteristics of another program component because of a special relationship between them.**

---

## Inheritance in Block Structure

Inheritance is not limited to OOP. An early form of inheritance appears in **block-structured programming languages** through **scope rules**.

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

* `i` is **inherited** from the outer block.
* `j` of the outer block is **hidden** because the inner block declares another `j`.
* `k` and inner `j` are local to the inner block.

This demonstrates **scope-based inheritance**.

---

## Inheritance in Object-Oriented Programming

Inheritance is mainly used between **classes**.

If

```
A ⇒ B
```

then

* **A** = Parent class (Superclass/Base class)
* **B** = Child class (Subclass/Derived class)

Objects and methods of **A** become available in **B** unless they are redefined.

Example:

```cpp
class Animal
{
public:
    void eat(){}
};

class Dog : public Animal
{
public:
    void bark(){}
};
```

`Dog` inherits the method `eat()` from `Animal`.

---

## Parent and Child Class

If

```
A ⇒ B
```

then

* A = Parent (Superclass/Base class)
* B = Child (Subclass/Derived class)

A is called the **immediate ancestor** of B.

---

# Types of Inheritance

## Single Inheritance

A child class has **only one parent class**.

```
Animal
   │
 Dog
```

**Example**

```cpp
class Dog : public Animal
```

---

## Multiple Inheritance

A child class inherits from **more than one parent class**.

```
      A
     / \
    B   C
     \ /
      D
```

Example

```cpp
class D : public B, public C
```

**Note**

* Supported in **C++**
* **Not supported directly in Java**

---

# 2. Derived Class

## Definition

A **derived class** is a class created from an existing **base class**.

It inherits:

* Data members
* Member functions

It is also called

* Child class
* Subclass

---

### Characteristics

* Reuses code from the base class.
* Can add new members.
* Can redefine inherited functions.
* Only **public inherited members** are visible to users.

---

## Inheritance Approaches

### a) Copy-Based Inheritance

* Derived object stores **its own copy** of inherited data.
* Every object has separate storage.
* No sharing between base and derived objects.

---

### b) Delegation-Based Inheritance

* Derived object uses the **base object's storage**.
* Data is **shared** instead of copied.
* Changes in the base object may affect the derived object.

---

# 3. Abstract Class

## Definition

An **abstract class** is a class that **cannot be instantiated** (cannot create objects).

It serves only as a **template** or **base class** for other classes.

---

### Java

Declared using

```java
abstract class Shape
```

It may contain

* Abstract methods
* Normal methods

---

### C++

Contains at least one **pure virtual function**.

Example

```cpp
class Shape
{
public:
    virtual void draw() = 0;
};
```

The `=0` indicates a **pure virtual function**.

---

## Why Abstract Class?

* Provides common structure.
* Forces subclasses to implement required methods.
* Prevents creation of incomplete objects.

---

# 4. Objects and Messages

## Object

An **object** is an **instance of a class**.

Objects are created through **instantiation**.

Example

```cpp
Student s1;
```

`s1` is an object.

---

## Instantiation

Instantiation is the **process of creating an object** from a class.

---

## Message

A **message** is a **request sent to an object** asking it to execute one of its methods.

A message contains:

* Method name
* Arguments

Example

```cpp
student.display();
```

Object:

```
student
```

Message:

```
display()
```

When the object receives the message, it invokes the corresponding method.

---

# 5. Polymorphism

## Definition

**Polymorphism** means **"many forms."**

It allows the **same operator or function name** to perform **different operations** depending on the object or data type.

---

## Types of Polymorphism

### A. Compile-Time Polymorphism (Static)

Resolved by the compiler before execution.

Achieved through:

### Function Overloading

Same function name

Different parameter lists

Example

```cpp
sum(int,int)
sum(float,float)
```

---

### Operator Overloading

Operators receive new meanings for user-defined classes.

Example

```
+
-
*
```

```md
Complex1 + Complex2 = Complex3
```

---

### Templates

Templates allow writing **generic functions and classes**.

Example

```cpp
template<class T>
```

One function works for multiple data types.

---

### B. Runtime Polymorphism (Dynamic)

Resolved during program execution.

Achieved through

### Method Overriding

A derived class provides its **own implementation** of a base class method.

Example

```cpp
class Animal
{
public:
    virtual void sound();
};

class Dog : public Animal
{
public:
    void sound();
};
```

The correct method is selected **at runtime**.

---

# Advantages of Inheritance

* Code reuse
* Easy maintenance
* Extensibility
* Supports hierarchical classification
* Reduces code duplication

---

# Advantages of Polymorphism

* Flexibility
* Easy code extension
* Reusability
* Dynamic behavior
* Better maintainability

---

# Important Differences

## Base Class vs Derived Class

| Base Class       | Derived Class         |
| ---------------- | --------------------- |
| Parent class     | Child class           |
| Provides members | Inherits members      |
| Independent      | Depends on base class |

---

## Single vs Multiple Inheritance

| Single        | Multiple         |
| ------------- | ---------------- |
| One parent    | Multiple parents |
| Simple        | Complex          |
| Java supports | C++ supports     |

---

## Compile-Time vs Runtime Polymorphism

| **Compile-Time Polymorphism**                                                      | **Runtime Polymorphism**                                                  |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| ✅ Also called **Static Polymorphism** / *early binding*.                           | Also called **Dynamic Polymorphism**. / *late binding*                    |
| ✅ The method/function is selected **before the program starts running**.           | The method/function is selected **while the program is running**.         |
| ✅The **compiler** decides which function to call.                                  | The **program (runtime system)** decides which method to call.            |
| ✅ Based on the **number and type of parameters**.                                  | Based on the **actual type of the object** at runtime.                    |
| ✅ Achieved through **function overloading, operator overloading, and templates**.  | Achieved through **method overriding** (using virtual methods).           |
| ✅ Faster because no decision is needed during execution.                           | Slightly slower because the decision is made during execution.            |
| Example: `add(2,3)` → calls integer version; `add(2.5,3.5)` → calls float version. | Example: `Animal a = Dog`; `a.sound()` executes `Dog`'s `sound()` method. |
| ✅ Less flexible                                                                    | More Flexible                                                             |



---

# Exam Tips (Very Important)

Remember these one-line definitions:

* **Inheritance:** Mechanism of acquiring properties of another class.
* **Base Class:** Parent class that provides members.
* **Derived Class:** Child class that inherits members.
* **Abstract Class:** Class that cannot be instantiated.
* **Object:** Instance of a class.
* **Instantiation:** Process of creating an object.
* **Message:** Request to invoke an object's method.
* **Polymorphism:** One interface, many forms.
* **Function Overloading:** Same function name with different parameters.
* **Operator Overloading:** Giving new meaning to operators.
* **Method Overriding:** Redefining a base class method in a derived class.


