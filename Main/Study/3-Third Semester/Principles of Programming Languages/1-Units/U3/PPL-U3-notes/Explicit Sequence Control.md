#third-semester #PPL 

# Sequencing Control Between Statements – Explicit Sequence Control

**Definition:**
Explicit sequence control means the **programmer explicitly changes the normal flow of execution** using statements such as `goto`, `break`, and `continue`. 

---

## 1. `goto` Statement

The **`goto`** statement transfers control directly to another statement identified by a **label**.

There are two types:

### a) Unconditional `goto`

* Control always jumps to the specified label.

**Example:**

```c
goto NEXT;

/* other statements */

NEXT:
printf("Hello");
```

---

### b) Conditional `goto`

* Control jumps to the label only if a condition is true.

**Example:**

```c
if (A == 0)
    goto NEXT;

NEXT:
printf("Hello");
```

### Disadvantage of `goto`

* Makes programs **unstructured**.
* Reduces readability and makes debugging difficult.
* Therefore, its use is generally discouraged. 

---

## 2. `break` Statement

The **`break`** statement immediately **terminates the current loop** or **switch statement** and transfers control to the statement following it.

**Example:**

```c
for(int i = 1; i <= 5; i++)
{
    if(i == 3)
        break;

    printf("%d ", i);
}
```

**Output:**

```text
1 2
```

In C, `break` also exits the **nearest enclosing `switch` statement**. 

---

## 3. `continue` Statement

The **`continue`** statement **skips the remaining statements of the current loop iteration** and starts the **next iteration**.

**Example:**

```c
for(int i = 1; i <= 5; i++)
{
    if(i == 3)
        continue;

    printf("%d ", i);
}
```

**Output:**

```text
1 2 4 5
```

---

# Exam-Oriented Short Answer

**Q. What is explicit sequence control?**

**Ans:**
Explicit sequence control allows the programmer to change the normal order of program execution using statements such as **`goto`**, **`break`**, and **`continue`**.

* **`goto`:** Transfers control to a labeled statement. It can be **unconditional** or **conditional**. Its use is discouraged because it makes programs unstructured.
* **`break`:** Terminates the nearest loop or `switch` statement.
* **`continue`:** Skips the rest of the current loop iteration and proceeds with the next iteration. 
