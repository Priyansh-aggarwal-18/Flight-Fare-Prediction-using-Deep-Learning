import shap
import joblib
import numpy as np

lgbm = joblib.load("models/lgbm.pkl")

explainer = shap.TreeExplainer(lgbm)

feature_names = [
    "total_stops",
    "journey_day",
    "journey_month",
    "dep_hour",
    "dep_min"
]


def explain_prediction(X_scaled):

    shap_values = explainer.shap_values(X_scaled)

    shap_values = shap_values[0]

    # Pair feature with importance
    feature_importance = list(zip(feature_names, shap_values))

    # Sort by impact
    feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)

    reasons = []

    for feature, value in feature_importance[:3]:

        if feature == "total_stops":
            if value > 0:
                reasons.append("More stops increased the flight price")
            else:
                reasons.append("Direct route reduced the price")

        elif feature == "journey_day":
            reasons.append("Travel date has high demand")

        elif feature == "dep_hour":
            reasons.append("Departure time affects pricing demand")

        elif feature == "journey_month":
            reasons.append("Seasonal demand influences price")

    if not reasons:
        reasons.append("Price determined by route demand")

    return reasons