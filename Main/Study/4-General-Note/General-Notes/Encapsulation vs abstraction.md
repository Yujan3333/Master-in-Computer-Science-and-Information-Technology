#general-note 

## Abstraction vs Encapsulation (Exam-Oriented)

These are two important concepts in **Object-Oriented Programming (OOP)** and are often asked in exams.

| **Abstraction**                                              | **Encapsulation**                                                                                                 |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Hides **implementation details**.                            | Hides **data** by restricting direct access.                                                                      |
| Focuses on **what an object does**.                          | Focuses on **how data is protected**.                                                                             |
| Achieved using **abstract classes** and **interfaces**.      | Achieved using **classes**, **private variables**, and **public methods (getters/setters)**.                      |
| Reduces complexity by showing only essential features.       | Protects data from unauthorized access and modification.                                                          |
| Example: Driving a car without knowing how the engine works. | Example: A bank account where the balance can only be accessed through methods like `deposit()` and `withdraw()`. |

---

## Simple Definitions

### Abstraction

> **Abstraction is the process of hiding implementation details and showing only the essential features of an object.**

### Encapsulation

> **Encapsulation is the process of wrapping data and methods into a single unit (class) and restricting direct access to the data.**

---

## Easy Example

### Abstraction

When you use an **ATM**, you only know:

* Insert card
* Enter PIN
* Withdraw money

You **do not know** how the ATM communicates with the bank.

➡️ **Hides implementation details.**

---

### Encapsulation

A bank account stores the balance as a **private** variable.

```java
class BankAccount {
    private double balance;

    public void deposit(double amount) {
        balance += amount;
    }

    public double getBalance() {
        return balance;
    }
}
```

You cannot directly do:

```java
account.balance = 1000000;   // Not allowed
```

Instead, you must use methods:

```java
account.deposit(1000);
account.getBalance();
```

➡️ **Hides data and protects it.**

---

## Memory Trick ⭐⭐⭐⭐⭐

### Abstraction

> **Hide HOW it works.**

Think:

```text
"What does it do?"
```

---

### Encapsulation

> **Hide the DATA.**

Think:

```text
"Who can access the data?"
```

---

## Real-Life Example

Imagine a **TV Remote**.

### Abstraction

You press the **Power** button.

You don't know how the TV turns on internally.

➡️ **Abstraction**

---

### Encapsulation

The electronic circuits inside the remote are enclosed in a case, so you cannot directly access or modify them.

➡️ **Encapsulation**

---

## Key Difference

```text
Abstraction:
Hide implementation (HOW)

Encapsulation:
Hide data (PROTECT DATA)
```

---

## Exam Definition (2 Marks)

### Abstraction

> **Abstraction is the process of hiding implementation details and exposing only the essential features of an object.**

### Encapsulation

> **Encapsulation is the process of binding data and methods into a single unit (class) while restricting direct access to the data.**

---

## One-Line Memory Trick ⭐⭐⭐⭐⭐

```text
Abstraction → Hide HOW it works.

Encapsulation → Hide the DATA.
```

### Easy Way to Remember

* **Abstraction = What**
* **Encapsulation = How (protecting the data inside)**
