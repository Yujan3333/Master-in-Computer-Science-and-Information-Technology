#advanced-cryptography #third-semester 

---

# Example

Suppose the secret is

$$
S=5
$$

Choose

$$
t=2
$$

Since

$$
t=2,
$$

we need a polynomial of degree

$$
1
$$

(a straight line).

Suppose we choose

$$
f(x)=5+2x
$$

Notice:

$$
f(0)=5
$$

So the secret is

$$
5.
$$

---

## Create Shares

Evaluate the polynomial.

For

$$
x=1
$$

$$
f(1)=5+2=7
$$

Share 1:

$$
(1,7)
$$

---

For

$$
x=2
$$

$$
f(2)=5+4=9
$$

Share 2:

$$
(2,9)
$$

---

For

$$
x=3
$$

$$
f(3)=5+6=11
$$

Share 3:

$$
(3,11)
$$

---

Now suppose everyone forgets the polynomial.

They only know

$$
(1,7)
$$

and

$$
(2,9)
$$

---

# Now comes Lagrange Interpolation

Lagrange simply asks:

> **"Which polynomial passes through these two points?"**

The answer is

$$
f(x)=5+2x
$$

because

When

$$
x=1
$$

$$
5+2(1)=7
$$

✔

When

$$
x=2
$$

$$
5+2(2)=9
$$

✔

So Lagrange reconstructs the original polynomial.

---

Finally,

find the secret:

$$
f(0)=5+2(0)=5
$$

Secret recovered!

---

# What Lagrange Actually Does

Think of it like this.

You know two points:

```text
(1,7)
(2,9)
```

Can you draw the line passing through them?

Yes.

That line is

$$
f(x)=5+2x
$$

Drawing that line mathematically is called **Lagrange Interpolation**.

---

# A Visual

```text
y

11 ● (3,11)

 9 ● (2,9)

 7 ● (1,7)

 5 ● (0,5) ← Secret

    ───────────────────── x
      0   1   2   3
```

The shares are just points on the same line.

Once you know enough points, you can redraw the line and then look at where it crosses the **y-axis** (when $$x=0$$).

That value is the secret.

---

# Do you need the [Lagrange formula](Lagrange%20formula.md)?

For understanding, **no**.

For exams, some teachers may ask for the formula:

$$
f(0)=\sum_{i=1}^{t} y_i
\prod_{\substack{j=1 \ j\ne i}}^{t}
\frac{-x_j}{x_i-x_j}
$$

But **don't memorize it yet**.

First understand this:

> **Lagrange Interpolation = A mathematical method that reconstructs the original polynomial from at least $$t$$ shares. After reconstructing the polynomial, the secret is obtained by computing $$f(0)$$.**

Once you're comfortable with the idea, I can show you **how that formula actually reconstructs the secret step by step using numbers**, with no skipped steps. That is the version most students finally understand.
