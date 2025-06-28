
### 🧠 **Self-Organizing Maps (SOMs)**

* **Type**: Unsupervised Artificial Neural Network
* **Purpose**: Dimensionality reduction and visualization of high-dimensional data
* **Structure**: Single-layer, feedforward, with neurons organized in 1D or 2D grids
* **Learning Type**: Competitive Learning

#### 🔄 Working Process:

1. **Competition**: All neurons compete; the one with weights closest to the input wins (winner-takes-all).
2. **Cooperation**: Neighbors of the winning neuron are also activated based on a neighborhood function (e.g., Gaussian).
3. **Synaptic Adaptation**: Weights of the winner and neighbors are updated using:

   $$
   w_j(n+1) = w_j(n) + \alpha(n) h_{ji}(n)(x - w_j(n))
   $$

#### 🔣 Mathematical Core:

* **Winning Neuron**:

  $$
  i(x) = \arg\min_j \|x - w_j\|
  $$
* **Neighborhood Function**:
  Typically Gaussian, width shrinks over time.

#### ✅ Applications:

* Data visualization (e.g., world poverty map)
* Pattern clustering
* Feature extraction

---

### 🔢 **Vector Quantization (VQ)**

* **Type**: Lossy compression method
* **Concept**: Input vectors are approximated by the nearest "codebook" vector
* **Components**:

  * **Encoder**: Maps input vectors to codebook indices
  * **Decoder**: Maps indices back to code vectors

---

### 🏷️ **Learning Vector Quantization (LVQ)**

* **Type**: Supervised classification (prototype-based)
* **Structure**: Input and output layers
* **Learning**: Similar to SOM, but uses class labels

#### ⚙️ LVQ Algorithm Steps:

1. Initialize weights using class-labeled training vectors.
2. For each input, find the closest neuron (Euclidean distance).
3. Update winning neuron's weights:

   * **If class matches**: Move closer
   * **If class differs**: Move away
4. Repeat until convergence.

---

### 🧮 Summary Table

| Concept | Type             | Learning                   | Purpose                    | Dimensionality |
| ------- | ---------------- | -------------------------- | -------------------------- | -------------- |
| SOM     | Unsupervised ANN | Competitive                | Visualization, clustering  | High → Low     |
| VQ      | Data Compression | -                          | Compression via prototypes | Any            |
| LVQ     | Supervised ANN   | Competitive + class labels | Classification             | Typically Low  |

---
