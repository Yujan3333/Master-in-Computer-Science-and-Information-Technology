### How QuickSort Works (Simple Explanation)  
---
Quick Sort is a **divide-and-conquer** sorting algorithm that works in three main steps:  

1. **Choose a Pivot (Randomly)**  
   - Pick a random element from the array. This element is called the **pivot**.  
2. **Divide the Array**  
   - Rearrange the array so that:  
     - All numbers **smaller** than the pivot go to the **left** side.  
     - All numbers **greater** than the pivot go to the **right** side. 
3. **Repeat the Process**  
   - Apply the same steps to the left and right parts separately until the whole array is sorted.  

Since the pivot is chosen **randomly**, this is called a **randomized algorithm**.

![](../../../../../../Images/Randomized%20Quicksort.png)
##### Pseudo Code
```md
INPUT: n-element array A function Randomized quicksort(A):  
- Return A # A is sorted if n = 1.  
- If not: i = Random number inside range (1, n)  
- Partition A into elements < x, x, and >x as illustrated in the  
accompanying diagram: X = A[i] # the pivot element  
- Use Quicksort to sort the arrays A[1 to i-1] and A[i+1 to n].  
- To create a sorted array, combine the answers.  
In the worst case scenario, this algorithm takes O(n²) time to  
sort n digits in case the pivot element chosen at random is the first  
or last element in the array.
```
![](../../../../../../Images/Randomized%20Quicksort%20Explained.png)
![](../../../../../../Images/Randomized%20Quicksort-Exp.png)



## References
[Randomized Algo-Medium](https://medium.com/@aditya.patil20/randomized-algorithms-a11fe076b8d9#:~:text=Las%20Vegas%20%3A,(nLogn).)
[Randomized Algo-Geeks4Geeks](https://www.geeksforgeeks.org/randomized-algorithms-set-2-classification-and-applications/)
[When to Choose Randomized Algo-Medium](https://medium.com/@sachin.shreya21/when-to-choose-randomized-algorithms-understanding-las-vegas-and-monte-carlo-algorithms-9324d5e9f996)
