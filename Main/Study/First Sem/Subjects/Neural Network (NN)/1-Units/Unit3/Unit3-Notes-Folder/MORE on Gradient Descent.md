#### The higher the gradient, the steeper the slope and the faster a model can learn. But if the slope is zero, the model stops learning. Said it more mathematically, a gradient is a partial derivative with respect to its inputs. > How big the steps are that Gradient Descent takes into the direction of the local minimum are determined by the learning rate. 


##### [[What is a Slope and Gradient]] ?
### 🌄 Think of a Hill and a Ball
Imagine you're on a hill, and you want to roll a ball down to the lowest point (the **minimum**). That lowest point is where the error of your model is smallest — that's what we want!

---

### 🧭 What is the Gradient?
The **gradient** tells us which direction is steepest downhill.  
Mathematically, it's like a **slope** — the **partial derivative** is just a fancy word for slope in each direction.

- **Big gradient** → steep slope → take big steps.
    
- **Small gradient** → flat area → take small steps.
    
- **Zero gradient** → completely flat → you're either at the bottom or stuck → no movement (no learning).
    


### 🏃‍♂️ What is Gradient Descent?
**Gradient Descent** is how your model “walks downhill” using the gradient to guide it.

- It uses the gradient to know **which direction to go**.
    
- It uses the **learning rate** to know **how big each step should be**.
    


### 🎚️ What is the Learning Rate?
The **learning rate** is just a number that controls **how big your steps** are.

- Too **big** → you might jump over the minimum or never reach it.
    
- Too **small** → you’ll get there, but very slowly.
    

### 🧠 Simple Summary
- Gradient = slope = tells the direction to move.
    
- Gradient Descent = way for the model to improve itself by reducing error.
    
- Learning Rate = controls step size.
    
- If the slope is **zero**, there's **no direction to go**, so learning **stops**.
    

---


