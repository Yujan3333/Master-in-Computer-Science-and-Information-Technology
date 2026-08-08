# Unit 7: Semantic Web (6 Hrs)

*(Based on: Algorithms of the Intelligent Web – Marmanis & Babenko, and Foundations of Semantic Web Technologies – Hitzler et al.)*

---

## 1. Introduction to the Semantic Web

The **Semantic Web** is an extension of the current Web where information is given **well-defined meaning**, enabling **machines to understand, interpret, and reason** over web data.

### Key Idea

> Make web data **machine-understandable**, not just human-readable.

### Traditional Web vs Semantic Web

* **Traditional Web**: Documents for humans (HTML pages)
* **Semantic Web**: Data for machines (linked, structured, meaningful data)

---

## 2. Why Semantic Web is Needed

Problems with the traditional web:

* Data is unstructured or semi-structured
* Machines cannot understand meaning
* Poor interoperability between systems

Semantic Web enables:

* Intelligent search
* Data integration across domains
* Automated reasoning
* Knowledge sharing

---

## 3. Core Components of the Semantic Web

The Semantic Web is built using layered technologies:

1. **URI (Uniform Resource Identifier)**
2. **RDF (Resource Description Framework)**
3. **RDFS (RDF Schema)**
4. **OWL (Web Ontology Language)**
5. **Logic & Reasoning**
6. **Applications**

---

## 4. Building Models (Knowledge Representation)

### Knowledge Representation

Knowledge is represented as **facts and relationships** using formal models.

### RDF Data Model

* Based on **triples**:

  * **Subject – Predicate – Object**

Example:

* (Nepal, hasCapital, Kathmandu)

This structure forms an **RDF graph**.

### Advantages

* Flexible
* Machine-readable
* Interoperable

---

## 5. Calculating with Knowledge (Reasoning)

### Reasoning

Reasoning allows machines to **infer new knowledge** from existing data.

Example:

* If: Kathmandu isCapitalOf Nepal
* And: Capital isCity
* Then: Kathmandu isCity

### Types of Reasoning

* Deductive reasoning
* Ontological reasoning

Reasoners use **logic rules** to derive implicit facts.

---

## 6. Exchanging Information

Semantic Web supports **data exchange across systems** using common standards.

### Benefits

* Data reuse
* Cross-domain integration
* Platform independence

### Linked Data

* Data published using RDF
* Connected using URIs
* Enables global data graph

---

## 7. Semantic Web Technologies

### a) RDF (Resource Description Framework)

* Basic data model of Semantic Web
* Represents data as triples
* Syntax formats: RDF/XML, Turtle, N-Triples

### Key Features

* Graph-based model
* Uses URIs for global identification

---

### b) RDF Schema (RDFS)

* Provides vocabulary for RDF
* Defines:

  * Classes
  * Properties
  * Hierarchies

Example:

* Class: Person
* Property: hasFriend

---

### c) OWL (Web Ontology Language)

OWL is more expressive than RDF and RDFS.

### Purpose

* Define complex relationships
* Support reasoning

### OWL Variants

* **OWL Lite** – Simple constraints
* **OWL DL** – Balance between expressiveness and decidability
* **OWL Full** – Maximum expressiveness

---

## 8. Ontology

### Definition

An **ontology** is a formal specification of concepts, relationships, and constraints in a domain.

### Components

* Classes
* Properties
* Individuals
* Axioms

### Role in Semantic Web

* Shared understanding
* Interoperability
* Reasoning support

---

## 9. Applications of Semantic Web

* Intelligent search engines
* Recommendation systems
* Knowledge graphs
* Bioinformatics
* E-government systems

---

## 10. Advantages of Semantic Web

* Machine-understandable data
* Better data integration
* Improved search accuracy
* Supports AI and intelligent systems

---

## 11. Limitations / Challenges

* Complexity of ontology creation
* Performance issues at large scale
* Lack of universal adoption
* Data quality issues

---

## 12. Exam-Oriented Short Answers

### Semantic Web

> An extension of the web that enables machines to understand and process data using formal semantics.

### RDF

> A framework for representing web data using subject–predicate–object triples.

### OWL

> A language used to define ontologies with rich semantics and reasoning support.

### Ontology

> A formal representation of knowledge within a domain using concepts and relationships.

---

## 13. Key Terms to Remember

* Semantic Web
* RDF Triple
* Ontology
* Reasoning
* Linked Data
* OWL DL

---

**End of Unit 7 Notes**
