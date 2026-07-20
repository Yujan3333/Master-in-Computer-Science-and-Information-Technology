#third-semester #PPL 

Here's an **easy-to-understand, exam-friendly** version without changing the meaning.

---

# Evaluation of Tree Representation of Expressions

When an expression is represented as a **tree**, the compiler must decide **the order in which operations should be evaluated** to generate the correct code.

There are four main problems in tree evaluation.

---

## Problem 1: Uniform Evaluation Rules

### Eager Evaluation

* For each operation (node) in the expression tree, **first evaluate all its operands**.
* After all operands are evaluated, **apply the operator**.
* This is called the **eager evaluation rule** because operands are always evaluated first.

### Lazy Evaluation

* **Do not evaluate operands immediately.**
* Pass the operands without evaluating them.
* The operator decides **whether evaluation is needed**.
* It is difficult to implement because it requires complex software simulation.

**Example:**

```text
5 + (3 × 2)
```

* **Eager:** First calculate `3 × 2 = 6`, then `5 + 6 = 11`.
* **Lazy:** Delay calculating `3 × 2` until it is actually needed.

---

## Problem 2: Side Effects

Some functions may **change the value of variables** while evaluating an expression. These changes are called **side effects**.

**Example:**

```text
c / func(y) + c
```

* The value of `c` and `func(y)` must be evaluated before division.
* If `func(y)` changes the value of `c`, the **order of evaluation becomes important**, because it affects the final result.

---

## Problem 3: Error Conditions

Errors may occur while evaluating expressions.

Common errors include:

* Divide by zero
* Arithmetic overflow
* Invalid array index (subscript out of range)

The evaluation order should help avoid or detect these errors.

---

## Problem 4: Short-Circuit Boolean Expressions

Boolean operators like **AND (`&&`)** and **OR (`||`)** are often used with relational expressions.

**Example:**

```c
if ((X == 0) || (Y / X < Z))
```

If `X == 0` is **true**, the second condition **`Y/X < Z` is not evaluated**.

This prevents a **divide-by-zero** error.

Similarly,

```c
while ((I > UB) && (A[I] < B))
```

If `I > UB` is **false**, `A[I] < B` is not evaluated, avoiding an **array index error**.

### Short-Circuit Evaluation

* In **C**, the left expression is evaluated first.
* The right expression is evaluated **only if needed**.
* This is called **short-circuit evaluation**.

In many other languages, **both operands are evaluated**, even if the result is already known.

**ADA** provides the operators **`and then`** and **`or else`** to perform short-circuit evaluation safely.

Example:

```ada
if (X = 0) or else (Y / X > Z) then
```

This avoids division by zero because the second condition is evaluated only if necessary.

---

# Exam-Oriented Summary

### Problems in Tree Evaluation

1. **Uniform Evaluation Rules**

   * Eager evaluation: evaluate operands first.
   * Lazy evaluation: evaluate operands only when needed.

2. **Side Effects**

   * Functions may modify variable values, making evaluation order important.

3. **Error Conditions**

   * Errors such as divide by zero and overflow may occur during evaluation.

4. **Short-Circuit Boolean Expressions**

   * In C, `&&` and `||` evaluate the second operand only if necessary, preventing unnecessary errors like divide by zero.
