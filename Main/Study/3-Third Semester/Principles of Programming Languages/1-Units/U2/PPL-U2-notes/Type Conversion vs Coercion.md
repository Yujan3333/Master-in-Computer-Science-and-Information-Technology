#third-semester #PPL 

This is a very common **PPL/Data Type** question.

# Type Conversion vs Coercion

| **Type Conversion**                              | **Coercion**                                                             |
| ------------------------------------------------ | ------------------------------------------------------------------------ |
| Explicit conversion performed by the programmer. | Implicit conversion performed automatically by the compiler/interpreter. |
| Also called **casting**.                         | Also called **implicit type conversion**.                                |
| Programmer specifies the target type.            | Language decides the target type.                                        |
| Gives more control to the programmer.            | Convenient but may lead to unexpected results.                           |
| Example: `(float)x`                              | Example: `int + float`                                                   |

---

# Type Conversion (Explicit)

The programmer intentionally converts one type into another.

### Example

```c
int x = 10;
float y = (float)x;
```

Here:

```text
10 → 10.0
```

The programmer explicitly requested the conversion.

---

# Coercion (Implicit)

The language automatically converts a value to a compatible type.

### Example

```c
int x = 10;
float y = 2.5;

float z = x + y;
```

Before addition:

```text
10 → 10.0
```

The compiler automatically converts `x` from `int` to `float`.

This automatic conversion is **coercion**.

---

# Another Example

```c
float x = 5 / 2;
```

Result:

```text
2.0
```

because:

```text
5 / 2 = 2
```

No coercion occurred before division.

But:

```c
float x = 5 / 2.0;
```

Here:

```text
5 → 5.0
```

Automatic conversion occurs.

This is **coercion**.

---

# Memory Trick

### Type Conversion

> **Programmer says: "Convert this."**

```c
(float)x
```

### Coercion

> **Compiler says: "I'll convert it automatically."**

```c
x + 2.5
```

---

# Exam Definitions

### Type Conversion

Type conversion is the **explicit conversion** of a value from one data type to another by the programmer.

### Coercion

Coercion is the **automatic conversion** of a value from one data type to another by the compiler or interpreter during expression evaluation.

---

# Exam Answer (5 Marks)

**Q. Differentiate between type conversion and coercion.**

| Type Conversion           | Coercion                                                    |
| ------------------------- | ----------------------------------------------------------- |
| Explicit conversion.      | Implicit conversion.                                        |
| Performed by programmer.  | Performed automatically by compiler/interpreter.            |
| Also called casting.      | Also called implicit type conversion.                       |
| Gives programmer control. | Determined by language rules.                               |
| Example: `(float)x`       | Example: `int + float` converts int to float automatically. |

### One-Line Revision

* **Type Conversion = Explicit (Programmer does it).**
* **Coercion = Implicit (Compiler does it).**
