# CARVISTA — Used Car Price Intelligence & Prediction

CARVISTA is a machine learning project that predicts the selling price of a used car based on vehicle characteristics such as brand, car model, manufacturing year, kilometers driven, fuel type, seller type, transmission, and ownership history.

The project combines data preprocessing, exploratory analysis, machine learning, model evaluation, and an interactive Streamlit application into one end-to-end workflow.

---

## Project Objective

The objective of CARVISTA is to build a regression model capable of estimating the selling price of a used car from its available features.

The project focuses on:

- Data inspection and preprocessing
- Feature engineering
- Handling missing values safely
- Encoding categorical variables
- Training a machine learning regression model
- Cross-validation and test-set evaluation
- Feature importance analysis
- Interactive price prediction through Streamlit

---

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- Git & Git LFS

---

## Machine Learning Model

CARVISTA uses a **Random Forest Regressor** inside a Scikit-learn pipeline.

The preprocessing pipeline includes:

- Median imputation for numerical features
- Most-frequent imputation for categorical features
- Standard scaling for numerical features
- One-hot encoding for categorical features
- Unknown-category handling during prediction

The model uses:

```text
RandomForestRegressor
n_estimators = 300
random_state = 42