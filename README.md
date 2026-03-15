# Building Permits Accepted Value Prediction (Machine Learning)

## Project Overview

In this project, I developed a machine learning model to predict the **accepted value of building permits** using historical permit data.  
The objective of the project is to identify important factors that influence permit approval values and build a predictive system capable of estimating the likely accepted value of new permits.

The workflow follows a complete data science pipeline including:

• Data Cleaning  
• Exploratory Data Analysis (EDA)  
• Feature Engineering  
• Model Training and Evaluation  
• Model Persistence  
• Deployment Readiness using Streamlit

This project demonstrates a reproducible and scalable machine learning workflow suitable for real-world predictive analytics.

---

## Dataset

The dataset contains historical records of building permits including information such as permit type, construction category, and estimated work value.

Due to GitHub file size limitations, the dataset is hosted externally.

Dataset Download Link:

Dropbox Dataset Link  
https://www.dropbox.com/YOUR_DATASET_LINK_HERE

---

## Data Cleaning and Preprocessing

The dataset was cleaned and prepared to ensure high quality inputs for the machine learning models.

Key preprocessing steps included:

• Handling missing values  
• Removing duplicate records  
• Standardizing column names  
• Converting date columns to datetime format  
• Engineering new features from temporal attributes  
• Outlier handling using capping techniques  
• Preparing numerical and categorical features for modeling

These steps ensure the dataset is consistent and suitable for predictive modeling.

---

## Exploratory Data Analysis (EDA)

Exploratory analysis was performed to better understand the dataset and identify patterns that may influence permit value predictions.

Key analyses included:

• Distribution analysis of numerical variables  
• Frequency analysis of categorical variables  
• Correlation analysis between features  
• Identification of high-impact variables

EDA helped reveal relationships between permit characteristics and their corresponding accepted values.

---

## Feature Engineering

Additional features were created to improve model performance.

Feature engineering steps included:

• Extracting temporal features from permit issue dates  
• Creating derived variables from work value indicators  
• Preparing categorical variables for model compatibility  
• Structuring the dataset for machine learning training

These engineered features improved the predictive capability of the models.

---

## Machine Learning Models

Multiple regression models were evaluated during this project.

Models explored included:

• Linear Regression (Baseline Model)  
• Random Forest Regressor  
• Gradient Boosting Regressor

After model comparison, **Random Forest Regressor** provided the best predictive performance and was selected as the final model.

---

## Model Performance

The final Random Forest model demonstrated strong predictive capability.

Evaluation metrics included:

• R² Score  
• Mean Squared Error (MSE)  
• Feature Importance Analysis

Feature importance analysis showed that **estimated value of work and permit classification features** were the most influential predictors in the model.

---

## Model Persistence

To enable reproducibility and reuse, the trained machine learning model was saved using Python serialization.

Saved model file:

permit_demo_model.pkl

This allows the model to be loaded later for predictions without retraining.

---

## Repository Structure

Building-Permits-Accepted-Value-Prediction-ML/

README.md → Project documentation  
myfirstnotebook22.ipynb → Full analysis and model development notebook  
permit_demo_model.pkl → Trained machine learning model  
app.py → Streamlit application for prediction interface  
requirements.txt → Python dependencies required to run the project

---

## Running the Project

To run this project locally, install the required dependencies.

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

This will launch a local web interface where new permit data can be entered for prediction.

---

## Technologies Used

Python  
Pandas  
NumPy  
Scikit-Learn  
Matplotlib  
Seaborn  
Streamlit

---

## Author

Martin ude  
Data Science and Machine Learning Portfolio Project

This repository demonstrates a complete **end-to-end machine learning workflow**, from raw data processing to predictive modeling and deployment readiness.
