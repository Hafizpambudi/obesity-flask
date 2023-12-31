from flask import Flask, request, jsonify
import  pickle
import numpy as np
import pandas as pd

model = pickle.load(open('modelml.pkl','rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return "hello world"


@app.route('/predict', methods=['POST'])
def predict():
    Gender = request.form.get('Gender')
    Age = request.form.get('Age')
    Height = request.form.get('Height')
    Weight = request.form.get('Weight')
    FAVC = request.form.get('FAVC')
    FCVC = request.form.get('FCVC')
    NCP = request.form.get('NCP')
    CAEC = request.form.get('CAEC')
    SMOKE = request.form.get('SMOKE')
    CH2O = request.form.get('CH2O')
    SCC = request.form.get('SCC')
    FAF = request.form.get('FAF')
    TUE = request.form.get('TUE')
    CALC = request.form.get('CALC')
    MTRANS = request.form.get('MTRANS')


    input_query = np.array([[Gender,Age,Height,Weight,FAVC,FCVC,NCP,CAEC,SMOKE,CH2O,SCC,FAF,TUE,CALC,MTRANS]])

    x_pred = pd.DataFrame(input_query,columns=[[Gender,Age,Height,Weight,FAVC,FCVC,NCP,CAEC,SMOKE,CH2O,SCC,FAF,TUE,CALC,MTRANS]])
    results = model.predict(x_pred)[0]

    return jsonify({'klasifikasi':results})


if __name__ == '__main__':
    app.run(debug=True)
