
# **ROCK Algorithm – Complete Numerical Example**
   
   ---
   
## **Given**
   
   Documents:
   
   $D_1 = {\text{judgment, faith, prayer, fair}}$
   $D_2 = {\text{fasting, faith, prayer}}$
   $D_3 = {\text{fair, fasting, faith}}$
   $D_4 = {\text{fasting, prayer, pilgrimage}}$
   
   Similarity threshold:
   $$[
   \theta = 0.3
   ]$$
   
   Number of clusters required:
   $$[
   k = 2
   ]$$
   
   Similarity measure (Jaccard Coefficient):
   $$[
   Sim(A,B) = \frac{|A \cap B|}{|A \cup B|}
   ]$$
   
   ---
   
## **Step 1: Compute Pairwise Similarities**
   
### $Sim(D_1, D_2)$
   
   $$[
   |D_1 \cap D_2| = 2,\quad |D_1 \cup D_2| = 5
   ]$$
   $$[
   Sim(D_1, D_2) = \frac{2}{5} = 0.4 \ge 0.3
   ]$$
   
   ---
   
### $Sim(D_1, D_3)$
   
   $$[
   |D_1 \cap D_3| = 2,\quad |D_1 \cup D_3| = 5
   ]$$
   $$[
   Sim(D_1, D_3) = \frac{2}{5} = 0.4 \ge 0.3
   ]$$
   
   ---
   
### $Sim(D_1, D_4)$ ❌
   
   $$[
   |D_1 \cap D_4| = 1,\quad |D_1 \cup D_4| = 6
   ]$$
   $$[
   Sim(D_1, D_4) = \frac{1}{6} \approx 0.17 < 0.3
   ]$$
   
   ---
   
### $Sim(D_2, D_3)$
   
   $$[
   |D_2 \cap D_3| = 2,\quad |D_2 \cup D_3| = 4
   ]$$
   $$[
   Sim(D_2, D_3) = \frac{2}{4} = 0.5 \ge 0.3
   ]$$
   
   ---
   
### $Sim(D_2, D_4)$
   
   $$[
   |D_2 \cap D_4| = 2,\quad |D_2 \cup D_4| = 4
   ]$$
   $$[
   Sim(D_2, D_4) = \frac{2}{4} = 0.5 \ge 0.3
   ]$$
   
   ---
   
### $Sim(D_3, D_4)$ ❌
   
   $$[
   |D_3 \cap D_4| = 1,\quad |D_3 \cup D_4| = 5
   ]$$
   $$[
   Sim(D_3, D_4) = \frac{1}{5} = 0.2 < 0.3
   ]$$
   
   ---
   
   ## **Step 2: Determine Neighbors**
   
   Two documents are neighbors if $Sim \ge \theta$.
   
| Document | Neighbors       |
| -------- | --------------- |
| $D_1$    | $D_2, D_3$      |
| $D_2$    | $D_1, D_3, D_4$ |
| $D_3$    | $D_1, D_2$      |
| $D_4$    | $D_2$           |

   ---
   
   ## **Step 3: Compute Links**
   
   $$[
   link(A,B) = |N(A) \cap N(B)|
   ]$$
   
| Pair        | Common Neighbors | Links |
| ----------- | ---------------- | ----- |
| $(D_1,D_2)$ | ${D_3}$          | 1     |
| $(D_1,D_3)$ | ${D_2}$          | 1     |
| $(D_2,D_3)$ | ${D_1}$          | 1     |
| $(D_2,D_4)$ | $\emptyset$      | 0     |
   
   ---
   
   ## **Step 4: Initialize Clusters**
   
   $$[
   {D_1}, {D_2}, {D_3}, {D_4}
   ]$$
   
   ---
   
   ## **Step 5: Compute Goodness Measure**
   
   ### **Goodness Formula**
   
   $$[
   g(C_i,C_j) =
   \frac{links(C_i,C_j)}
   {(n_i+n_j)^{1+2f(\theta)} - n_i^{1+2f(\theta)} - n_j^{1+2f(\theta)}}
   ]$$
   
   $$[
   f(\theta) = \frac{1-\theta}{1+\theta}
   ]$$
   
   ---
   
   ### **Calculate $f(\theta)$**
   
   $$[
   f(0.3) = \frac{0.7}{1.3} \approx 0.538
   ]$$
   
   $$[
   1+2f(\theta) = 2.076
   ]$$
   
   ---
   
   ### **Goodness for First Merge**
   
   All clusters are size 1.
   
   Example $(D_1,D_2)$:
   
   $$[
   g(D_1,D_2) =
   \frac{1}{2^{2.076} - 1 - 1}
   ]$$
   
   $$[
   2^{2.076} \approx 4.22
   ]$$
   
   $$[
   g(D_1,D_2) = \frac{1}{2.22} \approx 0.45
   ]$$
   
   (Same value for $(D_1,D_3)$ and $(D_2,D_3)$)
   
   ---
   
   ## **Step 6: First Merge**
   
   Choose any pair with maximum goodness:
   
   $$[
   C_1 = {D_1,D_2}
   ]$$
   
   Clusters now:
   $$[
   {D_1,D_2},\ {D_3},\ {D_4}
   ]$$
   
   ---
   
   ## **Step 7: Second Goodness Calculation**
   
   $$[
   links(C_1,D_3) = link(D_1,D_3) + link(D_2,D_3) = 1+1 = 2
   ]$$
   
   $$[
   g(C_1,D_3) =
   \frac{2}
   {3^{2.076} - 2^{2.076} - 1}
   ]$$
   
   $$[
   3^{2.076} \approx 9.72,\quad 2^{2.076} \approx 4.22
   ]$$
   
   $$[
   g(C_1,D_3) = \frac{2}{4.50} \approx 0.44
   ]$$
   
   $$[
   g(C_1,D_4) = 0
   ]$$
   
   ---
   
   ## **Step 8: Second Merge**
   
   $$[
   C_1 = {D_1,D_2,D_3}
   ]$$
   
   ---
   
   ## **Step 9: Stop Condition**
   
   Number of clusters = 2 → STOP.
   
   ---
   
   ## **Final Clusters**
   
   $$[
   \boxed{C_1 = {D_1,D_2,D_3}}
   ]$$
   
   $$[
   \boxed{C_2 = {D_4}}
   ]$$
   
   ---
   
   ## **Final Exam Conclusion**
   
   > Using ROCK with similarity threshold 0.3, documents $D_1$, $D_2$, and $D_3$ are clustered together due to high link-based goodness, while $D_4$ forms a separate cluster.
   
   ---
   

   