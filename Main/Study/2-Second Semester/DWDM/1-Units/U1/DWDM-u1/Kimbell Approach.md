## Kimball Approach (Bottom-Up Approach)

The **Kimball approach** is a data warehouse design methodology that builds the warehouse by creating **data marts first** and then integrating them into a complete data warehouse.

It focuses on business processes and dimensional modeling.

---

### Definition

> The Kimball approach is a **bottom-up** method where individual data marts are designed for specific business processes and later combined using conformed dimensions to form an enterprise data warehouse.

![](../../../../../../../Images/Second_Sem_Images/Kimbell%20Approach.png)


---

## Key Ideas

* Build **data marts first**
* Use **dimensional modeling**
* Use **star schema / snowflake schema**
* Integrate data marts using **conformed dimensions**
* Deliver results quickly

---

## Steps in Kimball Approach

1. Identify business processes

   * Sales, inventory, finance, marketing, etc.

2. Choose the grain

   * Decide what one row in the fact table represents
   * Example: one sale per item per day

3. Identify dimensions

   * Time, customer, product, store, etc.

4. Identify facts

   * Sales amount, quantity sold, profit, etc.

5. Build data marts

   * One data mart per business process

6. Integrate using conformed dimensions

   * Same dimension tables shared across marts
   * Example: same `Time`, `Product`, `Customer` dimensions

---

## Architecture

```
Source Systems → ETL → Data Marts → Integrated Data Warehouse
```

---

## Example

For a retail company:

* Sales Data Mart
* Inventory Data Mart
* Customer Data Mart

All use:

* Same Time dimension
* Same Product dimension

So they become integrated automatically.

---

## Advantages

* Faster implementation
* Easy to understand
* Business-user friendly
* High query performance
* Flexible and scalable
* Supports OLAP well

---

## Disadvantages

* Harder to maintain enterprise-wide consistency
* Risk of duplication if dimensions are not carefully designed
* Integration depends heavily on conformed dimensions

---

## One-line Exam Answer

> The Kimball approach is a bottom-up data warehouse design method that builds data marts using dimensional models and integrates them using conformed dimensions.
