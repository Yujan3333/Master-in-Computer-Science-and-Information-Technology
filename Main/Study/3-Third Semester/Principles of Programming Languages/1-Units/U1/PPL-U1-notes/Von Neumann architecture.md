#ppl #third-semester 

# Computer Hardware (Von Neumann Architecture)

## Definition

**Von Neumann Architecture** is a computer architecture in which **both program instructions and data are stored in the same main memory**.

It is the architecture used by most modern computers.

---

## How does it work?

### Step 1: Main Memory Stores Programs and Data

Main memory (RAM) stores:

* **Program instructions**
* **Data**

Example:

```text
Main Memory
-------------------------
Program:
1. Read x
2. Read y
3. Add x and y
4. Print result

Data:
x = 10
y = 20
```

So, **instructions and data are stored together**.

---

### Step 2: CPU (Interpreter) Fetches Instructions

The CPU repeatedly performs the **Fetch–Decode–Execute Cycle**:

1. **Fetch** an instruction from memory.
2. **Decode** the instruction (understand what to do).
3. **Execute** the instruction.

Example:

Instruction:

```text
ADD R1, R2
```

The CPU understands it means:

> Add the contents of register `R1` and `R2`.

---

### Step 3: Primitive Operations Execute

The CPU performs basic operations such as:

* Addition
* Subtraction
* Multiplication
* Division
* Comparison

Example:

```text
10 + 20 = 30
```

---

### Step 4: Result is Stored

The result may be stored:

* In a **register** (temporary storage)
* In **main memory**
* Sent to an **output device**

---

# Data Storage Components

The slide mentions four storage components.

## 1. Main Memory (RAM)

* Stores programs and data currently in use.
* Fast but temporary (volatile).

Example:
Running Microsoft Word or a C++ program.

---

## 2. Cache Memory

* Smaller and faster than RAM.
* Stores frequently used instructions and data.
* Speeds up CPU execution.

Example:
If the CPU repeatedly uses a variable, it may keep it in the cache.

---

## 3. Registers

* Very small storage locations **inside the CPU**.
* Fastest memory in the computer.
* Hold operands and intermediate results during execution.

Example:

```text
Register A = 10
Register B = 20
```

CPU performs:

```text
10 + 20
```

directly using the registers.

---

## 4. External Files (Secondary Storage)

Examples:

* Hard disk
* SSD
* USB drive

These store data permanently.

Example:

```text
report.docx
photo.jpg
student.txt
```

---

# Built-in Data Types

The hardware can directly manipulate basic data types such as:

* Integer
* Character
* Boolean
* Floating point

Example:

```cpp
int x = 10;
```

The CPU has instructions to directly add or compare integers.

---

# Programs are also Data

One important idea in the Von Neumann architecture is:

> **A program is also stored as data in memory.**

A machine instruction consists of:

* **Opcode (Operation Code):** What operation to perform (e.g., ADD, SUB, LOAD).
* **Operands:** The data or memory locations involved.

Example:

```text
ADD R1, R2
```

* **Opcode:** `ADD`
* **Operands:** `R1`, `R2`

---

# Overall Flow

```text
Program + Data
        │
        ▼
   Main Memory
        │
        ▼
       CPU
(Fetch → Decode → Execute)
        │
        ▼
Registers / Cache
        │
        ▼
Output or Memory
```

---

# Summary Table

| Component                | Function                                               |
| ------------------------ | ------------------------------------------------------ |
| **Main Memory (RAM)**    | Stores programs and data currently being used.         |
| **CPU (Interpreter)**    | Fetches, decodes, and executes instructions.           |
| **Primitive Operations** | Performs basic operations like add, subtract, compare. |
| **Cache Memory**         | Stores frequently used data for faster access.         |
| **Registers**            | Fastest storage inside the CPU for temporary data.     |
| **External Files**       | Permanent storage for programs and data.               |
| **Opcode**               | Specifies the operation to perform.                    |
| **Operands**             | Specify the data or locations used by the operation.   |

---

# Exam Answer (5 Marks)

**Q. Explain computer hardware based on the Von Neumann architecture.**

**Ans:**
The **Von Neumann architecture** is a computer architecture in which **both program instructions and data are stored in the same main memory**. The CPU repeatedly performs the **fetch–decode–execute cycle**, fetching instructions from memory, decoding them, and executing the required primitive operations. Data is stored in **main memory, cache memory, CPU registers, and external files**. Programs are also treated as data and are stored as **machine language instructions**, where each instruction consists of an **opcode** (operation code) and **operands** (data or memory locations). This architecture forms the basis of most modern computer systems.
