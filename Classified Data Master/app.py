import re
import joblib
from flask import Flask, render_template, request
import preprocess  
import numpy as np

app = Flask(__name__)

scaler = joblib.load('Models/scaler.h5')
model = joblib.load('Models/model.h5')


@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET']) 
def get_prediction() :
    if request.method == 'POST' :
        wtt = request.form['wtt']
        pti = request.form['pti']
        eqw = request.form['eqw']
        sbi = request.form['sbi']
        lqe = request.form['lqe']
        qwg = request.form['qwg']
        fdj = request.form['fdj']
        pjf = request.form['pjf']
        hqe = request.form['hqe']
        nxj = request.form['nxj']
        
    data = {'WTT' : wtt, 'PTI' : pti, 'EQW' : eqw ,
            'SBI' : sbi, 'LQE' : lqe, 'QWG' : qwg ,'FDJ' : fdj ,'PJF':pjf,'HQE':hqe,'NXJ':nxj}
    
    final_data = preprocess.preprocess_data(data)
    scaled_data = scaler.transform([final_data])
    prediction = int(model.predict(scaled_data)[0])
    if prediction == 0:
        prediction = 'Target'
    else :
        prediction = 'Not Target'
    
    # return str(round(prediction))
    return render_template('prediction.html', target = str(prediction))
        
        

if __name__ == '__main__' :
    app.run(debug = True)
    