#fuzzy-system #third-semester 

# 3. PID Controller (Exam Summary)

## Definition 

A **PID (Proportional–Integral–Derivative) Controller** is a **feedback control mechanism** widely used in industrial control systems. It calculates the **error** between the **Process Variable (PV)** and the **Setpoint (SP)** and minimizes this error by adjusting the **Manipulated Variable (MV)**. 

Error:

$$
e(t)=SP-PV
$$

---

# Main Idea

The PID controller combines **three control actions**:

* **P (Proportional)** → Present error
* **I (Integral)** → Past accumulated errors
* **D (Derivative)** → Future trend (rate of change)

The outputs of these three actions are added together to produce the **Manipulated Variable (MV)**, which controls the process. 

---

# PID Formula (Know It)

The notes state that the controller output is the sum of the three terms:

$$
u(t)=K_p e(t)+K_i\int e(t),dt+K_d\frac{de(t)}{dt}
$$

where

* $u(t)$ = Controller output (Manipulated Variable)
* $e(t)$ = Error
* $K_p$ = Proportional gain
* $K_i$ = Integral gain
* $K_d$ = Derivative gain 

> **Exam Tip:** You usually only need to remember the formula and what each term means, not derive it.

---

# 1. Proportional (P) Term ⭐⭐⭐⭐⭐

## Definition

The proportional term produces an output that is **proportional to the current error**.

Formula:

$$
P=K_p e(t)
$$

where

* $K_p$ = Proportional gain
* $e(t)$ = Current error 

### Key Points

* Looks at the **present error**.
* Large error → Large correction.
* Small error → Small correction.
* Fast response.

### Effect of Gain

* **High $K_p$**

  * Faster response.
  * May become unstable.
  * Can cause overshoot.

* **Low $K_p$**

  * Slow response.
  * Less sensitive.
  * May not respond well to disturbances. 

### Memory

> **Present**

---

# 2. Integral (I) Term ⭐⭐⭐⭐⭐

## Definition

The integral term depends on **both the magnitude and the duration of the error**. It adds (accumulates) the error over time.

Formula:

$$
I=K_i\int e(t),dt
$$



### Key Points

* Looks at **past accumulated errors**.
* Eliminates **steady-state error**.
* Improves long-term accuracy.
* Accelerates movement toward the setpoint.

### Disadvantage

Since it accumulates past errors, it can cause **overshoot** if the accumulated correction becomes too large. 

### Memory

> **Past**

---

# 3. Derivative (D) Term ⭐⭐⭐⭐⭐

## Definition

The derivative term depends on the **rate of change (slope) of the error**.

Formula:

$$
D=K_d\frac{de(t)}{dt}
$$



### Key Points

* Looks at **how fast the error is changing**.
* Predicts future behavior.
* Improves stability.
* Reduces overshoot.
* Improves settling time.

### Disadvantage

The notes mention that derivative action is sensitive to **high-frequency noise**, so practical PID controllers include filtering for the derivative term. 

### Memory

> **Future**

---

# Why is PID Popular?

According to the notes:

* Widely used in industry.
* Works well even without detailed knowledge of the process.
* Can be tuned for different applications by adjusting **$K_p$, $K_i$, and $K_d$**.
* Does **not guarantee** optimal control or system stability. 

---

# Variants of PID

The notes state that sometimes only one or two actions are needed. The unused gains are set to zero.

Examples:

* **P Controller**
* **PI Controller**
* **PD Controller**
* **I Controller**

The notes also mention:

* **PI controllers are common** because derivative action is sensitive to measurement noise.
* Without the integral term, the system may not reach the exact target value. 

---

# Easy Comparison Table

| Term  | Looks At                | Main Purpose                        | Main Drawback                                         |
| ----- | ----------------------- | ----------------------------------- | ----------------------------------------------------- |
| **P** | Present error           | Quick response                      | May leave steady-state error; high gain can overshoot |
| **I** | Past accumulated errors | Removes steady-state error          | Can cause overshoot                                   |
| **D** | Rate of change of error | Predicts future, improves stability | Sensitive to noise                                    |

---

# Advantages of PID

* Simple and widely used.
* Fast response.
* Reduces steady-state error (Integral).
* Improves stability (Derivative).
* Can be tuned for many industrial processes. 

---

# Limitations

* Requires tuning of gains ($K_p$, $K_i$, $K_d$).
* Does not always guarantee optimal or stable control.
* Derivative action is sensitive to measurement noise.

---

# 5-Mark Exam Answer

A **PID (Proportional–Integral–Derivative) Controller** is a widely used **feedback controller** that minimizes the error between the **Process Variable (PV)** and the **Setpoint (SP)** by adjusting the **Manipulated Variable (MV)**. It combines three control actions: **Proportional (P)**, which responds to the **current error**; **Integral (I)**, which accumulates **past errors** to eliminate steady-state error; and **Derivative (D)**, which uses the **rate of change of the error** to predict future behavior and improve stability. The controller output is the sum of these three terms:

$$
u(t)=K_p e(t)+K_i\int e(t),dt+K_d\frac{de(t)}{dt}
$$

PID controllers are widely used because they can be tuned for different applications, although they require proper tuning and do not guarantee optimal control or stability. 

---

# Super Memory Trick (Very Useful)

Think of three engineers controlling a heater:

* **P Engineer:** "How wrong is the temperature **right now**?" (**Present**)
* **I Engineer:** "Has it been wrong **for a long time**?" (**Past**)
* **D Engineer:** "How fast is the temperature changing, and **where is it heading**?" (**Future**)

### One-line memory:

* **P = Present**
* **I = Past**
* **D = Future**

This is one of the most common conceptual questions asked about PID controllers.
