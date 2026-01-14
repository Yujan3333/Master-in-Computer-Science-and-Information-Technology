## **Flow Control**

**1. Definition**

* **Flow control** regulates how information moves among **accessible objects** in a system.
* A **flow** occurs when a program:

  * **Reads** values from object X
  * **Writes** values into object Y

**2. Purpose**

* Ensures that information does **not leak** from more protected (sensitive) objects to less protected ones.
* Prevents both:

  * **Explicit flows** – direct assignment of data
  * **Implicit flows** – information inferred indirectly through program behavior

**3. Flow Policy**

* Defines **allowed channels** for information movement.
* **Example (simplest policy):**

  * Two classes:

    * **Confidential (C)**
    * **Nonconfidential (N)**
  * All flows are allowed **except** from C → N

---

### **Key Takeaways**

* Flow control is about **protecting sensitive data** during program execution.
* Policies can enforce **which objects can share information**.
* The simplest policy blocks **confidential → nonconfidential** flows.

---
