
## **ADT (Abstract Data Type)**

* **Definition:**
  An **ADT** is a **user-defined data type** that **encapsulates both data and methods** to operate on that data.
* **Purpose:** Allows the database to **store and manipulate complex objects** (like images, audio, multimedia, or nested collections).
* **Key Points:**

  1. **Encapsulation:** Data + operations (methods) together.
  2. **Abstraction:** Hides the internal implementation; users only see operations.
  3. **Supports complex objects:** Not just simple integers, strings, or dates.

---

### **Example in ORDBMS context:**

**Suppose we want to store a point in 2D space:**

```sql
CREATE TYPE Point AS OBJECT (
    x NUMBER,
    y NUMBER,
    MEMBER FUNCTION distance (p Point) RETURN NUMBER
);
```

* `Point` is an **ADT**.
* Data: `x` and `y`
* Method: `distance()`

You can now **store points as objects** in tables and **call methods on them**.

---

**Exam shortcut (one-liner):**

> **ADT = Abstract Data Type = user-defined type that combines data and methods to handle complex objects.**

---