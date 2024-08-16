
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import lightgbm as lgb
from sklearn.datasets import load_breast_cancer  # Example dataset

# Load your dataset (using a sample dataset for this example)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Preprocess your data if needed (e.g., scaling, encoding)
# This example data does not need preprocessing

# Define the models
log_reg = LogisticRegression(max_iter=1000)
rf = RandomForestClassifier(n_estimators=100)
lgbm = lgb.LGBMClassifier(n_estimators=100)

# List of models
models = [('Logistic Regression', log_reg), 
          ('Random Forest', rf), 
          ('LightGBM', lgbm)]

# Define the cross-validation method
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Perform cross-validation and collect results
results = {}
for model_name, model in models:
    cv_results = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
    results[model_name] = cv_results
    print(f"{model_name}: Mean Accuracy = {cv_results.mean():.4f}, STD = {cv_results.std():.4f}")

# Compare results
for model_name in results:
    print(f"{model_name}: {results[model_name]}")


