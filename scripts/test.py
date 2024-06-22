import prediction
import  pandas as pd
data ={'TV':230.1 , 
       'Radio':37.8, 
        'Newspaper':'69.2' }
df = pd.DataFrame([data])
prediction =prediction.predict_model(df)
print(prediction)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Return the received data for testing purposes
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
