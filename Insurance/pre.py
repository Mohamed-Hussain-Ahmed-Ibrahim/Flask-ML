import numpy as np
def Sex(gender):
    if gender.lower() == 'female':
        return 0 
    elif gender.lower() == 'male' :
        return 1
def Smoker(smok):
    if smok.lower() == 'no':
        return 0 
    elif smok.lower() == 'yes' :
        return 1
def Region(reg):
    if reg.lower() == 'southeast':
        return 1
    elif reg.lower() == 'southwest':
        return 2
    elif reg.lower() == 'northwest':
        return 3
    elif reg.lower() == 'northeast':
        return 4
def preprocess_data(data):
    age = data['Age']
    bmi = data['Body Mass Index']
    sex = Sex(data['Sex'])
    child = data['Children']
    smoke = Smoker(data['Smoker'])
    region = Region(data['Region'])
    final_data = [age,sex,bmi,child,smoke,region]
    return np.array(final_data)