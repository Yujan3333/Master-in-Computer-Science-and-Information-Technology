# 📘 **Unit 5: Reinforcement Learning – SUMMARY**

---

## ✅ **MOST IMPORTANT TOPICS FOR EXAM:**

### 1. **Reinforcement Learning Basics**
- **Agent** – learner/decision maker
- **Environment** – world agent interacts with
- **State (S)** – current situation
- **Action (A)** – what agent does
- **Reward (R)** – feedback from environment
- **Goal**: Maximize **cumulative reward**

---

### 2. **Markov Decision Process (MDP)**
- Defined by: **(S, A, P, R, γ)**
  - **S** = States
  - **A** = Actions
  - **P** = Transition probability  
    $$[ P(s'|s,a) = \text{Prob(next state is } s' \text{ given } s, a) ]$$
  - **R** = Reward function
  - **γ** = Discount factor (0 to 1)

---

### 3. **Key Formulas**

**Returns (Total discounted reward):**
$$[
G_t = R_{t+1} + γ R_{t+2} + γ^2 R_{t+3} + \dots
]$$

**Value Function (State-Value):**
$$[
V_\pi(s) = \mathbb{E}_\pi[G_t | S_t = s]
]$$
= Expected return starting from state \(s\) following policy \(\pi\)

**Action-Value Function (Q-Function):**
$$[
Q_\pi(s,a) = \mathbb{E}_\pi[G_t | S_t = s, A_t = a]
]$$
= Expected return from taking action \(a\) in state \(s\), then following \(\pi\)

---

### 4. **Bellman Equations – MUST KNOW!**

**Bellman Expectation Equation (for V):**
$$[
V_\pi(s) = \sum_a \pi(a|s) \sum_{s'} P(s'|s,a) [R(s,a,s') + γ V_\pi(s')]
]$$

**Bellman Optimality Equation (for Q*):**
$$[
Q_*(s,a) = \sum_{s'} P(s'|s,a) [R(s,a,s') + γ \max_{a'} Q_*(s',a')]
]$$

---

### 5. **Optimal Policy & Value**
- **Optimal Value Function**:  
$$[ V_*(s) = \max_\pi V_\pi(s) \\]$$
- **Optimal Policy**:  
  Choose action with highest Q-value:
  $$[
  \pi_*(a|s) = 
  \begin{cases} 
  1 & \text{if } a = \arg\max_a Q_*(s,a) \\
  0 & \text{otherwise}
  \end{cases}
  ]$$

---

### 6. **Solving MDPs – Two Main Algorithms**

**Value Iteration:**
1. Start with random \(V(s)\)
2. Update:  
  $$ [
   V_{k+1}(s) = \max_a \sum_{s'} P(s'|s,a) [R + γ V_k(s')]
   ]$$
3. Stop when values converge

**Policy Iteration:**
1. Start with random policy \(\pi\)
2. **Policy Evaluation**: Solve \(V_\pi(s)\) (Bellman expectation)
3. **Policy Improvement**: Update policy greedily:  
   $$[
   \pi'(s) = \arg\max_a Q_\pi(s,a)
   ]$$
4. Repeat until policy doesn’t change

---

### 7. **Example Problem (Grid World) – KNOW THIS!**
Given:
- States: grid cells
- Rewards: +1 (goal), -1 (bad), -0.04 (step cost)
- Transition probabilities (e.g., 0.8 intended, 0.1 left/right)
- γ = 1 or 0.9

**Calculate V(s)** using value iteration formula.

Example from slides (Page 46):
$$[
V(s_{11}) = -0.04 + \max[\ 0.8×(+1) + 0.1×0 + 0.1×0, \dots\ ]
]$$

---

## 🚨 **EXAM FOCUS AREAS:**
1. **Define MDP components**
2. **Write Bellman equations**
3. **Compute V(s) or Q(s,a)** given P, R, γ
4. **Difference between value iteration & policy iteration**
5. **Find optimal policy** from Q-values
6. **Interpret discount factor γ**

---

## 📝 **Quick Memory Tricks:**
- **γ = 0** → only care about immediate reward
- **γ = 1** → care equally about future (may diverge)
- **Value Iteration** → update values directly
- **Policy Iteration** → alternate between evaluating policy & improving it
- **Q-Learning** = model-free version (not in slides but good to know)

---

**You can master Unit 5 in 2–3 hours.**  
Focus on **Bellman equations** and **grid world example** — they’re almost guaranteed to be on the exam.

