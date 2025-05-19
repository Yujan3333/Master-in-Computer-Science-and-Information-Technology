
## Code
```python
from sklearn.preprocessing import OneHotEncoder

# Create the encoder
encoder = OneHotEncoder(sparse_output=False)

# Reshape y and encode it
y_encoded = encoder.fit_transform(y.values.reshape(-1, 1))

# Get the mapping of which column represents which category
print("\nCategory mapping:")
categories = encoder.categories_[0]  # Get the list of categories
for i, category in enumerate(categories):
    print(f"Column {i} represents: {category}")

# Example
# [1. 0. 0.]  # This is setosa
# [0. 1. 0.]  # This is versicolor
# [0. 0. 1.]  # This is virginica

# See what the encoded output looks like
print("One-hot encoded output:")
print(y_encoded[:5])  # Show first 5 rows

```

![](../../../../../../Images/iris%20output.png)