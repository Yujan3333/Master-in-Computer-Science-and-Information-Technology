## Concurrency Control and Recovery Problems in Distributed Databases
### 1. Dealing with Multiple Copies of Data Items

* Concurrency control must maintain **global consistency** among all replicas.
* Recovery mechanism must restore **all copies** and keep them consistent after failure.

---

### 2. Failure of Individual Sites

* Failure of one or two sites should **not stop the whole system**.
* Recovery scheme must repair failed sites before they are reused.
* Database availability should be preserved as much as possible.

---

### 3. Communication Link Failure

* Failure of network links may cause **network partitioning**.
* Even if all sites are running, communication failure can make the database unavailable.

---

### 4. Distributed Commit

* A transaction is split into subtransactions and executed at multiple sites.
* Commit must be coordinated using:

  * Two-Phase Commit (2PC)
  * Three-Phase Commit (3PC)

---

### 5. Distributed Deadlock

* Deadlocks may involve transactions at different sites.
* Must be detected and resolved in a **distributed manner**.

---

## Distributed Concurrency Control Based on Replicated Data

### 1. Primary Site Technique

**Idea:**
One site is chosen as the **primary site** (coordinator).

**Transaction Management:**

* All concurrency control and commit decisions are made here.
* In Two Phase Locking (2PL), this site:

  * Grants locks
  * Releases locks
* If all sites follow 2PL, serializability is guaranteed.

#### Advantages

* Simple extension of centralized 2PL.
* Data is locked at only one site but accessible everywhere.

#### Disadvantages

* Primary site becomes a bottleneck.
* If it fails, the entire system becomes inaccessible.

**Backup Site:**

* A backup acts as a shadow of the primary site.
* If the primary fails, the backup becomes the new primary.

![](../../../../../../../Images/Second_Sem_Images/Overview%20of%20Unit%206-primary%20site.png)

---

### 2. Primary Copy Technique

**Idea:**
Instead of a site, each **data item** has a designated primary copy.
Only the primary copy is locked to access the data item.

#### Advantages

* Locking load is distributed among sites.
* No single site becomes overloaded.

#### Disadvantages

* Identifying primary copies is complex.
* Requires a **distributed directory** to track primary copies.

---

## Recovery from Coordinator Failure

### Case 1: Primary Site without Backup

* Abort and restart all active transactions.
* Elect a new coordinator.
* Resume transaction processing.

### Case 2: Primary Site with Backup

* Suspend all active transactions.
* Backup site becomes the new primary.
* Choose a new backup site.
* Resume transaction management.

### Case 3: Both Primary and Backup Fail

* Use an **election algorithm** to select a new coordinator.

---

## Concurrency Control Based on Voting

**Idea:**
No primary site or primary copy exists.

**Procedure:**

1. Send lock request to all sites holding the data item.
2. If a **majority** grants the lock, the transaction proceeds.
3. Locking decision is broadcast to all involved sites.

**Timeout Rule:**

* If no vote is received within a time limit, the transaction is aborted.

**Advantage:**

* No single point of failure.

**Disadvantage:**

* High communication overhead.
* Slower than primary-based techniques.

---
