## Libraries required
import pandas as pd
import pickle

from flask import Flask
from flask import request
from flask import jsonify

## Inputs
model_name = 'model.bin'

with open(model_name, 'rb') as f_in: # very important to use 'rb' here, it means read-binary 
    mms, pca, lrc, LRpca_Params = pickle.load(f_in)

app = Flask('predict')

@app.route('/predict', methods=['POST'])

# Predict functions
def predict():
    cell = request.get_json() #Converts the JSON into a dictionary

    X = transform_data([cell])
    Diagnosis, y_pred = predict_from_model(X)

    text = f"Cell Diagnosis: {Diagnosis}\np Malignant: {y_pred}"
    print(text)
    result = {
        'Cell Diagnosis': Diagnosis,
        'Malignant Probability': float(y_pred)
    }
    return jsonify(result)

## Nested functions (Core logic)
def transform_data(cell):
    df_X = pd.DataFrame(cell, index=[0])
    iX = mms.transform(df_X)
    X = pca.transform(iX)
    return X

def predict_from_model(X):
    y_pred = lrc.predict_proba(X)[0,1]
    if y_pred >= 0.5:
        Diagnosis = "Malignant"
    else:
        Diagnosis = "Benign"
    return Diagnosis, y_pred

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)