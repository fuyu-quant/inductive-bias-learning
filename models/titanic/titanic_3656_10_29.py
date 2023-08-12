import numpy as np

def predict(x):
    df = x.copy()
    output = []
    for index, row in df.iterrows():
        # Do not change the code before this point.
        # Please describe the process required to make the prediction below.

        # The logic here is to give higher probability for survival if the passenger is a female, in first class, and embarked from Cherbourg.
        # This is based on the historical data that women, children, and the upper-class passengers were the first to be evacuated.
        # The age, fare, and number of siblings/spouses/parents/children are also considered.
        # The values are normalized to be between 0 and 1.

        y = (row['sex_female'] + row['class_First'] + row['embarked_C'] + row['age']/80 + row['fare']/500 + row['sibsp']/8 + row['parch']/6) / 7

        # Do not change the code after this point.
        output.append(y)
    return np.array(output)