Greedy algorithms build up a solution piece by piece, **always choosing the next piece that offers the most immediate benefit** (*locally optimal*), hoping that this leads to an **overall global optimum**.

---
### Key Characteristics

- Makes a sequence of choices.
    
- Never reconsiders earlier decisions.
    
- Fast and simple.
    
- Works best for problems with the **greedy-choice property** and **optimal substructure**.

---
### 🧩 Example 1: Tree Vertex Splitting

#### Problem Overview:

This is an **optimization problem in tree data structures**, often used in advanced scenarios such as **network design** or **tree layout optimization**.

#### Goal:

Minimize or optimize a function defined over a tree by **splitting certain vertices** and possibly reassigning subtrees. The objective might be to:

- Minimize communication cost.
    
- Balance the load across tree levels.
    
- Reduce the height or width of the tree.
    

#### Greedy Strategy:

In problems like **vertex cover on trees** or **minimizing the number of nodes used to cover all edges**, the greedy strategy can:

- Always pick the node that covers the most yet-uncovered edges.
    
- Proceed recursively on remaining subtrees.
    

##### Example Sub-problem – Minimum Vertex Cover on Tree:

A vertex cover of a tree is a set of nodes such that every edge is incident to at least one node in the set.

Greedy approximation:

- Traverse the tree from the leaves up (post-order).
    
- If a child is not in the cover, include the parent.
    

This greedy idea helps in reducing total number of nodes needed in the cover.

---

### 🧩 Example 2: Job Sequencing with Deadlines

#### Problem Overview:

Given `n` jobs with:

- A deadline `d[i]`
    
- A profit `p[i]`
    
- Each job takes **1 unit time**
    

#### Goal:

Schedule the jobs to **maximize total profit** such that:

- Each job is completed within its deadline.
    
- Only one job can be scheduled at a time.
    

#### Greedy Strategy:

1. **Sort jobs in decreasing order of profit.**
    
2. For each job, schedule it to the **latest free time slot before its deadline.**
    
3. If no such slot is available, skip the job.
    

#### Why It Works:

By scheduling higher-profit jobs first, and placing them as late as possible, it **leaves room** for smaller-profit jobs earlier, increasing the chances of completing more jobs.

##### Example:

Jobs:

|Job|Profit|Deadline|
|---|---|---|
|A|100|2|
|B|19|1|
|C|27|2|
|D|25|1|
|E|15|3|

After greedy scheduling, total profit = 142 (A, C, E) – scheduled in available slots before deadlines.

---

### ✅ Summary:

|Feature|Tree Vertex Splitting|Job Sequencing with Deadlines|
|---|---|---|
|Problem Type|Tree optimization / covering|Scheduling / Maximization|
|Goal|Optimize tree metric (cover, depth, etc.)|Maximize total profit|
|Greedy Decision|Choose node covering most edges/subtrees|Choose job with highest profit first|
|Suitable for Greedy?|In special cases (e.g., vertex cover)|Yes – classic greedy example|
|Complexity (approx)|O(n) or O(n log n) depending on problem|O(n log n) (due to sorting)|
