
#fuzzy-system #third-semester

# Sliding Mode FKBC (Fuzzy Knowledge-Based Controller)

## Definition

**Sliding Mode FKBC (Fuzzy Knowledge-Based Controller)** is a **nonlinear control technique** that combines **Sliding Mode Control (SMC)** with **Fuzzy Logic Control (FLC)** to obtain a controller that is **robust, smooth, and less sensitive to uncertainties**.

It retains the robustness of Sliding Mode Control while reducing its main drawback, **chattering**.

---

# Why is FKBC Needed?

Traditional **Sliding Mode Control (SMC)** has excellent robustness but suffers from **chattering**.

Chattering is the rapid switching of the control signal.

```text
Ideal SMC

ON OFF ON OFF ON OFF ON OFF ...
```

This rapid switching can cause:

* Mechanical wear
* Vibrations
* Noise
* Damage to actuators

FKBC replaces the abrupt switching with fuzzy reasoning, producing a smoother control signal.

```text
FKBC

──────╱╲────╱╲────╱╲────
(Smooth control)
```

---

# Working Principle of FKBC

The controller works in the following steps:

1. Measure the system state.
2. Calculate the error and change in error.
3. Normalize (scale) the inputs.
4. Apply fuzzy IF–THEN rules.
5. Generate a smooth control signal.
6. Control the plant while keeping the system near the sliding surface.

---

# Block Diagram

```text
Desired Output
      │
      ▼
 Error Calculation
      │
      ▼
Normalization
      │
      ▼
Fuzzy Rule Base
(IF–THEN Rules)
      │
      ▼
Defuzzification
      │
      ▼
Control Signal
      │
      ▼
Plant/System
      │
      ▼
Feedback
```

---

# Main Components

### 1. State Vector

Represents the current condition of the system.

Example

$$
x=
[x_1,x_2,\ldots,x_n]
$$

---

### 2. Sliding Surface

A desired surface on which the system should move.

Once the state reaches this surface, it slides toward the desired output.

---

### 3. Normalization

The input variables are scaled into a standard range (often between $-1$ and $1$).

This improves the performance of the fuzzy controller.

---

### 4. Fuzzy Rule Base

Uses expert knowledge in the form of IF–THEN rules.

Example

* IF error is Positive Large THEN control is Negative Large.
* IF error is Zero THEN control is Zero.
* IF error is Negative Large THEN control is Positive Large.

---

### 5. Defuzzification

Converts the fuzzy control action into a crisp control signal.

---

# Advantages

* High robustness.
* Reduces chattering.
* Handles parameter variations.
* Handles model uncertainties.
* Smooth control action.
* Suitable for nonlinear systems.
* Good tracking performance.

---

# Disadvantages

* Designing fuzzy rules can be difficult.
* Performance depends on proper tuning.
* More computationally complex than simple controllers.

---

# Applications

* Robot manipulators
* Motor speed control
* Industrial process control
* Aerospace systems
* Automotive control
* Servo systems

---

# Difference Between Sliding Mode Control and FKBC

| Sliding Mode Control   | Sliding Mode FKBC               |
| ---------------------- | ------------------------------- |
| Uses switching control | Uses fuzzy logic with switching |
| High robustness        | Higher robustness               |
| Severe chattering      | Chattering greatly reduced      |
| Abrupt control         | Smooth control                  |
| Less flexible          | More adaptive and flexible      |

---

# 5-Mark Exam Answer

**Sliding Mode Fuzzy Knowledge-Based Controller (FKBC)** is a nonlinear control technique that combines **Sliding Mode Control (SMC)** with **Fuzzy Logic Control (FLC)**. It is designed to control nonlinear systems in the presence of uncertainties, parameter variations, and external disturbances.

In FKBC, the system state is normalized and processed using fuzzy IF–THEN rules to generate a smooth control signal. This smooth control reduces the **chattering** problem found in conventional Sliding Mode Control while maintaining high robustness and good tracking performance.

**Advantages:** high robustness, reduced chattering, smooth control action, and effective handling of uncertainties.

**Applications:** robot manipulators, motor drives, industrial automation, aerospace, and automotive control systems.

---

## Easy way to remember

* **Sliding Mode Control (SMC)** = Robust but **chattering**.
* **FKBC** = **SMC + Fuzzy Logic** = Robust **with much less chattering**.
