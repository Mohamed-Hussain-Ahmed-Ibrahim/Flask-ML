import numpy as np
## data is du=ictionary contains all input from the user
def preprocess_data(data) :
    age = data['Age']
    
    number = data['Number']
    
    start = data['Start']
    
    final_data = [age,number,start]
    
    return np.array(final_data)
