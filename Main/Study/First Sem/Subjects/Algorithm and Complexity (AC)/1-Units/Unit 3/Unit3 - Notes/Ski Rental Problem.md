## 🏂 **Ski Rental Problem (Online Algorithm Example)**

---

### ✅ **Problem Statement:**

You have two options for skiing:

- **Rent skis** for **Rs. 1 per day**
    
- **Buy skis** for a one-time cost of **Rs. b** (e.g., Rs. 10)
    

But here’s the challenge:  
You **don’t know how many days** you will ski in total!

---

### ✅ **Goal:**

Minimize the total cost of skiing **without knowing the future** (i.e., how long you’ll ski).

---

### ✅ **Strategy (Online Algorithm):**

- **Rent skis every day until total rent = buy cost**
    
- Then **buy skis**
    

So:

- Rent for `b` days (Rs. 1 per day → Rs. b total)
    
- On day `b + 1`, **buy** the skis
    

---

### ✅ **Cost Comparison:**

|Scenario|Online Cost|Offline Optimal Cost|Competitive Ratio|
|---|---|---|---|
|You ski only 2 days|Rent = Rs. 2|Rent = Rs. 2|1.0|
|You ski for 10 days|Rent 10 days = Rs. 10|Buy = Rs. 10|1.0|
|You ski for 20 days|Rent 10 days + Buy = Rs. 20|Buy = Rs. 10|2.0|

> So the **worst case** cost is **2× optimal** → Competitive Ratio = **2**

---

### 🟩 **Why is this an Online Algorithm?**

- You make a decision **each day** without knowing whether you’ll ski tomorrow.
    
- Once you buy skis, you can’t go back.
    

---

### 📝 **Summary (for exam):**

> The **Ski Rental Problem** is a classic **online decision-making** problem where you must choose between **renting skis daily** or **buying them outright** without knowing how long you’ll ski.  
> The standard **online strategy** is to rent until total rent equals the buy cost, then buy.  
> This gives a **competitive ratio of 2**, meaning the cost is at most **twice** the optimal offline cost.