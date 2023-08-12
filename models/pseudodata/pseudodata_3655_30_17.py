import numpy as np
import pandas as pd

def predict(x):
    df = x.copy()
    output = []
    for index, row in df.iterrows():
        # Do not change the code before this point.
        # Please describe the process required to make the prediction below.

        # Calculate the sum of the absolute values of the first four columns
        sum_abs = abs(row['a']) + abs(row['b']) + abs(row['c']) + abs(row['d'])

        # Calculate the sum of the squares of the first four columns
        sum_squares = row['a']**2 + row['b']**2 + row['c']**2 + row['d']**2

        # Calculate the mean of the first four columns
        mean = (row['a'] + row['b'] + row['c'] + row['d']) / 4

        # Calculate the standard deviation of the first four columns
        std_dev = np.std([row['a'], row['b'], row['c'], row['d']])

        # Calculate the prediction as a weighted sum of the above four metrics
        y = 0.25 * sum_abs + 0.25 * sum_squares + 0.25 * mean + 0.25 * std_dev

        # Normalize the prediction to the range [0, 1]
        y = (y - df.min().min()) / (df.max().max() - df.min().min())

        # Do not change the code after this point.
        output.append(y)
    return np.array(output)