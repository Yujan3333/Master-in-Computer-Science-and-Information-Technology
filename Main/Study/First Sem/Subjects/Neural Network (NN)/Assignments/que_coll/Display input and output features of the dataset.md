- [Lab1 Heart Disease](#Lab1%20Heart%20Disease.md)
- [Lab2: Iris Prediction](#Lab2%20Iris%20Prediction)

---
## Lab1: Heart Disease
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


---
## Lab2: Iris Prediction
```python
#  1. Check the dataset for missing values and handle, if any.

# Check for missing values
print("Missing values:\n", df.isnull().sum())


#  2. Display input and output features of the dataset.
print("\nTotal colunms")
print(list(df.columns))

# Output Label
output_label = 'Species '

# Input features (everything except the 'species' column)
X = df.drop(output_label, axis=1)

# Output labels (just the 'species' column)
y = df[output_label]

print("Input Features (X):\n", list(X))
print("Output Label (y):", output_label)

# Shuffle the dataset
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Count and display number of tuples in output class
class_counts = df_shuffled['Species '].value_counts()
print("\nNumber of tuples in each class after shuffling:")
print(class_counts)
print("Shuffled Dataset:\n", df_shuffled)

```

###### Output
![](../../../../../../Images/iris%20input%20output%20features.png)
---
#### Explaining the shuffling code
`df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)`

 **Breaking It Down (Step by Step):**
1. **`df.sample(frac=1)`**
    - Takes your dataset (`df`) and **randomly shuffles all the rows**.
        
    - `frac=1` means "keep 100% of the data, just mix it up!"
        
2. **`random_state=42`**
    - Makes the shuffle **predictable** (like using the same shuffle pattern every time).
        
    - Without this, the shuffle would be different each time you run the code.
        
3. **`.reset_index(drop=True)`**
    - After shuffling, the old row numbers are messy (like cards out of order).
        
    - This **gives new, clean row numbers** (0, 1, 2, 3...).
        
    - `drop=True` means "throw away the old numbers, don’t keep them!"