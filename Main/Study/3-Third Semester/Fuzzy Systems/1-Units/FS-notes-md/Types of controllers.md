#fuzzy-system #third-semester 


---

# Types of Controllers (Quick Exam Notes)

## 1. On-Off Controller (Bang-Bang Controller)

### Definition

An **On-Off controller** switches only between **ON** and **OFF** states. There is no intermediate output. It is the simplest type of feedback controller. 

### Key Points

* Only two outputs:

  * ON
  * OFF
* Uses **hysteresis (deadband)** to avoid frequent switching.
* Cheap and simple.
* Commonly used in **thermostats** and **furnaces**.
* Can cause wear if switched too frequently.

### Example

* Temperature < 20°C → Heater ON
* Temperature > 20°C → Heater OFF

### Exam Keywords

* Binary controller
* Hysteresis
* Deadband
* Thermostat

---

# 2. Proportional (P) Controller

### Definition

The controller output is **directly proportional to the current error**.

$$
e = SP - PV
$$

Output:

$$
P_{out}=K_p e(t)+P_0
$$

where:

* SP = Set Point
* PV = Process Variable
* $K_p$ = Proportional gain 

### Key Points

* Looks at the **present error only**.
* Large error → Large correction.
* Small error → Small correction.
* Fast response.
* May leave **steady-state error**.

### Advantages

* Simple
* Quick response

### Disadvantages

* Cannot completely eliminate steady-state error.
* Very high gain may cause instability.

### Memory

> **Present Error**

---

# 3. PID Controller

### Definition

A **PID controller** combines three control actions:

* P → Proportional
* I → Integral
* D → Derivative

to minimize the error between the process variable and setpoint. It is the **most widely used industrial controller**. 

---

## (a) Proportional Term (P)

### Purpose

Reacts according to the **current error**.

### Key Points

* Looks at present error.
* Faster response.
* High gain → Overshoot/instability.
* Low gain → Slow response. 

**Memory**

> Present

---

## (b) Integral Term (I)

### Purpose

Uses the **accumulated past errors**.

### Key Points

* Eliminates steady-state error.
* Improves accuracy.
* Can cause overshoot because it accumulates errors. 

**Memory**

> Past

---

## (c) Derivative Term (D)

### Purpose

Uses the **rate of change of the error**.

### Key Points

* Predicts future error.
* Improves stability.
* Reduces overshoot.
* Improves settling time.
* Sensitive to measurement noise. 

**Memory**

> Future

---

## Easy Way to Remember PID

| Controller | Looks At     | Main Purpose                          |
| ---------- | ------------ | ------------------------------------- |
| **P**      | Present      | Quick correction                      |
| **I**      | Past         | Remove steady-state error             |
| **D**      | Future trend | Prevent overshoot & improve stability |

---

# 4. Adaptive Controller

### Definition

An **Adaptive Controller** automatically changes its controller parameters when the system characteristics change over time or are uncertain. 

### Why Needed?

Many real-world systems change over time, so a fixed controller may no longer perform well. Adaptive controllers **retune themselves automatically**. 

### Main Components

1. **Process Monitor** – Detects changes in the process.
2. **Adaptation Mechanism** – Updates controller parameters. 

### Types

* Feedforward Adaptive Control
* Feedback Adaptive Control
* Direct Method
* Indirect Method 

### Example

Aircraft control:

* Aircraft mass decreases as fuel is consumed.
* Controller automatically adjusts itself.

### Exam Keywords

* Self-tuning
* Parameter estimation
* Process monitor
* Adaptation mechanism

---

# 5. Model-Based Controller

### Definition

A **Model-Based Controller** uses a **mathematical (fuzzy) model of the process** to predict the system behavior and choose the best control action. 

### Main Parts

1. Fuzzy Process Model
2. Controller Performance Measure
3. Decision Maker

### Key Idea

Predict the output for different control actions and choose the one with the best predicted performance.

### Exam Keywords

* Mathematical model
* Prediction
* Decision maker

---

# 6. Model Predictive Controller (MPC)

### Definition

A **Model Predictive Controller (MPC)** predicts **future outputs** using:

* Current measurements
* A dynamic model of the process 

### Key Points

* Predicts future behavior.
* Selects the best future control action.
* Suitable for complex industrial processes.

### Exam Keywords

* Prediction
* Dynamic model
* Future output

---

# 7. MRAC (Model Reference Adaptive Controller)

### Definition

MRAC is an adaptive controller in which the system output is continuously compared with a **reference model**. The controller parameters are updated so that the plant behaves like the reference model. 

### Key Points

* Uses a **reference model**.
* Calculates **tracking error**:

$$
e = y_{plant} - y_{model}
$$

* Updates controller parameters automatically.
* Goal: Make the plant output match the reference model.

### Example

Robot arm position control.

### Exam Keywords

* Reference model
* Tracking error
* Adaptive controller

---

# Final One-Page Revision Table

| Controller      | Main Idea                    | Key Feature                             | Example                    |
| --------------- | ---------------------------- | --------------------------------------- | -------------------------- |
| **On-Off**      | ON or OFF only               | Simple, uses hysteresis/deadband        | Thermostat                 |
| **P**           | Uses current error           | Fast response                           | Temperature control        |
| **I**           | Uses accumulated past error  | Removes steady-state error              | PID control                |
| **D**           | Uses rate of change of error | Predicts future, reduces overshoot      | PID control                |
| **PID**         | Combines P + I + D           | Most common industrial controller       | Industrial process control |
| **Adaptive**    | Self-adjusts parameters      | Handles changing systems                | Aircraft control           |
| **Model-Based** | Uses process model           | Chooses best predicted action           | Fuzzy model controller     |
| **MPC**         | Predicts future outputs      | Dynamic model based                     | Chemical plants            |
| **MRAC**        | Follows a reference model    | Updates parameters using tracking error | Robot arm control          |

## Most Important Topics for Exams (⭐⭐⭐⭐⭐)

If your exam asks about controllers, focus most on:

1. **On-Off Controller** – definition, hysteresis, deadband, thermostat.
2. **P Controller** – current error, proportional gain, steady-state error.
3. **PID Controller** – **P = Present, I = Past, D = Future**, advantages and disadvantages of each term.
4. **Adaptive Controller** – definition, need, **process monitor** and **adaptation mechanism**.
5. **MRAC** – reference model, tracking error, adaptive parameter update.

The remaining controllers (**Model-Based** and **Model Predictive**) are usually asked as short notes unless your instructor emphasizes them.
