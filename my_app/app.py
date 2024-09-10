from fastapi import FastAPI, Query
from controller.LoadModel import LoadModel
from controller.GetPredictions import GetPredictions

app = FastAPI()

model_path = "model/crop_production_prediction_model.pkl"

model = LoadModel(model_path)

@app.get("/Crop Production Prediction")
def crop_production_prediction(state_name: int = Query(..., ge=0, le=33), 
                               district_name: int = Query(..., ge=0, le=643),
                               crop_year: int = Query(..., ge=1997, le=2015),
                               season: int = Query(..., ge=0, le=7), 
                               crop: int = Query(..., ge=0, le=125),
                               area: float = Query(..., ge=0.04, le=8580100.0)):
    
    inputs = [state_name, district_name, crop_year, season, crop, area]

    predictions = GetPredictions(model, inputs)

    return f"The Predicted Production is {predictions[0]:.2f}"