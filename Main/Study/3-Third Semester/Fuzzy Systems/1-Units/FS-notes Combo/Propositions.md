#fuzzy-system #third-semester 

# Propositions 

## Definition

A **proposition** is a **statement that is either True or False**.

Examples:

* "The coin is Head."
* "It is raining."
* "The die shows 6."

A proposition becomes **true** for some outcomes and **false** for others.

The notes define it as:

> **A proposition is the event (set of sample points) where the proposition is true.** 

---

# Understanding with Coin Toss

Suppose we toss **one coin**.

Sample space:

$$
S={H,T}
$$

where

* H = Head
* T = Tail

---

## Proposition A

Let

> **A = "The coin is Head."**

Now ask:

For which outcomes is this statement true?

| Outcome | Is A True? |
| ------- | ---------- |
| Head    | ✅ Yes      |
| Tail    | ❌ No       |

Therefore,

$$
A={H}
$$

This means the proposition is **the set of outcomes where it is true**.

---

## Proposition ¬A (NOT A)

NOT A means

> "The coin is NOT Head."

or simply

> "The coin is Tail."

| Outcome | Is ¬A True? |
| ------- | ----------- |
| Head    | ❌ No        |
| Tail    | ✅ Yes       |

Therefore,

$$
\neg A={T}
$$

---

# Two Coins Example

Suppose we toss **two coins**.

Random variables:

* X = First coin
* Y = Second coin

Atomic events:

| Event | X | Y |
| ----- | - | - |
| HH    | H | H |
| HT    | H | T |
| TH    | T | H |
| TT    | T | T |

---

## Proposition A

Let

> A = "First coin is Head"

Where is this true?

| Atomic Event | First Coin Head? |
| ------------ | ---------------- |
| HH           | ✅                |
| HT           | ✅                |
| TH           | ❌                |
| TT           | ❌                |

Therefore,

$$
A={HH,HT}
$$

Notice:

A proposition can contain **more than one atomic event**.

---

## Proposition B

Let

> B = "Second coin is Head"

Then

$$
B={HH,TH}
$$

---

## Proposition A ∧ B

"A AND B"

means

* First coin is Head
* Second coin is Head

Only one event satisfies both.

$$
A\land B={HH}
$$

---

## Proposition A ∨ B

"A OR B"

means

* First coin Head
* OR Second coin Head

Possible events:

* HH
* HT
* TH

Therefore

$$
A\lor B={HH,HT,TH}
$$

---

# Important Statement in the Notes

The notes say:

> **A proposition is a disjunction (OR) of the atomic events in which it is true.** 

What does this mean?

Suppose

> A OR B

is true for:

* HH
* HT
* TH

Then

$$
A\lor B
=======

(HH)\lor(HT)\lor(TH)
$$

In the notes, this is written using Boolean variables:

$$
(a\lor b)
=========

(\neg a\land b)
\lor
(a\land\neg b)
\lor
(a\land b)
$$

It simply lists **all atomic events where $a \lor b$ is true**.

---

# Probability of a Proposition

The notes write:

$$
P(a\lor b)
==========

P(\neg a\land b)
+
P(a\land\neg b)
+
P(a\land b)
$$

This means:

To find the probability of **A OR B**, add the probabilities of **all atomic events** where **A OR B** is true. 

---

# Types of Random Variables

The notes then classify random variables into three types. 

### 1. Boolean (Propositional) Random Variable

Can have only **two values**.

Examples:

* Coin = {Head, Tail}
* Light = {ON, OFF}
* Cavity = {True, False}

---

### 2. Discrete Random Variable

Has a **countable** number of values.

Examples:

* Dice = {1,2,3,4,5,6}
* Weather = {Sunny, Rainy, Cloudy, Snow}

The notes emphasize that the values must be:

* **Exhaustive** → They include every possible outcome.
* **Mutually Exclusive** → Only one value can occur at a time.

---

### 3. Continuous Random Variable

Can take **any value within an interval**.

Examples:

* Temperature = 21.6°C
* Height = 175.4 cm
* Weight = 62.3 kg

You can also make propositions such as:

> Temperature < 22°C

---

# Difference Between Atomic Event and Proposition

| Atomic Event            | Proposition                                  |
| ----------------------- | -------------------------------------------- |
| One complete outcome    | A statement                                  |
| Example: HH             | "First coin is Head"                         |
| Only one state          | Can include many atomic events               |
| Smallest possible event | Union (OR) of atomic events where it is true |

### Easy Memory Trick

* **Atomic Event = One exact outcome.**
* **Proposition = A condition or statement that may be true for one or more atomic events.**


