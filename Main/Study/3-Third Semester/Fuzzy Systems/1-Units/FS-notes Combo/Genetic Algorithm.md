#fuzzy-system #third-semester 


---

# 1. Genetic Algorithm (GA) ⭐⭐⭐⭐⭐

## Definition9

A **Genetic Algorithm (GA)** is an Artificial Intelligence optimization technique based on the **principles of natural selection** (survival of the fittest). It was introduced by **John Holland (1975)** and is used to find the best solution from a search space. 

---

## Applications

According to your notes, GA is used in:

* Image processing
* Signal processing
* Telecommunication
* Cryptography
* Computational optimization
* Operations research



---

# Basic Idea

GA works like biological evolution.

It repeatedly:

1. Creates candidate solutions.
2. Selects the best ones.
3. Combines them (crossover).
4. Introduces random changes (mutation).
5. Produces a better generation.

The process continues until the best solution is found.

---

# Important Terminologies ⭐⭐⭐⭐⭐

---

## 1. Population

### Definition

A **Population** is the collection of all candidate solutions (chromosomes) considered at one time.

Initialization methods:

* Random Initialization
* Heuristic Initialization



**Memory**

> Population = Collection of chromosomes

---

## 2. Chromosome

### Definition

A **Chromosome** is one complete candidate solution to the problem.



**Memory**

> One solution = One chromosome

---

## 3. Gene

### Definition

A **Gene** is one element (position) within a chromosome.



Example

```text
Chromosome = 101101

Genes = 1 0 1 1 0 1
```

---

## 4. Genotype

### Definition

The **Genotype** is the encoded representation of solutions used by the computer.



---

## 5. Phenotype

### Definition

The **Phenotype** is the actual real-world representation of the solution.



---

## 6. Encoding and Decoding

### Encoding

Converts

Real-world solution

↓

Computer representation

---

### Decoding

Converts

Computer representation

↓

Real-world solution

Decoding should be fast because it is repeatedly used during fitness evaluation.



---

# Encoding Methods ⭐⭐⭐⭐

---

## 1. Binary Encoding

* Most common encoding.
* Uses only **0 and 1**.

Example

```text
10110010
```

Used because it is simple.



---

## 2. Permutation Encoding

Used for **ordering problems** like

* Traveling Salesman Problem (TSP)
* Task scheduling


In permutation encoding, every chromosome is a string of numbers that represent a position in a sequence



Example

```text
1 5 3 2 6 4
```



---

## 3. Value Encoding

Used when values are

* Real numbers
* Characters
* Objects

Value Encoding is used when the solution contains complex values (such as real numbers, characters, or objects) that are difficult to represent using binary encoding. 

In value encoding, each chromosome is a sequence of values related to the problem



Example

```text
1.25 2.18 0.75
```



---

## 4. Tree Encoding

Used mainly in

* Genetic Programming
* Program evolution

Each chromosome is represented as a tree.



---

# Fitness Function ⭐⭐⭐⭐⭐

### Definition

A **Fitness Function** measures how good a solution is.

It

* Takes a solution as input.
* Produces a fitness value.

Higher fitness → Better solution.



---

# Genetic Operators ⭐⭐⭐⭐⭐

Genetic operators modify chromosomes to produce new generations.

They include

* Selection
* Crossover
* Mutation



---

# 1. Selection

### Definition

Selection chooses individuals that will reproduce and pass their genes to the next generation.



### Selection Methods

* Roulette Wheel Selection
* Stochastic Universal Sampling
* Tournament Selection
* Rank-Based Selection

---

## Roulette Wheel Selection ⭐⭐⭐⭐

Each chromosome occupies a portion of a wheel proportional to its fitness.

```
Higher fitness

		↓

Larger wheel area

		↓

Higher probability of selection
```

Formula mentioned in notes:

$$
P(i)=\frac{f_i}{\sum f}
$$

where

* $f_i$ = Fitness of individual


![](../../../../../../Images/Third_Sem_Images/Genetic%20Algorithm-%20Selection%20Roulette.png)


---

# 2. Crossover ⭐⭐⭐⭐⭐

### Definition

Crossover combines genetic material from two parents to produce offspring.



### Types

### One-Point Crossover

One crossover point is selected.

Everything after that point is exchanged.

![](../../../../../../Images/Third_Sem_Images/Genetic%20Algorithm-1p%20crossover.png)

---

### Multi-Point Crossover

Several crossover points are selected.

Multiple chromosome segments are exchanged.
![](../../../../../../Images/Third_Sem_Images/Genetic%20Algorithm-multipoint.png)

---

### Tree Crossover

Subtrees are exchanged.

Used for tree encoding.

---

# 3. Mutation ⭐⭐⭐⭐⭐

### Definition

Mutation introduces **small random changes** in chromosomes.

Purpose:

* Maintain diversity.
* Prevent premature convergence.
* Generate new solutions.



### Mutation Types

* Bit Flip Mutation
* Random Resetting
* Swap Mutation

---

## Bit Flip Mutation

Used in binary encoding.

Example

```text
101100

↓

100100
```

One or more bits are flipped.

---

## Swap Mutation

Two positions are selected.

Their values are exchanged.

Used mainly in permutation encoding.

![](../../../../../../Images/Third_Sem_Images/Genetic%20Algorithm-%20Mutation.png)


---

# GA Parameters ⭐⭐⭐

## Crossover Probability

Determines how often crossover occurs.

* 100% → Every offspring is created by crossover.
* 0% → Offspring are exact copies of parents.



---

## [Mutation Probability](Mutation%20Probability.md)

Determines how often mutation occurs.

* High mutation → Many genes change.
* Low mutation → Few changes.

Very high mutation can destroy good solutions.



---

# Termination Conditions ⭐⭐⭐

GA stops when:

1. No improvement for several iterations.
2. Maximum number of generations reached.
3. Desired fitness value achieved.



---

# GA Algorithm ⭐⭐⭐⭐⭐

According to your notes:

### Step 1

Generate random population.

	↓

### Step 2

Evaluate fitness.

	↓

### Step 3

Select parents.

	↓

### Step 4

Perform crossover.

	↓

### Step 5

Perform mutation.

	↓

### Step 6

Create new population.

	↓

### Step 7

Evaluate fitness.

	↓

### Step 8

If stopping condition is met → Stop.

Otherwise repeat.



---

# Advantages (Based on Notes)

* Finds good solutions through optimization.
* Applicable to many problem domains.
* Suitable for complex search spaces.
* Used in many AI applications such as image processing, cryptography, and optimization. 

---

# One-Page Revision Table

| Topic                    | Key Point                                         |
| ------------------------ | ------------------------------------------------- |
| **GA**                   | Optimization technique based on natural selection |
| **Population**           | Set of chromosomes                                |
| **Chromosome**           | One candidate solution                            |
| **Gene**                 | One element of a chromosome                       |
| **Genotype**             | Encoded representation                            |
| **Phenotype**            | Real-world representation                         |
| **Fitness Function**     | Measures solution quality                         |
| **Selection**            | Chooses parents                                   |
| **Roulette Wheel**       | Higher fitness → Higher selection probability     |
| **Crossover**            | Combines parents                                  |
| **Mutation**             | Randomly changes genes                            |
| **Binary Encoding**      | Uses 0 and 1                                      |
| **Permutation Encoding** | Ordering problems (TSP)                           |
| **Value Encoding**       | Real numbers/characters                           |
| **Tree Encoding**        | Genetic programming                               |
| **Termination**          | Stop when criteria are met                        |

---

# ⭐ Most Important Exam Topics

If your exam asks about **Genetic Algorithms**, prioritize these:

1. **Definition and applications of GA**
2. **Basic terminologies**: Population, Chromosome, Gene, Genotype, Phenotype
3. **Encoding methods** (Binary, Permutation, Value, Tree)
4. **Fitness Function**
5. **Genetic Operators**:

   * Selection (especially **Roulette Wheel Selection**)
   * Crossover (One-point, Multi-point, Tree)
   * Mutation (Bit Flip, Swap)
6. **GA Algorithm steps**
7. **Termination conditions**

These are the topics most likely to appear as **5-mark or 10-mark questions** based on the content of your notes.
