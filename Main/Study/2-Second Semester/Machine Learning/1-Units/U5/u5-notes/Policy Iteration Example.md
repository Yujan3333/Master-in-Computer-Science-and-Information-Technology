
## **📌 Problem Setup (Grid World)**

Same **2×2 grid**:

|       | Col 1    | Col 2     |
| ----- | -------- | --------- |
| Row 1 | $s_{11}$ | +1 (Goal) |
| Row 2 | $s_{21}$ | -1 (Pit)  |

**Given**:

* Reward for non-goal states: $-0.04$
* Transition: intended success = $0.8$, slip left/right = $0.1$ each
* Discount $\gamma = 1$

---

## **🎯 Policy Iteration Steps**

Policy iteration has **two main phases** per iteration:

1. **Policy Evaluation** — compute $V^\pi(s)$ for current policy $\pi$.
2. **Policy Improvement** — update $\pi$ to be greedy w.r.t. $V^\pi$.

---

## **📘 Initial Policy (given)**

$$
\pi_0(s_{11}) = \text{Right}, \quad \pi_0(s_{21}) = \text{Right}
$$

So initially, both states try to go Right.

---

## **Step 1: Policy Evaluation for $\pi_0$**

We solve the **Bellman Expectation Equation** for $V^{\pi_0}$.

For $s_{11}$ (action = Right):

$$
V(s_{11}) = R(s_{11}) + \gamma \big[ 0.8 V(\text{Goal}) + 0.1 V(s_{11}) + 0.1 V(s_{21}) \big]
$$

$$
V(s_{11}) = -0.04 + \big[ 0.8 \times 1 + 0.1 V(s_{11}) + 0.1 V(s_{21}) \big]
$$

$$
V(s_{11}) = 0.76 + 0.1 V(s_{11}) + 0.1 V(s_{21}) \quad (1)
$$

For $s_{21}$ (action = Right):

$$
V(s_{21}) = R(s_{21}) + \gamma \big[ 0.8 V(\text{Pit}) + 0.1 V(s_{11}) + 0.1 V(s_{21}) \big]
$$

$$
V(s_{21}) = -0.04 + \big[ 0.8 \times (-1) + 0.1 V(s_{11}) + 0.1 V(s_{21}) \big]
$$

$$
V(s_{21}) = -0.84 + 0.1 V(s_{11}) + 0.1 V(s_{21}) \quad (2)
$$

---

### **Solve the system of equations**

From (1):

$$
V(s_{11}) - 0.1 V(s_{11}) - 0.1 V(s_{21}) = 0.76
$$

$$
0.9 V(s_{11}) - 0.1 V(s_{21}) = 0.76 \quad (1')
$$

From (2):

$$
V(s_{21}) - 0.1 V(s_{11}) - 0.1 V(s_{21}) = -0.84
$$

$$
-0.1 V(s_{11}) + 0.9 V(s_{21}) = -0.84 \quad (2')
$$

---

**Solving**:

From (1'):
$$
0.9 V_{11} - 0.1 V_{21} = 0.76
;\Rightarrow;
9 V_{11} - V_{21} = 7.6 \quad (A)
$$

From (2'):
$$
-0.1 V_{11} + 0.9 V_{21} = -0.84
;\Rightarrow;

* V_{11} + 9 V_{21} = -8.4 \quad (B)
  $$

From (A):
$$
V_{21} = 9 V_{11} - 7.6
$$

Substitute into (B):

$$

* V_{11} + 9(9 V_{11} - 7.6) = -8.4
  $$

$$

* V_{11} + 81 V_{11} - 68.4 = -8.4
  $$

$$
80 V_{11} = 60
$$

$$
V_{11} = 0.75
$$

Then:

$$
V_{21} = 9 \times 0.75 - 7.6 = 6.75 - 7.6 = -0.85
$$

✅ **Evaluated policy values**:

$$
V^{\pi_0}(s_{11}) = 0.75, \quad V^{\pi_0}(s_{21}) = -0.85
$$

---

## **Step 2: Policy Improvement**

Update policy to be **greedy** with respect to $V^{\pi_0}$.

---

### **For $s_{11}$**

Using $V(s_{11}) = 0.75$, $V(s_{21}) = -0.85$:

1. **Right → Goal**
   $$
   0.8 \times 1 + 0.1 \times 0.75 + 0.1 \times (-0.85)
   = 0.8 + 0.075 - 0.085 = 0.79
   $$

2. **Left → stay $s_{11}$**
   $$
   0.8 \times 0.75 + 0.1 \times 0.75 + 0.1 \times (-0.85)
   = 0.6 + 0.075 - 0.085 = 0.59
   $$

3. **Up → stay $s_{11}$ + slip right to Goal**
   $$
   0.8 \times 0.75 + 0.1 \times 0.75 + 0.1 \times 1
   = 0.6 + 0.075 + 0.1 = 0.775
   $$

4. **Down → $s_{21}$ + slip left to Goal**
   $$
   0.8 \times (-0.85) + 0.1 \times 1 + 0.1 \times 0.75
   = -0.68 + 0.1 + 0.075 = -0.505
   $$

**Max** $= 0.79$ (Right)

$$
\pi_{\text{new}}(s_{11}) = \text{Right}
$$

---

### **For $s_{21}$**

1. **Right → Pit**
   $$
   0.8 \times (-1) + 0.1 \times 0.75 + 0.1 \times (-0.85)
   = -0.8 + 0.075 - 0.085 = -0.81
   $$

2. **Left → stay $s_{21}$**
   $$
   0.8 \times (-0.85) + 0.1 \times (-0.85) + 0.1 \times 0.75
   = -0.68 - 0.085 + 0.075 = -0.69
   $$

3. **Up → $s_{11}$ + slip right to Pit**
   $$
   0.8 \times 0.75 + 0.1 \times (-0.85) + 0.1 \times (-1)
   = 0.6 - 0.085 - 0.1 = 0.415
   $$

4. **Down → stay $s_{21}$ + slip left to Pit**
   $$
   0.8 \times (-0.85) + 0.1 \times (-1) + 0.1 \times (-0.85)
   = -0.68 - 0.1 - 0.085 = -0.865
   $$

**Max** $= 0.415$ (Up)

$$
\pi_{\text{new}}(s_{21}) = \text{Up}
$$

---

## **🔄 New Policy after 1st Improvement**

$$
\pi_1(s_{11}) = \text{Right}, \quad \pi_1(s_{21}) = \text{Up}
$$

---

## **Repeat Policy Evaluation for $\pi_1$**

For $s_{11}$ (Right):

$$
V(s_{11}) = -0.04 + [0.8 \times 1 + 0.1 V(s_{11}) + 0.1 V(s_{21})] \quad (1)
$$

For $s_{21}$ (Up):

$$
V(s_{21}) = -0.04 + [0.8 V(s_{11}) + 0.1 V(s_{21}) + 0.1 \times (-1)]
$$

$$
V(s_{21}) = -0.14 + 0.8 V(s_{11}) + 0.1 V(s_{21}) \quad (2)
$$

---

### **Solve**

From (1):

$$
0.9 V_{11} - 0.1 V_{21} = 0.76 \quad (A)
$$

From (2):

$$
-0.8 V_{11} + 0.9 V_{21} = -0.14 \quad (B')
$$

From (A):

$$
V_{21} = 9 V_{11} - 7.6
$$

Substitute:

$$
-0.8 V_{11} + 0.9(9 V_{11} - 7.6) = -0.14
$$

$$
-0.8 V_{11} + 8.1 V_{11} - 6.84 = -0.14
$$

$$
7.3 V_{11} = 6.7
$$

$$
V_{11} \approx 0.9178
$$

$$
V_{21} = 9 \times 0.9178 - 7.6 = 8.2602 - 7.6 = 0.6602
$$

---

## **🔄 Policy Improvement again**

For $s_{11}$, Right still best.
For $s_{21}$, Up still best.

Policy unchanged → **converged**.

---

## **🏁 Final Optimal Policy**

$$
\pi^*(s_{11}) = \text{Right}, \quad \pi^*(s_{21}) = \text{Up}
$$

Values:

$$
V^*(s_{11}) \approx 0.918, \qquad V^*(s_{21}) \approx 0.660
$$

---

## **📘 Summary**

Policy iteration:

1. Started with a guess policy (Right everywhere).
2. Evaluated it → got values.
3. Improved policy greedily → $s_{21}$ switched to Up.
4. Re-evaluated → values improved.
5. Improved again → policy unchanged → done.

✅ Found optimal policy in **2 iterations**.

