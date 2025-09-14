from flask import Flask, render_template, request
import joblib
import numpy as np

# Load trained Random Forest model
model = joblib.load("random_forest_model.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form inputs
        year = int(request.form["year"])
        month = int(request.form["month"])
        day = int(request.form["day"])
        hour = int(request.form["hour"])
        dayofweek = int(request.form["dayofweek"])
        is_weekend = int(request.form["is_weekend"])

        # ✅ Validation checks
        if not (2000 <= year <= 2100):
            return render_template("result.html", prediction="❌ Invalid Year. Enter between 2000–2100.")
        if not (1 <= month <= 12):
            return render_template("result.html", prediction="❌ Invalid Month. Enter between 1–12.")
        if not (1 <= day <= 31):
            return render_template("result.html", prediction="❌ Invalid Day. Enter between 1–31.")
        if not (0 <= hour <= 23):
            return render_template("result.html", prediction="❌ Invalid Hour. Enter between 0–23.")
        if not (0 <= dayofweek <= 6):
            return render_template("result.html", prediction="❌ Invalid Day of Week. Enter between 0–6.")
        if not (is_weekend in [0, 1]):
            return render_template("result.html", prediction="❌ Invalid Weekend Value. Use 0 or 1.")

        # Arrange features same as training
        features = np.array([[year, month, day, hour, dayofweek, is_weekend]])

        # Prediction
        prediction = model.predict(features)[0]

        return render_template(
            "result.html",
            year=year,
            month=month,
            day=day,
            hour=hour,
            prediction=f"⚡ Predicted Energy Demand: {prediction:,.2f} MW"
        )

    except Exception as e:
        return render_template("result.html", prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
