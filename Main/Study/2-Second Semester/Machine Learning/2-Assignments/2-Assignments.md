### Lab 1
- Write python programs to implement linear regression using Stochastic GD, Batch GD, and mini-batch GD (use batch size 8) without using library. 
- Display the fitted line. 
- Capture time needed to train the prediction models and compare each approach (Use data.csv). 
- Also compute root mean squared error  and computation time in each case.
[Lab1-Explanation](Assignment_notes/Lab1-Explanation.md)

---
### Lab 1 - Continued
- Write python programs to predict diabetes using logistic regression. 
- Implement the algorithm using library and without using library. 
- Implement batch gradient descent. 
- Find accuracy, precision, recall, F1-score, and specificity and compare both strategies (Use diabetes.csv). 
- Assume train/test split is 70:30.
- Change value of learning rate 0.01 to 0.00001.
- Compare performance of both algorithms and write down conclusion.
[Lab1-Contd Explanation](Assignment_notes/Lab1-Contd%20Explanation.md)

---

### Lab 2
1. Use ID3 decision tree, Naïve Bayes, and SVM classifier to predict liver disease. Compare performance of the algorithms in terms of Accuracy, Precision, recall, F1-score, and specificity.

2.	Compare performance of Linear Regression and SVR in stock price prediction.

   o	Collect/download daily trading of at least 5 different companies’ from Nepal Stock Exchange. Choose two banking stocks, one insurance stock, one hydro stock, one development bank stock.
   
   o	Arrange data in chronological order of date.
   o	Only Keep Low, High, Open, Close, and Volume attributes. Remove other attributes.
   o	Generate ‘next days close price’ which is simple close price shifted back by one position.
   o	Handle missing data. Replace missing value by average of previous and next value.
   o	Split data into training, and test sets in 8:2 ratio.
   o	Normalize data using standard scalar.
   o	Predict next day’s close price.
   o	Perform inverse transformation of predicted price and close price of test data.
   o	Plot curve of predicted and actual close prices of test data.
   o	Plot training and validation loss and accuracy curves.
   o	Compute RMSE, MAE, MAPE and R2 coefficient of predicted and actual stock prices.
   o	Compare performance of LR and SVR on the basis of above measures.
   
