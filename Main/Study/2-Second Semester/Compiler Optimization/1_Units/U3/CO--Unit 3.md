### Loop Overheads
Software
- Initialize Counter
- Increment/Decrement
- Test and Branch
Hardware
- Finite State Machine (FSM)
- Condition Check
- Extra Cycles for R/W memory
---
### Loop Induction Variable
- It is a kind of variable that is increased or decreased by a fixed amount on every iteration of a loop.

---
### Induction Variable Optimization
- Reducing the computation by introducing loop?

---
### [Preliminary Transformation](CO--u3/Preliminary%20Transformation.md)
- Usually we don't make program while keeping the **dependence test** in mind.
- The number of *transformation* done prior to the dependence test (*goal is to make the testing more accurate*) is known as **Preliminary Transformation**

---
### [Induction Variable Substitution](CO--u3/Induction%20Variable%20Substitution.md)

---
### [Loop Normalization](CO--u3/Loop%20Normalization.md)

---
### [Loop Normalization Algorithm](CO--u3/Loop%20Normalization%20Algorithm.md)

---
### Data Flow Analysis

---
### Data Flow properties
1. Available Expression
2. Reaching Definition

---
### [Definition of Use Graph](CO--u3/Definition%20of%20Use%20Graph.md)

- uses(b)
- defsout(b)
- killed(b)

---
### Blocks

---
### Reaches(b)

---
### Dead Code Elimination
#### [Dead Code Elimination Algorithm](CO--u3/Dead%20Code%20Elimination%20Algorithm.md)
---
### Constant Propagation

---
### [Single Static Assignment (SSA)](CO--u3/Single%20Static%20Assignment%20(SSA).md)
- Each use of variable is done by exactly one definition
- Merge Function

---
### Common sub-expression elimination

---
### Forward Substitution