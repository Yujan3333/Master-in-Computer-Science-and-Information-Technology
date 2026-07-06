#PPL 

# Parse Tree (Syntax Tree)

A **Parse Tree** is a **tree representation that shows how a string (sentence or program) is derived from a grammar (BNF/CFG).**

It shows **step-by-step how the start symbol is expanded into terminals** according to the grammar rules.

In compiler design, a parser builds a parse tree to check whether the input program follows the language grammar.

![](../../../../../../../Images/Third_Sem_Images/Parse%20Tree-fig.png)


---

## Why is a Parse Tree used?

* Checks whether the input is syntactically correct.
* Shows the hierarchical structure of a program.
* Helps the compiler understand expressions.
* Used during syntax analysis (parsing).

---

## Components of a Parse Tree

1. **Root Node**

   * The starting symbol of the grammar.

2. **Internal Nodes**

   * Non-terminals (e.g., `<expression>`, `<term>`).

3. **Leaf Nodes**

   * Terminals (actual symbols such as `a`, `+`, `5`, `(`, `)`).

---

## Example 1

### Grammar

```bnf
<expression> ::= <expression> + <term>
               | <term>

<term> ::= id
```

Suppose the input is

```text
id + id
```

### Parse Tree

```text
            <expression>
            /     |      \
   <expression>   +    <term>
        |                |
      <term>            id
        |
       id
```

### Reading the tree

1. Start with `<expression>`.
2. Apply the rule

```text
<expression> → <expression> + <term>
```

3. The left `<expression>` becomes

```text
<term>
```

4. `<term>` becomes

```text
id
```

5. The right `<term>` also becomes

```text
id
```

Reading the leaf nodes from **left to right** gives:

```text
id + id
```

---

# Example 2

### Grammar

```bnf
<expression> ::= <term>

<term> ::= <factor> * <factor>

<factor> ::= id
```

Input

```text
a * b
```

### Parse Tree

```text
         <expression>
               |
            <term>
         /     |     \
   <factor>    *   <factor>
       |              |
       a              b
```

Leaf nodes:

```text
a * b
```

---

# Example 3

### Grammar

```bnf
<expression> ::= (<expression>)
               | id
```

Input

```text
(id)
```

### Parse Tree

```text
           <expression>
         /      |        \
        (   <expression>   )
               |
              id
```

Leaves:

```text
( id )
```

---

# How to Draw a Parse Tree in an Exam

Suppose the grammar is

```bnf
S → A B

A → a

B → b
```

Input

```text
ab
```

### Step 1

Start with the root.

```text
S
```

### Step 2

Expand `S`.

```text
      S
     / \
    A   B
```

### Step 3

Replace `A` and `B`.

```text
      S
     / \
    A   B
    |   |
    a   b
```

Reading the leaves from left to right gives:

```text
ab
```

---

# Parse Tree vs Syntax Tree

| Parse Tree                     | Syntax Tree (AST)                               |
| ------------------------------ | ----------------------------------------------- |
| Shows every grammar rule used. | Removes unnecessary grammar details.            |
| Contains all non-terminals.    | Contains only important constructs.             |
| Larger and more detailed.      | Smaller and more compact.                       |
| Used during parsing.           | Used for semantic analysis and code generation. |

---

# Advantages of Parse Trees

* Verifies whether the input follows the grammar.
* Clearly represents the hierarchical structure of a program.
* Helps detect syntax errors.
* Serves as the basis for later compiler phases, such as semantic analysis.

---

# Disadvantages of Parse Trees

* Can become very large for complex programs.
* Includes many grammar-specific nodes that are not needed later.
* Usually converted into a simpler **Abstract Syntax Tree (AST)** for further compilation.

---

# Exam Answer (5 Marks)

A **Parse Tree (Syntax Tree)** is a tree representation that shows how an input string is derived from a grammar using production rules. The **root node** is the start symbol, **internal nodes** are non-terminals, and **leaf nodes** are terminals. A parser constructs the parse tree during syntax analysis to verify that the input program follows the language grammar.

**Example:**

Grammar:

```text
S → A B
A → a
B → b
```

Parse Tree:

```text
      S
     / \
    A   B
    |   |
    a   b
```

The leaf nodes read from left to right produce the input string **`ab`**. Parse trees are widely used in compiler design for syntax checking and as the foundation for later stages of compilation.
