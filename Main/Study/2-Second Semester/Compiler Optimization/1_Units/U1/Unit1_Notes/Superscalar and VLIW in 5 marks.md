
## Superscalar and VLIW Processors

A **multiple-issue processor** can issue more than one instruction in a single clock cycle. **Superscalar** and **VLIW** are two common types of multiple-issue processors.

### Superscalar Processor

In a **superscalar processor**, the **hardware dynamically decides** which instructions can be executed in parallel. The processor checks data dependencies, resource availability, and may execute instructions **out of order**. This approach provides flexibility but requires **complex hardware**.

### VLIW (Very Long Instruction Word) Processor

In a **VLIW processor**, the **compiler statically schedules** instructions at compile time. Multiple operations are packed into a single long instruction word, and the hardware executes them in parallel without runtime checking. This simplifies hardware but increases **compiler complexity**.

### Comparison

Superscalar processors rely on **hardware intelligence**, whereas VLIW processors rely on **compiler intelligence** to exploit instruction-level parallelism.

---

### (Optional last line if space allows)

Superscalar offers better adaptability, while VLIW offers simpler hardware design.
