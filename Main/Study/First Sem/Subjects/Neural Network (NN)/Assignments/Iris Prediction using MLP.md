- Check the dataset for missing values and handle, if any.

- Display input and output features of the dataset.

- Encode output attribute using one hot encoder.

- Shuffle the dataset and then count and display number of tuples in each class.

- Normalize input attributes using standard scalar.

- Split dataset into training/validation/test sets in 70:15:15 ratio.

- Construct an MLP with configuration 4x32x16x8x3. Use Adam optimizer and appropriate activation functions and train the model.

- Predict species of Iris flower for test data and display confusion matrix, weighted avg. accuracy, macro & micro recall, macro & micro precision and macro and micro F1-score.