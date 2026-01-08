
## **1️⃣ Definition (Exam Style)**

**RDF (Resource Description Framework):**

> RDF is a **standard framework for representing information about resources on the web**, using a **machine-readable format** that describes relationships between data in the form of **triples**.

---

## **2️⃣ Key Concepts**

1. **Resource**

   * Anything that can be identified on the web, like a webpage, person, book, or concept.
   * Identified by a **URI (Uniform Resource Identifier)**.

2. **Triple**

   * The **basic unit of RDF**.
   * Form: **Subject → Predicate → Object**

     * **Subject:** the resource you’re describing
     * **Predicate:** the property or relationship
     * **Object:** the value or another resource

   **Example:**

   * “John is a student”

     * Subject = John
     * Predicate = is a
     * Object = Student

3. **Graph Structure**

   * RDF data can be represented as a **directed graph**, where:

     * Nodes = Subjects/Objects
     * Edges = Predicates

---

## **3️⃣ Features**

* **Machine-readable:** Allows software to understand data semantics.
* **Extensible:** Can add new data without breaking old data.
* **Standardized:** Recommended by **W3C** for Semantic Web.

---

## **4️⃣ Uses of RDF**

* Linking data across the web (**Linked Data**)
* Storing metadata about resources (like authors, dates, keywords)
* Basis for **OWL** and **SPARQL** in Semantic Web applications

---

💡 **Memory Trick:** Think of RDF as **“subject-property-object”** statements forming a **web of connected facts**.

---
