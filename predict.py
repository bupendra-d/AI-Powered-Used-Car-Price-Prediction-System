import os
import joblib
import numpy as np
import pandas as pd


# Load Saved Model & Preprocessor
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "artifacts",
    "model.pkl"
)

PREPROCESSOR_PATH = os.path.join(
    BASE_DIR,
    "artifacts",
    "preprocessor.pkl"
)

# Load Once
model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)

# Format Price Function
def format_price(price):

    if price >= 10000000:
        return f"₹ {price / 10000000:.2f} Crore"

    elif price >= 100000:
        return f"₹ {price / 100000:.2f} Lakh"

    else:
        return f"₹ {price:,}"


# Prediction Function
def predict_price(input_data):

    try:

        # Convert dictionary to DataFrame
        input_df = pd.DataFrame([input_data])

        # Apply preprocessing
        transformed_data = preprocessor.transform(input_df)

        # Predict (log scale)
        prediction_log = model.predict(transformed_data)[0]

        # Convert back to original price
        predicted_price = np.expm1(prediction_log)
        predicted_price = round(predicted_price)

        # Market Segment
        if predicted_price < 300000:
            segment = "Budget Car"

        elif predicted_price < 700000:
            segment = "Economy Car"

        elif predicted_price < 1500000:
            segment = "Mid-Range Car"

        elif predicted_price < 3000000:
            segment = "Premium Car"

        else:
            segment = "Luxury Car"

        # Estimated Price Range
        lower_price = round(predicted_price * 0.95)
        upper_price = round(predicted_price * 1.05)

        # Recommendation
        if segment == "Luxury Car":

            recommendation = (
                "Luxury vehicles often have greater price variation due "
                "to optional features, service history, and condition. "
                "A professional inspection is recommended before purchase."
            )

        elif segment == "Budget Car":

            recommendation = (
                "Budget vehicles are highly price-sensitive. Verify "
                "maintenance records and vehicle condition before making "
                "a buying decision."
            )

        else:

            recommendation = (
                "The predicted price represents a fair market estimate based on similar used vehicles."
                "Buyers can use this estimate during negotiations, while sellers may consider listing "
                "slightly above the predicted value depending on vehicle condition, "
                "maintenance history, and local demand."
            )

        return {

            "price": format_price(predicted_price),

            "lower_price": format_price(lower_price),

            "upper_price": format_price(upper_price),

            "segment": segment,

            "recommendation": recommendation,

            "brand": input_df["Brand"].iloc[0],

            "model": input_df["model"].iloc[0],

            "year": input_df["Year"].iloc[0],

            "fuel": input_df["FuelType"].iloc[0],

            "owner": input_df["Owner"].iloc[0],

            "transmission": input_df["Transmission"].iloc[0],

            "km": input_df["kmDriven"].iloc[0]

        }

    except Exception as e:

        raise Exception(f"Prediction Error: {e}")