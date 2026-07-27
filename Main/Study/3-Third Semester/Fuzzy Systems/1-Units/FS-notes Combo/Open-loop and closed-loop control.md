#fuzzy-system #third-semester 
# Control Loop Basics (Exam Summary)

## Definition

A **control loop** is a process in which the **output of a system is continuously measured, compared with the desired value (setpoint), and corrected if necessary**. The goal is to keep the system operating at the desired value. 

---

# Water Tap Example (from the Notes)

The notes explain control loops using the example of **mixing hot and cold water**.

### Goal

Fill a container with water at the **desired temperature**.

### How it works

1. Touch the water to measure its temperature.
2. Compare it with the desired temperature.
3. If the water is too cold → open the hot tap more.
4. If the water is too hot → open the cold tap more.
5. Repeat until the desired temperature is reached.

This continuous process of **measuring → comparing → correcting** is called a **control loop**. 

---

# Important Terms

The notes introduce several terms used in control systems.

### 1. Process Variable (PV)

The **actual output** of the system that is measured.

**Example:**

* Actual water temperature.

---

### 2. Setpoint (SP)

The **desired value** of the output.

**Example:**

* Desired water temperature = **40°C**.

---

### 3. Manipulated Variable (MV) / Control Variable (CV)

The **input** that the controller changes to control the system.

**Example:**

* Position of the hot and cold water taps.

---

### 4. Error (e)

The difference between the desired value and the measured value.

$$
e = SP - PV
$$

where:

* **SP** = Setpoint
* **PV** = Process Variable

Example:

Desired temperature = 40°C

Measured temperature = 35°C

$$
e = 40 - 35 = 5^\circ C
$$

The controller uses this error to decide how much to adjust the taps. 

---

# How the Controller Works

After measuring the temperature:

1. Measure **PV**.
2. Calculate **Error**.
3. Decide the new **MV**.
4. Adjust the taps.
5. Measure again.

This process repeats continuously.

---

# Types of Control Actions

The notes briefly describe three control actions.

## 1. Proportional (P) Control

The tap position is changed **proportionally** to the current error.

* Large error → Large adjustment.
* Small error → Small adjustment.

Example:

If water is much colder than desired, open the hot tap much more.

- *Reacts to the current error and tries to get to SP*
---

## 2. Derivative (D) Control

Derivative control considers the **rate of temperature change**.

Example:

* If temperature is falling quickly, add more hot water.
* If temperature is rising quickly, reduce hot water.

It predicts future changes based on the current trend.

- *Doesn't try to overshoot if falling quickly or rising quickly*
- **Example** - *36->37 -> 38->39 too quickly rate of change is happening then tries to stop before it overshoots*
---

## 3. Integral (I) Control

Integral control considers **past errors**.

If the temperature has remained slightly too low for a long time, it gradually increases the hot water until the error disappears.

It removes long-term or steady-state error. 

- *Accumulates past errors. If the system keeps staying below or above the setpoint for a long time, it gradually increases or decreases the control until the error becomes zero.*

- *Removes **steady state error***
---

# Applications

According to the notes, controllers can regulate almost any measurable variable, including:

* Temperature
* Pressure
* Force
* Feed
* Flow rate
* Chemical composition
* Weight
* Position
* Speed 

---

# Open-Loop Control

The notes use **cruise control** as an example.

### Example

Suppose cruise control fixes the throttle position.

If:

* The road goes uphill → the car slows down.
* The road goes downhill → the car speeds up.

The controller **does not measure the car's speed**.

Therefore, it cannot correct the speed.

This is called an **open-loop controller**. 

### Characteristics

* No feedback.
* Output is not measured.
* Cannot compensate for disturbances.

---

# Closed-Loop Control

In a **closed-loop system**, a sensor continuously measures the output and sends it back to the controller.

### Cruise Control Example

Suppose:

Desired speed = **80 km/h**

Actual speed becomes **75 km/h** while climbing a hill.

The controller:

1. Measures speed.
2. Finds the error.
3. Opens the throttle more.
4. Speed returns to 80 km/h.

When going downhill, the controller reduces the throttle to maintain the desired speed.

This feedback allows the controller to compensate for changes automatically. 

---

# Closed-Loop Feedback Process

```text
Reference (SP)
      │
      ▼
 Compare with PV
      │
      ▼
 Error = SP − PV
      │
      ▼
 Controller
      │
      ▼
 Manipulated Variable (MV)
      │
      ▼
 Process/System
      │
      ▼
 Process Variable (PV)
      │
      └──────── Feedback ───────►
```

---

# Open-Loop vs Closed-Loop

| Open-Loop Control                      | Closed-Loop Control                  |
| -------------------------------------- | ------------------------------------ |
| No feedback                            | Uses feedback                        |
| Output is not measured                 | Output is continuously measured      |
| Cannot correct disturbances            | Automatically corrects disturbances  |
| Simpler and cheaper                    | More accurate but more complex       |
| Example: Fixed throttle cruise control | Example: Sensor-based cruise control |

---

# Key Points

* A **control loop** continuously **measures, compares, computes, and corrects** the system output.
* **PV (Process Variable)** is the measured output.
* **SP (Setpoint)** is the desired output.
* **MV/CV (Manipulated/Control Variable)** is the input adjusted by the controller.
* **Error** is calculated as:

$$
e = SP - PV
$$

* **Open-loop control** does not use feedback.
* **Closed-loop control** uses feedback to maintain the desired output.

---

# 5-Mark Exam Answer

**Control Loop Basics:**
A **control loop** is a mechanism in which the output of a system is continuously measured, compared with a desired value (**setpoint**), and corrected by a controller. The notes explain this using the example of adjusting hot and cold water taps to obtain the desired water temperature. The **Process Variable (PV)** is the measured output, the **Setpoint (SP)** is the desired value, the **Manipulated Variable (MV)** is the controller's input to the process, and the **Error (e)** is the difference between the setpoint and the process variable. Controllers may use **proportional**, **integral**, and **derivative** actions to reduce the error. The notes also distinguish **open-loop control**, which operates without feedback, from **closed-loop control**, which uses feedback to measure the output and automatically correct disturbances, making it more accurate and stable. 

---

## Exam Tip

Remember these four symbols—they are frequently asked:

* **SP** → Setpoint (desired value)
* **PV** → Process Variable (measured output)
* **MV/CV** → Manipulated/Control Variable (input adjusted by the controller)
* **e = SP − PV** → Error signal
