
### **Models of Parallel Computation**

#### 1. **PRAM Model (Parallel Random Access Machine)**

* Assumes:

  * Multiple processors working **synchronously**
  * Shared memory accessible by all processors
* Complexity Measure:

  * Performance evaluated using the formula:

    $$
    \text{Speedup} = \frac{T(n)}{T_p(n)}
    $$

    Where:

    * $T(n)$ = Best **sequential** time
    * $T_p(n)$ = Time taken with **p** processors
* Subtypes based on memory access:

  * EREW (Exclusive Read, Exclusive Write)
  * CREW (Concurrent Read, Exclusive Write)
  * CRCW (Concurrent Read, Concurrent Write)

#### 2. **Shared Memory Model**

* Like PRAM but **asynchronous**:

  * Processors do **not** execute in lockstep
  * Similar to **multiprogramming** on a single system
* Still uses a **single address space** (shared memory)

#### 3. **Network Model**

* Processors are connected via a **network topology**
* The focus is on the **communication pattern** and delays
* Examples of topologies:

  * Mesh
  * Hypercube
  * Ring
  * Tree

#### 4. **LogP Model**

* More **realistic** parallel model than PRAM
* Accounts for communication costs:

  * **L**: Latency — delay to send a message
  * **o**: Overhead — time processor spends sending/receiving
  * **g**: Gap — minimum time between message sends
  * **P**: Number of processors
* Emphasizes **scalability and efficiency** in real systems

---

