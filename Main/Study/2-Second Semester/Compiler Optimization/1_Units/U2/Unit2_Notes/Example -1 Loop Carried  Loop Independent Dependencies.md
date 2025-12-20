![](../../../../../../../Images/Second_Sem_Images/Example%20-1%20Loop%20Carried%20%20Loop%20Independent%20Dependencies.png)

----
### Given loop

```
Do I = 1, 9
   S1: A(I) = ...
   S2: ... = A(10 - I)
End Do
```

---

## Step 1: Dependence condition

Both statements access the same array element when

$$
I = 10 - J
$$

or

$$
I + J = 10
$$

---

## Step 2: Loop-independent dependence

Loop-independent means **same iteration**:

$$
I = J
$$

Substitute into $I + J = 10$:

$$
2I = 10 \Rightarrow I = 5
$$

✔ At `I = 5`, `S1` writes `A(5)` and `S2` reads `A(5)` **in the same iteration**.

➡ **Loop-independent dependence exists**

---

## Step 3: Loop-carried dependence

Loop-carried means **different iterations**:

$$
I \ne J
$$

Example:

* `S1` at `I = 2` writes `A(2)`
* `S2` at `J = 8` reads `A(2)`

✔ Access occurs across iterations.

➡ **Loop-carried dependence exists**

---

## ✅ Final Answer (exam-ready)

* **Loop-independent dependence:** ✔ Present (at `I = 5`)
* **Loop-carried dependence:** ✔ Present (for `I + J = 10`, `I ≠ J`)
* **Overall classification:**
  The loop has **both loop-independent and loop-carried true dependences**

---

If you want, I can also give a **one-sentence answer** exactly how examiners expect it.
