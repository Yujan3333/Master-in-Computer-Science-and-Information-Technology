
## 1️⃣ Introduction to Object-Oriented Databases

### 🔹 Traditional Database Models

Before OODB, databases were:

* **Hierarchical** (tree structure)
* **Network** (graph structure)
* **Relational** (tables – rows & columns)

👉 Relational DBs worked well for business data but **failed for complex applications**.

---

### 🔹 Why Object-Oriented Databases were created?

Because modern applications needed to store:

* Images
* Videos
* Engineering designs
* CAD/CAM data
* Multimedia
* Complex relationships

Also:

* Programming languages became **object-oriented** (Java, C++)
* Mismatch between **OOP programs and relational tables**

👉 Solution: **Object-Oriented Databases**

---

### 🔹 What is an Object-Oriented Database?

An **OODB** stores data as **objects**, just like in OOP.

✔ Keeps **real-world object → database object** mapping
✔ Objects have **data + behavior**

---

## 2️⃣ Overview of Object-Oriented Concepts

---

### 🔹 Object

An **object** has:

1. **State** → data / values
2. **Behavior** → operations / methods

👉 Example:

```
Student Object
State: name, roll, marks
Behavior: calculateResult(), updateMarks()
```

---

### 🔹 Why OODB is better than RDB?

| Relational DB            | Object-Oriented DB        |
| ------------------------ | ------------------------- |
| Data split across tables | Data stored as one object |
| No behavior              | Data + behavior           |
| Identity via primary key | System-generated OID      |

---

### 🔹 Object Structure

* Objects can be **simple or very complex**
* Can contain other objects

👉 In RDB: complex object → many tables
👉 In OODB: complex object → **single object**

---

### 🔹 Instance Variables

* Similar to attributes
* Store object state
* **Encapsulated** (hidden)

---

## 3️⃣ Encapsulation, Methods & Interfaces

---

### 🔹 Encapsulation (VERY IMPORTANT)

Encapsulation means:

> Hiding internal data and allowing access only through methods

✔ Improves security
✔ Improves maintainability

---

### 🔹 Operation Structure

An operation has two parts:

1. **Signature (Interface)** – name + parameters
2. **Method (Body)** – implementation

---

### 🔹 Interface

* Defines **only behavior**
* Not instantiable
* Used for inheritance

👉 Example:

```
Interface Shape
   area()
   perimeter()
```

---

### 🔹 Class

* Defines **state + behavior**
* Instantiable
* Objects are created from classes

👉 Example:

```
Class Circle
   radius
   area()
```

---

### 🔹 Message Passing

* Operations are invoked by **sending messages**
* Object executes corresponding method

---

### 🔹 Polymorphism (Operator Overloading)

Same operation name → different behavior

Example:

* `+` for integers → addition
* `+` for strings → concatenation

---

## 4️⃣ Object Identity (OID)

---

### 🔹 Object Identity

Each object has a **unique system-generated identifier (OID)**

✔ Independent of values
✔ Never changes (immutable)

---

### 🔹 Identity vs Equality (Exam Favorite)

* **Identical objects** → same OID
* **Equal objects** → same values but different OIDs

👉 Two employees with same data ≠ same object

---

## 5️⃣ Type Constructors (Very Important)

Used to build **complex objects**

---

### 🔹 Basic Type Constructors

1. **Atom** – basic values
   Example: integer, string, boolean

2. **Tuple (Struct)** – ordered collection
   Example:

   ```
   <name, age, salary>
   ```

3. **Collection** - set list dictionary
- **Set** – unordered, no duplicates
   Example:

   ```
   {Kathmandu, Pokhara}
   ```

---

### 🔹 Collection Constructors

| Constructor    | Description         |
| -------------- | ------------------- |
| Set            | No duplicates       |
| Bag (Multiset) | Duplicates allowed  |
| List           | Ordered, unlimited  |
| Array          | Ordered, fixed size |
| Dictionary     | Key-value pairs     |

---

### 🔹 User Defined Types (UDTs)

* Complex types built using constructors
* Used to represent real-world objects

---

## 6️⃣ Encapsulation & Object Persistence

---

### 🔹 Object Persistence

Persistence = object exists **even after program ends**

---

### 🔹 How Persistence is Achieved?

1. **Naming**

   * Object given a persistent name
2. **Reachability**

   * Object reachable from another persistent object

👉 If object is reachable → it is persistent

---

### 🔹 Difference from Relational DB

| Relational DB        | OODB                               |
| -------------------- | ---------------------------------- |
| All data persistent  | Objects can be transient           |
| Tables always stored | Must define persistent collections |

---

## 7️⃣ Type & Class Hierarchies and Inheritance

---

### 🔹 Type Hierarchy

Organizing types into **supertype–subtype** structure

---

### 🔹 Subtype

* Inherits attributes & methods
* Adds new features

---

### 🔹 Example (Very Important)

```
PERSON
 ├── EMPLOYEE
 └── STUDENT
```

EMPLOYEE adds: Salary, HireDate
STUDENT adds: Major, GPA

---

### 🔹 Inheritance Advantages

✔ Code reuse
✔ Natural modeling
✔ Easy maintenance

---

### 🔹 Extents

* Collection of all persistent objects of a type

| Type     | Extent               |
| -------- | -------------------- |
| EMPLOYEE | All employee objects |

---

### 🔹 Persistent vs Transient Collections

| Persistent         | Transient |
| ------------------ | --------- |
| Stored permanently | Temporary |
| Shared             | Local     |

---

## 8️⃣ Complex Objects

---

### 🔹 Unstructured Complex Objects

* Stored as BLOBs
* DB doesn’t understand structure

Examples:

* Images
* Videos
* Documents

---

### 🔹 Structured Complex Objects

* Structure known to DB
* Built using type constructors
* Methods supported

👉 OODB supports this well

---

## 9️⃣ Other Object-Oriented Concepts

---

### 🔹 Multiple Inheritance

* One subtype inherits from **multiple supertypes**

Example:

```
ENGINEERING_MANAGER
   inherits MANAGER + ENGINEER
```

---

### 🔹 Versions & Configurations

* Multiple versions of same object
* Used in design & engineering systems

👉 Configuration = compatible set of versions

---

## 🔟 Final Exam-Oriented Summary

### ⭐ Key Points to Remember

* OODB stores **objects, not tables**
* Object = state + behavior
* OID gives **unique identity**
* Encapsulation hides data
* Type constructors build complex objects
* Inheritance supports reuse
* OODB supports complex & multimedia data

---

## 📝 How to Write in Exam

* Start with **definition**
* Add **example**
* Draw **simple hierarchy diagram**
* Use keywords:
  *OID, Encapsulation, Inheritance, Persistence*

---
