![](../../../../../../../Images/Second_Sem_Images/Numerical%20Random%20Forest.png)

Construct random forest having 3 decision trees three by using feature sample {age, income, student} {age, income, credit_rating} and {Income, Student, credit_rating}.
Predict class label of the tuple:

**X = (age = youth, income = medium, student = yes,credit_rating=fair**)


---
# Answer
We build 3 trees using only the given feature subsets. For splitting, we use the same idea as ID3: choose the attribute with highest information gain among the allowed features.

Target tuple:
$$
X=(\text{youth},\ \text{medium},\ \text{yes},\ \text{fair})
$$

Class: buys_computer ∈ {yes, no}

---

## Tree 1

Features = {age, income, student}

From the ID3 example, **age** is the best root attribute.

Split by **age**:

1. age = youth
   Records: 1,2,8,9,11
   Classes: no, no, no, yes, yes → mixed
   Now use {income, student}.

For these:

* student = yes → records 9,11 → both **yes**
* student = no → records 1,2,8 → all **no**

So subtree:

```
age
 ├─ youth:
 │    └─ student
 │        ├─ yes → yes
 │        └─ no  → no
 ├─ middle_aged → yes (all are yes)
 └─ senior → depends, but not needed for X
```

Now classify X for Tree 1:

* age = youth
* student = yes

So prediction:
$$
T_1(X) = \text{yes}
$$

---

## Tree 2

Features = {age, income, credit_rating}

Again, **age** is best root.

Split by **age**:

1. age = youth
   Records: 1,2,8,9,11
   Classes: no, no, no, yes, yes

Use {income, credit_rating}.

Check credit_rating:

* fair → records 1,8,9 → no, no, yes (mixed)
* excellent → records 2,11 → no, yes (mixed)

Try income:
For youth:

* income = high → records 1,2 → no, no → no
* income = medium → records 8,11 → no, yes → mixed
* income = low → record 9 → yes

Then refine income = medium using credit_rating:

* record 8: fair → no
* record 11: excellent → yes

So subtree:

```
age
 ├─ youth:
 │    └─ income
 │        ├─ high → no
 │        ├─ low → yes
 │        └─ medium:
 │              └─ credit_rating
 │                   ├─ fair → no
 │                   └─ excellent → yes
 ├─ middle_aged → yes
 └─ senior → not needed here
```

Now classify X:

* age = youth
* income = medium
* credit_rating = fair

So:
$$
T_2(X) = \text{no}
$$

---

## Tree 3

Features = {income, student, credit_rating}

Now we cannot use age. We pick the best root among these.
From the classic example, **student** gives strong separation.

Split by **student**:

1. student = yes
   Records: 5,6,7,9,10,11,13
   Classes: yes, no, yes, yes, yes, yes, yes
   Mostly **yes**, one no.

Use {income, credit_rating}:

Check credit_rating:

* fair → records 5,9,10,13 → all **yes**
* excellent → records 6,7,11 → no, yes, yes → mixed

For excellent, check income:

* income = low → record 6 → no
* income = low? actually:

  * 6: low → no
  * 7: low → yes
  * 11: medium → yes

So subtree:

```
student
 ├─ yes:
 │    └─ credit_rating
 │        ├─ fair → yes
 │        └─ excellent:
 │              └─ income
 │                   ├─ low → (mostly yes, but one no; usually take majority → yes)
 │                   └─ medium → yes
 └─ no → mostly no (not needed for X)
```

Now classify X:

* student = yes
* credit_rating = fair

So:
$$
T_3(X) = \text{yes}
$$

---

## Final Voting (Random Forest)

Tree predictions:

| Tree   | Prediction |
| ------ | ---------- |
| Tree 1 | yes        |
| Tree 2 | no         |
| Tree 3 | yes        |

Majority vote:

$$
\text{yes, no, yes} \Rightarrow \boxed{\text{yes}}
$$

---

## Final Answer

The predicted class label for

$$
X=(\text{youth},\ \text{medium},\ \text{yes},\ \text{fair})
$$

using the Random Forest with 3 trees is:

$$\boxed{\text{buys\_computer = yes}}$$
