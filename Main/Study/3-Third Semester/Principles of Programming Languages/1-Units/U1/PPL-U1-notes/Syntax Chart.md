#PPL 

# Syntax Chart (Syntax Diagram / Railroad Diagram)

A **Syntax Chart** (also called a **Syntax Diagram** or **Railroad Diagram**) is a **graphical representation of a grammar**. It shows the rules of a programming language using **boxes, arrows, and paths** instead of BNF or EBNF notation.

It is commonly used in compiler design because it is easier to read and understand than grammar rules.

---

# Why is a Syntax Chart used?

* Visually represents grammar rules.
* Makes the syntax easier to understand.
* Helps programmers and compiler designers.
* Reduces confusion compared to long BNF rules.

---

# Basic Symbols

| Symbol    | Meaning                  |
| --------- | ------------------------ |
| ○ Start   | Beginning of the rule    |
| ○ End     | End of the rule          |
| Rectangle | Terminal or non-terminal |
| Arrow     | Direction of parsing     |
| Branch    | Choice (OR)              |
| Loop      | Repetition               |

---



# Example 1: Identifier
### EBNF
![](../../../../../../../Images/Third_Sem_Images/Syntax%20Chart-ebnf.png)
### Syntax Chart
![](../../../../../../../Images/Third_Sem_Images/Syntax%20Chart.png)

### EBNF

```text
<identifier> = <letter> {<letter> | <digit>}
```

### Syntax Chart

```text
(Start)
   |
   v
+---------+
| Letter  |
+---------+
     |
     v
  +---------------------------+
  | Letter OR Digit (repeat)  |
  +---------------------------+
     ^                       |
     |_______________________|
             |
             v
           (End)
```

### Examples

Valid:

```text
abc
student1
A25
```

Invalid:

```text
1abc
%
```

---

# Example 2: Integer

### EBNF

```text
<integer> = ["-"] <digit> {<digit>}
```

### Syntax Chart

```text
(Start)
   |
   v
(Optional "-")
   |
   v
+---------+
| Digit   |
+---------+
    |
    v
+------------------+
| Digit (repeat)   |
+------------------+
    ^            |
    |____________|
         |
         v
       (End)
```

Examples

Valid

```text
5
123
-45
```

---

# Example 3: Arithmetic Expression

### EBNF

```text
<expression> = <term> { ("+" | "-") <term> }
```

### Syntax Chart

```text
(Start)
   |
   v
+------+
| Term |
+------+
    |
    v
+----------------------+
| + OR -               |
+----------------------+
    |
    v
+------+
| Term |
+------+
    ^
    |
    +-------------------+
    |     Repeat        |
    +-------------------+
    |
    v
  (End)
```

Examples

```text
5+3

10-4+7

9+2-1+8
```

---

# Example 4: IF Statement

### EBNF

```text
if (condition) statement [else statement]
```

### Syntax Chart

```text
(Start)
   |
   v
+------+
| if   |
+------+
   |
   v
+------+
| ( )  |
+------+
   |
   v
+-----------+
| Condition |
+-----------+
   |
   v
+-----------+
| Statement |
+-----------+
   |
   v
(Optional)
   |
   +--------+
   | else   |
   +--------+
        |
        v
+-----------+
| Statement |
+-----------+
        |
        v
      (End)
```

---

# Syntax Chart vs BNF

| BNF                             | Syntax Chart                           |
| ------------------------------- | -------------------------------------- |
| Uses grammar rules              | Uses diagrams                          |
| Text-based                      | Graphical                              |
| Harder to visualize             | Easy to understand                     |
| Used in compiler specifications | Used for explanation and documentation |

---

# Advantages of Syntax Charts

* Easy to understand.
* Clearly shows the flow of grammar.
* Visually represents optional and repeated parts.
* Useful for learning and designing programming languages.

---

# Disadvantages of Syntax Charts

* Large diagrams become difficult to draw for complex grammars.
* Not as compact as BNF or EBNF.
* Harder to edit when grammar changes frequently.

---

# Exam Answer (5 Marks)

A **Syntax Chart (Syntax Diagram or Railroad Diagram)** is a **graphical representation of the grammar of a programming language**. It uses **boxes, arrows, branches, and loops** to illustrate how valid statements are formed. Syntax charts are easier to understand than BNF because they visually show the sequence, choice, optional parts, and repetition in a grammar.

**Example:**

Grammar:

```text
<integer> = ["-"] <digit> {<digit>}
```

Simplified syntax chart:

```text
(Start)
   |
(Optional "-")
   |
 Digit
   |
Repeat Digit
   |
 (End)
```

This diagram represents integers such as `5`, `123`, and `-45`. Syntax charts are widely used in compiler design and language documentation to explain grammar in a visual and intuitive way.
