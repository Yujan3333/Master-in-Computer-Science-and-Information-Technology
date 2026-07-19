
#fuzzy-system #third-semester #old-que #exam-paper-answer 

This is a **standard Genetic Algorithm (GA)** question. Since the question says:

> **"Use your own assumptions as required."**

you are free to choose:

* Initial population
* Selection method
* Crossover point
* Mutation position

The examiner mainly checks whether you know the **steps of one GA iteration**.

---

# Q3. Single Iteration of Genetic Algorithm (10 Marks)

## Given

Objective Function

$$
f(x)=\frac{x}{2}
$$

Range

$$
1\le x\le15
$$

Since we are **minimizing**,

the smaller the value of

$$
x
$$

the better the solution.

---

# Step 1: Encoding

Since

$$
1\le x\le15
$$

we need **4 bits**.

| x  | Binary |
| -- | ------ |
| 1  | 0001   |
| 2  | 0010   |
| 3  | 0011   |
| 4  | 0100   |
| 5  | 0101   |
| 6  | 0110   |
| 7  | 0111   |
| 8  | 1000   |
| 9  | 1001   |
| 10 | 1010   |
| 11 | 1011   |
| 12 | 1100   |
| 13 | 1101   |
| 14 | 1110   |
| 15 | 1111   |

---

# Step 2: Initial Population

Assume a random population of four chromosomes.

| Chromosome | Binary | x  | Fitness $$f(x)=x/2$$ |
| ---------- | ------ | -- | -------------------- |
| C1         | 1100   | 12 | 6                    |
| C2         | 0101   | 5  | 2.5                  |
| C3         | 0011   | 3  | 1.5                  |
| C4         | 1110   | 14 | 7                    |

---

## Since this is a minimization problem

Lower fitness is better.

Arrange them

| Chromosome | Fitness |
| ---------- | ------- |
| 0011       | 1.5     |
| 0101       | 2.5     |
| 1100       | 6       |
| 1110       | 7       |

Best chromosome

$$
0011
$$

---

# Step 3: Selection

Use **Tournament Selection** (or Roulette Wheel; either is acceptable if stated).

Select the two best parents.

Parent 1

$$
0011
$$

Parent 2

$$
0101
$$

---

# Step 4: Crossover

Choose a **single crossover point** after the second bit.

Parents

```text
Parent 1

00|11

Parent 2

01|01
```

Exchange the right parts.

Children

```text
Child 1

00|01

=

0001

Child 2

01|11

=

0111
```

---

Convert to decimal.

| Child   | Binary | x |
| ------- | ------ | - |
| Child 1 | 0001   | 1 |
| Child 2 | 0111   | 7 |

---

# Step 5: Mutation

Suppose mutation occurs in Child 2.

Flip the last bit.

Before mutation

```text
0111
```

After mutation

```text
0110
```

Now

$$
0110=6
$$

---

# Step 6: New Population

The new chromosomes become

| Chromosome | Binary | x | Fitness |
| ---------- | ------ | - | ------- |
| Child 1    | 0001   | 1 | 0.5     |
| Child 2    | 0110   | 6 | 3       |

---

# Final Result

The best chromosome after one iteration is

$$
0001
$$

which represents

$$
x=1
$$

Fitness

$$
f(x)=\frac{1}{2}=0.5
$$

Since the objective is minimization, this is the best solution obtained in this iteration.

---

# Flow of Genetic Algorithm

```text
Initial Population
        │
        ▼
Encoding
        │
        ▼
Fitness Evaluation
        │
        ▼
Selection
        │
        ▼
Crossover
        │
        ▼
Mutation
        │
        ▼
New Population
```

---

# Why Each Step is Performed (Easy to Remember)

* **Encoding:** Converts the solution into binary chromosomes.
* **Initial Population:** Starts with random candidate solutions.
* **Fitness Evaluation:** Measures how good each solution is.
* **Selection:** Chooses better parents for reproduction.
* **Crossover:** Combines parents to create new offspring.
* **Mutation:** Randomly changes bits to maintain diversity and avoid local optima.
* **New Population:** Replaces the old population and starts the next iteration.

---

### Exam Tip

For a **10-mark** question, always show:

1. Objective function.
2. Binary encoding table.
3. Random initial population.
4. Fitness calculation.
5. Selection.
6. Crossover (with crossover point).
7. Mutation (show the flipped bit).
8. Final offspring/new population.

Showing all these steps usually earns full marks, even if your assumed population differs from someone else's, because the question explicitly allows you to make assumptions.
