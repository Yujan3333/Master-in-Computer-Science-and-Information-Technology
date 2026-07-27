#fuzzy-system #third-semester #genetic-algorithm
 
 **The numbers `1 2 2 4` are NOT the values of $x$ (12, 25, 5, 19).** They are **the string numbers (IDs) of the chromosomes**.

Let's go through it slowly.

---

## Step 1: Initial Population

Suppose your initial population is:

| String No. | Chromosome |  x | Fitness |
| ---------- | ---------- | -: | ------: |
| **1**      | 01100      | 12 |     144 |
| **2**      | 11001      | 25 |     625 |
| **3**      | 00101      |  5 |      25 |
| **4**      | 10011      | 19 |     361 |

Notice:

* **String 1** → chromosome `01100`
* **String 2** → chromosome `11001`
* **String 3** → chromosome `00101`
* **String 4** → chromosome `10011`

The numbers **1, 2, 3, 4 are just labels**.

---

## Step 2: Roulette Wheel gives Actual Count

Suppose after spinning the roulette wheel we get:

| String | Actual Count |
| ------ | -----------: |
| 1      |            1 |
| 2      |            2 |
| 3      |            0 |
| 4      |            1 |

This means:

* **String 1** is selected **once**
* **String 2** is selected **twice**
* **String 3** is **not selected**
* **String 4** is selected **once**

---

## Step 3: Build the Mating Pool

Now we literally copy each chromosome according to its actual count.

### String 1

Actual Count = **1**

So write it **once**.

```
String 1
```

---

### String 2

Actual Count = **2**

Write it **twice**.

```
String 2
String 2
```

---

### String 3

Actual Count = **0**

Do **not** write it.

---

### String 4

Actual Count = **1**

Write it once.

---

So the mating pool becomes

```
1
2
2
4
```

This means:

* One copy of **String 1**
* Two copies of **String 2**
* Zero copies of **String 3**
* One copy of **String 4**

---

## If we write the actual chromosomes instead

Instead of writing string numbers, we could write the chromosomes themselves.

Original population:

| String | Chromosome |
| ------ | ---------- |
| 1      | 01100      |
| 2      | 11001      |
| 3      | 00101      |
| 4      | 10011      |

Mating pool becomes:

| Selected String | Chromosome |
| --------------- | ---------- |
| 1               | 01100      |
| 2               | 11001      |
| 2               | 11001      |
| 4               | 10011      |

Notice that **String 2 appears twice** because it had the highest fitness.

---

## If we write the x values instead

Since the strings decode to:

| String |  x |
| ------ | -: |
| 1      | 12 |
| 2      | 25 |
| 3      |  5 |
| 4      | 19 |

The mating pool would be:

```
12
25
25
19
```

This is **equivalent** to writing:

```
1
2
2
4
```

The textbook uses **string numbers** because it's easier to keep track of which chromosome is being copied.

---

## Visual Memory Trick

```
Original Population

String 1  -> 01100 -> x = 12
String 2  -> 11001 -> x = 25
String 3  -> 00101 -> x = 5
String 4  -> 10011 -> x = 19


Actual Count

String 1 -> 1 copy
String 2 -> 2 copies
String 3 -> 0 copies
String 4 -> 1 copy


Mating Pool

01100
11001
11001
10011
```

The mating pool is simply **the list of chromosomes chosen to become parents for crossover**. It is **not a new calculation**—it is just copying the selected chromosomes according to their actual counts.
