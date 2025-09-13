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

        # Arrange features same as training
        features = np.array([[year, month, day, hour, dayofweek, is_weekend]])

        # Make prediction
        prediction = model.predict(features)[0]

        return render_template(
            "result.html",
            year=year,
            month=month,
            day=day,
            hour=hour,
            prediction=f"{prediction:,.2f} MW"
        )

    except Exception as e:
        return render_template("result.html", prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
