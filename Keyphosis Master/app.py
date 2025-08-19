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
        age = request.form['age']
        number = request.form['number']
        start = request.form['start']
        
    data = {'Age' : age, 'Number' : number, 'Start' : start}
    
    final_data = preprocess.preprocess_data(data)
    scaled_data = scaler.transform([final_data])
    prediction = int(model.predict(scaled_data)[0])
    if prediction == 0:
        prediction = 'Absent'
    else :
        prediction = 'Present'
    
    # return str(round(prediction))
    return render_template('prediction.html', keyphosis = str(prediction))
        
        

if __name__ == '__main__' :
    app.run(debug = True)
    