# Building Permits Accepted Value Prediction (Machine Learning)

## Project Overview
This project builds a Machine Learning model to predict the **accepted permit value for building permits** using historical permit data.

The goal is to demonstrate a complete **end-to-end data science workflow**, including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Training
- Model Evaluation
- Feature Importance Analysis
- Model Deployment Preparation

---

## Dataset

The dataset used in this project contains historical building permit records used to train the machine learning model.

Due to GitHub file size limitations, the dataset is hosted externally.

Download the dataset here:

https://www.dropbox.com/scl/fi/8pv6zzpib9rgqqrnipwur/cleaned_building_permits_2005_2025.csv?rlkey=hr1scvzh9j1gu9y0md531ir6i&dl=1


## Trained Model

The trained Random Forest model is stored externally due to GitHub file size limitations.

Download the trained model here:

https://www.dropbox.com/scl/fi/nl2q81qdvu0jw64iw3b74/best_random_forest_model.pkl?rlkey=ad19f4q9akc8805y6oc2xo5rk&dl=1

---

# Project Workflow

## 1 Data Cleaning
The dataset was cleaned by:

- Removing duplicates
- Handling missing values
- Standardizing column names
- Converting data types
- Handling outliers

---

## 2 Exploratory Data Analysis (EDA)

EDA was performed to understand:

- Data distributions
- Relationships between variables
- Correlations between features
- Outlier behaviour

Visualizations used:

- Histograms
- Boxplots
- Scatter plots
- Correlation heatmaps

---

## 3 Feature Engineering

Additional features were created to improve model performance.

Examples include:

- Encoded categorical variables
- Derived numerical features
- Scaled inputs

---

## 4 Machine Learning Models

Several regression models were trained and compared.

Models tested:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

---

## 5 Model Evaluation

Models were evaluated using:

- Mean Squared Error (MSE)
- R² Score

The **Random Forest Regressor** produced the best performance.

---

## 6 Feature Importance

Feature importance analysis was performed using the Random Forest model to identify the variables that most influence permit value predictions.

---

# Tools & Technologies

Python libraries used:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- joblib

Development tools:

- Jupyter Notebook
- Git
- GitHub

---

# Repository Contents

```
Building-Permits-Accepted-Value-Prediction-ML
│
├── myfirstnotebook22.ipynb
├── requirements.txt
└── README.md
```

---

# Author

**Martin Ude**  
Data Science & Machine Learning Portfolio  
GitHub: https://github.com/martystats

---
