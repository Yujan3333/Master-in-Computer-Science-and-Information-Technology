## RAM Model (Sequential Computing)

- **One processor** does everything
- Each operation (add, subtract, etc.) takes **1 unit of time**
- No communication needed since there's only one processor

## Parallel Computing Challenge

**Problem:** Multiple processors need to **communicate and coordinate** their work

- This adds complexity that doesn't exist in sequential computing
- Called **inter-process communication**

## Two Main Parallel Computing Models:

### 1. **Fixed Connection Networks**

**Processors connected by specific wiring patterns**

- **Structure:** Graph where nodes = processors, edges = communication links
- **Examples:**
    - **Mesh:** Processors arranged in a grid (like a checkerboard)
    - **Hypercube:** More complex cube-like connections

**Communication:** Processors can only talk to their directly connected neighbors

### 2. **Shared Memory Model**

**All processors access the same memory pool**

- **Structure:** Multiple processors + one big shared memory block
- **Communication Process:**
    1. Processor A writes message to memory location
    2. Processor B reads from that same location
- **Advantage:** Any processor can talk to any other through shared memory

## Key Difference:

- **Fixed Connection:** Limited by physical wiring - like having walkie-talkies with limited range
- **Shared Memory:** Like having a bulletin board everyone can read/write to

Both models solve the same problem (processor communication) but in different ways