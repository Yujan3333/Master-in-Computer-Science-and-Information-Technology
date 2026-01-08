
## **Overfitting vs Underfitting**

| Parameter              | **Overfitting**                                          | **Underfitting**                                 |
| ---------------------- | -------------------------------------------------------- | ------------------------------------------------ |
| Definition             | Model learns **training data too well**, including noise | Model is **too simple** to capture data patterns |
| Model behavior         | Very complex                                             | Very simple                                      |
| Training accuracy      | Very high                                                | Low                                              |
| Test accuracy          | Low                                                      | Low                                              |
| Generalization         | Poor                                                     | Poor                                             |
| Bias                   | Low bias                                                 | High bias                                        |
| Variance               | High variance                                            | Low variance                                     |
| Cause                  | Too many features, deep model, small dataset             | Too few features, shallow model                  |
| Effect                 | Memorizes data                                           | Misses important patterns                        |
| Example                | Deep decision tree                                       | Linear model for complex data                    |
| Curve fitting          | Fits every point                                         | Cannot fit data properly                         |
| Error on training data | Very low                                                 | High                                             |
| Error on unseen data   | High                                                     | High                                             |
| Solution               | Pruning, regularization, more data                       | Increase model complexity                        |
| Common in              | Decision trees, k-NN (small k)                           | Linear regression, k-NN (large k)                |

---

## **Simple One-Line Explanation**

* **Overfitting:** *Too much learning*
* **Underfitting:** *Too little learning*

---

## **Perfect Fit (Just for understanding)**

* Balanced model
* Good training accuracy
* Good test accuracy

---
