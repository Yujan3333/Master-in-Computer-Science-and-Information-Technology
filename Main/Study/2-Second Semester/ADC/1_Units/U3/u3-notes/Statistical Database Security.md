
## **Statistical Databases**

**1. Purpose**

* Primarily used to **produce statistics** on various populations.
* Populations are sets of tuples in a relation that satisfy a **selection condition**.
* Users can retrieve **statistical summaries** but **not individual data**.

**2. Statistical Queries**

* Involve applying **aggregate/statistical functions** to a population of tuples.
* Common functions:

  * `COUNT` – number of tuples in a population
  * `SUM` – sum of values in a population
  * `AVERAGE` – mean value of a population
  * `MIN` / `MAX` – minimum or maximum values
  * `STANDARD DEVIATION` – spread of values

**Example:**

* Retrieve **average income** or **number of individuals** in a population.
* **Not allowed:** retrieving income of a specific individual.

**3. Security Considerations**

* **Goal:** Protect confidential data about individuals while allowing statistical summaries.
* Achieved by:

  * **Prohibiting queries** that retrieve specific attribute values.
  * **Allowing only aggregate/statistical queries.**
* **DBMS responsibility:** Ensure **individual confidentiality** while providing **useful summaries**.

**4. Inference Risk**

* Sequences of statistical queries could allow **deducing individual values**, especially if the population is **small**.
* Privacy protection must account for such inference attacks.

---

### **Key Takeaways**

* Statistical databases balance **useful statistical analysis** with **individual privacy**.
* Only **aggregate queries** are permitted; **direct access to individual data is forbidden**.
* DBMS must guard against **inference attacks** from multiple queries.

---
