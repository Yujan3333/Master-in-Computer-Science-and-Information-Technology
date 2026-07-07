#old-que #PPL #third-semester #exam-paper-answer 

# What is Message Binding?

In OOP, a **message** means a **method call**.

For example,

```cpp
obj.display();
```

Here,

* **Message:** `display()`
* **Receiver:** `obj`

**Message binding** is the process of deciding **which method should be executed** when a method is called.

---

# Two Types of Message Binding

```text
           Message Binding
                  |
      ------------------------
      |                      |
Compile-Time           Run-Time
(Static Binding)      (Dynamic Binding)
```

---

# 1. Compile-Time Message Binding (Static Binding)

## Definition

The method to be executed is determined **during compilation**, before the program runs.

It is also called:

* Early Binding
* Static Binding

---

## When does it happen?

* Function Overloading
* Operator Overloading
* Non-virtual functions in C++

The compiler already knows which function to call.

---

## Example (Function Overloading)

```cpp
class Demo {
public:
    void show() {
        cout << "No parameter";
    }

    void show(int x) {
        cout << "Integer parameter";
    }
};

int main() {
    Demo d;
    d.show();
    d.show(10);
}
```

### Compiler Decision

When the compiler sees:

```cpp
d.show();
```

it binds it to:

```cpp
show()
```

When it sees:

```cpp
d.show(10);
```

it binds it to:

```cpp
show(int)
```

This decision is made **before execution**.

---

## Diagram

```text
Source Code
      |
Compiler
      |
Chooses Correct Function
      |
Executable
```

---

## Characteristics

* Binding occurs during compilation.
* Faster execution.
* No runtime overhead.
* Used in **compile-time polymorphism**.

---

# Compile-Time Polymorphism

Compile-time polymorphism means the compiler decides which method to call.

Examples:

* Function Overloading
* Operator Overloading

---

# 2. Run-Time Message Binding (Dynamic Binding)

## Definition

The method to execute is determined **while the program is running**.

Also called:

* Late Binding
* Dynamic Binding

---

## When does it happen?

Occurs with:

* Method Overriding
* Virtual Functions (C++)

The compiler cannot determine the exact method in advance.

---

## Example (Virtual Function)

```cpp
class Animal {
public:
    virtual void sound() {
        cout << "Animal sound";
    }
};

class Dog : public Animal {
public:
    void sound() override {
        cout << "Bark";
    }
};

int main() {
    Animal* a = new Dog();
    a->sound();
}
```

---

### What Happens?

During compilation:

The compiler only knows:

```cpp
Animal* a;
```

It does **not** know whether `a` will point to:

* Animal
* Dog
* Cat

During execution:

```cpp
a = new Dog();
```

Now the object is actually a **Dog**.

Therefore,

```cpp
a->sound();
```

calls

```cpp
Dog::sound()
```

The decision is made **at runtime**.

---

## Diagram

```text
Compile Time

Animal* a

↓

Runtime

a → Dog Object

↓

Dog::sound()
```

---

## Characteristics

* Binding occurs during execution.
* Supports inheritance.
* Supports method overriding.
* Slightly slower because the decision is made at runtime.
* Used in **run-time polymorphism**.

---

# Run-Time Polymorphism

Run-time polymorphism means the actual method is selected while the program is running.

Examples:

* Method Overriding
* Virtual Functions

---

# Comparison

| Feature          | Compile-Time Binding                       | Run-Time Binding                     |
| ---------------- | ------------------------------------------ | ------------------------------------ |
| Also called      | Static Binding / Early Binding             | Dynamic Binding / Late Binding       |
| Binding Time     | During compilation                         | During execution                     |
| Decision made by | Compiler                                   | Runtime system                       |
| Polymorphism     | Compile-time polymorphism                  | Run-time polymorphism                |
| Examples         | Function overloading, Operator overloading | Method overriding, Virtual functions |
| Speed            | Faster                                     | Slightly slower                      |

---

# Easy Memory Trick

### Compile-Time Binding

Think:

```text
Compiler already knows
↓

Which function to call
```

Examples:

```text
Function Overloading

Operator Overloading
```

---

### Run-Time Binding

Think:

```text
Compiler doesn't know

↓

Actual object decides

↓

Virtual Function
```

Examples:

```text
Method Overriding

Virtual Functions
```

---

# Exam Answer (3–5 Marks)

**Message binding** is the process of associating a method call (message) with the actual method that will be executed.

There are two types:

1. **Compile-Time (Static/Early) Binding:** The compiler determines which method to call during compilation. It is used in **compile-time polymorphism**, such as **function overloading** and **operator overloading**.

2. **Run-Time (Dynamic/Late) Binding:** The method is selected during program execution based on the actual object. It is used in **run-time polymorphism**, such as **method overriding** with **virtual functions**.

### One-Line Memory Trick

* **Compile-Time Polymorphism = Static/Early Binding = Overloading**
* **Run-Time Polymorphism = Dynamic/Late Binding = Overriding + Virtual Functions**
