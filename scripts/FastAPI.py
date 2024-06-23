from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
import joblib
import os

app = FastAPI()

@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url='/docs', status_code=status.HTTP_302_FOUND)

@app.get("/predict/")
def predict(tv: float, radio: float, newspaper: float):
    model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models/advertising_model.pkl'))
    
    if not os.path.exists(model_path):
        raise HTTPException(status_code=404, detail="Model file not found")
    
    model = joblib.load(model_path)
    prediction = model.predict([[tv, radio, newspaper]])
    return {"prediction": prediction[0]}
