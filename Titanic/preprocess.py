import numpy as np
def Gender(gender):
    if gender.lower() == 'female':
        return 0
    elif gender.lower() == 'male':
        return 1 
   

def Embarked(embark):
    if embark.lower() == 's' : 
        return 0
    elif embark.lower() == 'c' :
        return 1
    elif embark.lower() == 'q' :
        return 2
    

## data is du=ictionary contains all input from the user
def preprocess_data(data) :
    age = data['Age']
    
    fare = data['Fare']
    
    pclass = data['PClass']
    
    sex = Gender(data['Sex'])    
    
    sibsp = data['SibSp']
    
    parch = data['Parch']
    
    embark = Embarked(data['Embarked'])
    
    final_data = [pclass,sex,age,sibsp,parch,fare,embark]
    
    return final_data
        