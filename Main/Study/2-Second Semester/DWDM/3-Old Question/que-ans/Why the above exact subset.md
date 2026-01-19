## **Understanding Candidate Rule Generation**

Suppose our **frequent itemset** is:

$$
L = {A, B, C}
$$

The rule generation idea is:

> For **every non-empty subset** $S$ of $L$, we can form a rule:
>
> $$
> S \Rightarrow (L - S)
> $$

where $L - S$ is the set of items in $L$ **not in $S$**.

This guarantees that the **union of LHS and RHS is exactly the frequent itemset**, which is necessary because confidence is based on **support-count of the whole frequent itemset**.

---

### **Step 1: List all non-empty subsets of L**

$$
{A}, {B}, {C}, {A,B}, {A,C}, {B,C}
$$

We **do not include the full set** ${A,B,C}$ because we need something to go on the RHS.

---

### **Step 2: Generate rules for each subset S**

Rule formula:

$$
S \Rightarrow (L - S)
$$

* If $S = {A}$, then $L - S = {B,C}$ → Rule: ${A} \Rightarrow {B,C}$ ✅
* If $S = {B}$, then $L - S = {A,C}$ → Rule: ${B} \Rightarrow {A,C}$ ✅
* If $S = {C}$, then $L - S = {A,B}$ → Rule: ${C} \Rightarrow {A,B}$ ✅
* If $S = {A,B}$, then $L - S = {C}$ → Rule: ${A,B} \Rightarrow {C}$ ✅
* If $S = {A,C}$, then $L - S = {B}$ → Rule: ${A,C} \Rightarrow {B}$ ✅
* If $S = {B,C}$, then $L - S = {A}$ → Rule: ${B,C} \Rightarrow {A}$ ✅

---

### **Important Notes**

1. **Every subset generates exactly one rule** using $S \Rightarrow (L-S)$.
   That’s why in the previous example I only wrote a few; it wasn’t complete.

2. **You do not generate "vice versa" for every small subset separately**, because if you take $C \Rightarrow AB$, that is already included in $S = {C}$.

3. The smaller subsets (single items) give rules with multiple items on RHS; the larger subsets (2 items) give rules with single items on RHS.

So the **full set of candidate rules for {A,B,C}** is:

* ${A} \Rightarrow {B,C}$
* ${B} \Rightarrow {A,C}$
* ${C} \Rightarrow {A,B}$
* ${A,B} \Rightarrow {C}$
* ${A,C} \Rightarrow {B}$
* ${B,C} \Rightarrow {A}$

No need to flip them the other way; it would be **repetition**.

---
