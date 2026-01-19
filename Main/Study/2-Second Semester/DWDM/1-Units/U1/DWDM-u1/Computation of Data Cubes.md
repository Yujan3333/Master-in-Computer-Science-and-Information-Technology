Think of a **data cube** as a table that can be summarized in many ways
(by time, by location, by product, by customer, etc.).
Each way of summarizing is called a **cuboid**.

To compute these cuboids, we have three strategies:

---

### 1. No Materialization

Nothing is pre-computed.
Only the base data is stored.

* All summaries are calculated **when the user asks**
* Very low storage cost
* Very slow query response

Simple line for exam:

> No materialization means no cuboids are pre-computed; all aggregates are computed on demand, leading to low storage but very slow query performance.

---

### 2. Full Materialization

All possible cuboids are pre-computed and stored.

* Very fast query response
* Very high storage cost
* Suffers from **curse of dimensionality** (number of cuboids grows exponentially)

Simple line for exam:

> Full materialization pre-computes and stores all possible cuboids, giving fast query performance but requiring very large storage space.

---

### 3. Partial Materialization

Only some important cuboids are pre-computed.

* Balanced approach
* Medium storage
* Medium speed

Simple line for exam:

> Partial materialization selectively pre-computes only a subset of cuboids, providing a trade-off between storage space and query response time.

---

Easy comparison table for exam:

| Method                  | Pre-computation | Storage Cost | Query Speed |
| ----------------------- | --------------- | ------------ | ----------- |
| No materialization      | None            | Very low     | Very slow   |
| Full materialization    | All cuboids     | Very high    | Very fast   |
| Partial materialization | Some cuboids    | Medium       | Medium      |

---

One-line memory trick:

* **No** materialization → compute later → slow
* **Full** materialization → compute everything → fast but heavy
* **Partial** materialization → compute smartly → balanced
