```python
# b) Display input and output features of the dataset.

## What are we going to do?
  # See all the column names
  # Separate input features(X) and output label(Y)
  # Print them Clearly

# Show all column names
print("All Columns in Dataset:")
print(df.columns.tolist())

# Output feature (the thing we want to predict)
output_feature = 'HeartDisease'

# Input features (everything except the output)
input_features = df.drop(columns=[output_feature]).columns.tolist()

print("\nInput Features:")
for col in input_features:
    print("-", col)

print("\nOutput Feature:")
print(output_feature)


# Shuffle data just prep for next
df = df.sample(frac=1).reset_index(drop=True)
```
##### Output
![](../../../../../../Images/Display%20input%20and%20output%20features%20of%20the%20dataset.png)