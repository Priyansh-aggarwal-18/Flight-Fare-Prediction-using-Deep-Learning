from fastapi import FastAPI
from pydantic import BaseModel
from model_service import predict_price
from shap_explainer import explain_prediction
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(title="AI Flight Price Predictor")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FlightRequest(BaseModel):
    source: str
    destination: str
    stops: int
    date: str
    departure_time: str


@app.get("/")
def home():
    return {"message": "Flight Price Prediction API running"}


@app.post("/predict")
def predict_flight_price(request: FlightRequest):

    prediction, features_scaled = predict_price(request)

    explanation = explain_prediction(features_scaled)

    return {
        "predicted_price": prediction,
        "reason": explanation
    }