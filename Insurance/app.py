import joblib
from flask import Flask, render_template, request
import pre
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
        bmi = request.form['bmi']
        sex = request.form['sex']
        child = request.form['child']
        smoke = request.form['smoke']
        region = request.form['region']
        
    data = {'Age' : age, 'Body Mass Index' : bmi, 'Sex' : sex, 
            'Children' : child, 'Smoker' : smoke, 'Region' : region}
    
    final_data = pre.preprocess_data(data)
    scaled_data = scaler.transform([final_data])
    scaled_data = scaled_data[0][:10]
    scaled_data = scaled_data.reshape(1, -1)
    prediction = int(model.predict(scaled_data)[0])
    
    # return str(round(prediction))
    return render_template('prediction.html', charge = str(prediction))
        
        

if __name__ == '__main__' :
    app.run(debug = True)
    