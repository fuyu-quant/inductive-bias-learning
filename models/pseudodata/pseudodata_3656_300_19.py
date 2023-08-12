import numpy as np

def predict(x):
    df = x.copy()
    output = []
    for index, row in df.iterrows():
        # Do not change the code before this point.
        # Please describe the process required to make the prediction below.

        # Calculate the sum of the values in columns a, b, c, and d
        sum_values = row['a'] + row['b'] + row['c'] + row['d']

        # Normalize the sum to a range between 0 and 1
        normalized_sum = (sum_values - df[['a', 'b', 'c', 'd']].values.min()) / (df[['a', 'b', 'c', 'd']].values.max() - df[['a', 'b', 'c', 'd']].values.min())

        # The probability of the target being 1 is proportional to the normalized sum
        y = normalized_sum

        # Do not change the code after this point.
        output.append(y)
    return np.array(output)