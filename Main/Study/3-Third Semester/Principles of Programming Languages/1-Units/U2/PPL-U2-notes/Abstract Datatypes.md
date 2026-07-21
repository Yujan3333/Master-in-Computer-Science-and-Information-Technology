#PPL  #third-semester 

### **Abstract Data Type (ADT) – Short Exam Notes**

#### **Definition**

An **Abstract Data Type (ADT)** is a data type that **encapsulates (hides)** the data representation and provides only the **operations (functions/methods)** to access and manipulate the data.

* **Data representation is hidden.**
* **Only predefined operations are accessible.**
* **Access control** prevents direct modification of internal data.

---

### **Characteristics of ADT**

* Encapsulation of data and operations.
* Data hiding through access control.
* Well-defined interface (operations).
* Implementation can change without affecting the user.
* Improves modularity and security.

---

## **Built-in Types as ADTs**

Built-in data types (e.g., `int`, `float`, `char`) are also **Abstract Data Types**.

**Example: Float**

* Stores floating-point values.
* Supports operations like `+`, `-`, `*`, `/`.
* User **cannot access or modify** the internal memory representation.
* Different systems may use different internal representations.

---

## **User-defined Types as ADTs**

A programmer can create an ADT (e.g., `Stack`, `Queue`, `BankAccount`).

Features:

* Internal representation is hidden.
* Only defined methods can access the data.
* Type declaration and operations are kept together.
* Users create objects and use only the provided interface.

---

### **Example (Stack ADT)**

```text
Data (Hidden):
    items[]

Operations:
    push()
    pop()
    peek()
    isEmpty()
```

The user can call `push()` or `pop()`, but **cannot directly access** the internal array.

---

### **Advantages of ADT**

* Hides implementation details.
* Improves security.
* Makes programs easier to maintain.
* Promotes code reuse.
* Reduces errors.
* Allows implementation changes without affecting user programs.

---

## **Exam Questions**

### **Q. What is an Abstract Data Type (ADT)?**

**Ans:**
An Abstract Data Type (ADT) is a data type that hides its internal data representation and provides only a set of operations to manipulate the data through a well-defined interface.

---

### **Q. Why are built-in data types considered ADTs?**

**Ans:**
Because their internal representation is hidden from the programmer, and they can only be accessed using the operations provided by the programming language.

---

### **Q. What are the characteristics of a user-defined ADT?**

**Ans:**

* Data hiding
* Encapsulation
* Well-defined interface
* Hidden implementation
* Objects accessed only through defined operations

---

### **Q. Give examples of ADTs.**

**Ans:**

* Stack
* Queue
* List
* Bank Account
* Floating-point (`float`) type

---

### **One-line Definition (2 Marks)**

**Abstract Data Type (ADT):** A data type that hides its implementation and allows access only through a defined set of operations.
