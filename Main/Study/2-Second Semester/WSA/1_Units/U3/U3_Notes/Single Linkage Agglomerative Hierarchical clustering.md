- [Single Linkage](https://www.youtube.com/watch?v=tXYAdGn-SuM&t=18s)
## Question
![](../../../../../../../Images/Second_Sem_Images/Single%20linkage%20hierarchical%20clustering.png)

### Formula
![](../../../../../../../Images/Second_Sem_Images/Single%20linkage%20hierarchical%20clustering-1.png)

---
## Answer

### Step 1 : Find the distance from each point to all point
- Minimum Distance
![](../../../../../../../Images/Second_Sem_Images/Single%20linkage%20hierarchical%20clustering-2.png)

---
### Step 2 : Find the minimum Distance is `2` for `c and e`
- Here the minimum distance is between *c and e*. 
- Merge *c and e*
![](../../../../../../../Images/Second_Sem_Images/Single%20linkage%20hierarchical%20clustering-3.png)

---
### Step 3 : Find all the points of new cluster `ce`
![](../../../../../../../Images/Second_Sem_Images/Single%20linkage%20hierarchical%20clustering-4.png)

---
### Step 4 : Minimum distance again is between `a` and `ce` is `3`
![](../../../../../../../Images/Second_Sem_Images/Single%20linkage%20hierarchical%20clustering-5.png)

---
### Step 5 :  Updating the distance of cluster `ace` to all other points
![](../../../../../../../Images/Second_Sem_Images/Single%20linkage%20hierarchical%20clustering-6.png)

---
### Step 6 : Again the Minimum point is `5` between `b and d`

![](../../../../../../../Images/Second_Sem_Images/Single%20linkage%20hierarchical%20clustering-7.png)

---
### Step 7 : Updating the Final distance of the cluster `bd`

![](../../../../../../../Images/Second_Sem_Images/Single%20linkage%20hierarchical%20clustering-8.png)


---
### Dendrogram
![](../../../../../../../Images/Second_Sem_Images/Single%20linkage%20hierarchical%20clustering-9.png)