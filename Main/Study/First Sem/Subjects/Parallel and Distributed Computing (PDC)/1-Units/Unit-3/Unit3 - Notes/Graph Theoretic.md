
### Undirected Graph

* A graph where edges have no direction.
* Edges are unordered pairs of vertices.
* Example: Edge between vertices *u* and *v* means connection both ways.

### Subgraph

* A graph formed from a subset of vertices and edges of another graph.
* Contains some or all vertices and edges of the original graph.

### Connected Graph

* A graph in which **there is a path between every pair of vertices**.
* No vertex is isolated from any other.

### Bi-connected Graph (2-Connected Graph)

* A connected graph where **removing any single vertex (and edges incident to it) still leaves the graph connected**.
* No vertex is a "cut-vertex."

### Cut-Vertex (Articulation Point)

* A vertex *v* in graph *G* is a cut-vertex if **removing *v* (and its incident edges) disconnects the graph**.
* Its removal increases the number of connected components.

### Cut-Edge (Bridge)

* An edge {x,y} in *G* is a cut-edge or bridge if **removing this edge disconnects the graph**.
* Its removal increases the number of connected components.

### Clique

* A subset of vertices all pairwise adjacent.
* Equivalently, a **complete subgraph**.
* Every two vertices in the clique have an edge connecting them.

### Matching

* A set of edges in a graph with **no two edges sharing a common vertex**.
* Used in pairing problems, assignments, and more.

---
