from flask import Flask, render_template, request

from predict import predict_price


# Create Flask Application
app = Flask(__name__)


# Home Page
@app.route("/")
def home():

    return render_template("index.html")


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Collect User Inputs
        year = int(request.form["Year"])
        km_driven = float(request.form["kmDriven"])

        # Feature Engineering (same as training)
        km_per_year = km_driven / max((2026 - year), 1)

        data = {

            "Brand": request.form["Brand"],
            "model": request.form["model"],
            "Year": year,
            "kmDriven": km_driven,
            "km_per_year": km_per_year,
            "Transmission": request.form["Transmission"],
            "Owner": request.form["Owner"],
            "FuelType": request.form["FuelType"]

        }

        # Make Prediction
        result = predict_price(data)

        # Market Segment Color
        segment = result["segment"]

        segment_color = {

            "Budget Car": "green",

            "Economy Car": "#0077b6",

            "Mid-Range Car": "orange",

            "Premium Car": "purple",

            "Luxury Car": "crimson"

        }.get(segment, "#0077b6")

        return render_template(

            "index.html",

            predicted_price=result["price"],

            lower_price=result["lower_price"],

            upper_price=result["upper_price"],

            segment=segment,

            segment_color=segment_color,

            pricing_insight=result["recommendation"],

            brand=result["brand"],
                
            model=result["model"],
                
            year=result["year"],
                
            fuel=result["fuel"],
                
            owner=result["owner"],
                
            transmission=result["transmission"],
                
            km=result["km"]
            
            )
    

    except Exception as e:

        import traceback
        traceback.print_exc()

        return render_template(

            "index.html",

            predicted_price="Prediction Failed!",

            lower_price="-",

            upper_price="-",

            segment="-",

            segment_color="#0077b6",

            recommendation=str(e),
            
            )


# Run Flask
if __name__ == "__main__":

    app.run(debug=True)