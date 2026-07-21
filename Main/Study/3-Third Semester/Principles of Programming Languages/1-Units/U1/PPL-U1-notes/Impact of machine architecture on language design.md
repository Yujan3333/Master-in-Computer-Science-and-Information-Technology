#PPL #third-semester 

# 1. Early Languages

> **"Early languages were designed to run programs efficiently on expensive hardware."**

### Meaning

In the 1950s–1970s:

* Computers were **very expensive**.
* Memory and CPU speed were **limited**.
* Every CPU cycle mattered.

Therefore, programming languages were designed to generate **very efficient machine code**, even if they were difficult to write.

### Example

Assembly Language

```assembly
MOV AX, 5
ADD AX, 10
```

* Very fast execution ✅
* Very difficult to write and debug ❌

**Focus:** Machine efficiency.

---

# 2. Modern Languages

> **"Today, machines are inexpensive... programmers are expensive."**

### Meaning

Today:

* Computers are cheap.
* CPUs are very fast.
* Memory is abundant.

But **programmers' time is costly**.

So languages are designed to make programming:

* Easier
* More readable
* Less error-prone
* Easier to maintain

Even if the program runs a little slower.

### Example

Python

```python
total = sum(numbers)
```

This is much easier to write than implementing the loop manually in assembly or low-level code.

**Focus:** Programmer productivity.

---

# Comparison

| Early Languages                         | Modern Languages                                                    |
| --------------------------------------- | ------------------------------------------------------------------- |
| Hardware was expensive                  | Hardware is inexpensive                                             |
| Programmers were relatively cheaper     | Programmers are expensive                                           |
| Focus on execution speed                | Focus on ease of programming                                        |
| Generated highly efficient machine code | Prioritize readability and maintainability, even if slightly slower |
| Example: Assembly                       | Example: Python, Java                                               |

---

# 3. Machine Architecture Influences Language Design

The slide says machine architecture affects language design in **two ways**.

---

## (1) Underlying Computer

This means the **actual hardware** on which the program runs.

It includes:

* CPU
* Memory
* Registers
* Input/Output devices

The programming language must work with these hardware components.

### Example

C was designed close to the hardware, allowing direct memory access and pointer manipulation.

---

## (2) Execution Model (Virtual Computer)

Not every language runs directly on hardware.

Some languages first run on a **virtual machine**.

### Example: Java

```text
Java Program
      ↓
Java Compiler
      ↓
Bytecode
      ↓
JVM (Java Virtual Machine)
      ↓
Actual Hardware
```

The **JVM** is a **virtual computer**.

The programmer writes Java code, and the JVM executes it on the real hardware.

Another example is **.NET**, where C# programs run on the **Common Language Runtime (CLR)**.

---

# Easy Exam Answer (5 Marks)

**Q. Explain the impact of machine architecture on language design.**

**Ans:**

* Earlier, computers were expensive and had limited resources. Therefore, programming languages were designed to produce efficient machine code, even though programs were difficult to write.
* Today, computers are inexpensive and powerful, while programmers are expensive. Hence, modern languages emphasize simplicity, readability, maintainability, and programmer productivity, even if execution is slightly slower.
* Machine architecture influences language design in two ways:

  1. **Underlying Computer:** The actual hardware (CPU, memory, I/O) on which programs execute.
  2. **Execution Model (Virtual Computer):** Some languages execute through a virtual machine, such as the **Java Virtual Machine (JVM)**, instead of running directly on hardware.

---

## Memory Trick

Remember the progression:

**Old Languages → Fast Machine Code → Difficult to Program**

⬇️

**Modern Languages → Easy to Program → Slightly Slower Execution**

And remember the **2 influences**:

* **Hardware (Underlying Computer)**
* **Virtual Machine (Execution Model)**
