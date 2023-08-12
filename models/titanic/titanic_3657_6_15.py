import numpy as np

def predict(x):
    df = x.copy()
    output = []
    for index, row in df.iterrows():
        # Do not change the code before this point.
        # Please describe the process required to make the prediction below.

        # Here we are using a simple rule-based approach to predict the target.
        # We are assuming that if the passenger is female, young, and belongs to the first class, 
        # then there is a high probability that the target is 1. 
        # Otherwise, we assume that the probability is low.
        if row['sex_female'] == 1.0 and row['age'] <= 30.0 and row['pclass'] == 1.0:
            y = 0.9
        else:
            y = 0.1

        # Do not change the code after this point.
        output.append(y)
    return np.array(output)