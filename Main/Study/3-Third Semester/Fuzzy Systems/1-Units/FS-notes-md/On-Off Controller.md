#fuzzy-system #third-semester 

# 1. On-Off Controller (Exam Summary)

## Definition

An **On-Off Controller** (also called a **Bang-Bang Controller** or **Hysteresis Controller**) is a **feedback controller** that switches abruptly between only **two states: ON and OFF**. There is **no intermediate output**. It is commonly used in systems that accept a binary input, such as a furnace or a residential thermostat. 

---

# Key Points ⭐⭐⭐⭐⭐

* Also called **Bang-Bang Controller**.
* Has only **two outputs**:

  * ON
  * OFF
* Works using **feedback**.
* Used where the actuator has only two states.
* **Simple, cheap, and effective**.
* Common applications:

  * Thermostat
  * Furnace
  * Refrigerator

---

# Hysteresis (Very Important)

### Definition

**Hysteresis** means the controller's output depends **not only on the current input but also on the past input (history).** 

### Why is it Needed?

Without hysteresis, the controller would switch ON and OFF repeatedly when the process variable is very close to the setpoint.

Example:

Suppose

Setpoint = **25°C**

Without hysteresis

```text
24.9°C → Heater ON

25.0°C → Heater OFF

24.9°C → Heater ON

25.0°C → Heater OFF
```

This rapid switching is called **chattering**.

---

# Deadband (Very Important)

To prevent rapid switching, the controller introduces a **deadband**.

### Definition

A **deadband** is a small region around the setpoint where **no control action is taken**. 

Example

Suppose

Setpoint = **25°C**

Deadband = **±1°C**

```text
Temperature < 24°C
↓

Heater ON
```

```text
24°C–26°C
↓

No switching
```

```text
Temperature > 26°C
↓

Heater OFF
```

This greatly reduces unnecessary switching and equipment wear.

---

# Advantages

* Very simple.
* Low cost.
* Easy to implement.
* Reliable for simple systems.

---

# Disadvantages

* Cannot produce smooth control.
* Causes oscillation around the setpoint.
* Frequent switching can wear out valves or relays.
* Uses hysteresis/deadband to reduce switching.

---

# Process Gain (Exam Note)

### Definition

**Process Gain (K)** is the ratio of the **change in output** to the **change in input**. It tells us how sensitive the process output is to changes in the input. 

Formula:

$$
K=\frac{\Delta \text{Output}}{\Delta \text{Input}}
$$

---

### Components of Process Gain

According to the notes, Process Gain has **three components**:

1. **Sign**

   * Positive → Output increases when input increases.
   * Negative → Output decreases when input increases.

2. **Value**

   * Magnitude of sensitivity.

3. **Units**

   * Depend on the variables used. 

---

### Example (From Notes)

Pressure changes

$$
21 \rightarrow 29\ \text{psi}
$$

Valve position changes

$$
30% \rightarrow 22%
$$

$$
K=\frac{29-21}{22-30}
=\frac{8}{-8}
=-1
\ \text{psi}/(%\text{vp})
$$

Negative gain means:

> **As the input increases, the output decreases.**

---

# Process Control (Exam Summary)

The notes explain **error-based control** using a **temperature controller** in a Continuous Stirred Tank Reactor (CSTR). 

### Steps

1. Sensor measures temperature.
2. Temperature is compared with the setpoint.
3. Error is calculated.

$$
e = SP - PV
$$

4. Controller sends a signal to the heating coil.
5. Heating coil adjusts the temperature.
6. The process repeats continuously.

This is called **error-based control** because the controller's action depends on the **difference (error)** between the desired and actual values.

---

# One-Line Difference

| On-Off Controller | PID Controller              |
| ----------------- | --------------------------- |
| Only ON or OFF    | Continuously adjusts output |
| Simple            | More accurate               |
| Uses hysteresis   | Uses P, I and D actions     |

---

# 5-Mark Exam Answer

**On-Off Controller:**
An **On-Off Controller**, also known as a **Bang-Bang Controller** or **Hysteresis Controller**, is a feedback controller that switches abruptly between **ON** and **OFF** states. It is commonly used in systems with binary actuators such as thermostats and furnaces. To prevent rapid switching near the setpoint, practical systems use **hysteresis** or a **deadband**, which creates a range around the setpoint where no control action occurs. The notes also define **Process Gain** as the ratio of the change in output to the change in input, indicating the sensitivity of the process. Error-based process control compares the measured process variable with the setpoint, calculates the error, and generates a control signal to reduce that error. 

---

## Exam Tips ⭐

Remember these keywords:

* **On-Off Controller = Bang-Bang Controller**
* **Hysteresis** → Depends on present **and past** input.
* **Deadband** → Region around the setpoint where **no switching** occurs.
* **Process Gain**:

$$
K=\frac{\Delta \text{Output}}{\Delta \text{Input}}
$$

* **Error-based control**:

$$
e = SP - PV
$$

These are the points most commonly asked in short and long theory questions.
