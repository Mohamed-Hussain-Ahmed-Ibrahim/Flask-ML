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
        fare = request.form['fare']
        pclass = request.form['pclass']
        sex = request.form['sex']
        sibsp = request.form['sibsp']
        parch = request.form['parch']
        embark = request.form['embark']
        
    data = {'Age' : age, 'Fare' : fare, 'PClass' : pclass, 
            'Sex' : sex, 'SibSp' : sibsp, 'Parch' : parch, 'Embarked' : embark}
    
    final_data = preprocess.preprocess_data(data)
    scaled_data = scaler.transform([final_data])
    #scaled_data = scaled_data[0][:10]
    #scaled_data = scaled_data.reshape(-1,1)
    prediction = int(model.predict(scaled_data)[0])
    if prediction == 1:
        prediction = 'Survived'
    else :
        prediction = 'Not Survived'
    # return str(round(prediction))
    return render_template('prediction.html',  surv = str(prediction))
        
        

if __name__ == '__main__' :
    app.run(debug = True)
    