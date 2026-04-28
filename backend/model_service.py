import numpy as np
import joblib
from tensorflow.keras.models import load_model
from feature_engineering import create_features

# Load models once
scaler = joblib.load(r"models/scaler.pkl")
lgbm = joblib.load(r"models/lgbm.pkl")
stack_model = joblib.load(r"models/stack_model.pkl")
dl_model = load_model(r"models/dl_model.keras")


def predict_price(request):

    features = create_features(request)

    X = np.asarray(features).reshape(1, -1)

    X_scaled = scaler.transform(X)

    pred_lgbm = lgbm.predict(X_scaled)[0]

    pred_dl = dl_model.predict(X_scaled)[0][0]

    stack_input = np.array([[pred_lgbm, pred_dl]])

    final_pred = stack_model.predict(stack_input)[0]

    return float(pred_lgbm), X_scaled