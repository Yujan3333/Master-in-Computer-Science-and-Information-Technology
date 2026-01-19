## **Role of Concept Hierarchies in Data Mining**

**Definition:**
A **concept hierarchy** organizes data attributes into **multiple levels of abstraction**, from detailed to generalized forms.

**Purpose:**

* Helps in **data summarization** and **generalization**
* Reduces complexity and improves pattern discovery
* Enables **multi-level mining**: find patterns at different granularity levels

**Example:**

* Attribute: `Location`
* Concept hierarchy:

  ```
  City → State → Country
  Pokhara → Gandaki → Nepal
  Dhangadi → Sudurpashchim → Nepal
  ```
* In mining sales data:

  * Instead of analyzing city-level sales only, you can **aggregate by state or country**.
  * Enables patterns like: *“Sales of TVs are high in Gandaki province.”*

**Another Example:**

* Attribute: `Time`

  ```
  Day → Month → Quarter → Year
  ```
* Patterns can be discovered at monthly, quarterly, or yearly levels.

---

### **Exam-ready Summary**

* **Data Mining Primitives:** Commands or specifications that define the **what, where, and how** of a data mining task.
* **Concept Hierarchies:** Provide **levels of abstraction** for attributes, enabling generalized pattern discovery and multi-level mining.

---
