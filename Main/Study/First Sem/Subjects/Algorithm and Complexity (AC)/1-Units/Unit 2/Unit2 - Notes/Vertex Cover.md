
### ✅ **Definition:**

In a graph, a **vertex cover** is a **subset of vertices** such that **every edge in the graph has at least one of its endpoints in this subset**.

- That means: for every edge (u,v)∈E, either u, v, or **both** are in the vertex cover set.


![](../../../../../../../../Attachments/Vertex%20Cover.png)

A vertex cover of a graph G=(V,E) is a subset of vertices V′⊆V such that for every edge (u,v)∈E, at least one of u or v (or both) is in V′. The minimum size vertex cover problem asks for the smallest possible size of such a set V′.

The image displays a graph that is a 5-cycle, also known as a pentagon. Let's denote the vertices as v1​,v2​,v3​,v4​,v5​ in a circular order.

To find the minimum size vertex cover for a cycle graph Cn​:

- **For an even cycle $C_{2k}​$ , the minimum vertex cover size is k.**
- **For an odd cycle $C_{2k+1​}$ the minimum vertex cover size is k+1.**

In this case, the graph is a 5-cycle (C5​), which is an odd cycle where n=5. Here, 2k+1=5, so k=2. The minimum vertex cover size for C5​ is k+1=2+1=3.

Let's verify this by trying to select vertices:

1. If we select two non-adjacent vertices, say the two white ones at the top, they can cover two edges. The remaining three edges still need to be covered, requiring at least one more vertex.
    
2. If we select three vertices, we can cover all edges. For example, if we select three consecutive vertices, say v1​,v2​,v3​.
    
    - (v5​,v1​) is covered by v1​.
    - (v1​,v2​) is covered by v1​ or v2​.
    - (v2​,v3​) is covered by v2​ or v3​.
    - (v3​,v4​) is covered by v3​.
    - (v4​,v5​) is not covered. This selection won't work.
    
    Let's try selecting three vertices such that no two are adjacent (this is an independent set). An independent set in a C5​ can have a maximum size of 2 (e.g., two white vertices or two orange vertices that are not adjacent). Consider selecting three vertices in a way that covers all edges. If we pick the two orange vertices at the bottom and one of the white vertices, let's say the top white vertex.
    
    - Let the vertices be labelled 1-5 clockwise starting from the top orange: Orange (1), White (2), Orange (3), Orange (4), White (5).
    - Edges are (1,2), (2,3), (3,4), (4,5), (5,1).
    - If we pick {1, 3, 4}:
        - (1,2) covered by 1.
        - (2,3) covered by 3.
        - (3,4) covered by 3 or 4.
        - (4,5) covered by 4.
        - (5,1) covered by 1. This set {1, 3, 4} of size 3 is a vertex cover.

Therefore, the minimum size vertex cover for the given 5-cycle graph is **3**.