## RAID (Redundant Array of Independent Disks)

RAID is a technique that combines multiple physical disks into one logical unit to improve:

* Performance
* Reliability
* Storage capacity

---

## RAID 0 (Striping)

**Idea:** Data is split and stored across multiple disks.

**Features:**

* No redundancy
* High speed
* No fault tolerance

**Advantage:**

* Very fast read/write

**Disadvantage:**

* If one disk fails, all data is lost

**Use:** When performance is more important than safety.

---

## RAID 1 (Mirroring)

**Idea:** Same data is stored on two disks.

**Features:**

* Complete data duplication
* High reliability

**Advantage:**

* Data safe even if one disk fails

**Disadvantage:**

* Storage efficiency is only 50%

**Use:** When data safety is critical.

---

## RAID 2 (Bit-level Striping with Hamming Code)

**Idea:**

* Data is striped at bit level
* Extra disks store error-correcting codes (ECC)

**Features:**

* Very complex
* Rarely used in practice

**Advantage:**

* Error detection and correction

**Disadvantage:**

* High cost and complexity

---

## RAID 3 (Byte-level Striping with Dedicated Parity)

**Idea:**

* Data is striped at byte level
* One disk stores parity

**Features:**

* One disk is dedicated for parity

**Advantage:**

* Good for large sequential data

**Disadvantage:**

* Parity disk becomes bottleneck

---

## RAID 4 (Block-level Striping with Dedicated Parity)

**Idea:**

* Data is striped in blocks
* One disk stores parity

**Features:**

* Faster random reads than RAID 3

**Advantage:**

* Better read performance

**Disadvantage:**

* Parity disk bottleneck during writes

---

## RAID 5 (Block-level Striping with Distributed Parity)

**Idea:**

* Data and parity are distributed across all disks

**Features:**

* No dedicated parity disk
* Fault tolerance for one disk failure

**Advantage:**

* Good balance between performance and reliability

**Disadvantage:**

* Write operations are slower due to parity update

---

## RAID 6 (Block-level Striping with Double Distributed Parity)

**Idea:**

* Similar to RAID 5, but uses **two parity blocks**

**Features:**

* Can tolerate failure of **two disks**
* Parity is distributed

**Advantage:**

* Very high reliability

**Disadvantage:**

* More storage overhead
* Slower writes than RAID 5

---

## Quick Comparison (Exam Style)

| RAID Level | Redundancy               | Disk Failure Tolerance | Performance     |
| ---------- | ------------------------ | ---------------------- | --------------- |
| RAID 0     | No                       | 0                      | Very High       |
| RAID 1     | Yes (Mirroring)          | 1                      | High read       |
| RAID 2     | Yes (ECC)                | 1                      | Rarely used     |
| RAID 3     | Yes (Parity)             | 1                      | High sequential |
| RAID 4     | Yes (Parity)             | 1                      | Good reads      |
| RAID 5     | Yes (Distributed Parity) | 1                      | Balanced        |
| RAID 6     | Yes (Double Parity)      | 2                      | High safety     |

---

**One-line memory trick:**

* RAID 0 → Speed
* RAID 1 → Safety
* RAID 5 → Balance
* RAID 6 → Maximum safety
