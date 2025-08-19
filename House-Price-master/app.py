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
        qual = request.form['qual']
        cond = request.form['cond']
        sf1 = request.form['sf1']
        area = request.form['area']
        bed = request.form['bed']
        garage = request.form['garage']
        
    data = {'qual' : qual, 'cond' : cond, 'sf1' : sf1, 
            'area' : area, 'bed' : bed, 'garage' : garage}
    
    final_data = preprocess.preprocess(data)
    scaled_data = scaler.transform([final_data])
   # scaled_data = scaled_data[0][:10]
    prediction = int(model.predict(scaled_data)[0])
    
    # return str(round(prediction))
    return render_template('prediction.html', house_price = str(prediction))
        
        

if __name__ == '__main__' :
    app.run(debug = True)
    