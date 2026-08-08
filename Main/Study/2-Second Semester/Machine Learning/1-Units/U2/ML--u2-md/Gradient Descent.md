
- [Slope](Slope.md)
- [Gradient Descent Detail](../../../../../1-First%20Semester/Subjects/Neural%20Network%20(NN)/1-Units/Unit%203/NN-u3-md/Gradient%20Descent%20Detail.md)
- [Types of Gradient Descent](Types%20of%20Gradient%20Descent.md)
- [Convex Vs Non-Convex Functions](Convex%20Vs%20Non-Convex%20Functions.md)

## In Summary

- Gradient descent is an **optimization algorithm** used to minimize some *convex function(U shaped curve)* by iteratively moving in the direction of steepest descent as defined by the *negative of the gradient*. 
	  - Negative of the gradient to get the global minima.

- Used to update the parameters of our model. Parameters refer to *coefficients* in Linear Regression and *weights* in neural networks.

#### Figure- Gradient Descent
![](../../../../../../../Images/Second_Sem_Images/Gradient%20Descent.png)
![](../../../../../../../Images/Second_Sem_Images/Gradient%20Descent-pos%20and%20neg.png)



### Steep slope = Large gradient = Long step = Faster initial learning.
- When the slope is steep, the gradient is large. This means we are far from the minimum, and the model can take big steps towards it.
- With a sufficient learning rate, the model's parameters can quickly move a significant distance across the landscape. 
- This is where "**faster learning**" happens, as the model rapidly reduces its loss.

### Gentle slope = Small gradient = Short step = Slower fine-tuning.
- As the model approaches the minimum, the slope becomes gentler, and the gradient becomes smaller.
- Slower but crucial for precision.


### Zero slope = Zero gradient = No step = Learning stops.
- There's no gradient arrow because there's no direction of descent. 
- However, if it's stuck on a flat plateau or a local minimum that isn't the best overall solution, the model has stopped learning effectively

