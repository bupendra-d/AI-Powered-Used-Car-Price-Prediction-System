# AI Powered Used Car Price Prediction System

An end-to-end Machine Learning project that predicts the resale price of used cars using historical market listings. The system leverages advanced regression techniques, feature engineering, and a Flask web application to provide real-time price predictions with business insights.



# Live Demo
Experience the deployed application here:

** Live Application:** : https://ai-powered-used-car-price-prediction.onrender.com

Note: This application is deployed on Render's free tier. If the app has been inactive for some time, the initial request may take 30–60 seconds to load while the server wakes up.



##  Project Overview

Pricing a used car is a challenging task because resale value depends on multiple interacting factors such as vehicle age, brand, model, fuel type, ownership history, transmission type, and kilometers driven.

This project builds an AI-powered price prediction system capable of estimating the fair market value of a used vehicle based on its characteristics.

The application is designed to assist:
-  Used car buyers
-  Dealerships
-  Online automobile marketplaces
-  Individual sellers

by providing data-driven price recommendations.



# Objectives
- Predict the resale price of used vehicles.
- Analyze factors influencing vehicle prices.
- Compare multiple regression algorithms.
- Optimize model performance using hyperparameter tuning.
- Deploy the trained model using Flask.
- Provide an interactive web interface for real-time predictions.


#  Dataset

**Source**

Used Car Dataset (Open Source)

Dataset Size
- Initial Records: **14,993**
- Final Records after cleaning: **13,982**

Features Used
- Brand
- Model
- Manufacturing Year
- Kilometers Driven
- Fuel Type
- Transmission
- Owner
- Posted Month
- Ask Price (Target)



#  Data Cleaning

The following preprocessing steps were performed:
- Removed duplicate records
- Converted data types
- Checked missing values
- Handled missing values in `kmDriven`
- Parsed posting date
- Extracted:
  - Posted Year
  - Posted Month
  - Month Name
- Standardized categorical values
- Removed unnecessary columns
- Verified data quality



# Exploratory Data Analysis (EDA)

Comprehensive exploratory analysis was performed to understand the dataset.

### Target Variable Analysis

- Distribution of AskPrice
- Histogram
- Boxplot
- Summary statistics
- Skewness
- Kurtosis
- Percentile analysis


### Numerical Feature Analysis

Analyzed
- Manufacturing Year
- Kilometers Driven

Performed
- Histograms
- Boxplots
- Distribution analysis
- Summary statistics
- Outlier detection


### Categorical Feature Analysis

Analyzed
- Brand
- Fuel Type
- Transmission
- Owner

Performed
- Count plots
- Frequency distributions
- Business interpretation


### Feature vs Target Analysis

Visualized relationships between
- Year vs AskPrice
- Brand vs AskPrice

using boxplots to understand price variation.



### Correlation Analysis
- Computed Pearson correlation among numerical variables to identify relationships with vehicle price.


### Outlier Analysis
- Detected outliers using boxplots.
- Instead of removing them, business reasoning was applied because luxury vehicles naturally represent genuine extreme values.


### Key Findings:

- **Most used cars are priced below ₹10 lakh**, with a highly right-skewed price distribution driven by a small number of premium and luxury vehicles.

- **Brand, Model and Manufacturing Year** are the strongest predictor of resale price, with newer vehicles consistently commanding higher prices due to lower depreciation.

- **Kilometers Driven shows a negative relationship with price**—higher mileage generally reduces resale value, although its impact is weaker than vehicle age.

- **The dataset reflects the real Indian used car market**, being dominated by Petrol/Diesel vehicles and mass-market brands such as Maruti Suzuki, Hyundai, Honda, and Toyota.

- **Extreme values represent genuine market behavior rather than data errors**, including luxury vehicles, high-mileage cars, and classic models, so they were retained for model training.




# Feature Engineering

Several new features were evaluated.

### Created Feature

**Kilometers Driven Per Year**


km_per_year = kmDriven / Vehicle Age
```

This captures annual vehicle usage instead of total mileage.

Additional engineered features were evaluated, and only meaningful predictors were retained.

Final Modeling Features
- Brand
- Model
- Year
- kmDriven
- km_per_year
- FuelType
- Transmission
- Owner



#  Machine Learning Pipeline

Target Variable
- y = log1p(AskPrice)
- A logarithmic transformation was applied to reduce target skewness.

Predictions are converted back using

expm1()

during inference.


## Data Preprocessing Pipeline

Numerical Features
- Median Imputation
- StandardScaler

Categorical Features
- Most Frequent Imputation
- One Hot Encoding

Implemented using
- Pipeline
- ColumnTransformer



#  Models Trained

The following regression algorithms were compared.
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Extra Trees Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

Evaluation Metrics
- MAE
- RMSE
- R² Score
- Adjusted R²
- Cross Validation R²
- Training Time



#  Hyperparameter Tuning

RandomizedSearchCV was used for optimization.

Tuned Models
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- XGBoost Regressor

The tuned models were compared against their baseline counterparts.



#  Final Model

Final Selected Model

**XGBoost Regressor**

Reasons
- Excellent generalization
- Robust performance
- Handles nonlinear relationships effectively
- Performs well on mixed numerical and categorical data



#  Model Evaluation

Evaluation included
- Actual vs Predicted Plot
- Residual Plot
- Absolute Error Distribution
- Feature Importance Analysis

These visualizations confirmed that the model performs reliably for the majority of vehicles while larger errors mainly occur for premium and luxury cars.



#  Feature Importance

Top Important Features
- Brand
- Model
- Fuel Type
- Transmission
- Manufacturing Year
- Kilometers Driven Per Year

The analysis demonstrates that both vehicle specifications and usage patterns significantly influence resale price.



#  Flask Web Application

A lightweight Flask application was developed for deployment.

Users provide
- Brand
- Model
- Manufacturing Year
- Kilometers Driven
- Fuel Type
- Transmission
- Owner

The application returns
- Estimated Market Price
- Expected Price Range
- Market Segment
- Pricing Insight
- Vehicle Summary



#  Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib

### Deployment
- Flask
- HTML
- CSS
- JavaScript
- Render



# Project Structure

AI Powered Used Car Price Prediction System
│   .gitignore
│   app.py
│   predict.py
|   images
│   Procfile
│   README.md
│   requirements.txt
│   runtime.txt
│       
├───artifacts
│       model.pkl
│       preprocessor.pkl
│       
├───datasets
│      feature_engineered_dataset.csv
│      used_cars_clean.csv
│      used_cars_dataset_v2.csv
│      
├───notebook
│      1-Data Inspection and Cleaning.ipynb
│      2-Exploratory Data Analysis (EDA).ipynb
│      3-Feature Engineering.ipynb
│      4-Model Building.ipynb
│      5-Brand Model Mapping.ipynb       
│           
├───static
│      brand_model.json
│      script.js
│      style.css
│      
├───templates
│       index.html       



#  Deployment

The project is deployed using **Render**.

Deployment includes
- Flask Backend
- XGBoost Model
- Saved Preprocessing Pipeline
- Dynamic Brand-Model Dropdown
- Responsive User Interface



#  Business Applications

The system can be used by
- Used Car Dealerships
- Online Vehicle Marketplaces
- Individual Buyers
- Individual Sellers
- Vehicle Valuation Platforms

to estimate fair market prices.



# Limitations

Although the model performs well, several real-world factors are unavailable in the dataset.

Examples include
- Vehicle condition
- Accident history
- Service records
- Insurance history
- Number of previous owners beyond first/second
- Registration state
- Color
- Variant/Trim
- Optional features
- Market demand by city
- Seasonal demand

These factors may influence the final selling price.



#  Future Improvements

Potential enhancements include
- Deep Learning based regression models
- LightGBM and CatBoost comparison
- Real-time web scraping of used car listings
- Explainable AI using SHAP
- REST API deployment
- Docker containerization
- Cloud deployment using AWS or Azure



# Author

**Bupendra Devegade**

BBA (Hons) – Business Analytics

Machine Learning | Data Science | AI

⭐ If you found this project useful, consider giving it a star!