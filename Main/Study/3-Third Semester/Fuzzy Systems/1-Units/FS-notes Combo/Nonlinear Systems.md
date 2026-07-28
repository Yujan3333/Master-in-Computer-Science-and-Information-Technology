
#fuzzy-system #third-semester

# Nonlinear Systems

## Definition

A **nonlinear system** is a system that **does not satisfy the principles of superposition and homogeneity**. Therefore, its output is **not directly proportional** to its input.

---

## Conditions for a Linear System

A system is **linear** only if it satisfies **both** of the following properties.

### 1. Additivity (Superposition)

If

$$
y_1=f(x)
$$

and

$$
y_2=f(z)
$$

then

$$
f(x+z)=f(x)+f(z)
$$

**Example**

Suppose

$$
f(x)=2x
$$

Then

$$
f(2+3)=2(5)=10
$$

and

$$
f(2)+f(3)=4+6=10
$$

Hence, the additivity property is satisfied.

---

### 2. Homogeneity (Scaling)

If

$$
y=f(x)
$$

then

$$
f(ax)=af(x)
$$

where $a$ is any constant.

**Example**

Let

$$
f(x)=2x
$$

Take

$$
a=3,\qquad x=2
$$

Then

$$
f(3\times2)=f(6)=12
$$

and

$$
3f(2)=3\times4=12
$$

Hence, homogeneity is satisfied.

---

## Nonlinear System

A system is **nonlinear** if it violates **either** additivity or homogeneity.

**Example**

Let

$$
f(x)=x^2
$$

Check additivity:

$$
f(2+3)=25
$$

but

$$
f(2)+f(3)=4+9=13
$$

Since

$$
25\ne13
$$

the system is **nonlinear**.

---

# Why Nonlinear Systems are Difficult

* Output is not proportional to input.
* Superposition principle cannot be applied.
* Mathematical analysis is more difficult.
* Most real-world systems are nonlinear.

---

# Sliding Mode Control (SMC)

## Definition

**Sliding Mode Control (SMC)** is a **robust nonlinear control technique** used to control systems in the presence of:

* Model uncertainty
* Parameter variations
* External disturbances

It forces the system states to move along a predefined **sliding surface** until the desired output is achieved.

---

## Working Principle

1. Define a sliding surface.
2. Drive the system state toward the surface.
3. Once it reaches the surface, the controller keeps the state sliding along it toward the desired value.

```text
State

        •
      /
    /
Sliding Surface ---------------------> Desired State
```

---

## Advantages

* Highly robust.
* Handles uncertainties well.
* Good tracking performance.
* Works well for robotic manipulators and motor control.

---

## Disadvantage

The controller switches rapidly between control actions, producing

**Chattering**

which causes

* vibration,
* wear of mechanical parts,
* high stress on actuators.

---

## Solution to Chattering

Introduce a **Boundary Layer** around the sliding surface.

Instead of switching abruptly,

```text
ON ←→ OFF ←→ ON ←→ OFF
```

the controller changes smoothly.

This greatly reduces chattering.

---

# Fuzzy Knowledge-Based Controller (FKBC)

## Definition

A **Fuzzy Knowledge-Based Controller (FKBC)** is a fuzzy controller that uses **IF–THEN fuzzy rules** and expert knowledge to control nonlinear systems.

It combines fuzzy logic with sliding mode control to improve robustness and reduce chattering.

---

## Working Principle

1. Measure system states.
2. Normalize (scale) the inputs.
3. Apply fuzzy IF–THEN rules.
4. Compute the control action.
5. Send the control signal to the plant.

---

## Advantages of FKBC over Sliding Mode Control

* Higher robustness.
* Reduced chattering.
* Better handling of uncertainties.
* Smooth control action.
* Better performance for nonlinear systems.

---

# Difference Between Sliding Mode Control and FKBC

| Sliding Mode Control           | FKBC                                          |
| ------------------------------ | --------------------------------------------- |
| Uses switching control         | Uses fuzzy IF–THEN rules                      |
| High robustness                | Higher robustness                             |
| Chattering problem             | Chattering greatly reduced                    |
| Abrupt control action          | Smooth control action                         |
| Suitable for nonlinear systems | More suitable for uncertain nonlinear systems |

---

# 5-Mark Exam Answer

A **nonlinear system** is a system that does not satisfy the **additivity (superposition)** and **homogeneity (scaling)** properties. Therefore, its output is not directly proportional to its input. Most practical systems such as robots, motors, and industrial processes are nonlinear.

**Sliding Mode Control (SMC)** is a robust nonlinear control method that maintains good performance even in the presence of uncertainties and disturbances. However, it suffers from **chattering**, which causes rapid switching of the control signal.

A **Fuzzy Knowledge-Based Controller (FKBC)** combines fuzzy logic with control techniques to reduce chattering while improving robustness. It uses fuzzy IF–THEN rules to generate smooth control actions, making it more effective than conventional sliding mode control for nonlinear systems.
