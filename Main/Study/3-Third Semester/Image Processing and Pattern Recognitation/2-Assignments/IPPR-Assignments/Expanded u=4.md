
# 🔹 For $u=4$ (FULL EXPANSION LIKE $u=3$)

## ✅ Step 1: Formula

$$F(4)=\sum_{x=0}^{7} f(x)e^{-j2\pi(4)x/8}$$

---

## ✅ Step 2: Expand Summation

$$F(4)=f(0)e^{-j2\pi(4)(0)/8}+f(1)e^{-j2\pi(4)(1)/8}+f(2)e^{-j2\pi(4)(2)/8}+f(3)e^{-j2\pi(4)(3)/8}+f(4)e^{-j2\pi(4)(4)/8}+f(5)e^{-j2\pi(4)(5)/8}+f(6)e^{-j2\pi(4)(6)/8}+f(7)e^{-j2\pi(4)(7)/8}$$

---

## ✅ Step 3: Substitute $f(x)$

$$=3e^{-j0}+2e^{-j2\pi(4)/8}+3e^{-j2\pi(8)/8}+1e^{-j2\pi(12)/8}+4e^{-j2\pi(16)/8}+5e^{-j2\pi(20)/8}+0e^{-j2\pi(24)/8}+2e^{-j2\pi(28)/8}$$

---

## ✅ Step 4: Simplify Exponents

$$=3e^{-j0}+2e^{-j\pi}+3e^{-j2\pi}+1e^{-j3\pi}+4e^{-j4\pi}+5e^{-j5\pi}+0e^{-j6\pi}+2e^{-j7\pi}$$

---

## ✅ Step 5: Convert to Values

Using:

* $$e^{-j0}=1$$
* $$e^{-j\pi}=-1$$
* $$e^{-j2\pi}=1$$
* $$e^{-j3\pi}=-1$$
* $$e^{-j4\pi}=1$$
* $$e^{-j5\pi}=-1$$
* $$e^{-j6\pi}=1$$
* $$e^{-j7\pi}=-1$$

---

## ✅ Step 6: Substitute Numerical Values

$$F(4)=3(1)+2(-1)+3(1)+1(-1)+4(1)+5(-1)+0(1)+2(-1)$$

---

## ✅ Step 7: Solve

$$=3-2+3-1+4-5+0-2$$

$$=0$$

---

## ✅ Final Answer

$$F(4)=0$$

---

# 🔹 Why NO need to calculate $u=5,6,7$?

## ✅ Property (VERY IMPORTANT)

If $f(x)$ is **real**, then:

$$F(N-u)=\overline{F(u)}$$

---

## ✅ Meaning

* Second half of DFT = **mirror of first half**
* Only imaginary sign changes

---

## ✅ Apply here ($N=8$)

| Already found | Use for |
| ------------- | ------- |
| $F(1)$        | $F(7)$  |
| $F(2)$        | $F(6)$  |
| $F(3)$        | $F(5)$  |

---

## ✅ Example

$$F(3)=0.414+j5.828$$

So:

$$F(5)=0.414-j5.828$$

---

# 🔹 WHY this works (intuition)

Because complex exponentials are symmetric:

$$e^{-j\theta} \text{ and } e^{j\theta}$$

👉 They are conjugates
👉 So results repeat in reverse

---

# 🔹 IMPORTANT EXAM RULE

## ✅ When you CAN skip (like this question)

✔ Input is **real-valued**
✔ DFT question
✔ No special instruction

👉 Then:

* Solve only **half (0 to N/2)**
* Use conjugate for rest

---

## ❌ When you CANNOT skip

You must calculate all values if:

* Input is **complex**
* Question says **“compute all values directly”**
* No symmetry (rare but possible)

---

# 🔹 What to do in similar questions?

👉 YES — do exactly same method:

### Step pattern:

1. Write formula
2. Expand summation
3. Substitute values
4. Convert exponentials
5. Solve
6. Use symmetry (if real signal)

---

# ✅ Final Exam Strategy (VERY IMPORTANT)

👉 Always write:

* Full steps for **at least one or two values**
* Then write:

“Remaining values obtained using conjugate property”

---

# ✅ One-line Viva Answer

“For real signals, DFT outputs are symmetric, so higher frequency terms are complex conjugates of lower ones.”

---
