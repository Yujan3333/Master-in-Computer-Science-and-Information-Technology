Assume this SQL query:

```sql
SELECT E.ENAME, D.DNAME
FROM EMPLOYEE E, DEPARTMENT D
WHERE E.DNO = D.DNO
AND E.SALARY > 50000
AND D.LOCATION = 'KTM';
```

Relational algebra form:

$$\pi_{ENAME,DNAME}(\sigma_{E.SALARY>50000\land D.LOCATION='KTM'}(EMPLOYEE;\bowtie_{E.DNO=D.DNO};DEPARTMENT))$$

---

## Tree 1 (Bad / Unoptimized Tree)

Join first, then apply selections and projections:

```
        π
        |
        σ (E.SALARY>50000 AND D.LOCATION='KTM')
        |
        ⋈ (E.DNO = D.DNO)
       / \
 EMPLOYEE  DEPARTMENT
```

Problem:

* Joins full EMPLOYEE and DEPARTMENT tables.
* Very large intermediate result.
* Slow and costly.

---

## Tree 2 (Good / Heuristically Optimized Tree)

Push selections and projections before join:

```
                   π
                   |
           ⋈ (E.DNO = D.DNO)
            /            \
         /                  \
        π                    π
        |                    |
    σ(E.SAL>50000)   σ(D.LOCATION='KTM')
       |                         |
    EMPLOYEE               DEPARTMENT
```

---

## Five Heuristic Rules Shown with This Example

### 1. Perform Selection Early

Apply σ before join:

Instead of:
$$\sigma(EMPLOYEE\bowtie DEPARTMENT)$$

Do:
$$\sigma(EMPLOYEE)\bowtie\sigma(DEPARTMENT)$$

Here:

* $\sigma_{E.SALARY>50000}(EMPLOYEE)$
* $\sigma_{D.LOCATION='KTM'}(DEPARTMENT)$

This reduces rows before joining.

---

### 2. Perform Projection Early

Project only needed columns:

EMPLOYEE needs: ENAME, DNO
DEPARTMENT needs: DNAME, DNO

$$\pi_{ENAME,DNO}(\sigma_{E.SALARY>50000}(EMPLOYEE))$$
$$\pi_{DNAME,DNO}(\sigma_{D.LOCATION='KTM'}(DEPARTMENT))$$

This reduces columns before join.

---

### 3. Push Operations Down the Tree

Move σ and π as close to leaf nodes as possible.

Bad:
$$\sigma(\pi(EMPLOYEE\bowtie DEPARTMENT))$$

Good:
$$\pi(\sigma(EMPLOYEE))\bowtie\pi(\sigma(DEPARTMENT))$$

---

### 4. Execute Most Restrictive Condition First

If:

* Salary > 50000 removes 70% employees
* Location = 'KTM' removes 90% departments

Apply both before join so the join size becomes very small.

---

### 5. Avoid Large Intermediate Results

Compare sizes:

Tree 1:
$$|EMPLOYEE\bowtie DEPARTMENT|$$
(very large)

Tree 2:
$$|\sigma(EMPLOYEE)\bowtie\sigma(DEPARTMENT)|$$
(very small)

Smaller intermediate relations → faster execution.

---

## Final Exam Line

Bad tree:
$$\pi(\sigma(EMPLOYEE\bowtie DEPARTMENT))$$

Good tree:
$$\pi((\pi(\sigma(EMPLOYEE)))\bowtie(\pi(\sigma(DEPARTMENT))))$$

This shows **5 heuristic rules** using **2 trees** in the simplest possible way.
