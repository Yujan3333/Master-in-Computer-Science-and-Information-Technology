#third-semester #PPL 

This topic explains **how a coroutine resumes execution from where it previously stopped**. The wording is technical, but the idea is actually simple.

---

# Implementation of Coroutine

## Key Idea

Unlike a normal subroutine, **only one activation (instance) of each coroutine exists at a time**.

This means:

* A coroutine is **not recreated** every time.
* Its execution state is **saved**.
* When resumed, it **continues from the previous point**.

---

# Important Terms

### 1. Activation Record

An **activation record (stack frame)** stores information about a running coroutine, such as:

* Local variables
* Parameters
* Return address
* **Resume point**

---

### 2. CIP (Current Instruction Pointer)

CIP stores the **address of the next instruction to execute**.

Think of it as a **bookmark** in the program.

Example:

```text id="q13e1p"
1. Read data
2. Process data
3. Print result
```

If execution stops after line 2,

CIP points to:

```text id="k0d8ww"
3. Print result
```

---

### 3. Resume Point

A **resume point** is a memory location inside the activation record that stores the value of the **CIP**.

It remembers:

> **"Where should execution continue next time?"**

---

# What happens when `resume B` is executed inside Coroutine A?

Suppose:

```text id="0abslr"
Coroutine A
Coroutine B
```

A is currently running.

Now A executes:

```text id="nx9ktm"
resume B
```

The following steps occur.

---

## Step 1

Save A's current execution point.

```text id="fybbz5"
A:
Line 25
```

The current **CIP** (line 25) is stored in **A's resume point**.

```
A Activation Record

Resume Point = Line 25
```

---

## Step 2

Read B's saved resume point.

Suppose earlier B stopped at

```
Line 40
```

B's activation record contains

```
Resume Point = Line 40
```

---

## Step 3

Load B's resume point into CIP.

Now

```
CIP = Line 40
```

---

## Step 4

Execution continues in B.

Instead of starting at line 1,

B resumes at

```
Line 40
```

---

# Diagram

```text id="9b93bs"
Coroutine A running
        │
        │ resume B
        ▼
Save A's CIP
(Line 25)

        │
        ▼

Load B's Resume Point
(Line 40)

        │
        ▼

Coroutine B resumes
from Line 40
```

---

# Real-Life Analogy

Imagine two students studying.

### Student A

Stops reading at

```
Page 35
```

Places a bookmark.

Then Student B starts reading.

Student B already has a bookmark at

```
Page 70
```

So B starts from page 70,

not page 1.

Later,

B stops,

places another bookmark,

and A continues from page 35.

That bookmark is exactly like the **resume point**.

---

# Why is CIP saved?

Because without saving the instruction pointer,

the coroutine would always restart from the beginning,

which would make it behave exactly like a normal subroutine.

Saving the CIP allows it to continue from where it stopped.

---

# Exam Answer (5 Marks)

**Q. Explain the implementation of a coroutine.**

**Ans:**

* Only **one activation** of each coroutine exists at a time.
* Each coroutine has an **activation record** that stores its execution information.
* A special location called the **resume point** is reserved in the activation record to store the **Current Instruction Pointer (CIP)**.
* When a coroutine executes a **resume** instruction, the current CIP is saved in its own resume point.
* The saved CIP of the target coroutine is loaded into the CIP.
* The target coroutine then resumes execution from its previously saved location instead of starting from the beginning.

---

## Memory Trick

Remember the sequence:

```text id="l5jvru"
Running A
    │
    ▼
Save A's CIP
    │
    ▼
Load B's CIP
    │
    ▼
Resume B
```

**Save current → Load next → Continue execution**. This is the core idea behind coroutine implementation.
