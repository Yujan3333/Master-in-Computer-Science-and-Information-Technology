#fuzzy-system #third-semester #genetic-algorithm 

Consider the problem of maximizing the function, f(x) = $x^2$ where x is permitted to vary
between 0 to 31.

---

# What is the GA trying to do?

The problem is

$$
f(x)=x^2
$$

where

$$
0 \le x \le 31
$$

We want the **largest value of $x^2$**.

Obviously,

$$
31^2=961
$$

is the maximum.

But GA **doesn't directly test all 32 numbers**.

Instead, it behaves like evolution.

It keeps improving a population of solutions.

---

# Imagine a competition

Suppose 4 students compete.

Each student has a score.

Higher score → more likely to survive.

Then

* best students reproduce
* children inherit traits
* random mutation occurs

Eventually the class becomes stronger.

GA is exactly this.

---

# Step 1 — Create Initial Population

![](../../../../../../Images/Third_Sem_Images/Numerical%20of%20GA-selection.png)


Randomly choose 4 numbers.

Suppose

| String | Binary |
| ------ | ------ |
| 1      | 01100  |
| 2      | 11001  |
| 3      | 00101  |
| 4      | 10011  |

These are called **chromosomes**.

Nothing has happened yet.

We simply picked 4 random solutions.

---

# Step 2 — Decode

Computers store binary.

Humans understand decimal.

Convert binary to decimal.

Example

```
01100
```

means

$$
8+4=12
$$

because

```
0×16
1×8
1×4
0×2
0×1
```

Therefore

$$
x=12
$$

Do this for everyone.

| Binary | Decimal |
| ------ | ------- |
| 01100  | 12      |
| 11001  | 25      |
| 00101  | 5       |
| 10011  | 19      |

Now we finally know the candidate solutions.

---

# Step 3 — Calculate Fitness

Fitness tells us

> **How good is this solution?**

Problem says

$$
f(x)=x^2
$$

Simply square every number.

| x  | Fitness |
| -- | ------- |
| 12 | 144     |
| 25 | 625     |
| 5  | 25      |
| 19 | 361     |

Now notice something.

Who is strongest?

Obviously

```
625
```

This chromosome is the strongest.

---

# Step 4 — Selection Probability

Now GA asks

> **Who deserves to reproduce?**

Not everyone equally.

```
Better fitness

↓

Higher chance.
```

First find total fitness.

$$
144+625+25+361=1155
$$

Now probability

**Formula**

$$
P_i=\frac{f_i}{\sum f}
$$

---

**For String 1**

$$
P_1=\frac{144}{1155}=0.1247
$$

which is

12.47%

---

**For String 2**

$$
P_2=\frac{625}{1155}=0.5411
$$

54.11%

---

**Continue**

| Fitness | Probability |
| ------- | ----------- |
| 144     | 12.47%      |
| 625     | 54.11%      |
| 25      | 2.16%       |
| 361     | 31.26%      |

**Notice**

```
Largest fitness

↓

Largest probability.
```

Exactly what we want.

---

# Why Probability?

Because GA is based on

**survival of the fittest.**

The strongest should have

more babies.

Not guaranteed,

just more likely.

---

# Step 5 — Expected Count

This is where many students panic.

Actually it is simple.

**Average fitness**

$$
=\frac{1155}{4}
$$

because population size is 4.

$$
288.75
$$

Now

**Expected Count**

$$
=\frac{Fitness}{Average\ Fitness}
$$

---

Example

String 1

$$
\frac{144}{288.75}
=0.4987
$$

Nearly

0.5

Meaning

> On average this chromosome deserves about half a place.

---

String 2

$$
\frac{625}{288.75}
=2.16
$$

Meaning

This chromosome deserves about

2 places.

---

Expected count only tells us

**how many copies we expect.**

It is **not mandatory**.

Many questions skip this.

---

# Step 6 — Roulette Wheel

This is the easiest part if you imagine pizza.

Imagine a pizza.

Whole pizza

=

100%

Now cut according to probabilities.

```
String2
###############
###############
###############
54%

String4
##########
31%

String1
####
12%

String3
.
2%
```

Now spin the wheel.

Wherever pointer stops,

that chromosome is selected.

Since String 2 occupies

54%

it is likely to be selected

twice.

String 3 occupies only

2%.

Almost impossible.

Hence

Actual Count becomes

| String | Actual Count |
| ------ | ------------ |
| 1      | 1            |
| 2      | 2            |
| 3      | 0            |
| 4      | 1            |

![](../../../../../../Images/Third_Sem_Images/Numerical%20of%20GA-count.png)


Notice

Actual Count is based on

roulette wheel,

not exact mathematics.

---

# Step 7 — Mating Pool

Now write chromosomes according to actual count.

Original

```
Count
1
2
3
4
```

Actual Count

```
Count
1
2
0
1
```

Therefore mating pool becomes

```
This is String
1
2
2  //Its actual count is 2
4
```

*String 3 disappears. and String 2 is repeated 2 times as its count suggests*

Because it was weak.

This is survival of the fittest.

==Further Detail==
[GA-Further Expanding on this part](GA-Further%20Expanding%20on%20this%20part.md)

---

# Step 8 — Crossover

Now parents produce children.

Suppose

```
Parent1

11001

Parent2

10011
```

Choose crossover point.

Suppose after third bit.

```
110|01

100|11
```

Swap the last parts.

Children

```
11011

10001
```

That's all crossover is.

It exchanges genes.


![](../../../../../../Images/Third_Sem_Images/Numerical%20of%20GA-crossover.png)

---

# Step 9 — Decode Again

Children are binary.

Convert them back.

Suppose

```
11011
```

Decimal

27

Fitness

$$
27^2=729
$$

Now compare.

Did fitness improve?

Usually yes.

---

# Step 10 — Mutation

Mutation is a tiny random change.

Example

```
11011
```

Flip one bit.

```
11111
```

Now

Decimal

31

Fitness

$$
31^2=961
$$

Boom!

Mutation accidentally created an even better solution.

![](../../../../../../Images/Third_Sem_Images/Numerical%20of%20GA-mutation.png)



---

# Entire Flow in One Picture

```text
Random Population
        │
        ▼
Decode Binary
        │
        ▼
Calculate Fitness
        │
        ▼
Selection Probability
        │
        ▼
Roulette Wheel
        │
        ▼
Mating Pool
        │
        ▼
Crossover
        │
        ▼
Mutation
        │
        ▼
New Population
        │
        ▼
Repeat Until Best Solution
```

---

# What should you remember for exams?

For any GA numerical, **always follow this exact sequence**:

1. **Generate initial population** (binary chromosomes)
2. **Decode binary → decimal**
3. **Calculate fitness**
4. **Find total fitness**
5. **Calculate selection probability**
   $$
   P_i=\frac{f_i}{\sum f}
   $$
6. **(Optional)** Calculate expected count
7. **Perform Roulette Wheel Selection**
8. **Create mating pool**
9. **Perform crossover**
10. **Perform mutation**
11. **Decode offspring and calculate new fitness**
12. **Repeat until termination**

---
