#advanced-cryptography #third-semester 

Perfect. Let's do **one complete Lagrange Interpolation example** step by step. I'll explain every step so you understand **why** it works, not just how.

---

# Problem

Suppose we have these **2 shares**:

$$
(1,7)
$$

$$
(2,9)
$$

We know

$$
t=2
$$

Our goal is to find the secret

$$
S=f(0).
$$

---

# Step 1: Write the Formula

For two points, Lagrange interpolation is

$$
f(0)=y_1L_1(0)+y_2L_2(0)
$$

where

$$
L_1(0)=\frac{0-x_2}{x_1-x_2}
$$

and

$$
L_2(0)=\frac{0-x_1}{x_2-x_1}
$$

Don't panic! We'll substitute the numbers.

---

# Step 2: Find the Values

We have

$$
x_1=1,\qquad y_1=7
$$

$$
x_2=2,\qquad y_2=9
$$

---

# Step 3: Calculate $$L_1(0)$$

Substitute the values:

$$
L_1(0)=\frac{0-2}{1-2}
$$

$$
=\frac{-2}{-1}
$$

$$
=2
$$

---

# Step 4: Calculate $$L_2(0)$$

$$
L_2(0)=\frac{0-1}{2-1}
$$

$$
=\frac{-1}{1}
$$

$$
=-1
$$

---

# Step 5: Find the Secret

Now use

$$
f(0)=y_1L_1(0)+y_2L_2(0)
$$

Substitute the values:

$$
=(7)(2)+(9)(-1)
$$

$$
=14-9
$$

$$
=5
$$

Therefore,

$$
\boxed{f(0)=5}
$$

The secret is

$$
\boxed{5}
$$

---

# Where did this 5 come from?

Remember the original polynomial?

$$
f(x)=5+2x
$$

The shares were

| x | f(x) |
| - | ---- |
| 1 | 7    |
| 2 | 9    |

Lagrange used only these two points and recovered

$$
f(0)=5.
$$

So it successfully found the secret **without ever being told the polynomial**.

---

# Visual Understanding

```text
Original polynomial

f(x)=5+2x

        │

Generate shares

(1,7)
(2,9)

        │

Polynomial is lost ❌

        │

Only shares remain

(1,7)
(2,9)

        │

Use Lagrange Interpolation

        │

Recover

f(0)=5

        │

Secret = 5
```

---

# Why Does This Work?

Lagrange Interpolation creates the **only line** that passes through:

* $$ (1,7) $$
* $$ (2,9) $$

Once that line is reconstructed, it asks:

> **"What is the value when $$x=0$$?"**

That value is the secret.

---

# Exam Tip ⭐

You are **not expected to derive the Lagrange formula**. Just remember:

1. Use at least **$$t$$ shares**.

2. Apply **Lagrange Interpolation**.

3. Compute

   $$
   f(0)
   $$

4. The value of

   $$
   f(0)
   $$

   is the **secret**.

This is the level of understanding expected in most MCA cryptography exams.
