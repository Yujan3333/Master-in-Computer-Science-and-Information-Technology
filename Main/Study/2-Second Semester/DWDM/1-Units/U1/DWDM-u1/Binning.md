## Data Cleaning 2: Handling Noisy Data

### a) Binning Method

Binning is a **data smoothing technique** that reduces noise by grouping nearby values into bins and replacing them with a representative value.

It is a **three-step process**:

1. **Sort the data**
2. **Create bins** using a partitioning method
3. **Smooth each bin** using mean, median, or boundary values

---

## Step 1: Sort the data

Example (price in dollars):

```
4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34
```

---

## Step 2: Create bins

Two common methods:

### 1. Equal-width (distance) partitioning

* Divide data into $k$ bins of equal width
* Width formula:
  $$W=(max-min)/k$$
* Each bin has the same range of values

---

### 2. Equal-depth (frequency) partitioning

* Divide data into $k$ bins
* Each bin has **approximately the same number of items**

Given: depth = 4

So bins are:

```
Bin 1: 4, 8, 9, 15
Bin 2: 21, 21, 24, 25
Bin 3: 26, 28, 29, 34
```

---

## Step 3: Smoothing the bins

### a) Smoothing by **Bin Means**

Replace each value in a bin by the **mean** of that bin.

Bin 1:
Mean = $(4+8+9+15)/4=9$

```
9, 9, 9, 9
```

Bin 2:
Mean = $(21+21+24+25)/4=23$

```
23, 23, 23, 23
```

Bin 3:
Mean = $(26+28+29+34)/4=29$

```
29, 29, 29, 29
```

---

### b) Smoothing by **Bin Boundaries**

Replace values with the **nearest boundary value** (min or max of the bin).

Bin 1: boundaries = 4 and 15

```
4, 4, 4, 15
```

Bin 2: boundaries = 21 and 25

```
21, 21, 25, 25
```

Bin 3: boundaries = 26 and 34

```
26, 26, 26, 34
```

---

## One-line exam definition:

> Binning is a noise reduction technique that smooths data by grouping sorted values into bins and replacing them with bin means, medians, or boundary values.

---

## Short exam answer:

> The binning method handles noisy data by sorting values, dividing them into equal-width or equal-depth bins, and smoothing each bin using mean, median, or boundary values to reduce random variation.
