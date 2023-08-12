import numpy as np
import pandas as pd

def predict(x):
    df = x.copy()
    output = []
    for index, row in df.iterrows():
        # Do not change the code before this point.
        # Please describe the process required to make the prediction below.

        # Here we are using a simple rule-based approach to predict the target.
        # The rules are based on the observations from the given data.
        # For example, if 'sex_female' is 1, 'class_First' is 1 and 'fare' is high, the probability of survival is high.
        # Similarly, if 'sex_male' is 1, 'class_Third' is 1 and 'fare' is low, the probability of survival is low.
        # This is a very basic approach and may not give accurate results for complex datasets.

        if row['sex_female'] == 1 and row['class_First'] == 1 and row['fare'] > 50:
            y = 0.9
        elif row['sex_male'] == 1 and row['class_Third'] == 1 and row['fare'] < 10:
            y = 0.1
        else:
            y = 0.5

        # Do not change the code after this point.
        output.append(y)
    return np.array(output)