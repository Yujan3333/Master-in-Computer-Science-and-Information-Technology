```python
# c) Encode non-numeric input attributes using Label Encoder.
  # from sklearn.preprocessing import LabelEncoder

# Make a copy to avoid modifying original DataFrame
df_encoded = df.copy()

# Encode non-numeric input attributes using Label Encoder.
# The 5 non-numeric attributes present in the dataset
categorical_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

# Create an empty dictionary to store LabelEncoder objects for each column
# (This helps reuse the same encoding later if new data comes in)
label_encoders = {}

for col in categorical_cols:
    
    # Initialize a LabelEncoder for the current column
    le = LabelEncoder()

    # Fit the encoder to the column's unique values and transform the column
    # Example: If 'Sex' has 'Male' and 'Female', it may convert them to 1 and 0
    df_encoded[col] = le.fit_transform(df[col])

    # Store the encoder in the dictionary for future use
    label_encoders[col] = le  


# Print the DataFrame after encoding
print("DataFrame after Label Encoding:\n", df_encoded)

```
###### Output
![](../../../../../../Images/encoding%20non%20numeric.png)

---
## What Each Part Does:

1. **`LabelEncoder()`**
    
    - A tool that converts text categories (like "Male"/"Female") into numbers (like `0` and `1`).
        
2. **`fit_transform()`**
    
    - **Step 1 (Fit):** Learns all unique categories in the column (e.g., `['Male', 'Female']`).
        
    - **Step 2 (Transform):** Replaces each category with a number (e.g., `Male → 1`, `Female → 0`).
        
3. **`label_encoders[col] = le`**
    
    - Saves the encoder so you can reuse it later (e.g., to encode new data consistently).
        
4. **Why Do This?**
    
    - Machine learning models need numbers, not text. Encoding converts text into numbers they can understand.
        

### **Example Before & After Encoding:**

**Before:**

| Sex    | ChestPainType |
| ------ | ------------- |
| Male   | Atypical      |
| Female | Typical       |
| Male   | Non-anginal   |

**After:**

| Sex (Encoded) | ChestPainType (Encoded) |
| ------------- | ----------------------- |
| 1             | 0                       |
| 0             | 2                       |
| 1             | 1                       |

### Key Notes

- **Label Encoding assigns arbitrary numbers** (e.g., `0, 1, 2`).
    
    - This is fine for categories like `Sex` (Male/Female) where order doesn’t matter.
        
    - Not ideal for categories like `"Low", "Medium", "High"` (where order matters—use **Ordinal Encoding** instead).
        
- For categories without order (e.g., colors), **One-Hot Encoding** is often better.