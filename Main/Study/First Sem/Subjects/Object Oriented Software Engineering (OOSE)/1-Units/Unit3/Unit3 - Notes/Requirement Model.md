- The **Requirement Model** is the **first and most important model** in the Object-Oriented Software Engineering process.

- It describes **what the system should do** — from the **user’s perspective** — without worrying about **how** it will be implemented.


**Mentioned in Notes**
- Problem Domain Objects
- Interface
- Use Case Model

---
## ✅ **1. Problem Domain Objects (Entity Objects)**

### 🔹 **Definition:**

Problem Domain Objects (a.k.a. **Entity Objects**) are objects that represent **real-world, core concepts** of the system. They reflect the **business logic** and **data** the system must handle.

### 🔹 **Purpose:**

- Capture essential **domain knowledge**.
    
- Help create a **logical object-oriented view** of the system.
    
- Remain stable even if interfaces or technologies change.
    

### 🔹 **In Online Bookstore System:**

|Entity|Attributes|Behaviors|
|---|---|---|
|**Book**|Title, Author, ISBN, Price, Stock|`getStock()`, `updatePrice()`|
|**Customer**|Name, Email, Address|`updateProfile()`, `viewOrders()`|
|**Order**|ID, Date, Items, Status|`calculateTotal()`, `changeStatus()`|
|**ShoppingCart**|List of Items, Total|`addItem()`, `checkout()`|

👉 These objects are used in **Analysis Model** to define what the system manages and persists.

---

## ✅ **2. Interface Design (Boundary Objects)**

### 🔹 **Definition:**

Interface Design (linked to **Boundary Objects**) defines **how users interact** with the system through **screens**, **inputs**, and **visual feedback**. It maps **use cases** into **concrete UI behaviors**.

### 🔹 **Purpose:**

- Allow users or systems to **access and interact** with core functionalities.
    
- Ensure the interface is **consistent** with user expectations.
    
- Help developers and stakeholders **visualize** system behavior early.
    

### 🔹 **In Online Bookstore System:**

|Interface|Elements|Related Use Case|
|---|---|---|
|**Search Page**|Search bar, Filters, Results list|Search Book|
|**Book Details**|Title, Price, Add to Cart|View Book Details|
|**Cart Page**|Items, Total, Checkout button|Manage Cart|
|**Login Page**|Email, Password, Login|Login/Register|

👉 These interfaces are designed during **Requirement & Analysis Phase**, often using **UI sketches or mockups** to simulate system behavior.

---

## 🧠 **How They Work Together:**

- **Use Case**: "Place Order"
    
- **Actor**: Customer
    
- **Interface (Boundary Object)**: Cart Page, Checkout Page
    
- **Control Object**: OrderController (handles process flow)
    
- **Entity Objects**: Customer, Order, Book
    

Each **interface** provides access to a **use case**, which internally triggers **control logic** and manipulates **problem domain objects**.

---

## ✍️ Exam-Style Summary:

> In Objectory methodology, the **Analysis Model** identifies:
> 
> - **Problem Domain Objects (Entity Objects)** to represent core business data and logic, and
>     
> - **Interface Design (Boundary Objects)** to define how users interact with the system.
>     
> 
> Using an Online Bookstore System as an example, entities like **Book**, **Order**, and **Customer** hold the business logic, while interfaces like **Search Page**, **Book Details**, and **Cart Page** provide the user-facing side. This approach ensures a consistent and user-focused system design.


----
---
## 🧱 Main Components of the Requirement Model:

### 1. ✅ Use Cases

- Describe **interactions** between a user (actor) and the system.
    
- Each use case represents a **goal** that an actor wants to achieve.
    

**Example:**  
Use case: `Place Order` – a customer selects items, enters delivery info, and confirms the order.

---

### 2. ✅ Actors

- Represent **users or external systems** that interact with the system.
    

**Example:**

- Customer (human user)
    
- Payment Gateway (external system)
    

---

### 3. ✅ Use-Case Diagram

- A **visual representation** showing actors and their related use cases.
    
- Helps stakeholders quickly understand the system behavior.
    

---

### 4. ✅ Supplementary Specifications

- Describes **non-functional requirements**, such as:
    
    - Performance
        
    - Security
        
    - Usability
        
    - Constraints