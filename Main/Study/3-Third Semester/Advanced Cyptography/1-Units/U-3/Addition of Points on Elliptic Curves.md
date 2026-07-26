#advanced-cryptography #third-semester 

# Addition of Points on Elliptic Curves

Point addition is the **basic operation** in Elliptic Curve Cryptography (ECC). Unlike RSA, ECC does **not** use ordinary integer multiplication. Instead, it uses **addition of points** on an elliptic curve.

An elliptic curve over a finite field is generally defined as:

$$
y^2 = x^3 + ax + b
$$

where

$$
4a^3 + 27b^2 \ne 0
$$

to ensure the curve has no singularities.

---

# Case 1: Adding Two Different Points

Suppose two distinct points

$$
P=(x_1,y_1)
$$

and

$$
Q=(x_2,y_2), \qquad P\ne Q
$$

Then,

$$
R=P+Q=(x_3,y_3)
$$

### Step 1: Compute the slope

$$
\lambda=\frac{y_2-y_1}{x_2-x_1}
$$

(In finite fields, division means multiplying by the modular inverse.)

---

### Step 2: Compute the new x-coordinate

$$
x_3=\lambda^2-x_1-x_2
$$

---

### Step 3: Compute the new y-coordinate

$$
y_3=\lambda(x_1-x_3)-y_1
$$

Thus,

$$
P+Q=(x_3,y_3)
$$

---

# Geometric Interpretation

![Image](https://images.openai.com/static-rsc-4/0-7gHmKbqaEW-qxFv321YDt4-W_hbEGmUOH_uL3TzBNAWE8VTJIEADYR5aBwquso1qL5Uvd7cOWed4MXgL3CbBzIFCrSqD1IqXp5W2wQtWfuX08yo7NaBAEFwwXZMprhD1TY6k6kcYU0CvERt9TULRInOuHv2HunzLbuivIdfXcWWgZmIpaWglqeRdmFXZsW?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/LVfpN4lY8aLVPoiwNETJlZAvGPYbaDyDcjiRKwOsBlJ9sn1mhJdfAoX-w_iK6xfv0Wo0cs8U2U7lavKOF9wVYw5dKy_rk3-AueixiOPVkQiJINf0fFxaWcLsyXcKBG1mD1NRQ56wQ9MMKgMfZyBaWP--Q_pzYbZFtqHU3Wbb6EXZ3DTE-tLPJAwKfiM8_dvm?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/MFl5kO40Q0XFmFPuCA5hEHB3M2KMXEhP6OQI38Jy7dwwBJmFPEfKtnpVSuM_mqcLctrnYzWCNE6ahD4lGjz9NRElw03x3YC2bShHigOsnONGi8mnWLGqdN0tUoUXqfETrs0hyyNXY7mCDrli4CcUl2nolPTbzy0DMMt7zTVH5qxKzrtiPn_92lS4WgR0Zq0l?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/w0pcMnwUvi7fjEM-CnRmJCnvTEb7VQt9Z20XZwDgCuiXY-pqtpdhDI6RrzYBUWG5Z1AAy3GHTrYnbCzJkCGN9DR2GKmAD_jnCxaJ8ZVzAxTv-oEpfDo7u__ekWhhUInZgDqC2wV_xzFDxoyPb95lp1n7sHBMBL_aSCtphRAO7SGuWy1yOSXteEI3XRUnDUz_?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/U9N6fHsf8GTXGReN0L1rEoT0-hWnkewX3sVR6imJ29qdoZEN7Q4Ktlimrjia4PWhclQCDJ24wztZWbs8mB847y_lLjE5jLjJws2jrBfnleUKbTocsikkuPohxz1HwXZhMRbr_d1DlLZXGVDAeRT_R2EdTzeTcnSCGB-isLrdwf9XJO15Ha1eyuunRuV08xuv?purpose=fullsize)

1. Draw a line through points $P$ and $Q$.
2. The line intersects the curve at a third point.
3. Reflect that third point across the x-axis.
4. The reflected point is

$$
P+Q.
$$

---

# Case 2: Point Doubling ($P=Q$)

When adding a point to itself,

$$
R=2P=P+P
$$

the line becomes a **tangent** to the curve.

### Step 1: Compute the slope

$$
\lambda=\frac{3x_1^2+a}{2y_1}
$$

---

### Step 2: Compute x-coordinate

$$
x_3=\lambda^2-2x_1
$$

---

### Step 3: Compute y-coordinate

$$
y_3=\lambda(x_1-x_3)-y_1
$$

Hence,

$$
2P=(x_3,y_3)
$$

---

# Special Cases

### 1. Identity Element

There exists a special point called the **point at infinity**, denoted by

$$
O.
$$

It acts as the identity element.

$$
P+O=P
$$

---

### 2. Adding a Point to Its Inverse

If

$$
Q=(x,-y)
$$

then

$$
P+(-P)=O
$$

because the line through them is vertical.

---

# Numerical Example (Real Numbers)

Let

$$
P=(2,5), \qquad Q=(-1,2)
$$

### Step 1

$$
\lambda=\frac{2-5}{-1-2}
=\frac{-3}{-3}
=1
$$

### Step 2

$$
x_3=1^2-2-(-1)=0
$$

### Step 3

$$
y_3=1(2-0)-5=-3
$$

Therefore,

$$
P+Q=(0,-3)
$$

*(In practical ECC, calculations are performed modulo a prime, not over the real numbers.)*

---

# Why Point Addition is Important

Point addition is the foundation of ECC because repeated addition creates **scalar multiplication**:

$$
kP=P+P+\cdots+P
$$

($P$ added $k$ times.)

Scalar multiplication is easy to compute, but reversing it (finding $k$ from $P$ and $Q=kP$) is computationally hard. This hard problem is known as the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**, which provides the security for ECC.

---

# Exam Answer (5 Marks)

**Addition of Points on Elliptic Curves**

* Point addition is the fundamental operation in ECC.
* For two different points $P=(x_1,y_1)$ and $Q=(x_2,y_2)$,

$$
\lambda=\frac{y_2-y_1}{x_2-x_1}
$$

$$
x_3=\lambda^2-x_1-x_2
$$

$$
y_3=\lambda(x_1-x_3)-y_1
$$

giving

$$
P+Q=(x_3,y_3).
$$

* For point doubling ($P=Q$),

$$
\lambda=\frac{3x_1^2+a}{2y_1}
$$

$$
x_3=\lambda^2-2x_1
$$

$$
y_3=\lambda(x_1-x_3)-y_1.
$$

* The point at infinity $O$ is the identity element:

$$
P+O=P.
$$

* Point addition is repeatedly used to perform scalar multiplication, which is the basis of ECC security through the Elliptic Curve Discrete Logarithm Problem (ECDLP).
