
## ✅ **Models in Ivar Jacobson’s Objectory Methodology (Model Architecture)**

Objectory structures software development into **interconnected models**, each representing a specific **view** of the system. These together form the **model architecture** in OOSE.

---

### 🔷 1. Requirements Model

- **Purpose**: Capture what the system should do — from the user's perspective.
    
- **Key Elements**:
    
    - **Use cases** (e.g., “Place Order”, “Login”)
        
    - **Actors** (e.g., Customer, Admin)
        
    - Supplementary specs (non-functional requirements)
        
- **Role in Architecture**: **Foundation** — defines system behavior from the outside.
    

---

### 🔷 2. Analysis Model

- **Purpose**: Understand the **problem domain** in an object-oriented way.
    
- **Key Elements**:
    
    - **Boundary objects** (UI & system interfaces)
        
    - **Entity objects** (core data, e.g., Customer, Order)
        
    - **Control objects** (use-case logic controllers)
        
- **Role in Architecture**: Defines the **logical architecture** — system behavior and structure, abstracted from technology.
    

---

### 🔷 3. Design Model

- **Purpose**: Convert analysis into a **detailed, technical design** for implementation.
    
- **Key Elements**:
    
    - Refined classes, interfaces
        
    - Framework & utility classes
        
    - Subsystems, layers, design patterns
        
- **Role in Architecture**: Forms the **concrete architecture** — a blueprint for coding.
    

---

### 🔷 4. Implementation Model _(Construction Phase)_

- **Purpose**: **Build the system** — translate design into executable code.
    
- **Key Elements**:
    
    - Source code (classes, methods)
        
    - Packages, modules, deployment units
        
- **Role in Architecture**: **Physical architecture** — shows how the system is realized in code.
    

---

### 🔷 5. Test Model

- **Purpose**: **Verify and validate** the system.
    
- **Key Elements**:
    
    - Test cases derived from use cases
        
    - Unit, integration, and system tests
        
    - Test scripts and reports
        
- **Role in Architecture**: Ensures **quality** — links to all other models by testing their outputs.
    

---

## 🧠 Visual Summary Table:

|Model|Purpose|Key Artifacts|Role in Architecture|
|---|---|---|---|
|Requirements|What the system should do|Use Cases, Actors, Specs|External Behavior/Foundation|
|Analysis|Understand the problem domain|Boundary, Entity, Control Objects|Logical Architecture|
|Design|Plan the implementation|Refined Classes, Interfaces, Layers|Concrete Software Architecture|
|Implementation|Build the system (code)|Source Code, Modules, Components|Physical Architecture|
|Test|Validate and verify|Test Cases, Scripts, Results|Quality Assurance|

---

## ✍️ In Exams You Can Say:

> In Ivar Jacobson’s Objectory methodology, software is developed through a set of structured models: the **Requirements Model** defines external behavior using use cases; the **Analysis Model** defines object-based logic; the **Design Model** maps that logic to a concrete technical architecture; the **Implementation Model** constructs the working code; and the **Test Model** ensures the system meets expectations. These models together form the **model architecture** of Object-Oriented Software Engineering.
