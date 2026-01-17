## Inmon Approach (Top-Down Approach)

The **Inmon approach** builds the **enterprise data warehouse (EDW) first**, and then creates data marts from it.

It focuses on creating a centralized, integrated, and normalized warehouse before departmental analysis.

---

### Definition

> The Inmon approach is a **top-down** methodology where a centralized enterprise data warehouse is built first, and data marts are derived from it.

![](../../../../../../../Images/Second_Sem_Images/Inman%20Approach-1.png)

![](../../../../../../../Images/Second_Sem_Images/Inman%20Approach.png)

---

## Key Ideas

* Build **Enterprise Data Warehouse first**
* Use **normalized (3NF) schema**
* Data marts are created **after** EDW
* Strong emphasis on **data integration and consistency**
* Long-term, enterprise-wide view

---

## Steps in Inmon Approach

1. Collect data from source systems
2. Clean, integrate, and transform data
3. Store data in **Enterprise Data Warehouse (3NF model)**
4. Create departmental **data marts** from EDW
5. Perform analysis and reporting on data marts

---

## Architecture

```
Source Systems → ETL → Enterprise Data Warehouse → Data Marts → OLAP/Reports
```

---

## Example

For a company:

* First build one large centralized EDW
* Then create:

  * Sales data mart
  * Finance data mart
  * HR data mart

All data marts come from the same EDW.

---

## Advantages

* High data consistency
* Enterprise-wide integration
* No duplication of data
* Strong data governance
* Better for large organizations

---

## Disadvantages

* Slow implementation
* High initial cost
* Complex design
* Benefits are seen late

---

## One-line Exam Answer

> The Inmon approach is a top-down data warehouse design method that builds a centralized enterprise data warehouse first and then derives data marts from it.

