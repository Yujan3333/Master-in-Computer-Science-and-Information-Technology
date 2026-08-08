Assume a small universe of four web pages: A, B, C, and D. Suppose that page B had a link to pages C and A, page C had a link to page A, and page D had links to all three pages. 
![](../../../../../../../Images/Second_Sem_Images/PageRank%20Algorithm-que.png)

- [Solving Using PR damping factor](Solving%20Using%20PR%20damping%20factor.md)

---
The **PageRank algorithm** is an iterative method that assigns a numerical weight to each element (web page) in a linked set, reflecting its relative importance. The fundamental idea is that a page is more important if it receives links from other important pages.

For the small universe of four web pages (A, B, C, and D) with the specified links, the algorithm's first step is to model the link structure and calculate the initial PageRank scores.

### 1. Define the Link Structure and Initial PageRank

* **Total Pages (N):** 4 (A, B, C, D)
* **Initial PageRank ($PR_0$):** Each page starts with an equal share of the total PageRank, $1/N$.
    $$PR_0(A) = PR_0(B) = PR_0(C) = PR_0(D) = \frac{1}{4} = 0.25$$
* **Outbound Links ($L(P)$):** Count the total number of links originating from each page.
    * **B links to C and A:** $L(B) = 2$
    * **C links to A:** $L(C) = 1$
    * **D links to A, B, and C:** $L(D) = 3$
    * **A links to none:** $L(A) = 0$ (This is a *dangling node* or *sink*).

### 2. Apply the PageRank Formula (Simplified Iteration)

The PageRank of a page $P_i$ at a given iteration is the sum of the PageRanks transferred from all pages $P_j$ that link to $P_i$. The PageRank transferred is the linking page's previous PageRank divided by its total number of outbound links.

$$PR(P_i) = \sum_{P_j \in B_{P_i}} \frac{PR(P_j)}{L(P_j)}$$
where $B_{P_i}$ is the set of pages linking to $P_i$.

* **Handle Dangling Nodes (Sinks):** A page with no outbound links (like A) would effectively absorb PageRank without passing it on, causing the total PageRank to drop. In a basic model without the damping factor, a common approach is to ignore the ranks contributed by sinks or distribute their rank equally among all pages.

**For this example, let's use the simple iterative transfer for the first step, ignoring the damping factor ($d$) for clarity, but explicitly noting the sink node A:**

* **Page A receives links from B, C, and D.**
    $$PR_1(A) = \frac{PR_0(B)}{L(B)} + \frac{PR_0(C)}{L(C)} + \frac{PR_0(D)}{L(D)}$$
    $$PR_1(A) = \frac{0.25}{2} + \frac{0.25}{1} + \frac{0.25}{3}$$
    $$PR_1(A) \approx 0.125 + 0.25 + 0.0833 \approx \mathbf{0.4583}$$

* **Page B receives links from D.**
    $$PR_1(B) = \frac{PR_0(D)}{L(D)} = \frac{0.25}{3} \approx \mathbf{0.0833}$$

* **Page C receives links from B and D.**
    $$PR_1(C) = \frac{PR_0(B)}{L(B)} + \frac{PR_0(D)}{L(D)}$$
    $$PR_1(C) = \frac{0.25}{2} + \frac{0.25}{3}$$
    $$PR_1(C) \approx 0.125 + 0.0833 \approx \mathbf{0.2083}$$

* **Page D receives links from none.**
    $$PR_1(D) = \mathbf{0}$$

**Note on PageRank Sum:** The sum of $PR_1(A)+PR_1(B)+PR_1(C)+PR_1(D)$ is $0.4583 + 0.0833 + 0.2083 + 0 = 0.7499$. This is less than the initial sum of 1.0 because page A, a sink node, did not have any outbound links to pass its rank on, and we have not included the $\frac{PR_0(A)}{L(A)}$ term in the sum since $L(A)=0$.

### 3. Incorporate Damping Factor (The Complete Algorithm)

The actual PageRank algorithm uses a **damping factor** ($d$, typically set to $0.85$) to solve the sink and loop problems. It represents the probability that a random surfer will continue clicking links, while $1-d$ is the probability they will "teleport" to a random page.

The full iterative formula is:
$$PR(P_i) = \frac{1-d}{N} + d \sum_{P_j \in B_{P_i}} \frac{PR(P_j)}{L(P_j)}$$
For pages with no outbound links ($L(P_i)=0$), their PageRank is distributed to all pages through the "teleportation" part.

Using the damping factor $d=0.85$ and $N=4$:
$$\frac{1-d}{N} = \frac{1-0.85}{4} = \frac{0.15}{4} = 0.0375$$

* **Handling Sink Node A:** Since $L(A)=0$, page A's entire PageRank is distributed equally to all pages via the teleportation component in the full PageRank matrix calculation. For simplicity in this manual iterative example, we would typically treat its distribution as if it linked to all pages, but only if its PageRank is high enough to affect the ranks significantly. Assuming the rank of A is included in the teleportation to preserve the sum, the next iteration is calculated as follows:

    $$PR_{k+1}(P_i) = 0.0375 + 0.85 \times \left( \sum_{P_j \in B_{P_i}} \frac{PR_k(P_j)}{L(P_j)} \right)$$

This process of applying the formula is **repeated iteratively** (Iteration 2, Iteration 3, etc.) until the PageRank values for all pages **converge** to a stable value. The page with the highest final PageRank is considered the most important.

You can learn more about the iterative process and convergence of PageRank, including the mathematics involving eigenvectors and matrices, by watching [Page Rank Algorithm Solved Example in Machine Learning](https://www.youtube.com/watch?v=eQAeYUP2KJE). This video provides a solved example of the PageRank algorithm calculation.


[Youtube](https://www.youtube.com/watch?v=eQAeYUP2KJE)