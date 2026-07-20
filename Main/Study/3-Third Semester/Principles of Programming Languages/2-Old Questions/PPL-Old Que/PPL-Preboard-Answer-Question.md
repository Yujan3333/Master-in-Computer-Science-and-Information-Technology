#old-que #third-semester #PPL 

# **1. Define Syntax and Semantics. Explain different stages in language translation.**

### **Ans:**

### **Syntax**

Syntax is the set of rules that defines the correct structure or grammar of a programming language.

**Example:**

```c
int a = 10;   // Correct
int = a 10;   // Incorrect
```

### **Semantics**

Semantics refers to the meaning of a syntactically correct program.

---

### **Stages of Language Translation**

1. **Lexical Analysis** – Converts source code into tokens.
2. **Syntax Analysis** – Checks grammar and creates a parse tree.
3. **Semantic Analysis** – Checks meaning, data types, and declarations.
4. **Intermediate Code Generation** – Produces intermediate code.
5. **Code Optimization** – Improves code efficiency.
6. **Code Generation** – Produces machine/assembly code.
7. **Symbol Table Management** – Stores information about identifiers.
8. **Error Handling** – Detects lexical, syntax, and semantic errors.

---

# **2. Discuss Type Equivalence. Explain different storage management techniques.**

### **Ans:**

### **Type Equivalence**

Type equivalence determines whether two data types are considered the same.

**Types:**

* **Name Equivalence:** Types are equivalent only if they have the same declared name.
* **Structural Equivalence:** Types are equivalent if they have the same structure.

---

### **Storage Management Techniques**

1. **Static Storage Allocation**

   * Memory allocated before execution.
   * Exists throughout the program.

2. **Stack Storage Allocation**

   * Stores local variables and function calls.
   * Memory is automatically allocated and released.

3. **Heap Storage Allocation**

   * Dynamic memory allocation during execution.
   * Used with `malloc()` or `new`.

---

# **3. What are the benefits of using inheritance? What is an abstract class? Compare compile-time polymorphism with run-time polymorphism.**

### **Ans:**

### **Benefits of Inheritance**

* Code reusability.
* Reduces code duplication.
* Easier maintenance.
* Supports hierarchical relationships.

---

### **Abstract Class**

An abstract class is a class that **cannot be instantiated** and contains one or more abstract methods that must be implemented by subclasses.

---

### **Compile-Time vs Run-Time Polymorphism**

| Compile-Time        | Run-Time                 |
| ------------------- | ------------------------ |
| Early binding       | Late binding             |
| Method overloading  | Method overriding        |
| Faster              | Slower                   |
| Decided by compiler | Decided during execution |

---

# **4. What do you mean by language standardization and language internationalization?**

### **Ans:**

### **Language Standardization**

It is the process of defining official rules and specifications for a programming language to ensure consistency and portability.

### **Language Internationalization**

It is the process of designing software so it can support multiple languages and regions without changing the source code.

---

# **5. How do programming environments affect language design?**

### **Ans:**

Programming environments influence language design by providing tools and facilities for software development.

**Effects:**

* Better IDE support.
* Easier debugging.
* Improved portability.
* Rich libraries and frameworks.
* Faster software development.

---

# **6. What do you mean by hierarchies of virtual machines?**

### **Ans:**

A **Virtual Machine (VM)** provides an abstraction between hardware and applications.

**Hierarchy:**

```text
Application
     ↓
High-Level Language
     ↓
Compiler/Interpreter
     ↓
Virtual Machine
     ↓
Operating System
     ↓
Hardware
```

**Advantages:**

* Platform independence.
* Security.
* Portability.
* Automatic memory management.

---

# **7. Explain attribute grammar along with its use in the design of programming languages.**

### **Ans:**

An **Attribute Grammar** is a context-free grammar with attributes and semantic rules used to describe the meaning of programs.

**Types:**

* **Synthesized Attributes** – Computed from child nodes.
* **Inherited Attributes** – Passed from parent or sibling nodes.

**Uses:**

* Type checking.
* Semantic analysis.
* Syntax-directed translation.
* Intermediate code generation.

---

# **8. What is binding and binding time? Explain different classes of binding times.**

### **Ans:**

### **Binding**

Binding is the association between a program entity (such as a variable or function) and its property (such as type, value, or memory location).

### **Binding Time**

Binding time is the time at which the binding occurs.

### **Classes of Binding Time**

1. **Language Design Time** – Language features are decided.
2. **Language Implementation Time** – Compiler implementation decisions.
3. **Compile Time** – Variable types and memory locations are determined.
4. **Link Time** – Program modules are linked together.
5. **Load Time** – Memory addresses are assigned when the program loads.
6. **Run Time** – Dynamic bindings occur during program execution.
