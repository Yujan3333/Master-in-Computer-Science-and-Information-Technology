- [ Superscalar and VLIW in 5 marks](%20Superscalar%20and%20VLIW%20in%205%20marks.md)
## First: the basic idea

Normally:

* CPU does **1 instruction per clock**

Multiple-issue CPU:

* CPU does **2 or more instructions per clock**

Now the question is:

> **Who decides which instructions run together?**

That’s the **only real difference**.

---

## 1️⃣ Superscalar (CPU is smart)

### Simple meaning

> In a **superscalar processor**, the **CPU hardware itself** decides which instructions can run at the same time.

### Analogy (very important)

👨‍🏫 **Teacher checks copies during exam**

* Students submit papers randomly
* Teacher decides **which copies to check together**
* Teacher handles conflicts

➡ Teacher = **CPU hardware**

---

### What happens inside CPU

* CPU looks at upcoming instructions
* Checks:

  * Data dependency
  * Resource availability
* Issues **multiple instructions per cycle** if safe

### Example

```text
I1: ADD
I2: MUL
I3: LOAD
```

CPU sees:

* ADD and LOAD can run together
* MUL waits

✔ Decision done **at runtime**

---

### Key points (easy to remember)

* Decision by **hardware**
* Instructions can run **out of order**
* Hardware is **complex**
* Programmer/compiler does **less work**

---

## 2️⃣ VLIW (Compiler is smart)

### Simple meaning

> In **VLIW**, the **compiler decides in advance** which instructions will run together.

### Analogy

🧑‍💻 **Student arranges copies before exam**

* Copies are already grouped
* Teacher just checks as given
* No decision making during exam

➡ Student = **compiler**

---

### How VLIW works

* Compiler groups instructions into **one long instruction**
* CPU simply executes them in parallel

Example VLIW instruction:

```text
[ ADD | LOAD | NOP | MUL ]
```

* Each slot = one functional unit
* `NOP` if nothing fits

---

### Key points (easy to remember)

* Decision by **compiler**
* Hardware is **simple**
* Needs **very good compiler**
* Code size is larger

---

## Superscalar vs VLIW (super simple table)

| Point                    | Superscalar  | VLIW         |
| ------------------------ | ------------ | ------------ |
| Who decides parallelism? | CPU hardware | Compiler     |
| Decision time            | Runtime      | Compile time |
| Hardware                 | Complex      | Simple       |
| Compiler work            | Less         | More         |

---

## One-line memory trick (EXAM GOLD)

* **Superscalar** → *“CPU decides”*
* **VLIW** → *“Compiler decides”*

---

## Why examiners love this topic

Because it connects:

* Pipelining
* Hazards (RAW, WAR, WAW)
* Compiler optimization
* Instruction scheduling

---

## Final takeaway

> Superscalar relies on **smart hardware**,
> VLIW relies on a **smart compiler**.
