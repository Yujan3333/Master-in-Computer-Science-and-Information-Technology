what are the main reasons in construction phase ? What is done in construction phase ? Explain

## ✅ **Construction Phase in OOSE**

The **construction phase** is where the system is **actually built and refined**, translating the earlier models into working software. It bridges the gap between **analysis** and **real implementation**.
![](../../../../../../../../Images/First_Sem_Images/Answer%20of%20construction%20phase.png)

---

### 🔷 **Three Main Reasons for the Construction Phase:**

### 🔧 Analysis Model is Not Sufficiently Formal
    
- The analysis model gives a high-level, conceptual view.

- For real implementation, we need more precision:
        
    - What exact operations should objects provide?
            
    - How should objects communicate in detail?
            
- Therefore, the model must be **refined into a formal design**.
        
### 🧱 Adaptation to the Implementation Environment
    
- The analysis assumes an **idealized environment**.
        
- In reality, we must adapt to:
        
    - Programming languages
            
    - Frameworks and platforms
            
    - Performance limitations
            
- Construction ensures that the design fits the **real-world environment**.
        
### ✅ Validation of the Analysis Results
    
- As we begin building the system, we **test the correctness** of the analysis.
        
- If requirements or analysis are unclear, construction helps **reveal and clarify** them.
        
- It acts as a **feedback loop** to refine earlier phases.
        

---

### 🔷 **Models Produced in Construction Phase:**

The construction phase is divided into **two sub-phases**:

#### 1. **Design Model**

- A detailed refinement of the **analysis model**.
    
- Takes into account:
    
    - **Implementation constraints**
        
    - **Component structure**
        
    - **Layered architecture**
        
- Describes **classes, interfaces, interactions**, and **subsystems** in technical detail.
    

#### 2. **Implementation Model**

- Represents the **actual source code**.
    
- Includes:
    
    - Classes, methods, modules
        
    - File/package organization
        
    - Coding of designed behavior
        
- This is where the system is **physically realized**.
    

---

## ✍️ **Summary:**
### ✅ Construction Phase – Key Points

- The **construction phase** bridges the gap between **high-level analysis** and **executable code**.
    
- It is necessary for **three main reasons**:
    
    1. **Analysis model lacks formal precision**  
        → Needs refinement for actual coding (e.g., defining operations, object interactions clearly).
        
    2. **Adaptation to real-world environment**  
        → The ideal assumptions in analysis must be adjusted for real platforms, tools, and constraints.
        
    3. **Validation of analysis results**  
        → Building the system helps reveal unclear or incomplete parts of the requirements and analysis.
        
- The construction phase produces **two main models**:
    
    - **Design Model**:
        
        - A refined, formal version of the analysis model.
            
        - Includes technical structure, subsystems, interfaces, and patterns.
            
    - **Implementation Model**:
        
        - The actual source code and program structure.
            
        - Includes modules, classes, files, and code organization.
            
- The phase ensures the system is:
    
    - **Buildable**
        
    - **Correct**
        
    - **Adapted to its implementation environment**