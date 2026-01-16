# 1️⃣ STAR SCHEMA ⭐ (Easiest)

### 👉 Idea

* **ONE fact table in the center**
* **Dimension tables directly connected**
* Shape looks like a **star**

### 📊 Example Tables

**Fact:** Sales
**Dimensions:** Time, Product, Customer, Store

---

### 📐 Simple Figure (Exam-friendly)

```
           Time
            |
Product --- FACT_SALES --- Customer
            |
          Store
```

---

### 📋 Tables View

```
FACT_SALES
-------------------------
Sale_ID
Product_ID
Customer_ID
Time_ID
Store_ID
Sales_Amount
Quantity
```

```
PRODUCT        CUSTOMER        TIME        STORE
--------       --------        ----        -----
Product_ID     Customer_ID     Time_ID     Store_ID
Name           Name            Date        City
Category       Address         Month       Country
Price
```

### ✅ Key Points

* Simple
* Fast queries
* Dimension tables are **NOT normalized**

---

# 2️⃣ SNOWFLAKE SCHEMA ❄️ (Star → Broken Dimensions)

### 👉 Idea

* Same as star schema
* BUT **dimension tables are normalized**
* Dimensions split into **smaller tables**
* Shape looks like a **snowflake**

---

### 📐 Simple Figure

```
                 Year
                  |
               Month
                  |
Product --- FACT_SALES --- Customer
   |
Category
   |
Subcategory
```

---

### 📋 Tables View

```
PRODUCT
--------
Product_ID
Name
Category_ID
```

```
CATEGORY
---------
Category_ID
Category_Name
```

```
TIME
-----
Time_ID
Month_ID
```

```
MONTH
------
Month_ID
Year
```

---

### ✅ Key Points

* Less redundancy
* More joins
* Slightly slower than star
* Looks complex ❄️

---

# 3️⃣ FACT CONSTELLATION / GALAXY SCHEMA 🌌 (Big One)

### 👉 Idea

* **Multiple fact tables**
* **Shared dimension tables**
* Looks like **many stars together**

---

### 📐 Simple Figure

```
                Time
                 |
Product --- FACT_SALES --- Customer
                 |
               Store

Product --- FACT_INVENTORY --- Store
                 |
               Supplier
```

---

### 📋 Tables Example

```
FACT_SALES           FACT_INVENTORY
----------           --------------
Product_ID           Product_ID
Customer_ID          Store_ID
Time_ID              Time_ID
Sales_Amount         Stock_Level
```

Shared Dimensions:

```
PRODUCT, TIME, STORE
```

---

### ✅ Key Points

* Used in **large data warehouses**
* Complex
* Powerful
* Supports many business processes

---

# 🔥 ONE-GLANCE MEMORY TABLE (EXAM GOLD)

| Schema             | Fact Tables | Dimension Tables | Shape        |
| ------------------ | ----------- | ---------------- | ------------ |
| Star               | 1           | Simple           | ⭐ Star       |
| Snowflake          | 1           | Normalized       | ❄️ Snowflake |
| Fact Constellation | Many        | Shared           | 🌌 Galaxy    |

---

# 🧠 Easy Exam Line to Write

> **Star schema** has a single fact table connected to denormalized dimensions.
> **Snowflake schema** is a normalized version of star schema.
> **Fact constellation** consists of multiple fact tables sharing common dimensions.

---
