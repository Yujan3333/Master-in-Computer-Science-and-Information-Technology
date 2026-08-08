#fuzzy-system #third-semester 

These are **selection methods in Genetic Algorithms (GA)**. The purpose of selection is to choose **better individuals (genomes/chromosomes)** from the population for reproduction.

The basic idea:

> Higher fitness → higher chance of being selected.

---

## 1. Roulette Wheel Selection

Also called **fitness proportionate selection**.

Imagine a roulette wheel where each individual gets a slice based on its fitness.

* Higher fitness → bigger slice
* Lower fitness → smaller slice
* Spin the wheel randomly → selected individual

### Example:

| Individual | Fitness | Probability |
| ---------- | ------: | ----------: |
| A          |      50 |         50% |
| B          |      30 |         30% |
| C          |      20 |         20% |

A has the largest chance of being selected.

It is called roulette because selection works like spinning a wheel.

**Problem:**

* Very fit individuals may dominate too quickly.
* Weak individuals may disappear early.

---

# 2. Stochastic Universal Sampling (SUS)

An improved version of roulette wheel selection.

Instead of spinning the wheel many times randomly:

* Place multiple equally spaced pointers on the wheel.
* Select all individuals at once.

Example:

For selecting 4 parents:

```
|----|----|----|----|
 ^    ^    ^    ^
 P1   P2   P3   P4
```

Advantages:

* More balanced selection.
* Prevents one individual from being selected too many times.
* Maintains population diversity.

---

# 3. Tournament Selection

Individuals compete in small groups (tournaments).

Steps:

1. Randomly pick some individuals.
2. Compare their fitness.
3. The best one wins.
4. Select the winner as parent.

Example:

Population:

```
A fitness = 90
B fitness = 70
C fitness = 50
D fitness = 30
```

Tournament size = 2

Pick:

```
A vs C
```

A wins → selected.

Pick:

```
B vs D
```

B wins → selected.

Advantages:

* Simple.
* Does not require fitness normalization.
* Can control selection pressure using tournament size.

---

# 4. Rank-Based Selection

Selection is based on **rank**, not actual fitness value.

First sort individuals:

| Rank | Individual | Fitness |
| ---- | ---------- | ------: |
| 1    | A          |     100 |
| 2    | B          |      80 |
| 3    | C          |      20 |
| 4    | D          |       5 |

Then assign probability according to rank.

Example:

| Individual | Rank probability |
| ---------- | ---------------: |
| A          |              40% |
| B          |              30% |
| C          |              20% |
| D          |              10% |

Difference from roulette:

* Roulette uses actual fitness.
* Rank selection uses only order.

---

# Quick Comparison

| Method         | Selection Based On | Main Idea                             |
| -------------- | ------------------ | ------------------------------------- |
| Roulette Wheel | Fitness value      | Bigger fitness = bigger wheel area    |
| SUS            | Fitness value      | Multiple roulette selections together |
| Tournament     | Competition        | Best among randomly chosen group wins |
| Rank-based     | Rank/order         | Higher rank gets higher chance        |

---

### Easy memory:

* **Roulette → Spin wheel**
* **SUS → Multiple roulette pointers**
* **Tournament → Fight and winner survives**
* **Rank → Sort and give probability by position**
