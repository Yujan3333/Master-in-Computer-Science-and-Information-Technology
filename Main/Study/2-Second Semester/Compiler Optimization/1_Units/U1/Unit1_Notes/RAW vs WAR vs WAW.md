
## Data Hazards in Pipelining

| Hazard  | Full Form         | What goes wrong                            | Instruction dependency |
| ------- | ----------------- | ------------------------------------------ | ---------------------- |
| **RAW** | Read After Write  | Read happens **before** the required write | True dependency        |
| **WAR** | Write After Read  | Write happens **before** the required read | Anti-dependency        |
| **WAW** | Write After Write | Writes happen in **wrong order**           | Output dependency      |

---

## 1️⃣ RAW – Read After Write (Most common)

### Meaning

An instruction **tries to read a value before it is written** by a previous instruction.

### Example

```text
I1: R1 = R2 + R3
I2: R4 = R1 + R5
```

* `I2` needs `R1`
* `I1` has not written `R1` yet ❌

### Problem

`I2` reads **old or incorrect value**

### Occurs in

* Almost all pipelines

### Solution

* Pipeline stall
* Forwarding (bypassing)

---

## 2️⃣ WAR – Write After Read

### Meaning

An instruction **writes to a register before an earlier instruction reads it**.

### Example

```text
I1: R4 = R1 + R2
I2: R1 = R3 + R5
```

* `I1` needs to **read R1**
* `I2` **writes to R1 early** ❌

### Problem

`I1` reads **wrong value**

### Occurs in

* Out-of-order execution pipelines

### Does NOT occur in

* In-order pipelines

### Solution

* Register renaming

---

## 3️⃣ WAW – Write After Write

### Meaning

Two instructions **write to the same register**, but **order of writes is reversed**.

### Example

```text
I1: R1 = R2 + R3
I2: R1 = R4 + R5
```

Correct order:

```text
I1 writes → I2 writes
Final R1 = result of I2
```

Pipeline problem:

```text
I2 writes first
I1 writes later ❌
```

### Problem

Final value becomes **incorrect**

### Occurs in

* Superscalar
* Out-of-order execution

### Solution

* Register renaming
* In-order writeback

---

## Dependency Types (Very Important)

| Hazard | Dependency type   |
| ------ | ----------------- |
| RAW    | True dependency   |
| WAR    | Anti-dependency   |
| WAW    | Output dependency |

---

## Quick Memory Trick

* **RAW** → "Need value, not written yet"
* **WAR** → "Overwrite before read"
* **WAW** → "Wrong write order"

---

## One-line exam definitions

* **RAW:** Instruction reads a register before a previous instruction writes to it.
* **WAR:** Instruction writes to a register before a previous instruction reads it.
* **WAW:** Two instructions write to the same register and write order is violated.

---