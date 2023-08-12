import numpy as np
import pandas as pd

def predict(x):
    df = x.copy()
    output = []
    for index, row in df.iterrows():
        # Do not change the code before this point.
        # Please describe the process required to make the prediction below.

        # Here we are assuming that the target is more likely to be 1 if Feature_1 is greater than 0.5 and Feature_2 is less than 0.
        # This is a simple rule-based approach and may not be accurate for complex datasets.
        if row['Feature_1'] > 0.5 and row['Feature_2'] < 0:
            y = 1
        else:
            y = 0

        # Do not change the code after this point.
        output.append(y)
    return np.array(output)

# Example usage:
# df = pd.DataFrame({
#     'Feature_1': [1.131, 1.314, 2.05, 0.175, 1.21],
#     'Feature_2': [-0.562, -0.443, 0.283, -0.015, -0.488],
#     'target': [1.0, 1.0, 1.0, 1.0, 1.0]
# })
# print(predict(df))