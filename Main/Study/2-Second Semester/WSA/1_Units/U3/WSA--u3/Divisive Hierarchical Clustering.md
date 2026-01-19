- [DIANA - Divisive Hierarchical Clustering](http://youtube.com/watch?v=jcdT_pVRqlE)

## Question
![](../../../../../../../Images/Second_Sem_Images/Divisive%20Hierarchical%20Clustering.png)

---
## Answer
### All in One Cluster
- Initially all points are in Cluster $C_i$ = {a,b,c,d,e} and $C_j$ = ${\phi}$
- Find the average Dissimilarity of objects in $C_i$ 
- Find the distances
#### Finding the Average Dissimilarity of a
![](../../../../../../../Images/Second_Sem_Images/Divisive%20Hierarchical%20Clustering-2.png)
#### Similarly finding the Average Dissimilarity of b c d and e

![](../../../../../../../Images/Second_Sem_Images/Divisive%20Hierarchical%20Clustering-3.png)
- Here choosing between `a` and `b` as they have the same value
- Remove `b` from Cluster $C_i$ and add to Cluster $C_J$

---
### Remaining Iterations
- Find the distance from `a` to every other points in $C_i$ and also subtract from Cluster of $C_j$
![](../../../../../../../Images/Second_Sem_Images/Divisive%20Hierarchical%20Clustering-4.png)
- `d` is added to the second cluster as `d` is positive and biggest

---
### Again repeating in Cluster $C_j$
- **IF POSITIVE VALUE THEN ONLY WE CHANGE CLUSTER**

![](../../../../../../../Images/Second_Sem_Images/Divisive%20Hierarchical%20Clustering-5.png)

---
### Now Decide to further divide the obtained Clusters
- Find the **DIAMETER** of both Clusters
- Max **DIAMETER** is divided

![](../../../../../../../Images/Second_Sem_Images/Divisive%20Hierarchical%20Clustering-6.png)

---