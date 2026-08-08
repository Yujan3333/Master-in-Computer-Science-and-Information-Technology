
| Feature         | Bagging                            | Boosting                                            | Stacking                                                          |
| --------------- | ---------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------- |
| **Training**    | Parallel (independent models)      | Sequential (each model learns from previous errors) | Parallel/Sequential (different models)                            |
| **Focus**       | Reduce variance                    | Reduce bias                                         | Combine strengths of different models                             |
| **Weighting**   | Equal vote                         | Weighted (misclassified points get more weight)     | Meta-model learns how to combine predictions                      |
| **Overfitting** | Less prone if base model is stable | Can overfit if too many rounds                      | Depends on base/meta-models                                       |
| **Examples**    | Random Forest                      | AdaBoost, Gradient Boosting, XGBoost                | Any combination (e.g., Logistic Regression + Decision Tree + SVM) |
| **Output**      | Majority vote / Average            | Weighted sum / vote                                 | Meta-model output                                                 |
