import numpy as np

def predict(x):
    df = x.copy()
    output = []
    for index, row in df.iterrows():
        # Do not change the code before this point.
        # Please describe the process required to make the prediction below.

        # Calculate the probability based on the given features
        pclass_prob = {1: 0.63, 2: 0.47, 3: 0.24}
        sex_prob = {'female': 0.74, 'male': 0.19}
        age_prob = {0: 0.67, 1: 0.38, 2: 0.40, 3: 0.44, 4: 0.09}
        fare_prob = {0: 0.68, 1: 0.50, 2: 0.44, 3: 0.15}
        
        pclass = row['pclass']
        age = row['age']
        sex_female = row['sex_female']
        fare = row['fare']
        
        # Calculate the probability based on pclass
        pclass_probability = pclass_prob[pclass]
        
        # Calculate the probability based on sex
        if sex_female == 1:
            sex_probability = sex_prob['female']
        else:
            sex_probability = sex_prob['male']
        
        # Calculate the probability based on age
        if age <= 16:
            age_group = 0
        elif age <= 32:
            age_group = 1
        elif age <= 48:
            age_group = 2
        elif age <= 64:
            age_group = 3
        else:
            age_group = 4
        age_probability = age_prob[age_group]
        
        # Calculate the probability based on fare
        if fare <= 7.91:
            fare_group = 0
        elif fare <= 14.454:
            fare_group = 1
        elif fare <= 31:
            fare_group = 2
        else:
            fare_group = 3
        fare_probability = fare_prob[fare_group]
        
        # Calculate the final probability
        y = pclass_probability * sex_probability * age_probability * fare_probability

        # Do not change the code after this point.
        output.append(y)
    return np.array(output)