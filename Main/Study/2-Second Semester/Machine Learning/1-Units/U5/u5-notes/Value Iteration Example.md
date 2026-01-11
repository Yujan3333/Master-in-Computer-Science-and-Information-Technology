![](../../../../../../../Images/Second_Sem_Images/Value%20Iteration%20Example.png)

---
## Answer
Think of value iteration as *“try every action, see where it can take you, average the future values using probabilities, then choose the best.”*
Let us walk slowly using your numbers.

We only update **non-terminal states**:
$(s_{11})$ and $(s_{21})$

Terminal:
$$
V(\text{Goal})=+1,\qquad V(\text{Pit})=-1
$$

Reward for any move from non-terminal:
$$
R = -0.04,\quad \gamma = 1
$$

Formula:
$$
V_{k+1}(s)= -0.04 + \max_a \sum_{s'} P(s'|s,a)V_k(s')
$$

---

### Iteration 0 (Initialization)

$$
V_0(s_{11})=0,\qquad V_0(s_{21})=0
$$

---

## Iteration 1

### For $(s_{11})$

Try all actions:

1. **Right → Goal**
   $$
   0.8(1)+0.1(0)+0.1(0)=0.8
   $$

2. **Up → wall**
   $$
   0.8(0)+0.1(1)+0.1(0)=0.1
   $$

3. **Left → wall**
   $$
   0
   $$

4. **Down → $s_{21}$**
   $$
   0
   $$

Best = $(0.8)$

$$
V_1(s_{11})=-0.04+0.8=0.76
$$

---

### For $(s_{21})$

1. **Right → Pit**
   $$
   0.8(-1)+0.1(0)+0.1(0)=-0.8
   $$

2. **Up → $s_{11}$**
   $$
   0.8(0)+0.1(0)+0.1(-1)=-0.1
   $$

3. **Left / Down → wall**
   $$
   0
   $$

Best = $(0)$

$$
V_1(s_{21})=-0.04+0= -0.04
$$

So after iteration 1:
$$
V_1(s_{11})=0.76,\qquad V_1(s_{21})=-0.04
$$

---

## Iteration 2

Now use updated values.

### For $(s_{11})$

Right:
$$
0.8(1)+0.1(0.76)+0.1(-0.04)
$$
$$
=0.8+0.076-0.004=0.872
$$

$$
V_2(s_{11})=-0.04+0.872=0.832
$$

Other actions give smaller values, so Right is still best.

---

### For $(s_{21})$

Try **Up**:
$$
0.8(0.76)+0.1(-0.04)+0.1(-1)
$$
$$
=0.608-0.004-0.1=0.504
$$

Try **Left / Down**:
$$
0
$$

Try **Right**:
$$
-0.8
$$

Best = $(0.504)$

$$
V_2(s_{21})=-0.04+0.504=0.464
$$

Now:
$$
V_2(s_{11})=0.832,\qquad V_2(s_{21})=0.464
$$

---

## What is happening intuitively?

* $(s_{11})$ is close to the **Goal**, so its value grows quickly.
* $(s_{21})$ is close to the **Pit**, so initially it is bad.
* But once $(s_{11})$ becomes valuable, going **Up** from $(s_{21})$ becomes smart.
* That’s why $(s_{21})$ becomes positive later.

The agent learns:

> “Avoid Pit → go Up → then Right → reach Goal.”

---

## Final Optimal Policy

After convergence:

| State      | Best Action     |
| ---------- | --------------- |
| $(s_{11})$ | Right → Goal    |
| $(s_{21})$ | Up → $(s_{11})$ |

---

## Exam-friendly intuition line:

> “Value iteration propagates rewards backward from terminal states.
> States near the goal get high values first, then neighboring states become valuable as safer paths are discovered.”

That’s the heart of this numerical example.
