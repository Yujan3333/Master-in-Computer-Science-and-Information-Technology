# 🔹 OLAP Operations in Multidimensional Data Model

OLAP operations are used to **analyze data cubes** from different perspectives.

---

## 1. **Slice**

* Selects a **single dimension** of the cube to create a **subcube**.
* Example: Select sales data for `Time = Q1`.
* Effect: Reduces dimensionality by 1.

```
Original Cube → Slice on Time = Q1 → Subcube with only Q1 data
```

![](../../../../../../../Images/Second_Sem_Images/OLAP%20Operations-slice.png)

---

## 2. **Dice**

* Selects **two or more dimensions** from the cube to create a **smaller subcube**.
* Example: Select `Location = Mahendranagar or Dhangadi`, `Time = Q1 or Q2`, `Product = TV or PC`.

```
Original Cube → Dice → Subcube satisfying multiple criteria
```
![](../../../../../../../Images/Second_Sem_Images/OLAP%20Operations.png)


---

## 3. **Roll-up (Drill-up)**

* Performs **aggregation** by climbing **up a concept hierarchy** or reducing dimensions.
* Example: Aggregate city-level sales to **province-level sales**.
* Effect: View **summary data**.
![](../../../../../../../Images/Second_Sem_Images/OLAP%20Operations-rollup.png)


---

## 4. **Drill-down (Roll-down)**

* Reverse of Roll-up.
* Moves **down the hierarchy** or adds a new dimension.
* Example: From quarterly sales to **monthly sales**, or from province to city-level.
* Effect: View **detailed data**.
![](../../../../../../../Images/Second_Sem_Images/OLAP%20Operations-1.png)

---

## 5. **Pivot (Rotate)**

* **Rotates the cube axes** to view data from a different perspective.
* Example: Swap rows and columns in a report to analyze products by location instead of location by products.

---

## 📝 Quick Exam Summary Table

| Operation  | Description                      | Example                                            |
| ---------- | -------------------------------- | -------------------------------------------------- |
| Slice      | Select one dimension             | Time = Q1                                          |
| Dice       | Select multiple dimensions       | Location = Dhangadi/Mahendranagar, Product = TV/PC |
| Roll-up    | Aggregate data / climb hierarchy | City → Province                                    |
| Drill-down | Detail data / descend hierarchy  | Province → City                                    |
| Pivot      | Rotate axes for new view         | Swap Product and Location axes                     |

---

💡 **Tip for exams:**

* Draw a **small 3D cube diagram** showing one example of **slice, dice, roll-up, drill-down, pivot**.
* Even a 2D representation is enough to score marks.

---
