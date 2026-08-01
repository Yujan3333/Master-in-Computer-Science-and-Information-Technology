#ippr #third-semester 

This is a **rectangular pulse Fourier Transform** problem. It appears frequently in DIP and Signals exams.

---

# Question

Sketch the following waveform in the time domain and calculate its Fourier Transform.

$$
f(t)=
\begin{cases}
3, & -2\le t\le 2\
0, & \text{otherwise}
\end{cases}
$$

---

# Step 1: Sketch the Signal

The signal has:

* Amplitude = 3
* Exists from $t=-2$ to $t=2$
* Zero elsewhere

```text
f(t)

3 |          ┌─────────────┐
  |          │             │
  |          │             │
0 |──────────┘             └──────────────► t
          -2              2
```

The pulse width is

$$
T=2-(-2)=4
$$

---

# Step 2: Fourier Transform Formula

The continuous-time Fourier Transform is

$$
F(\omega)
=========

\int_{-\infty}^{\infty}
f(t)e^{-j\omega t},dt
$$

Since

$$
f(t)=3
$$

only for

$$
-2\le t\le2,
$$

the limits become

$$
F(\omega)
=========

\int_{-2}^{2}
3e^{-j\omega t},dt
$$

Take the constant outside.

$$
F(\omega)
=========

3\int_{-2}^{2}
e^{-j\omega t},dt
$$

---

# Step 3: Integrate

We know

$$
\int e^{-j\omega t},dt
=

\frac{e^{-j\omega t}}{-j\omega}
$$

Therefore,

$$
F(\omega)
=

3
\left[
\frac{e^{-j\omega t}}{-j\omega}
\right]_{-2}^{2}
$$

Substitute the limits.

$$

\frac{3}{-j\omega}
\left(
e^{-j2\omega}
-

e^{j2\omega}
\right)
$$

---

# Step 4: Apply Euler Identity

Using

$$
e^{-j\theta}-e^{j\theta}
========================

-2j\sin\theta
$$

with

$$
\theta=2\omega,
$$

we get

$$
F(\omega)
=========

\frac{3}{-j\omega}
(-2j\sin2\omega)
$$

Cancel $j$.

$$
F(\omega)
=========

\frac{6\sin2\omega}{\omega}
$$

---

# Final Answer

$$
\boxed{
F(\omega)
=========

\frac{6\sin(2\omega)}{\omega}
}
$$

---

# Alternative sinc Form

Since

$$
\operatorname{sinc}(x)
=

\frac{\sin x}{x},
$$

we can also write

$$
F(\omega)
=

12
,
\operatorname{sinc}(2\omega)
$$

because

$$
12,
\frac{\sin(2\omega)}{2\omega}
=

\frac{6\sin(2\omega)}{\omega}.
$$

---

# Important Observation

Since the signal is

* **real**, and
* **even**,

its Fourier Transform is also

* **real**, and
* **even**.

---

# Exam Answer (10 Marks)

**Given:**

$$
f(t)=
\begin{cases}
3, & -2\le t\le2\
0, & \text{otherwise}
\end{cases}
$$

**Sketch:**

```text
f(t)

3 |          ┌─────────────┐
  |          │             │
  |          │             │
0 |──────────┘             └──────────────► t
          -2              2
```

**Fourier Transform:**

$$
F(\omega)
=

\int_{-\infty}^{\infty}
f(t)e^{-j\omega t},dt
$$

$$

3\int_{-2}^{2}
e^{-j\omega t},dt
$$

$$

3
\left[
\frac{e^{-j\omega t}}{-j\omega}
\right]_{-2}^{2}
$$

$$

\frac{3}{-j\omega}
\left(
e^{-j2\omega}
-

e^{j2\omega}
\right)
$$

Using

$$
e^{-j\theta}-e^{j\theta}
=

-2j\sin\theta,
$$

we obtain

$$
\boxed{
F(\omega)
=========

\frac{6\sin(2\omega)}{\omega}
}
$$

This is the Fourier Transform of the given rectangular pulse.
