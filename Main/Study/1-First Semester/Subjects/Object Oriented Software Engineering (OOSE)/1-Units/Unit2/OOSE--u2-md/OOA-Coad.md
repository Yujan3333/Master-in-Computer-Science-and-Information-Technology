### Object-Oriented Analysis (OOA) by Coad and Yourdon

The Coad and Yourdon methodology is an approach to Object-Oriented Analysis (OOA) that focuses on modeling system functionality using object-oriented concepts, primarily aiming to reduce complexity in problem domains.

**Key Aspects:**

- **Motivation:** Developed to tackle more challenging problem domains and provide a consistent representation across analysis, design, and programming.

- **Core Concepts:** Centers on identifying **classes** and **objects**, defining their **attributes**, **services** (methods/operations), and **structures** (like inheritance and whole-part relationships). It also emphasizes communication between objects through **messages**.


- **Five Major Activities (iterative, not sequential):**
    
	1. **Finding Classes & Objects:** Identifying relevant entities in the problem domain.
    
	2. **Identifying Structures:** Recognizing generalization-specialization (inheritance) and whole-part (aggregation/composition) relationships.
    
	3. **Identifying Subjects:** Grouping related classes into logical clusters to manage complexity.
    
	4. **Defining Attributes:** Specifying the data elements for each class/object.
    
	5. **Defining Services:** Detailing the behaviors or operations that objects can perform.

---
### Five Layers of the OOA Model:
	
- The resulting OOA model is structured into a Subject layer, Class & Object layer, Structure layer, Attribute layer, and Service layer.


1. **Subject Identification (Domain Model):**
    
    - Break down the system into subject areas (like modules).
        
    - Helps manage complexity.
        
2. **Class and Object Model:**
    
    - Identify **classes** and **objects** in the real world.
        
    - Specify attributes and relationships.
        
    - Example: `Customer`, `Order`, `Product`.
        
3. **Structure Model:**
    
    - Focuses on **inheritance** and **class hierarchies**.
        
    - Define generalization/specialization (e.g., `Employee` → `Manager`, `Developer`).
        
4. **Behavior Model:**
    
    - Describes how objects behave over time.
        
    - Uses **state diagrams** to show changes in state.
        
5. **Interaction Model:**
    
    - Describes how objects collaborate.
        
    - Uses **data flow** and **message passing** diagrams.

---
### Transition to Design (OOD): 
	
- The design phase (OOD) in Coad/Yourdon extends this analysis model by adding components for Human Interaction, Problem Domain refinement, Task Management, and Data Management.


