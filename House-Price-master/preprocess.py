import numpy as np
def preprocess(data):
    qual = data['qual']
    cond = data['cond']
    sf1 = data['sf1']
    area = data['area']
    bed = data['bed']
    garage = data['garage']
    final_data = [qual,cond,sf1,area,bed,garage]
    return np.array(final_data)