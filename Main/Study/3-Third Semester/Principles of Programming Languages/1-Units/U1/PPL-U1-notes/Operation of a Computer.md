#PPL #third-semester 


> **A programming language is a way to tell a computer how to use these six components.**



---

# Operation of a Computer

A computer consists of **six major components**, and every programming language provides features to work with them.

---

# 1. Data

### Definition

Data is the **information stored and processed by a computer**.

A computer must be able to store different kinds of data.

Examples:

* Integer
* Float
* Character
* Boolean
* Arrays
* Objects

### Example

```cpp
int age = 20;
float salary = 5000.5;
char grade = 'A';
```

Here,

* `20`
* `5000.5`
* `'A'`

are data values.

### Programming Language Feature

Programming languages provide **data types** such as:

* int
* float
* char
* bool

---

# 2. Primitive Operations

### Definition

Primitive operations are the **basic operations performed on data**.

Examples:

* Addition (+)
* Subtraction (-)
* Multiplication (*)
* Division (/)
* Comparison (<, >, ==)

### Example

```cpp
int c = a + b;
```

Here

```text
+
```

is a primitive operation.

### Programming Language Feature

Programming languages provide

* Arithmetic operators
* Logical operators
* Relational operators

---

# 3. Sequence Control

### Definition

Sequence control determines **the order in which statements are executed**.

Without sequence control, the computer would not know what to execute first.

### Example

```cpp
x = 10;
y = 20;
z = x + y;
```

The statements execute in order.

Programming languages also provide

```cpp
if
switch
for
while
do-while
```

to change the order of execution.

---

# 4. Data Access

### Definition

Data access means **obtaining the required data before performing an operation and storing the result afterward**.

Simply,

> **Read data → Process data → Store result**

### Example

```cpp
cin >> age;
```

The program accesses user input.

Another example

```cpp
sum = a + b;
```

The CPU accesses `a` and `b` from memory before performing addition.

### Programming Language Feature

* Variables
* Arrays
* Pointers
* Input/Output statements

---

# 5. Storage Management

### Definition

Storage management controls **how memory is allocated, used, and released**.

### Example

```cpp
int x;
```

Memory is allocated for `x`.

Another example

```cpp
new Student();
```

Memory is dynamically allocated.

Later,

```cpp
delete p;
```

Memory is released.

### Programming Language Feature

* Variable declaration
* Dynamic memory allocation (`new`, `malloc`)
* Garbage collection (Java, Python)

---

# 6. Operating Environment

### Definition

The operating environment provides communication between the program and the outside world.

Examples

* Keyboard
* Mouse
* File
* Printer
* Internet
* Operating System

### Example

```cpp
cin >> name;
```

Reads from keyboard.

```cpp
ofstream file("abc.txt");
```

Writes to a file.

### Programming Language Feature

* File handling
* Input/Output
* Networking
* System calls

---

# Summary Table

| Component                 | Meaning                               | Example                             |
| ------------------------- | ------------------------------------- | ----------------------------------- |
| **Data**                  | Information stored by the computer    | `int`, `float`, `char`              |
| **Primitive Operations**  | Basic operations on data              | `+`, `-`, `*`, `/`, `==`            |
| **Sequence Control**      | Controls execution order              | `if`, `for`, `while`                |
| **Data Access**           | Reads and writes data                 | `cin`, variables, arrays            |
| **Storage Management**    | Allocates and deallocates memory      | `new`, `delete`, garbage collection |
| **Operating Environment** | Communicates with external devices/OS | File handling, keyboard, printer    |

---

# Easy Memory Trick

Remember:

**D P S D S O**

👉 **"Data Performs Sequential Data Storage Operations"**

or simply:

* **D** = Data
* **P** = Primitive Operations
* **S** = Sequence Control
* **D** = Data Access
* **S** = Storage Management
* **O** = Operating Environment

---

# Exam Answer (5 Marks)

**Q. Explain the six major components involved in the operation of a computer.**

**Ans:**

1. **Data:** Stores information such as integers, characters, and arrays.
2. **Primitive Operations:** Performs basic operations like arithmetic and comparison.
3. **Sequence Control:** Determines the order in which instructions are executed using control statements.
4. **Data Access:** Retrieves data for processing and stores the results.
5. **Storage Management:** Allocates and manages memory for programs and data.
6. **Operating Environment:** Provides communication with external devices, files, and the operating system.

These six components correspond closely to the major aspects of **programming language design**, since every programming language provides features to represent data, perform operations, control execution, access data, manage memory, and interact with the external environment.
