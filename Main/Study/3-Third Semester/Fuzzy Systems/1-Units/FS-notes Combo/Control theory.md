#fuzzy-system #third-semester 

# Control Theory 

## Definition

**Control Theory** is an interdisciplinary branch of **engineering and mathematics** that studies the behavior of **dynamic systems** and how to control them to produce the desired output.

A **controller** adjusts the system's input so that the output follows a desired value called the **reference (or set point)**. 

---

# Simple Explanation

Think of driving a car.

Suppose you want to maintain a speed of **60 km/h**.

* **Reference (Set Point)** = 60 km/h
* **Current Speed** = 55 km/h

The controller (you) notices the difference and presses the accelerator to increase the speed.

If the speed becomes **65 km/h**, you reduce the accelerator.

This continuous adjustment is the basic idea of **control theory**.

---

# Important Terms

### 1. Dynamic System

A **dynamic system** is a system whose output changes with time.

Examples:

* Car speed
* Room temperature
* Water level in a tank
* Robot movement

---

### 2. Reference (Set Point)

The **reference** is the **desired output**.

Examples:

* Desired temperature = 25°C
* Desired speed = 60 km/h

---

### 3. Controller

The **controller** compares the actual output with the desired output and adjusts the input to reduce the difference.

---

# Negative Feedback

The notes explain that control theory uses a **negative feedback loop**. 

The process is:

```text
Desired Output (Reference)
            │
            ▼
      Compare with
      Actual Output
            │
            ▼
 Error = Desired − Actual
            │
            ▼
      Controller
            │
            ▼
     Adjust System Input
            │
            ▼
      System Output
            │
            └────────── Feedback ──────────►
```

### Why is it called Negative Feedback?

Because the **actual output is subtracted from the desired output** to produce the **error**:

$$
\text{Error}=\text{Desired Output}-\text{Actual Output}
$$

The controller uses this error to correct the system.

---

# Characteristics of Control Theory

According to the notes, control theory:

* Deals with **influencing the behavior of dynamic systems**.
* Is an **interdisciplinary field**.
* Originated in **engineering and mathematics**.
* Has applications in:

  * Psychology
  * Sociology
  * Criminology
  * Financial systems 

---

# Four Functions of a Control System

The notes state that every control system performs **four basic functions**.

### 1. Measure

Measure the current output.

Example:

Measure the room temperature.

---

### 2. Compare

Compare the measured value with the desired value.

Example:

Desired = 25°C

Measured = 22°C

Difference = 3°C

---

### 3. Compute

Determine what action should be taken.

Example:

Increase heater power.

---

### 4. Correct

Apply the corrective action.

Example:

Turn the heater on until the room reaches 25°C.

---

# Five Elements of a Control System

The notes list **five elements**:

| Element               | Function                                             |   |
| --------------------- | ---------------------------------------------------- | - |
| Detector              | Detects the physical quantity.                       |   |
| Transducer            | Converts the physical quantity into a usable signal. |   |
| Transmitter           | Sends the signal to the controller.                  |   |
| Controller            | Computes the corrective action.                      |   |
| Final Control Element | Applies the corrective action to the system.         |   |

> **Note:** According to the notes, the **measuring function** is completed by the **Detector, Transducer, and Transmitter**.

---

# Objective of Control Theory

The notes state that the main objective is:

* To calculate the **proper corrective action**.
* To maintain **system stability**.
* To ensure the system reaches and maintains the **set point**.
* To prevent the system from **oscillating** around the set point. 

---

# Real-Life Example: Air Conditioner

Suppose:

* Desired temperature = **24°C**
* Current temperature = **28°C**

The control system works as follows:

1. **Measure** → Sensor measures 28°C.
2. **Compare** → Difference = 24 − 28 = −4°C.
3. **Compute** → Controller decides to increase cooling.
4. **Correct** → Air conditioner cools the room.

When the room reaches **24°C**, the controller reduces or stops cooling to maintain the set temperature.

---

# Key Points

* Control theory studies **dynamic systems**.
* The **reference (set point)** is the desired output.
* The **controller** adjusts the system input to achieve the desired output.
* It uses **negative feedback**, where the actual output is subtracted from the desired output to calculate the error.
* A control system performs four functions: **Measure, Compare, Compute, and Correct**.
* Its objective is to achieve **stability** and maintain the **set point** without oscillations.

---

# 5-Mark Exam Answer

**Control Theory** is an interdisciplinary branch of engineering and mathematics that deals with controlling the behavior of **dynamic systems**. A controller manipulates the system's input so that the output follows a desired **reference (set point)**. It uses a **negative feedback loop**, where the actual output is compared with the desired output to generate an **error signal**, which is then used by the controller to make corrective actions. According to the notes, a control system performs four basic functions: **Measure, Compare, Compute, and Correct**. These are carried out using five elements: **Detector, Transducer, Transmitter, Controller, and Final Control Element**. The main objective of control theory is to maintain **system stability**, achieve the desired set point, and avoid oscillations. 

---

## Exam Tip

Remember these two lists:

### Four Functions

* Measure
* Compare
* Compute
* Correct

### Five Elements

* Detector
* Transducer
* Transmitter
* Controller
* Final Control Element

These are frequently asked in theory questions.
