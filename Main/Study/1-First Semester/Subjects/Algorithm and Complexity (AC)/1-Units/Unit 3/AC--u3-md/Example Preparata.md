

* How bitonic sequences are built
* How bitonic merges are performed
* And how the final sorted output is obtained

---

## 🔢 Input

Let’s sort the array:

```
A = [8, 3, 5, 4, 7, 6, 1, 2]
```

We assume **n = 8** (a power of two) for the bitonic sorting network to work nicely.

---

## 🧱 Step 1: Build Bitonic Sequences

We recursively divide the array and form **bitonic sequences**.

### Level 1: Form bitonic pairs via compare-exchange

We make increasing or decreasing pairs by comparing elements:

```
(8,3) → [3,8] ↑  
(5,4) → [5,4] ↓  
(7,6) → [6,7] ↑  
(1,2) → [2,1] ↓  
```

Resulting pairs (bitonic sequences of length 2):

```
[3,8] (↑), [5,4] (↓), [6,7] (↑), [2,1] (↓)
```

---

### Level 2: Merge to bitonic sequences of length 4

#### Merge \[3,8] (↑) and \[5,4] (↓):

We concatenate the two:

```
[3,8,5,4] → This is a bitonic sequence
```

#### Merge \[6,7] (↑) and \[2,1] (↓):

We concatenate the two:

```
[6,7,2,1] → This is a bitonic sequence
```

---

## 🔀 Step 2: Bitonic Merge

### Merge \[3,8,5,4]

* Compare (3,4), (8,5) → After compare-exchange: (3,4), (5,8)

Now sort recursively:

* Left = \[3,4] → already sorted
* Right = \[5,8] → already sorted

Result:

```
[3,4,5,8]
```

---

### Merge \[6,7,2,1]

* Compare (6,1), (7,2) → After compare-exchange: (1,2), (6,7)

Now sort recursively:

* Left = \[1,2]
* Right = \[6,7]

Result:

```
[1,2,6,7]
```

---

## 🔗 Step 3: Final Optimal Merge

We now merge:

```
[3,4,5,8] and [1,2,6,7]
```

Using optimal merging network logic:

* Compare (3,1), (4,2), (5,6), (8,7)

  * Results after compare-exchange: \[1,2,5,7], \[3,4,6,8]

Now recursively sort:

* Merge \[1,2,5,7] and \[3,4,6,8] → Final sorted list

Final Result:

```
[1,2,3,4,5,6,7,8]
```

---

## ✅ Summary

Input:

```
[8, 3, 5, 4, 7, 6, 1, 2]
```

Preparata’s Steps:

1. Build bitonic pairs → \[3,8], \[5,4], \[6,7], \[2,1]
2. Merge to bitonic 4-length → \[3,8,5,4], \[6,7,2,1]
3. Bitonic merge → \[3,4,5,8], \[1,2,6,7]
4. Final merge → **\[1,2,3,4,5,6,7,8]**

