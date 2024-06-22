from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os
app = Flask(__name__)
model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models/advertising_model.pkl'))
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Ensure 'Newspaper' is a float
    data['Newspaper'] = float(data['Newspaper'])
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame([data])
    
    # Make predictions
    prediction = model.predict(df)
    
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
