#third-semester #PPL 

This is a common **PPL (Scope & Referencing Environment)** question.

# Local vs Non-Local Referencing Environment

| **Local Referencing Environment**                                          | **Non-Local Referencing Environment**                                              |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Consists of variables declared **inside the current block or subprogram**. | Consists of variables declared **outside the current block but accessible to it**. |
| Variables are local to the current function/block.                         | Variables belong to enclosing blocks or global scope.                              |
| Access is direct within the current scope.                                 | Access depends on the language's scoping rules (usually static/lexical scope).     |
| Has higher priority if local and non-local variables have the same name.   | Used only when a matching local variable is not found.                             |
| Example: Local variables of a function.                                    | Example: Global variables or variables of an enclosing function.                   |

---

## Example

```c
int x = 10;        // Non-local (global)

void fun() {
    int y = 20;    // Local
    printf("%d %d", x, y);
}
```

### Here:

* **Local Referencing Environment:** `y`
* **Non-Local Referencing Environment:** `x`

---

## Definitions

### Local Referencing Environment

The **local referencing environment** is the collection of all variables declared **within the current subprogram or block**.

### Non-Local Referencing Environment

The **non-local referencing environment** is the collection of variables declared **outside the current subprogram or block** that are still accessible according to the scoping rules.

---

### Memory Trick

* **Local** → **Inside** the current function/block.
* **Non-local** → **Outside** the current function/block but still **accessible**.
