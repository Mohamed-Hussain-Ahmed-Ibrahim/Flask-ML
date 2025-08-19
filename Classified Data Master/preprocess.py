import numpy as np
    
## data is du=ictionary contains all input from the user
def preprocess_data(data) :
    wtt = data['WTT']
    pti = data['PTI']
    eqw = data['EQW']
    sbi = data['SBI']
    lqe = data['LQE']
    qwg = data['QWG']
    fdj = data['FDJ']
    pjf = data['PJF']
    hqe = data['HQE']
    nxj = data['NXJ']
    
    final_data = [wtt,pti,eqw,sbi,lqe,qwg,fdj,pjf,hqe,nxj]
    
    return np.array(final_data)