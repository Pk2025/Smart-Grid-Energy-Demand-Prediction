# Smart-Grid-Energy-Demand-Prediction

Internship Projet Currently working on


##  Download the Trained Random Forest Model

The model is too large for GitHub. Download it directly using the link below:

**Direct download**:  
https://drive.google.com/uc?export=download&id=19jnFeUVsKuPwFCHxlANWWRq0xKZjiMtS

THIS IS THE random_forest_model.pkl file which is used in the project but can't upload as it is to big

**Command-line (recommended)**:
```bash
pip install gdown
gdown --id 19jnFeUVsKuPwFCHxlANWWRq0xKZjiMtS -O random_forest_model.zip


Overview

The Smart Grid Energy Demand Prediction project leverages AI/ML techniques to forecast energy demand in a smart grid system. Accurate demand prediction helps utility companies optimize energy distribution, reduce wastage, prevent outages, and lower operational costs. This project uses the Random Forest algorithm to predict energy consumption based on historical and environmental data.

Features

Predict short-term and long-term energy demand in smart grids.

Utilizes Random Forest Regressor for accurate prediction.

Handles large datasets efficiently with feature engineering and preprocessing.

Provides insights on energy usage patterns.

Supports visualization of predicted vs actual demand for analysis.

Dataset

Historical energy consumption data, weather data, and time-related features.

Features may include:

Date and time

Temperature, humidity, and other environmental variables

Historical energy consumption

Holidays and weekends

Dataset sources: Kaggle Smart Grid Datasets
 or other public energy datasets.

Technologies Used

Programming Language: Python 3.x

Libraries:

pandas, numpy — Data manipulation and preprocessing

scikit-learn — Random Forest and model evaluation

matplotlib, seaborn — Data visualization

joblib — Saving and loading trained models

Installation

Clone the repository:

git clone https://github.com/<your-username>/smart-grid-energy-prediction.git
cd smart-grid-energy-prediction


Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt

Usage

Place your dataset in the data/ folder.

Update the dataset path in the code if needed.

Run the model training script:

python train_model.py


Run the prediction script:

python predict.py


Visualize results:

python visualize.py

Project Structure
smart-grid-energy-prediction/
│
├── data/                  # Dataset files
├── notebooks/             # Jupyter notebooks for EDA and experiments
├── models/                # Saved trained models
├── train_model.py         # Script to train the Random Forest model
├── predict.py             # Script to make predictions
├── visualize.py           # Script to visualize predictions
├── requirements.txt       # Python dependencies
└── README.md

Model Evaluation

Metrics used:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

R² Score

The model is evaluated on a test set to ensure predictive accuracy.

Future Enhancements

Implement additional algorithms like XGBoost, LSTM, or Gradient Boosting for improved accuracy.

Integrate real-time data feeds for live prediction.

Deploy as a web application or API for energy providers.

Explore seasonal and regional energy demand patterns.

References

Kaggle: Smart Grid Datasets

Scikit-learn Documentation: Random Forest

Energy Demand Forecasting Research Papers

License

This project is licensed under the MIT License — see the LICENSE
 file for details.
