| No. | **K-Means**                                  | **K-Medoids**                                         |
| --- | -------------------------------------------- | ----------------------------------------------------- |
| 1   | Uses **mean** as cluster center              | Uses **medoid (actual data point)** as cluster center |
| 2   | Centroid **may not be a real data point**    | Medoid is **always a real data point**                |
| 3   | Sensitive to **outliers and noise**          | **Less sensitive** to outliers                        |
| 4   | Works best with **numeric data**             | Works with **numeric and categorical data**           |
| 5   | Uses **Euclidean distance** commonly         | Can use **any distance measure**                      |
| 6   | Faster and **computationally efficient**     | Slower and **computationally expensive**              |
| 7   | Not robust for noisy datasets                | More **robust** for noisy datasets                    |
| 8   | Minimizes **sum of squared distances**       | Minimizes **sum of distances**                        |
| 9   | Cluster center changes continuously          | Cluster center chosen from dataset                    |
| 10  | Poor performance with non-spherical clusters | Handles **arbitrary shaped clusters** better          |
| 11  | Initialization affects result greatly        | Less affected by initialization                       |
| 12  | Not suitable for small datasets with noise   | Good for **small, noisy datasets**                    |
| 13  | Simple algorithm                             | More complex than K-Means                             |
| 14  | Memory usage is lower                        | Memory usage is higher                                |
| 15  | Common algorithm used in practice            | Used when robustness is required                      |
| 16  | Examples: Lloyd’s algorithm                  | Examples: PAM, CLARA                                  |
| 17  | Distance recalculation is easy               | Distance recalculation is expensive                   |
| 18  | Cannot handle missing values well            | Can handle missing values better                      |
| 19  | Not good for categorical attributes          | Suitable for mixed attributes                         |
| 20  | Centroid may lie outside cluster             | Medoid always lies inside cluster                     |
