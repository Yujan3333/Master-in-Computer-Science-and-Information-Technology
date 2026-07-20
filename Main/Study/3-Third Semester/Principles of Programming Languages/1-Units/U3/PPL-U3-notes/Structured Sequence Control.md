#PPL #third-semester 

# Structured Sequence Control

**Definition:**
Structured sequence control uses **structured control statements** to control the flow of execution in a program. Most programming languages provide control statements for **composition**, **selection (alteration)**, and **iteration**. 

---

## 1. Compound Statements (Composition)

A **compound statement** is a **group of statements** treated as a **single statement**.

* The statements inside the block are executed **in the order they are written**.
* It is the basic way of representing the **composition** (sequence) of statements.

**Example:**

```c
{
    int a = 5;
    int b = 10;
    printf("%d", a + b);
}
```

Here, all statements inside `{ }` form one **compound statement**.

**Advantage:**

* Groups multiple statements into one logical block.
* Improves readability and program organization. 

---

## 2. Conditional Statements (Alteration/Selection)

A **conditional statement** selects **one of two or more alternative statements** based on a condition.

* The condition is usually written using **relational** (`>`, `<`, `==`) and **Boolean** (`&&`, `||`, `!`) operators.
* Common conditional statements are:

  * `if`
  * `if-else`
  * `switch` (case)

**Example:**

```c
if (x > 0)
    printf("Positive");
else
    printf("Negative");
```

Only one branch is executed depending on the condition.

**Advantage:**

* Enables decision making in a program. 

---

## 3. Iteration Statements

**Iteration statements** are used to **repeat a block of statements** multiple times.

An iteration statement has:

* **Head:** Controls how many times the loop executes.
* **Body:** Contains the statements to be repeated.

Common iteration statements are:

* `for`
* `foreach`
* `while`
* `do-while`

**Example:**

```c
for(int i = 1; i <= 5; i++)
{
    printf("%d ", i);
}
```

The **head** is:

```c
i = 1; i <= 5; i++
```

The **body** is:

```c
printf("%d ", i);
```

**Advantage:**

* Reduces code repetition.
* Makes programs shorter and more efficient. 

---

# Exam-Oriented Short Notes

**Q. What is structured sequence control?**
**Ans:** Structured sequence control uses structured control statements to control program execution through **composition**, **selection (alteration)**, and **iteration**. 

**Q. What is a compound statement?**
**Ans:** A compound statement is a group of statements enclosed in a block and treated as a single statement. The statements execute in the order they are written. 

**Q. What is a conditional statement?**
**Ans:** A conditional statement selects one of two or more alternatives based on a condition. Common examples are `if`, `if-else`, and `switch`. 

**Q. What is an iteration statement?**
**Ans:** An iteration statement repeatedly executes a block of code. It consists of a **head** (loop control) and a **body** (statements to repeat). Common loops are `for`, `while`, `do-while`, and `foreach`. 
