#fuzzy-system #third-semester 

These are two of the most confusing topics in fuzzy systems because they look similar. The key difference is **what kind of function you are extending**.

---

# 1. Extension Principle

## Idea

The **Extension Principle** extends a **normal (crisp) function** so that it can accept **fuzzy sets** as input.

Instead of

$$
y=f(x),
$$

we have

$$
\tilde{A}
\longrightarrow
f
\longrightarrow
\tilde{B}
$$

where

* Input = fuzzy set
* Function = crisp
* Output = fuzzy set

---

## Crisp Example

Suppose

$$
f(x)=2x
$$

and

$$
X={1,2,3}.
$$

Then

| x | f(x) |
| - | ---- |
| 1 | 2    |
| 2 | 4    |
| 3 | 6    |

Nothing fuzzy here.

---

## Now make the input fuzzy

Let

$$
\tilde A=
\left\{
\frac{0.3}{1}
+
\frac{0.8}{2}
+
\frac{0.5}{3}
\right\}
$$

Apply

$$
f(x)=2x.
$$

Each element keeps its membership.

| x | Membership | Output |
| - | ---------: | -----: |
| 1 |        0.3 |      2 |
| 2 |        0.8 |      4 |
| 3 |        0.5 |      6 |

So

$$
\tilde B=
\left\{
\frac{0.3}{2}
+
\frac{0.8}{4}
+
\frac{0.5}{6}
\right\}
$$

This is the **Extension Principle**.

---

# General Formula

If

$$
y=f(x),
$$

then

$$
\mu_B(y)
========

\max_{x:f(x)=y}
\mu_A(x)
$$

If several values of $x$ produce the same $y$, we take the **maximum** membership.

---

# Example

Suppose

$$
f(x)=x^2
$$

and

$$
X={-2,2}
$$

Both produce

$$
4.
$$

Suppose

$$
\mu(-2)=0.4,\qquad
\mu(2)=0.8.
$$

Then

$$
\mu(4)
=

 \max(0.4,0.8)
=====
0.8.
$$

This is why the Extension Principle uses **max**.

---

# 2. Generalized Extension Principle

Now suppose the function has **more than one input**.

Instead of

$$
y=f(x),
$$

we have

$$
z=f(x,y).
$$

Both inputs are fuzzy.

---

Example

$$
z=x+y.
$$

Input fuzzy sets

$$
A=
\left\{
\frac{0.5}{1}
+
\frac{1}{2}
\right\}
$$

and

$$
B=
\left\{
\frac{0.6}{3}
+
\frac{0.8}{4}
\right\}.
$$

---

## Step 1

Form every possible pair.

| Pair  |
| ----- |
| (1,3) |
| (1,4) |
| (2,3) |
| (2,4) |

---

## Step 2

Find each pair's membership.

Use

$$
\min
$$

because both inputs must occur together.

| Pair  |          Membership |
| ----- | ------------------: |
| (1,3) | $\min(0.5,0.6)=0.5$ |
| (1,4) | $\min(0.5,0.8)=0.5$ |
| (2,3) |   $\min(1,0.6)=0.6$ |
| (2,4) |   $\min(1,0.8)=0.8$ |

---

## Step 3

Apply

$$
z=x+y.
$$

| Pair  | Output |
| ----- | -----: |
| (1,3) |      4 |
| (1,4) |      5 |
| (2,3) |      5 |
| (2,4) |      6 |

---

## Step 4

Combine repeated outputs using **max**.

Output 4

$$
0.5
$$

Output 5

comes from two pairs.

$$
\max(0.5,0.6)=0.6
$$

Output 6

$$
0.8
$$

Final fuzzy output

$$
C=
\left\{
\frac{0.5}{4}
+
\frac{0.6}{5}
+
\frac{0.8}{6}
\right\}
$$

---

# General Formula

For

$$
z=f(x_1,x_2,\ldots,x_n)
$$

the generalized extension principle is

$$
\mu_C(z)
========

\max_{f(x_1,\ldots,x_n)=z}
\left[
\min\bigl(
\mu_{A_1}(x_1),
\ldots,
\mu_{A_n}(x_n)
\bigr)
\right].
$$

Notice:

* **min** combines the memberships of all input fuzzy sets.
* **max** combines multiple input combinations that produce the same output.

---

# Difference

| Extension Principle                                               | Generalized Extension Principle                                              |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| One input fuzzy set                                               | Two or more input fuzzy sets                                                 |
| Function: $y=f(x)$                                                | Function: $z=f(x,y,\ldots)$                                                  |
| Keep the membership of each input (or take max if outputs repeat) | First use **min** for each input combination, then **max** if outputs repeat |
| Example: $y=2x$                                                   | Example: $z=x+y$                                                             |

## Easy way to remember

* **Extension Principle:** **One fuzzy input** → apply the function.
* **Generalized Extension Principle:** **Multiple fuzzy inputs** → make all input combinations, use **min** for each combination, apply the function, then use **max** for repeated outputs.

Think of it this way:

```text
Extension Principle

Fuzzy Set
    │
    ▼
f(x)
    │
    ▼
Fuzzy Set


Generalized Extension Principle

Fuzzy Set A ──┐
              ├──► f(x,y,...) ───► Fuzzy Set
Fuzzy Set B ──┘
```

The generalized version is simply the extension principle expanded to functions with **multiple fuzzy inputs**.
