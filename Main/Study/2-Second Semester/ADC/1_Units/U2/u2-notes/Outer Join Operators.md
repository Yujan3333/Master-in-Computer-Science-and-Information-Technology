### Outer Join Operators

* **LEFT OUTER JOIN**: keeps all tuples from the left relation.
* **RIGHT OUTER JOIN**: keeps all tuples from the right relation.
* **FULL OUTER JOIN**: keeps all tuples from both relations
  (equivalent to: LEFT OUTER JOIN ∪ RIGHT OUTER JOIN).

Example:

```sql
SELECT FNAME, DNAME
FROM EMPLOYEE LEFT OUTER JOIN DEPARTMENT
ON DNO = DNUMBER;
```

Meaning:

* If an employee has a matching department → show `(FNAME, DNAME)`
* If an employee has **no** matching department → show `(FNAME, NULL)`

So no employee is lost in the result.

---

## Implementing Outer Join by Modifying Join Algorithms

Any normal join algorithm (Nested Loop, Sort-Merge, Hash Join) can be adapted.

For **LEFT OUTER JOIN**:

1. Treat the **left relation** as the outer relation.
2. For each tuple in the left relation:

   * Try to find matching tuples in the right relation.
   * If a match exists → output concatenated tuple.
   * If no match exists → output:

     ```
     (left_tuple attributes, NULLs for right attributes)
     ```

So logic becomes:

```
for each tuple r in R:
    matched = false
    for each tuple s in S:
        if join_condition(r,s) is true:
            output (r,s)
            matched = true
    if matched == false:
        output (r, NULLs)
```

This is the core idea of LEFT OUTER JOIN.

For:

* **RIGHT OUTER JOIN** → symmetric (right relation is outer).
* **FULL OUTER JOIN** → combine both.

---

## Implementing Outer Join Using Relational Algebra Operators

Given your example:

EMPLOYEE ⟕ DEPARTMENT
(join condition: DNO = DNUMBER)

Steps:

1. **Compute the normal join**

```
TEMP1 ← πFNAME,DNAME (EMPLOYEE ⋈DNO=DNUMBER DEPARTMENT)
```

This gives only matching employees and departments.

---

2. **Find employees that did not appear in the join**

```
TEMP2 ← πFNAME(EMPLOYEE) − πFNAME(TEMP1)
```

This gives employees with **no department**.

---

3. **Pad these tuples with NULL for department**

```
TEMP2 ← TEMP2 × 'null'
```

Now TEMP2 looks like:

```
(FNAME, NULL)
```

---

4. **Union both results**

```
RESULT ← TEMP1 ∪ TEMP2
```

This produces the **LEFT OUTER JOIN** result.

---

## Cost of Outer Join

Since it is built using:

* Join
* Projection
* Difference
* Cartesian product (for null padding)
* Union

Total cost =

```
Cost(join) +
Cost(projections) +
Cost(difference) +
Cost(union)
```

So outer joins are generally more expensive than simple inner joins.

---

## Intuition

Normal JOIN:

> “Give me only matching rows.”

LEFT OUTER JOIN:

> “Give me all left rows.
> If no match exists, fill right side with NULL.”
