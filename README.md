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

# Dataset
The dataset contains historical **building permit records**, including:

- Permit type
- Work category
- Location features
- Property attributes
- Permit issue year
- Permit values

These variables are used to predict the **accepted permit value**.

Due to GitHub file size limitations, the full dataset is not stored in this repository.

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
