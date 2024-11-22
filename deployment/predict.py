import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
from flask import Flask, request, jsonify

model = joblib.load(open('best_model.pkl','rb'))

app = Flask('Cirrhosis')

@app.route('/predict', methods=['POST'])
def predict():
    person_data = request.get_json()
   
    x=pd.DataFrame([person_data])

    cat=x.select_dtypes(include=[object])

    for i in cat:
        x[i]=LabelEncoder().fit_transform(cat[i])

    test=x.values.reshape(1, -1)

    prediction = model.predict(test)[0]
    
    status=None
    if prediction == 0:
        status = "D (Death)"

    elif prediction==1:
        status = "C (Censored)"

    else:
        status = "CL (censored due to liver transplantation)"
    
    result={
        int(prediction):(status)
    }
    
    return jsonify([result])

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 9696)
