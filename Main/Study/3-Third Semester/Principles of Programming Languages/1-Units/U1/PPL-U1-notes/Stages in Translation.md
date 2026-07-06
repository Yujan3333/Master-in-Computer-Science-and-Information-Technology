#PPL 
# Figure

- Two major parts: *Analysis and synthesis*

![](../../../../../../../Images/Third_Sem_Images/Stages%20in%20Translation-fig.png)


# Stages in Translation (Exam Summary)

Translation is divided into **two main stages**:

1. **Analysis of the Source Program (Front End)**
2. **Synthesis of the Object Program (Back End)**

---

# 1. Analysis of the Source Program

This phase analyzes the source code and checks whether it is correct.

## a) Lexical Analysis (Scanner)

* Reads the source code **character by character**.
* Groups characters into **lexemes**.
* Converts lexemes into **tokens** (identifier, keyword, operator, number, etc.).
* Stores identifiers in the **symbol table**.
* Uses **Finite State Automata (FSA)**.

**Output:** Tokens

---

## b) Syntax Analysis (Parser)

* Takes tokens from the lexical analyzer.
* Checks whether the program follows the grammar rules.
* Builds a **Parse Tree (Syntax Tree)**.

**Output:** Parse Tree

---

## c) Semantic Analysis

* Checks the **meaning** of the program.
* Uses the parse tree and symbol table.
* Detects errors such as:

  * Type mismatch
  * Undeclared variables
  * Invalid function arguments
  * Incompatible operands

**Output:** Semantically correct intermediate representation.

---

# 2. Synthesis of the Object Program

This phase converts the analyzed program into an executable program.

## a) Optimization

* Improves the intermediate code.
* Makes the program faster and/or smaller.
* Removes unnecessary instructions.

---

## b) Code Generation

* Converts optimized intermediate code into:

  * Assembly language
  * Machine code
  * Object code

---

## c) Linking and Loading

* Combines separately compiled modules and libraries.
* Resolves function and variable addresses.
* Produces the **final executable program** ready to run.

---

# Bootstrapping

* **Bootstrapping** is the process of using a compiler to compile **its own source code**.
* It creates a **self-hosting compiler**, which can compile itself as well as other programs.

---

# Flow Diagram (Easy to Remember)

```text
Source Program
      │
      ▼
Lexical Analysis
      │
      ▼
Syntax Analysis
      │
      ▼
Semantic Analysis
      │
      ▼
Optimization
      │
      ▼
Code Generation
      │
      ▼
Linking & Loading
      │
      ▼
Executable Program
```

---

# Exam Definitions (1–2 Marks)

* **Lexical Analysis:** Converts source code into tokens.
* **Syntax Analysis:** Checks grammar and builds a parse tree.
* **Semantic Analysis:** Checks the meaning and detects semantic errors.
* **Optimization:** Improves intermediate code for better performance.
* **Code Generation:** Converts optimized code into machine/object code.
* **Linking and Loading:** Combines object files and libraries to create the final executable.
* **Bootstrapping:** The process of building a compiler that can compile its own source code (self-hosting compiler).
