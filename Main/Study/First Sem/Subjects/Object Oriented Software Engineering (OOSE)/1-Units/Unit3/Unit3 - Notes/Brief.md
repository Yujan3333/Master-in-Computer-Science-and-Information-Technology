 **Unit 3: Architecture, Real-Time Systems, Databases, Components, and Testing** based on Ivar Jacobson’s Object-Oriented Software Engineering (OOSE) method.

---

## ✅ **1. Architecture (Model Architecture)**

Jacobson’s approach uses **five models** that evolve over time to build the system:

|Model Type|What It Does|
|---|---|
|**Requirements Model**|Defines what the system must do using **use cases** (user scenarios).|
|**Analysis Model**|Identifies key **objects** (Entity, Boundary, Control) and their relationships.|
|**Design Model**|Turns the analysis into a **detailed plan** using technology and patterns.|
|**Implementation Model**|Converts the design into **real code and files**.|
|**Test Model**|Describes how to **test** the system based on use cases.|

🔁 These models work together and evolve throughout the project. This structure is called the **model architecture**.

---

## ✅ **2. Analysis**

- The goal is to **understand the problem** deeply.
    
- Focus is on **what the system must do**, not how.
    
- Use **use cases** to guide the analysis.
    
- Identify:
    
    - **Entity objects** (hold data)
        
    - **Boundary objects** (interface with users/systems)
        
    - **Control objects** (handle workflows/processes)
        

---

## ✅ **3. Construction (Implementation)**

- Now we build the system (coding).
    
- The **design is turned into real classes and code**.
    
- Follow OOP principles: **encapsulation, inheritance, polymorphism**.
    
- Implementation reflects the **design model** closely.
    

---

## ✅ **4. Real-Time Systems**

Although Jacobson’s book doesn't go deep into real-time systems, OOAD can still support them:

|Type|Meaning|Example|
|---|---|---|
|**Hard Real-Time**|Must meet deadlines or failure occurs|Flight control|
|**Soft Real-Time**|Missing deadline causes delay, not disaster|Video streaming|
|**Firm Real-Time**|Missing deadline makes output useless|Stock trading|

➡️ Use **control objects**, **message timing**, and **state diagrams** to model time-sensitive behavior.

---

## ✅ **5. Database (RDBMS vs Object DBMS)**

- **RDBMS (Relational Database)**: Most systems use this; store data in tables.
    
    - Use **Object-Relational Mapping (ORM)** to convert objects to rows and columns.
        
- **Object DBMS**: Store objects directly (less common).
    
    - No mapping needed; but limited adoption.
        
- Jacobson’s method includes a **persistence layer** to manage how objects are stored in databases.
    

---

## ✅ **6. Components**

- **Component** = A group of objects with a clear job and interface.
    
- Components help in:
    
    - **Reusability**
        
    - **Modularity**
        
    - **Independent development**
        
- Tools like **version control** and **component libraries** help manage components.
    
- Design Model helps group classes into components.
    

---

## ✅ **7. Testing**

Testing is done throughout the process and is **use case-driven**.

|Level|What It Tests|
|---|---|
|**Unit Testing**|Tests single objects (e.g., class methods)|
|**Integration Testing**|Tests object interaction (e.g., object A calls object B)|
|**System Testing**|Tests the full system based on requirements|

- **Test cases come from use cases** (great for traceability).
    
- The **Test Model** describes test plans, cases, and results.
    

---

## 🧠 Final Summary (Quick Map)

```
Use Cases → Analysis Model → Design Model → Code (Implementation) → Testing
    ↓             ↓                ↓                 ↓              ↓
Requirements  Objects + Logic   Architecture    Classes + Files   Test Cases
```

