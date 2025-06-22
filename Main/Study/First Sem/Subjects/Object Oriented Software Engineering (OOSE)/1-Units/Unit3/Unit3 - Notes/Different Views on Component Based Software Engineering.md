## 💡 1. **Object-Oriented View**

> **Think in terms of objects and classes (like in Java, C++, or Python).**

### ✅ What it means:

- A **component is made up of one or more classes** that work together.
    
- These classes could be:
    
    - **Problem domain classes**: Deal with the business logic or the real-world part of the system (e.g., `Order`, `Customer`).
        
    - **Infrastructure classes**: Help with the technical parts (e.g., database handling, networking).
        
- The component **encapsulates** these classes—meaning you only interact with the component, not the individual classes inside.
    

### 🧠 Example:

- A **"Payment Processing"** component may contain:
    
    - `PaymentValidator` class (problem domain)
        
    - `TransactionLogger` class (infrastructure)
        
    - `PaymentGatewayAdapter` class (infrastructure)
        

> These classes work together and are hidden inside one component.

---

## 💡 2. **Conventional View**

> **Think in terms of traditional modules or functions, like in C or older software designs.**

### ✅ What it means:

- A **component is like a function or module** with a clear purpose.
    
- It has:
    
    - **Internal logic** (what it does)
        
    - **Data structures** it uses internally
        
    - **Interfaces** so that other parts of the software can call it and send data to it.
        

> This is similar to old-school modular programming but with more formality.

### 🧠 Example:

- A component for **“Math operations”** might include:
    
    - Functions like `add(x, y)` and `multiply(x, y)`
        
    - Internal logic for how it performs those calculations
        
    - Other modules can use it by calling these functions through its interface.
        

---

## 💡 3. **Process-Related View**

> **Think in terms of reusable components stored in a library or marketplace.**

### ✅ What it means:

- Components are **pre-built**, **stored in libraries** (called repositories), and **reused** in many projects.
    
- These are often **GUI elements** or **standard utilities**.
    
- Focus is on **reusability** and **easy retrieval**.
    

### 🧠 Example:

- In a library of UI components, you might find:
    
    - A **Button** component
        
    - A **TextField** component
        
    - A **DataGrid** component
        

### 📌 Summary Table:

|View|What is a component?|Focus|Example|
|---|---|---|---|
|Object-Oriented View|Set of cooperating classes (domain + technical)|**Encapsulation** of logic|PaymentProcessing with multiple classes|
|Conventional View|Module/function with data and interface|**Functionality** + data|MathOperations module|
|Process-Related View|Pre-built reusable software in libraries|**Reuse** from libraries|UI Button or Grid component|