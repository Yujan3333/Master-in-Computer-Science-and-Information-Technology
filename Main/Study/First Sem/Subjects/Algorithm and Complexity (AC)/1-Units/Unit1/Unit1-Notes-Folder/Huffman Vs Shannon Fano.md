

|Aspect|**Shannon-Fano Coding**|**Huffman Coding**|
|---|---|---|
|**Inventors**|Claude Shannon & Robert Fano|David Huffman|
|**Year**|~1949|1952|
|**Approach**|Top-down (divide-and-conquer)|Bottom-up (greedy algorithm)|
|**Procedure**|1. Sort symbols by frequency. 2. Recursively split into two equal-probability groups. 3. Assign `0` and `1` to the branches.|1. Build a min-heap of symbols based on frequency. 2. Combine two lowest-frequency nodes into one. 3. Repeat until one root remains.|
|**Code Optimality**|**Not always optimal.** May result in longer codes.|**Optimal prefix code** with the **minimum average code length**.|
|**Prefix Property**|Yes|Yes|
|**Complexity**|O(n log n)|O(n log n)|
|**Example Usage**|Theoretical or educational use|Widely used (e.g., ZIP, JPEG, MP3)|
|**Tree Structure**|May be unbalanced|Always optimal and compact|
