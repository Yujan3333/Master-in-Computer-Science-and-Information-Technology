- A Las Vegas algorithm were introduced by *Laszlo Babai* in 1979.

- A Las Vegas algorithm is an algorithm which uses *randomness*, but gives *guarantees* that the *solution* obtained for given problem is correct. It takes the *risk* with *resources* used. 

 - Example: **Quick Sort** 
	 - For that we find out central element which is also called as pivot element and each element is compared with this pivot element. 
	 - Sorting is done in less time or it requires more time is dependent on how we select the pivot element. 
	 - To pick the pivot element randomly we can use Las-Vegas algorithm.
---
#### [Randomized Quicksort](Randomized%20Quicksort.md)
- When using Randomised QuickSort to sort an input array, the estimated **worst-case time complexity** is *O(nLogn)*.

- In the worst case, it can take O(n^2) time, but on average, it runs in O(nlog⁡n).

- The worst case will happen when doing pairwise comparison, taking **O(n2**), where the time needed grows as a square of the number of digits to be sorted. This algorithm’s runtime can be lowered to **O(n log(n))** using randomization, though.

---
#### Definition
A Las-Vegas algorithm take the risk with the resources used for computation but it does not take risk with the result i.e. it gives correct and expected output for the given problem.

##### **When to Use Las Vegas Algorithms:**

**a. Approximation Problems:** Las Vegas algorithms are ideal when dealing with optimization problems where you need an approximation to a solution. They provide solutions that are typically close to the optimal result while still ensuring correctness.

**b. NP-Hard Problems:** When dealing with NP-hard problems that are computationally intractable in the worst-case, Las Vegas algorithms can provide practical solutions within a reasonable amount of time.