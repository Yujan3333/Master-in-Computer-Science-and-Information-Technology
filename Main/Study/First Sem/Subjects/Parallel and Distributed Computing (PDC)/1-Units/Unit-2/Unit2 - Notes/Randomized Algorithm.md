[Randomized Algorithm - Monte Carlo and Las Vegas](../../../../Algorithm%20and%20Complexity%20(AC)/1-Units/Unit%201/Unit1-Notes-Folder/Randomized%20Algorithm%20-%20Monte%20Carlo%20and%20Las%20Vegas.md)



---

## ✅ Randomized Algorithms — Quick Refresher

> Algorithms that use **random choices** during execution, often to improve **speed**, **simplicity**, or **practicality**, at the cost of **probabilistic correctness** or **variable run-time**.

---

## 📘 Fermat's Primality Test (Monte Carlo)

### 🔹 Fermat’s Little Theorem:

If $p$ is a **prime** and $b$ is not divisible by $p$, then:

$$
b^{p-1} \equiv 1 \pmod{p}
$$

In other words, for a **prime** $p$, most values of $b \in \mathbb{Z}_p$ (i.e., $1 < b < p$) satisfy:

$$
b^{p-1} \mod p = 1
$$

---

### 🧪 Fermat Test Steps:

1. Input a number $p$ to test for primality.
2. Randomly choose $b \in \{2, 3, ..., p-2\}$
3. Compute $b^{p-1} \mod p$
4. If result $\neq 1$, then:

   * $p$ is **definitely composite**
5. If result = 1, then:

   * $p$ **might be prime**
   * But could be a **pseudoprime** for base $b$

Repeat with multiple random bases $b$ to increase confidence.

---

## ⚠️ Weakness of Fermat's Test:

Some composite numbers (called **Carmichael numbers**) pass the Fermat test for **all** $b$ co-prime to them:

* Example: 561, 1105, etc.

So Fermat test alone is **not sufficient** for guaranteed correctness.

---

## 🧠 Why It’s Monte Carlo:

* Always **fast** (runs in $O(\log p)$ time using modular exponentiation)
* **Might be wrong** (declaring a composite number as probably prime)
* Error probability decreases with **more random trials**

---

## 🧮 Types of Randomized Algorithms:

| Type            | Behavior                                   | Example                                               |
| --------------- | ------------------------------------------ | ----------------------------------------------------- |
| **Monte Carlo** | Always fast, answer **may be incorrect**   | Fermat’s primality test                               |
| **Las Vegas**   | Always correct, **running time is random** | Randomized Quicksort (output is correct; time varies) |

---

## ✅ Summary for Exam:

* Fermat test uses randomness to **choose bases $b$**.
* It’s a **Monte Carlo algorithm** — fast, but small chance of error.
* Multiple trials increase confidence.
* Useful in **cryptography** where fast primality checks are needed (e.g., RSA key generation).

---

Let me know if you want:

* Miller-Rabin (a stronger version of Fermat test) [Primality Testing](../../../../Algorithm%20and%20Complexity%20(AC)/1-Units/Unit%201/Unit1-Notes-Folder/Primality%20Testing.md)
* Python code for Fermat’s test
* Examples of Las Vegas algorithms
