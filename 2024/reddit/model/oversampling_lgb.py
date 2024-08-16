import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.datasets import load_breast_cancer

# Load dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Create train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Initialize LightGBM model
model = lgb.LGBMClassifier(is_unbalance=True, n_estimators=100, random_state=42)

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]

# Evaluate
print(classification_report(y_test, y_pred))
print(f"AUC: {roc_auc_score(y_test, y_pred_prob):.4f}"

####
# SMOTE oversampling
####
from imblearn.over_sampling import SMOTE

# Apply SMOTE to the training data
smote = SMote(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Initialize LightGBM model
model_resampled = lgb.LGBMClassifier(n_estimators=100, random_state=42)

# Train model on resampled data
model_resampled.fit(X_train_resampled, y_train_resampled)

# Predictions
y_pred_resampled = model_resampled.predict(X_test)
y_pred_prob_resampled = model_resampled.predict_proba(X_test)[:, 1]

# Evaluate
print(classification_report(y_test, y_pred_resampled))
print(f"AUC: {roc_auc_score(y_test, y_pred_prob_resampled):.4f}")
