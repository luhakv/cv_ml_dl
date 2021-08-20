import numpy as np
import pickle

from flask import Flask, request

app = Flask(__name__)

with open('model.pkl', 'rb') as pkl_file:
    model_from_file = pickle.load(pkl_file)

@app.route('/predict')
def hello_func():
    value = request.args.get('value')
    value_to_predict = np.array([float(value)]).reshape(-1, 1)
    prediction = model_from_file.predict(value_to_predict)[0]
    return f'the result is {prediction}!'


if __name__ == '__main__':
    app.run('localhost', 5000)