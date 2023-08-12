Here is a simple Python code that uses a linear regression model to predict the probability of the target being 1. This code assumes that the input 'x' is a pandas DataFrame with columns 'Feature_1', 'Feature_2', and 'target'.

```python
import numpy as np
import pandas as pd

def predict(x):
    df = x.copy()
    output = []

    # Calculate the mean and standard deviation of each feature for each target value
    means = df.groupby('target').mean()
    stds = df.groupby('target').std()

    # Calculate the probability of each target value
    prob_target = df['target'].value_counts(normalize=True)

    for index, row in df.iterrows():
        # Calculate the probability of the features given each target value
        prob_feature_given_target = [
            np.exp(-((row[['Feature_1', 'Feature_2']] - means.loc[i]) ** 2) / (2 * stds.loc[i] ** 2)).prod()
            for i in [0, 1]
        ]

        # Calculate the probability of each target value given the features
        prob_target_given_feature = [
            prob_feature_given_target[i] * prob_target[i]
            for i in [0, 1]
        ]

        # Normalize the probabilities
        prob_target_given_feature = prob_target_given_feature / np.sum(prob_target_given_feature)

        # The predicted probability of the target being 1 is the second element
        y = prob_target_given_feature[1]

        output.append(y)

    return np.array(output)
```

This code uses the Bayes' theorem to calculate the probability of each target value given the features. The probability of the features given each target value is assumed to follow a Gaussian distribution, and is calculated using the mean and standard deviation of each feature for each target value. The probability of each target value is calculated from the frequency of each target value in the data. The predicted probability of the target being 1 is the second element of the normalized probabilities of each target value given the features.