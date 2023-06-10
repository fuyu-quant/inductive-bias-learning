import numpy as np

def predict(x):
    df = x.copy()
    output = []
    for index, row in df.iterrows():
        # Do not change the code before this point.
        
        # Calculate the probability based on the given data
        pclass = row['pclass']
        sex = row['sex']
        age = row['age']
        fare = row['fare']
        embarked = row['embarked']
        who = row['who']
        adult_male = row['adult_male']
        alone = row['alone']

        # Initialize probability
        prob = 0

        # Consider the effect of pclass
        if pclass == 1:
            prob += 0.3
        elif pclass == 2:
            prob += 0.2
        else:
            prob += 0.1

        # Consider the effect of sex
        if sex == 'female':
            prob += 0.35
        else:
            prob += 0.15

        # Consider the effect of age
        if age <= 16:
            prob += 0.25
        elif age <= 32:
            prob += 0.2
        elif age <= 48:
            prob += 0.15
        elif age <= 64:
            prob += 0.1
        else:
            prob += 0.05

        # Consider the effect of fare
        if fare <= 10:
            prob += 0.1
        elif fare <= 20:
            prob += 0.15
        elif fare <= 30:
            prob += 0.2
        else:
            prob += 0.25

        # Consider the effect of embarked
        if embarked == 'C':
            prob += 0.1
        elif embarked == 'Q':
            prob += 0.05
        else:
            prob += 0.15

        # Consider the effect of who
        if who == 'child':
            prob += 0.25
        elif who == 'woman':
            prob += 0.35
        else:
            prob += 0.15

        # Consider the effect of adult_male
        if adult_male:
            prob -= 0.1

        # Consider the effect of alone
        if alone:
            prob -= 0.05

        # Normalize the probability
        prob = min(max(prob, 0), 1)

        # Do not change the code after this point.
        output.append(prob)
    return np.array(output)