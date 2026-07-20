#third-semester #PPL 

# 10 Marks

## 1. Explain Sequence Control and its types.

**Brief Answer:**
Sequence control determines the order in which program statements are executed. It is divided into **Expressions, Statements, Declarative Programming, and Subprograms**. It can also be **implicit** (language-defined) or **explicit** (programmer-controlled). 

---

## 2. Explain sequence control with arithmetic expressions.

**Brief Answer:**
Arithmetic expressions are evaluated using **precedence**, **associativity**, and **parentheses**. Expressions can be represented using **expression trees** and written in **prefix, postfix, or infix notation**. 

---

## 3. Explain semantics for expressions.

**Brief Answer:**
Semantics define the order in which expressions are evaluated. **Prefix** and **postfix** expressions are evaluated using a **stack**, while **infix** expressions use precedence and parentheses. 

---

## 4. Explain evaluation of tree representation of expressions.

**Brief Answer:**
Tree evaluation involves **eager and lazy evaluation**, handling **side effects**, **error conditions**, and **short-circuit Boolean evaluation** to generate correct code. 

---

## 5. Explain sequencing control between statements.

**Brief Answer:**
Statement sequencing controls the execution order using **composition**, **alternation**, and **iteration**. It also includes **explicit control** (`goto`, `break`, `continue`) and **structured control** (`if`, `switch`, loops). 

---

# 5 Marks

## Q1. What is sequence control?

**Answer:**
Sequence control determines the order in which operations and statements are executed in a program. 

---

## Q2. Explain implicit and explicit sequence control.

**Answer:**

* **Implicit:** Execution order defined by the language.
* **Explicit:** Programmer changes execution using parentheses, loops, or conditional statements. 

---

## Q3. Explain operator precedence and associativity.

**Answer:**

* **Precedence** decides which operator is evaluated first.
* **Associativity** decides the evaluation order of operators with the same precedence. 

---

## Q4. Explain expression tree.

**Answer:**
An expression tree represents an arithmetic expression as a tree. The root is the main operator, leaves are operands, and lower-level operations are evaluated first. 

---

## Q5. Differentiate between prefix, postfix, and infix notation.

**Answer:**

* **Prefix:** Operator before operands (`+AB`)
* **Postfix:** Operator after operands (`AB+`)
* **Infix:** Operator between operands (`A+B`) 

---

## Q6. Explain eager and lazy evaluation.

**Answer:**

* **Eager evaluation:** Operands are evaluated before applying the operator.
* **Lazy evaluation:** Operands are evaluated only when needed. 

---

## Q7. What are side effects?

**Answer:**
A side effect occurs when evaluating an expression changes the program state, such as modifying a variable. The evaluation order becomes important. 

---

## Q8. Explain short-circuit evaluation.

**Answer:**
Short-circuit evaluation stops evaluating a Boolean expression once the result is known, preventing unnecessary operations such as divide-by-zero. 

---

## Q9. Explain basic statements in sequence control.

**Answer:**
Basic statements include **assignment**, **subprogram call**, **input**, and **output** statements that control normal program execution. 

---

## Q10. Explain composition, alternation, and iteration.

**Answer:**

* **Composition:** Sequential execution of statements.
* **Alternation:** Selection between alternatives (`if`, `switch`).
* **Iteration:** Repeated execution using loops. 

---

## Q11. Explain explicit sequence control.

**Answer:**
Explicit sequence control changes the normal execution flow using **`goto`**, **`break`**, and **`continue`** statements. 

---

## Q12. Explain structured sequence control.

**Answer:**
Structured sequence control uses **compound statements**, **conditional statements**, and **iteration statements** to organize program execution clearly and avoid unstructured code. 

---

# ⭐ One-Line Revision

* **Sequence Control:** Order of program execution.
* **Precedence:** Higher-priority operator executes first.
* **Associativity:** Order of operators with the same precedence.
* **Expression Tree:** Tree representation of expressions.
* **Prefix:** Operator before operands.
* **Postfix:** Operator after operands.
* **Infix:** Operator between operands.
* **Eager Evaluation:** Evaluate operands first.
* **Lazy Evaluation:** Evaluate operands only when needed.
* **Side Effect:** Expression changes program state.
* **Short-Circuit:** Stops Boolean evaluation when the result is already known.
* **Composition:** Sequential execution.
* **Alternation:** Decision making.
* **Iteration:** Repetition using loops.
* **Explicit Control:** `goto`, `break`, `continue`.
* **Structured Control:** Compound, conditional, and iteration statements.
