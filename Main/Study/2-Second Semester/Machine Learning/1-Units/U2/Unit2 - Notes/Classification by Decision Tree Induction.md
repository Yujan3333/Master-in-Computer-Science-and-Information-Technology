- Decision tree induction is a supervised machine learning process that builds a flowchart-like model (a decision tree).
- A decision tree is a tree-structured model where **internal nodes** represent *tests on attributes*, **branches** represent *outcomes of the test*, and **leaf nodes** represent *class labels or decisions.*

## Decision Tree Induction
 
 Decision tree induction is the process of learning a decision tree from a set of **class-labeled training tuples**.
 
 A **decision tree** is a flowchart-like tree structure in which:
 
 * **Internal nodes (non-leaf nodes)** represent a test on an attribute
 * **Branches** represent the outcome of the test
 * **Leaf nodes (terminal nodes)** represent class labels
 
 ---
 
## Decision Tree Prediction
 
 To make a prediction for a given tuple:
 
 * The attribute values of the tuple are tested against the decision tree
 * A path is followed from the **root node** to a **leaf node**
 * The class label stored at the leaf node is the **predicted class** for the tuple
 
 ---
 
## Algorithm for Constructing a Decision Tree
 
 Decision tree construction follows a **greedy approach** and uses a **top-down, divide-and-conquer strategy**.
 
### Steps:
 
 1. Initially, all training tuples are placed at the **root node**
 2. Select the best attribute and **partition the data** based on attribute values
 3. Repeat the process recursively for each partition
 
### Stopping Conditions:
 
 * **If all tuples at a node belong to the same class**
   → Assign that class label to the node
 
 * **If no attributes remain for further partitioning**
   → Assign the class label using **majority voting**
 
 * **Otherwise**
   → Continue partitioning (go back to Step 2)
 
 ---
## Decision Tree Algorithms
 
 Some commonly used decision tree algorithms are:
 
 * **ID3 (Iterative Dichotomiser 3)**
 * **C4.5** (successor of ID3)
 * **CART (Classification and Regression Tree)**
 
 ---
 
## Attribute Selection Measures
 
 Decision tree classifiers use attribute selection measures to determine the best attribute for splitting the data. Some common measures are:
 
 * **Information Gain**
 * **Gain Ratio**
 * **Gini Index**
 
 ---
 