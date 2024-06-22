import joblib
import os 
model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models/advertising_model.pkl'))
model = joblib.load(model_path)

def predict_model(features):
    pred= model.predict(features)
    return pred
