#advanced-cryptography 

# Syntactic Elements of a Programming Language

## Definition

**Syntactic elements** are the **basic building blocks** of a programming language. They determine how programs are written and how different parts of a program are formed.

---

Shortform- **CIOK-NC-BD-FreeFixedFormat-ES**
# 1. Character Set

## Definition

A **character set** is the collection of all characters that can be used in a programming language. It is also called the **alphabet of the language**.

Common character sets include:

* ASCII
* EBCDIC
* Unicode

## Example

Characters include:

```text
A B C
a b c
0 1 2
+ - * /
( ) { }
```

## Exam Definition

> **A character set is the collection of letters, digits, symbols, and special characters that can be used to write programs.**

---

# 2. Identifiers

## Definition

**Identifiers** are the names given to program elements such as:

* Variables
* Functions
* Classes
* Structures
* Arrays

Most languages follow these rules:

* Begin with a letter or underscore (`_`)
* Can contain letters, digits, and underscores
* Cannot start with a digit
* Cannot be a keyword

## Example

Valid identifiers:

```c
studentName
total_marks
sum1
```

Invalid identifiers:

```c
1student
float
total-marks
```

## Exam Definition

> **Identifiers are user-defined names used to identify program elements such as variables, functions, and classes.**

---

# 3. Operator Symbols

## Definition

**Operators** are special symbols that perform operations on data.

Common operators include:

* `+` Addition
* `-` Subtraction
* `*` Multiplication
* `/` Division
* `%` Modulus

Some languages use words like `PLUS` or `TIMES` instead of symbols.

## Example

```c
sum = a + b;
```

Here,

* `=` is the assignment operator.
* `+` is the addition operator.

## Exam Definition

> **Operator symbols are special characters or words used to perform operations on data.**

---

# 4. Keywords (Reserved Words)

## Definition

**Keywords** are predefined words that have a special meaning in a programming language.

They **cannot be used as identifiers**.

Common keywords:

* `if`
* `else`
* `while`
* `for`
* `int`
* `float`
* `return`

## Example

Correct:

```c
int age;
```

Incorrect:

```c
int int;
```

(`int` cannot be used as a variable name.)

## Exam Definition

> **Keywords are reserved words with predefined meanings that cannot be used as programmer-defined identifiers.**

---

# 5. Noise Words

## Definition

**Noise words** are optional words added to improve the readability of a program.

They **do not change the meaning** of the program.

### Example

In **COBOL**:

```text
GO TO label
```

* `GO` is required.
* `TO` is optional (noise word).

## Exam Definition

> **Noise words are optional words used to improve readability without changing the meaning of a statement.**

---

# 6. Comments

## Definition

**Comments** are notes written inside a program to explain the code.

Comments are ignored by the compiler and are used for documentation and readability.

### Types

### Single-line comment

```c
// Calculate total marks
```

### Multi-line comment

```c
/*
Calculate
Total Marks
*/
```

## Exam Definition

> **Comments are non-executable statements used to explain program code and improve readability.**

---

# 7. Blanks (Spaces)

## Definition

**Blanks (spaces)** separate words and improve readability.

Different programming languages have different rules for spaces.

In **C**, spaces generally do not affect the meaning of a program (except inside string literals).

## Example

Both are valid:

```c
a=b+c;
```

```c
a = b + c;
```

The second is easier to read.

## Exam Definition

> **Blanks are spaces used to separate program elements and improve readability.**

---

# 8. Delimiters and Brackets

## Definition

**Delimiters** mark the beginning or end of program constructs.

**Brackets** are paired delimiters used to group statements or expressions.

### Common Delimiters

* `;`
* `,`
* `:`

### Common Brackets

* `()`
* `{}`
* `[]`

## Example

```c
if(a > b)
{
    max = a;
}
```

Here:

* `()` contain the condition.
* `{}` enclose the block of statements.
* `;` marks the end of a statement.

## Exam Definition

> **Delimiters separate or terminate program elements, while brackets group related expressions or statements.**

---

# 9. Free-Field and Fixed-Field Formats

## A. Free-Field Format

### Definition

In a **free-field format**, statements can be written **anywhere on a line**, and spacing or indentation does not affect the program.

### Example (C)

```c
int a=10;
```

```c
int        a =      10;
```

Both are valid.

---

## B. Fixed-Field Format

### Definition

In a **fixed-field format**, the **position of characters on a line is important**.

Older languages such as **FORTRAN** use fixed-field formatting.

### Example

A statement may need to start in a specific column.

## Exam Definition

> **Free-field format allows statements to be written anywhere on a line, whereas fixed-field format requires statements to appear in specific positions.**

---

# 10. Expressions

## Definition

An **expression** is a combination of:

* Variables
* Constants
* Operators
* Function calls

that produces a value.

## Example

```c
a + b
```

```c
x * y + 5
```

```c
(a+b)/2
```

Each expression evaluates to a value.

## Exam Definition

> **An expression is a combination of operands and operators that evaluates to a single value.**

---

# 11. Statements

## Definition

A **statement** is a complete instruction that tells the computer to perform a task.

Statements may be:

* Simple
* Compound (nested)

## Examples

Assignment statement:

```c
x = 10;
```

Conditional statement:

```c
if(x > 0)
    printf("Positive");
```

Loop statement:

```c
for(i=0;i<5;i++)
    printf("%d", i);
```

## Exam Definition

> **A statement is a complete instruction that performs a specific task in a program.**

---

# Summary Table

| Syntactic Element             | Purpose                              | Example                               |
| ----------------------------- | ------------------------------------ | ------------------------------------- |
| **Character Set**             | Defines allowed characters           | `A`, `1`, `+`, `{`                    |
| **Identifiers**               | Names for variables, functions, etc. | `totalMarks`, `sum1`                  |
| **Operator Symbols**          | Perform operations                   | `+`, `-`, `*`, `/`                    |
| **Keywords**                  | Reserved words with special meaning  | `if`, `while`, `int`                  |
| **Noise Words**               | Improve readability                  | `TO` in `GO TO` (COBOL)               |
| **Comments**                  | Explain the program                  | `// comment`                          |
| **Blanks (Spaces)**           | Improve readability                  | `a = b + c;`                          |
| **Delimiters & Brackets**     | Separate and group program elements  | `;`, `()`, `{}`                       |
| **Free-/Fixed-Field Formats** | Control statement positioning        | C (free-field), FORTRAN (fixed-field) |
| **Expressions**               | Produce a value                      | `a + b`, `(x+y)/2`                    |
| **Statements**                | Complete instructions                | `x = 10;`, `if(x>0)`                  |

---

# Quick Revision

* **Character Set:** Allowed characters in a language.
* **Identifiers:** User-defined names for program elements.
* **Operators:** Symbols that perform operations.
* **Keywords:** Reserved words with predefined meanings.
* **Noise Words:** Optional words that improve readability.
* **Comments:** Notes ignored by the compiler.
* **Blanks:** Spaces used to improve readability.
* **Delimiters & Brackets:** Symbols that separate or group program elements.
* **Free-Field Format:** Statements can be written anywhere on a line.
* **Fixed-Field Format:** Statement position on the line is important.
* **Expressions:** Combinations of operands and operators that produce a value.
* **Statements:** Complete instructions executed by the computer.
