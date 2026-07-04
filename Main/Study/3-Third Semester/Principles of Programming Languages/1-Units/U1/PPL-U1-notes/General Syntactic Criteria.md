#PPL 

Below are **exam-friendly notes** that are easy to remember while still containing the important points.

---

# General Syntactic Criteria

General syntactic criteria are the qualities that make a programming language **easy to use, understand, verify, and translate**.

There are **five main syntactic criteria**:

1. Readability
2. Writability
3. Ease of Verifiability
4. Ease of Translation
5. Lack of Ambiguity

---

# 1. Readability

## Definition

**Readability** is the ease with which a programmer can **read and understand a program**.

A readable program clearly shows the algorithm and data used. Such programs are often called **self-documenting programs** because they are easy to understand even without many comments.

## Features that Improve Readability

* Natural and simple statement format
* Structured statements
* Meaningful keywords and noise words
* Embedded comments
* Long and meaningful identifiers (variable names)
* Mnemonic operator symbols
* Free-format coding (flexible spacing and indentation)
* Complete data declarations

## Example

Easy to read:

```c
totalMarks = english + math + science;
```

Hard to read:

```c
t = e + m + s;
```

## Exam Definition

> **Readability is the ease with which a programmer can read and understand a program. A readable program clearly represents its algorithm and data and is often called self-documenting.**

---

# 2. Writability

## Definition

**Writability** is the ease with which a programmer can **write programs** in a language.

A language with simple and regular syntax makes programming faster and easier.

## Features that Improve Writability

* Simple statement formats
* Structured statements
* Concise syntax
* Meaningful operator symbols
* Meaningful identifiers

## Example

Easy to write:

```c
sum = a + b;
```

Difficult languages may require much longer syntax for the same task.

## Exam Definition

> **Writability is the ease with which programmers can write programs using a programming language. It is improved by simple, regular, and concise syntax.**

---

# 3. Ease of Verifiability

## Definition

**Ease of Verifiability** is the ease with which a program can be **checked or mathematically proved to be correct**.

It is closely related to readability and writability.

If a program is easy to understand, it is also easier to verify.

## Example

A structured program with meaningful variable names is easier to verify than one with confusing logic.

## Exam Definition

> **Ease of Verifiability is the ability to easily check or prove that a program is correct. Readable and well-structured programs are easier to verify.**

---

# 4. Ease of Translation

## Definition

**Ease of Translation** is the ease with which a compiler or interpreter can **translate a program into executable machine code**.

This criterion focuses on the needs of the compiler rather than the programmer.

Programs become harder to translate when a language contains many special or complex syntactic constructs.

## Example

![](../../../../../../../Images/Third_Sem_Images/General%20Syntactic%20Criteria-%20ex.png)

Simple syntax:

```c
x = y + z;
```

is easier for a compiler to translate than very complex language constructs.

## Exam Definition

> **Ease of Translation is the ease with which a compiler or interpreter can translate a program into executable code. Simpler syntax makes translation easier.**

---

# 5. Lack of Ambiguity

## Definition

A programming language should have **only one meaning for every valid statement**.

If a statement can be interpreted in more than one way, it is called **ambiguous**.

## Why is Ambiguity a Problem?

Ambiguity may cause:

* Different interpretations
* Unexpected program behavior
* Compiler confusion

---

## Example: Dangling Else Problem

Consider these two statements:

```text
if condition then statement1
```

and

```text
if condition then statement1
else statement2
```

Now combine them:

```text
if condition1 then
    if condition2 then
        statement1
    else
        statement2
```

Here, it is unclear whether the `else` belongs to:

* the first `if`, or
* the second `if`.

This confusion is called the **Dangling Else Problem**.

---

### Interpretation 1

```text
if condition1 then
{
    if condition2 then
        statement1;
    else
        statement2;
}
```

Here, `else` belongs to the **inner if**.

---

### Interpretation 2

```text
if condition1 then
{
    if condition2 then
        statement1;
}
else
{
    statement2;
}
```

Here, `else` belongs to the **outer if**.

Because both interpretations are possible, the statement is **ambiguous**.

Modern programming languages solve this by defining that **`else` is matched with the nearest unmatched `if`**.

## Exam Definition

> **Lack of Ambiguity means every valid statement in a programming language should have only one interpretation. Ambiguous statements can have multiple meanings and should be avoided.**

---

# Summary Table

| Syntactic Criterion       | Meaning                                    | Main Goal                         |
| ------------------------- | ------------------------------------------ | --------------------------------- |
| **Readability**           | Easy to read and understand                | Helps programmers understand code |
| **Writability**           | Easy to write programs                     | Makes programming easier          |
| **Ease of Verifiability** | Easy to check correctness                  | Helps verify program correctness  |
| **Ease of Translation**   | Easy for compiler/interpreter to translate | Simplifies compilation            |
| **Lack of Ambiguity**     | One statement has only one meaning         | Prevents confusion and errors     |

---

# One-Line Revision

* **Readability:** Easy to **read**.
* **Writability:** Easy to **write**.
* **Ease of Verifiability:** Easy to **prove correct**.
* **Ease of Translation:** Easy for the **compiler to translate**.
* **Lack of Ambiguity:** Every statement has **only one meaning**.
