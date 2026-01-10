
### **Formula**

$$
 \text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2}
 $$
 

Where:

* (N) = number of observations
* $(y_i)$ = actual value of the i-th observation
* ($\hat{y}_i)$ = predicted value of the i-th observation

---

### **Explanation**

1. Subtract the predicted value from the actual value → gives the **error** for each observation.
2. Square the error → penalizes large errors more heavily.
3. Take the mean of all squared errors → gives **Mean Squared Error (MSE)**.
4. Take the square root → gives **RMSE**, bringing the error back to the **same unit as the original variable**.

---

✅ **Key point:** Lower RMSE means the model predictions are closer to actual values.

---

