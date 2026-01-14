Yes, very often it **returns empty**, but the important point is *how* it is used.

Semantic Query Optimization is used **before execution** to check whether:

1. The query is impossible
2. The query is redundant
3. The query can be simplified

So DBMS can:

* Avoid scanning tables
* Avoid joins
* Avoid disk I/O
* Save time and cost

Returning empty is just one special case.

---

## Case 1: Query is Impossible → Return Empty

### Given

Constraint:

> $AGE\ge18$

Query:

```sql
SELECT *
FROM STUDENT
WHERE AGE < 18;
```

### Logic

From DB:
$$AGE\ge18$$

From query:
$$AGE<18$$

Both cannot be true together.

### Action by DBMS

* DBMS does **not execute** the query.
* Directly returns an **empty result**.
* No table scan, no computation.

This is the strongest use.

---

## Case 2: Query is Redundant → Remove Condition

### Given

Constraint:

> $SALARY\ge10000$

Query:

```sql
SELECT *
FROM EMPLOYEE
WHERE SALARY >= 10000;
```

Since every employee already satisfies:
$$SALARY\ge10000$$

The WHERE clause is useless.

Optimized query:

```sql
SELECT *
FROM EMPLOYEE;
```

Here:

* Result is NOT empty
* Query becomes simpler and faster

---

## Case 3: Query Can Be Simplified

### Given

Constraint:

> Every employee works in exactly one department.

Query:

```sql
SELECT *
FROM EMPLOYEE E, DEPARTMENT D
WHERE E.DNO = D.DNO;
```

The join is always valid.
Optimizer may choose a simpler join plan because it knows:

* No missing matches
* No NULLs
* Join is safe

---

## So how is it used?

Semantic optimization is used to:

| Situation             | Action                   |
| --------------------- | ------------------------ |
| Condition impossible  | Return empty immediately |
| Condition always true | Remove it                |
| Join guaranteed       | Simplify execution       |
| Contradiction found   | Skip query execution     |

---

## Exam One Line

Semantic query optimization uses constraints to either:

* Detect impossible queries and return empty, or
* Remove redundant conditions and simplify queries before execution.
