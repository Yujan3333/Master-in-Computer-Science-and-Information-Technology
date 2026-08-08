## **Mining Class Comparisons**

### **Purpose**

* Instead of describing just **one class**, this method compares a **target class** with **contrasting classes**.
* Goal: Find patterns that **distinguish the target from others**.
* Classes are comparable if they share **similar attributes**.
  **Example:** Graduate students vs. Undergraduate students (comparable)
  **Non-example:** Person, address, item (not comparable)

---

### **Steps / Method**

1. **Data Collection**

   * Collect **relevant data** for both target and contrasting classes.
   * Example (DMQL query):

   ```sql
   use Big_University_DB
   mine comparison as "graduate vs undergraduate students"
   in relevance to name, gender, major, birth_place, birth_date, residence, phone#, gpa
   for "graduate students" where status in "graduate"
   versus "undergraduate students" where status in "undergraduate"
   analyze count%
   from student
   ```

---

2. **Dimension Relevance Analysis**

   * Select only **important attributes** for comparison.
   * Remove irrelevant or weakly relevant attributes: **name, phone#, residence, birth_place**.
   * Example:

| Target (Graduate)      | Contrasting (Undergraduate) |
| ---------------------- | --------------------------- |
| Major, Birth_date, GPA | Major, Birth_date, GPA      |

---

3. **Synchronous Generalization**

   * Generalize attribute values for both classes using **concept hierarchies**.
   * Example: `Birth_date → Age_range`, `GPA → grade categories`.
   * Generalized table:

   **Graduate students:**

| Major    | Age_range | GPA       | Count % |
| -------- | --------- | --------- | ------- |
| Science  | 21–25     | Good      | 5.53%   |
| Science  | 26–30     | Good      | 5.02%   |
| Science  | >30       | Very Good | 5.86%   |
| Business | >30       | Excellent | 4.68%   |

   **Undergraduate students:**

| Major    | Age_range | GPA       | Count % |
| -------- | --------- | --------- | ------- |
| Science  | 16–20     | Fair      | 5.53%   |
| Science  | 16–20     | Good      | 4.53%   |
| Science  | 26–30     | Good      | 2.32%   |
| Business | >30       | Excellent | 0.68%   |

---

4. **Presentation of Derived Comparison**

   * Visualize in **tables, graphs, rules**, or **cross-tabs**.
   * Include **contrasting measure**, e.g., count% difference.
   * Example insight:

     > 5.02% of graduate Science students aged 26–30 have a “Good” GPA, whereas only 2.32% of undergraduates have the same characteristic.

---

### **Exam Tip**

* Focus on these **keywords**: **target vs contrasting class**, **relevant attributes**, **generalization**, **presentation (tables/graphs)**.
* Small **diagram or table** showing generalized comparison often fetches marks.

---