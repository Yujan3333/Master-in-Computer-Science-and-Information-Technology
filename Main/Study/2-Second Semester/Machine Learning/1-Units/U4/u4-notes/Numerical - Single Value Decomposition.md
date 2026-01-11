[SVD - Mahesh Huddar](https://www.youtube.com/watch?v=q-J8WueQpek)

---
## Que
![](../../../../../../../Images/Second_Sem_Images/Numerical%20-%20Single%20Value%20Decomposition.png)

---
## Answer

### Step 1 
- Find the transpose of column and multiply A and $A^T$
- A x $A^T$
- $A^T$ x A
![](../../../../../../../Images/Second_Sem_Images/Numerical%20-%20Single%20Value%20Decomposition-1.png)

### Step 3 - Find U - Left Singular Vector
- Calculating eigen value and eigen vector first using $AA^T$ - $\lambda$I = 0
- Then Calculate `U`
- While finding u=[x,y] put the value of $\lambda$ found above and find the eigen vectors of `U` and *Normalize them also*

#### For $\lambda$ = 0
![](../../../../../../../Images/Second_Sem_Images/Numerical%20-%20Single%20Value%20Decomposition-2.png)

#### For $\lambda$ = 100
![](../../../../../../../Images/Second_Sem_Images/Numerical%20-%20Single%20Value%20Decomposition-3.png)
#### Calculated U
- Priority to higher $\lambda$ = 100 given
![](../../../../../../../Images/Second_Sem_Images/Numerical%20-%20Single%20Value%20Decomposition-4.png)


### Step 4 - Find $V^T$ Right Singular Vector
- Similar find the eigen values and eigen vector $A^T$A - $\lambda$I = 0

![](../../../../../../../Images/Second_Sem_Images/Numerical%20-%20Single%20Value%20Decomposition-5.png)

#### For first eigen value
![](../../../../../../../Images/Second_Sem_Images/Numerical%20-%20Single%20Value%20Decomposition-6.png)

#### For Second eigen value
![](../../../../../../../Images/Second_Sem_Images/Numerical%20-%20Single%20Value%20Decomposition-7.png)

#### Rearrange the eigen values in eigen vector
![](../../../../../../../Images/Second_Sem_Images/Numerical%20-%20Single%20Value%20Decomposition-8.png)

---
### Calculating S
![](../../../../../../../Images/Second_Sem_Images/Numerical%20-%20Single%20Value%20Decomposition-10.png)