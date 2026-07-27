#fuzzy-system #third-semester 
# Mutation Probability

## Definition ⭐⭐⭐

**Mutation Probability** determines **how often genes (bits) of a chromosome are randomly changed** during the mutation operation. 

---

## Key Points

* It controls **how frequently mutation occurs**.

* **0% mutation probability**
  * No mutation is performed.
  * Offspring are copied directly after crossover without any changes.

* **100% mutation probability**
  * Every bit of every chromosome is changed (flipped).
  * The chromosome becomes completely inverted.



---

## Why not use 100% Mutation?

Normally, mutation changes **only a few bits**, making small improvements to the solution.

However, if the mutation probability is **100%**:

* Every bit is flipped.
* The chromosome is completely inverted.
* This behaves like **inversion rather than normal mutation**.
* The population loses good solutions and **degenerates very quickly**, behaving almost as if there were **no useful mutation**.



---

## Example

Original chromosome:

```text
101100
```

### Normal Mutation (Low Probability)

Only one bit changes:

```text
101100
   ↓
101000
```

Small change → Small variation in the solution.

---

### 100% Mutation

Every bit flips:

```text
101100
↓
010011
```

Entire chromosome is inverted.

---

## 2-Mark Exam Answer

**Mutation Probability** is the probability that genes of a chromosome will be mutated. If it is **0%**, no mutation occurs and offspring remain unchanged after crossover. If it is **100%**, every bit of the chromosome is changed, resulting in complete inversion of the chromosome. Therefore, mutation probability is usually kept low so that only a few bits change, maintaining diversity without destroying good solutions. 

---

## Memory Trick

* **0%** → **No mutation** (copy only)
* **Low % (preferred)** → **Few bits change** ✅
* **100%** → **All bits flip (inversion)** ❌
