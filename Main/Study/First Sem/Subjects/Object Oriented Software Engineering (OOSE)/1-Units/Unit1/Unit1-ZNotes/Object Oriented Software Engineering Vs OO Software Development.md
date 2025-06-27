- [Practical Example](#Practical%20Example.md)

## Easy points
| **Point**            | **OOSE (Object-Oriented Software Engineering)** | **OOSD (Object-Oriented Software Development)**   |
| -------------------- | ----------------------------------------------- | ------------------------------------------------- |
| **1. Focus**         | Full software process (plan to maintenance)     | Mainly on coding and implementation               |
| **2. Tools Used**    | UML, diagrams, models                           | Programming languages (Java, Python, C++)         |
| **3. Main Activity** | Project planning, analysis, design              | Writing code using OO principles                  |
| **4. Who Uses It**   | Software engineers and architects               | Software developers and programmers               |
| **5. Goal**          | Build high-quality, reusable systems            | Create working software using classes and objects |
|                      |                                                 |                                                   |

- *Focus* on *Main Activities* to get to *Goal* using some *Tools*. But *Who uses it* Really?
---

| Concept      | **OOSE (Object-Oriented Software Engineering)**                                                                                           | **OOSD (Object-Oriented Software Development)**                                                                           |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Focus**    | Emphasizes **methodology**, **process**, **tools**, and **management** of object-oriented software projects.                              | Focuses on the **coding**, **design**, and **implementation** of object-oriented programs.                                |
| **Scope**    | Broad – covers entire software life cycle including planning, requirement analysis, design, testing, and maintenance using OO principles. | Narrower – mainly involves the **technical process** of building software using OO languages like Java, C++, Python, etc. |
| **Involves** | Project management, modeling (like UML), design methodologies, software quality, reuse, and documentation.                                | Class design, object interaction, inheritance, encapsulation, and code implementation.                                    |
| **Used By**  | Software engineers and architects who plan and manage the software engineering process.                                                   | Developers and programmers who build object-oriented applications.                                                        |

---

## Practical Example
###  Practical Example: "E-Commerce System"

Let’s design an online store (e.g., Amazon) using OOSE/OOSD:

#### **Step 1: OOSE (Design Phase)**

- **Abstraction:** Identify core objects:

```md
- User (Customer, Admin)
- Product
- Order
- ShoppingCart
- Payment
```

- **Encapsulation:** Hide internal details (e.g., `Payment.process()` hides card details).
    
- **Inheritance:** `Customer` and `Admin` inherit from `User`.
    
- **Polymorphism:** `Payment` can be `CreditCard`, `PayPal`, etc.

#### **Step 2: OOSD (Implementation Phase)**

**Java Code Snippet:**
```md
// Abstraction & Encapsulation
class Product {
    private String id;
    private double price;
    // Getters/setters (encapsulation)
}

// Inheritance
class User {
    protected String email;
}
class Customer extends User {  // Customer IS-A User
    private ShoppingCart cart;
}

// Polymorphism
interface Payment {
    void process();
}
class CreditCard implements Payment {
    public void process() { System.out.println("Paid via Card"); }
}
```
![](../../../../../../../../Images/First_Sem_Images/Object%20Oriented%20Software%20Engineering%20Vs%20OO%20Software%20Development-fig.png)