Karger’s Algorithm is a **randomized algorithm** used to find the **minimum cut** in an **undirected**, **connected graph**. It’s a beautifully simple yet powerful algorithm that works by **contracting edges randomly**.

---

## ✂️ What is a Minimum Cut?

A **cut** in a graph is a way to divide the graph's vertices into two **disjoint** sets such that **at least one edge** goes from one set to the other.

- The **minimum cut** is the cut with the **fewest number of crossing edges**.
    
- Goal: **Find the smallest number of edges whose removal disconnects the graph.**
    

---

## 🧠 Idea Behind Karger’s Algorithm

> Randomly **merge vertices** (contract edges) until only two vertices remain.  
> The edges **between these two supernodes** form a **cut**.

---

### 🧮 Step-by-Step Algorithm

1. **Input:** An undirected, connected graph G=(V,E)G = (V, E)G=(V,E)
    
2. While there are more than 2 vertices in the graph:
    
    - Pick an edge (u,v)(u, v)(u,v) **uniformly at random** from the edge set EEE.
        
    - **Contract** the edge (u,v)(u, v)(u,v):
        
        - Merge vertices uuu and vvv into a single vertex.
            
        - Remove all self-loops (edges that go from the merged node back to itself).
            
3. After all contractions, only two "supernodes" are left.
    
4. The **remaining edges between the two supernodes** represent one **possible cut**.
    
5. Return the number of these edges as the size of the cut.
    

---

### 🔁 Why Repeat?

Because the algorithm is **randomized**, it might not always give the **minimum** cut.  
To improve accuracy:

- Run the algorithm multiple times (say n2log⁡nn^2 \log nn2logn times).
    
- Keep track of the **smallest cut size** found.
    

> The **probability** of finding the correct minimum cut in one run is at least 2n(n−1)\frac{2}{n(n-1)}n(n−1)2​.

---

### ⏱️ Time Complexity

- One run of Karger’s Algorithm takes **O(n2)O(n^2)O(n2)** time.
    
- Repeating it O(n2log⁡n)O(n^2 \log n)O(n2logn) times gives high probability of success.
    
- So, total time is O(n4log⁡n)O(n^4 \log n)O(n4logn), but improved versions exist with O(n2log⁡3n)O(n^2 \log^3 n)O(n2log3n).
    

---

### 🧑‍🏫 Example

Let's say we have a graph:

less

CopyEdit

`A --- B | \   | |  \  | C --- D`

Run Karger's:

- Randomly pick an edge, say (A, B), and contract → merge A and B into one node.
    
- Remove self-loops.
    
- Repeat until two nodes remain.
    
- Count remaining edges between the two nodes — that’s a cut.
    

If you run it enough times, you will likely get the minimum cut (e.g., 2 edges in this case).

---

### ✅ Key Points for Exam

| Feature             | Description                                     |
| ------------------- | ----------------------------------------------- |
| **Problem Solved**  | Minimum cut in an undirected graph              |
| **Technique**       | Random edge contraction                         |
| **Probabilistic?**  | Yes, gives correct answer with high probability |
| **Time Complexity** | O(n2)O(n^2)O(n2) per run                        |
| **How to Improve**  | Repeat O(n2log⁡n)O(n^2 \log n)O(n2logn) times   |
| **Important Use**   | Fast approximation when deterministic is slow   |