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
        temp = request.form['temp']
        humidity = request.form['Humidity']
        hour = request.form['hour']
        month = request.form['month']
        season = request.form['season']
        weather = request.form['weather']
        day = request.form['day']
        
    data = {'temperature' : temp, 'humidity' : humidity, 'hour' : hour, 
            'month' : month, 'season' : season, 'weather' : weather, 'day' : day}
    
    final_data = preprocess.preprocess_data(data)
    scaled_data = scaler.transform([final_data])
    prediction = int(model.predict(scaled_data)[0])
    
    # return str(round(prediction))
    return render_template('prediction.html', bikes_count = str(prediction))
        
        

if __name__ == '__main__' :
    app.run(debug = True)
    