![](../../../../../../../../Images/First_Sem_Images/Answer%20-%20🐸%20Frog%20Jump%20Problem.png)

### 🐸 **Problem: Frog Jump**

Imagine a frog sitting on the first stone (index 1) of a path. There's a series of stones ahead, and each stone tells how far the frog can jump from there.

You are given an array like:

```
A = [2, 3, 1, 1, 4]
```

* At stone 1 (value 2), frog can jump to **next 1 or 2 stones** (i.e., to index 2 or 3).
* At stone 2 (value 3), frog can jump to next **1, 2, or 3 stones** (i.e., index 3, 4, or 5).
* At stone 3 (value 1), frog can jump to next **only 1 stone** (i.e., index 4).
* ...
* The frog wants to reach the **last stone** using the **fewest jumps**.

---

### 💡 What We Want to Find

We want to know:
**What is the minimum number of jumps needed** to go from stone 1 to the last stone?

---

### 🧠 Dynamic Programming (DP) Idea

Let’s use a list called `dp[]` to keep track of the **minimum jumps needed to reach each stone**.

* `dp[i]` = Minimum jumps required to reach stone `i` from stone 1.

---

### 🧱 Step-by-Step Construction of dp\[]

**Initialize:**

* We know we start at stone 1, so:

  ```
  dp[1] = 0  → we need 0 jumps to stay on the first stone
  ```

* We don’t know how to reach other stones yet, so we start them with infinity (a very large number):

  ```
  dp[2] = ∞
  dp[3] = ∞
  ...
  ```

---

### 🔁 Filling dp\[i] using Previous dp\[k]

For every stone `i` from 2 to n:

* We look back at **each previous stone k = 1 to i-1** and check:

  > Can frog jump from `k` to `i`?

That is true if:

```
i - k <= A[k]   → current stone is within jump range of stone k
```

If so, we update:

```
dp[i] = min(dp[i], dp[k] + 1)
```

That means:

> To reach stone `i`, we may take the best route through some previous stone `k`.

---

### ✅ Example: A = \[2, 3, 1, 1, 4]

We’ll calculate `dp[1]` to `dp[5]` step-by-step:

#### Initial:

```
dp[1] = 0
dp[2] = ∞
dp[3] = ∞
dp[4] = ∞
dp[5] = ∞
```

---

#### i = 2:

Check from stone 1:

* Can frog jump from 1 → 2? YES, because 2 - 1 = 1 ≤ A\[1] = 2
* So: `dp[2] = min(∞, dp[1] + 1) = 1`

---

#### i = 3:

Check:

* From 1 → 3: 3 - 1 = 2 ≤ A\[1] = 2 → YES → dp\[3] = min(∞, dp\[1]+1) = 1
* From 2 → 3: 3 - 2 = 1 ≤ A\[2] = 3 → YES → dp\[3] = min(1, dp\[2]+1) = 1 (no change)

---

#### i = 4:

Check:

* From 2 → 4: 4 - 2 = 2 ≤ A\[2] = 3 → YES → dp\[4] = min(∞, dp\[2]+1) = 2
* From 3 → 4: 4 - 3 = 1 ≤ A\[3] = 1 → YES → dp\[4] = min(2, dp\[3]+1) = 2

---

#### i = 5:

Check:

* From 2 → 5: 5 - 2 = 3 ≤ A\[2] = 3 → YES → dp\[5] = min(∞, dp\[2]+1) = 2
* From 3 → 5: 5 - 3 = 2 > A\[3] = 1 → NO
* From 4 → 5: 5 - 4 = 1 ≤ A\[4] = 1 → YES → dp\[5] = min(2, dp\[4]+1) = 2

---

### Final dp Table:

| i (stone) | 1 | 2 | 3 | 4 | 5 |
| --------- | - | - | - | - | - |
| dp\[i]    | 0 | 1 | 1 | 2 | 2 |

So the **minimum number of jumps = dp\[5] = 2**

---

### 📦 Final Notes:

* This DP method checks **all previous positions** to see where we can jump from.
* Each position may take up to `O(n)` checks → so total time = `O(n^2)`
* It guarantees the correct minimum number of jumps.

---

### 📌 Key Formula to Memorize

$$
dp[i] = \min_{\substack{1 \leq k < i \\ i - k \leq a_k}} \left( dp[k] + 1 \right)
$$

