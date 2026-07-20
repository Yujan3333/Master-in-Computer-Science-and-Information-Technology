#third-semester #PPL 

# Semantics for Expressions

**Semantics** determine the **order in which an expression is evaluated** to produce the final result.

---

## 1. Evaluation of Prefix Expression (Using Stack)

If **P** is a prefix expression, it is evaluated using a **stack**.

1. If the next item is an **operator**, push it onto the stack and note the number of operands (arguments) it requires. If it requires **n operands**, it is called an **n-ary operator**.

2. If the next item is an **operand**, push it onto the stack.

3. When the **top n items of the stack are the operands needed by the last operator**, apply the operator to those operands. Replace the operator and its operands with the **result**.

**Example:**

```text
+ * A B C
```

Equivalent infix expression:

```text
(A × B) + C
```

---

## 2. Evaluation of Postfix Expression (Using Stack)

If **P** is a postfix expression, it is evaluated using a **stack**.

1. If the next item is an **operand**, push it onto the stack.

2. If the next item is an **n-ary operator**, its required **n operands** will be the top **n items** on the stack. Apply the operator and replace those operands with the **result**.

**Example:**

```text
AB*C+
```

Equivalent infix expression:

```text
(A × B) + C
```

---

## 3. Evaluation of Infix Expression

**Infix notation** is the most common notation, where the **operator is placed between operands**.

**Example:**

```text
A + B
```

### Problems of Infix Notation

1. **Suitable only for binary operations.**

   * A language cannot use only infix notation; it must also use **prefix or postfix** internally.
   * This makes translation more complex.

2. **Ambiguity**

   * If an expression contains more than one operator, the order of evaluation may be **ambiguous** unless **parentheses** or operator precedence rules are used.

**Example:**

```text
A + B × C
```

This is interpreted as:

```text
A + (B × C)
```

because `×` has higher precedence than `+`.

---

### Quick Revision

* **Prefix:** Operator **before** operands (`+AB`) → evaluated using a **stack**.
* **Postfix:** Operator **after** operands (`AB+`) → evaluated using a **stack**.
* **Infix:** Operator **between** operands (`A+B`) → uses **precedence and parentheses** to determine evaluation order.
