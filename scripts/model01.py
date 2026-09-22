from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

base_Dir = Path(__file__).resolve().parent.parent
csv_path = base_Dir / "data" / "processed" / "rawdataCA_cleaned.csv"

df = pd.read_csv(csv_path)
df = df[df['damage'] != 'Inaccessible'].copy()

structural_cols = [
    'roof_construction', 'eaves', 'vent_screen', 'exterior_siding', 'window_pane',
    'deck_porch_on_grade', 'deck_porch_elevated', 'patio_cover_carport',
    'fence_attached_to_structure'
]
df[structural_cols] = df[structural_cols].fillna('Not Assessed')

feature_cols = structural_cols + ['structure_type', 'structure_category']

X = pd.get_dummies(df[feature_cols])
y = df['damage']


#Randon Forest Model 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=200, random_state=42, n_jobs=-1,
    class_weight='balanced'
    )
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

#confusion matrix
labels = ['No Damage', 'Affected (>0-10%)', 'Minor (10-25%)', 'Major (25-50%)', 'Destroyed (>50%)']
cm = confusion_matrix(y_test, y_pred, labels=labels)
cm_df = pd.DataFrame(cm, index=labels, columns=labels)
print(cm_df)

#Expected value approach
import numpy as np

damage_map = {
    'No Damage': 0.0,
    'Affected (>0-10%)': 5.0,
    'Minor (10-25%)': 17.5,
    'Major (25-50%)': 37.5,
    'Destroyed (>50%)': 75.0
}

# Get probability of each class for every test-set row
probs = model.predict_proba(X_test)          # shape: (n_rows, 5)
class_order = model.classes_                  # order of columns in `probs`
midpoints = np.array([damage_map[c] for c in class_order])

expected_damage = probs @ midpoints           # weighted average per row

# Compare against the TRUE numeric damage % for each row
true_damage = y_test.map(damage_map)

mae = np.mean(np.abs(expected_damage - true_damage))
print(f"Mean Absolute Error: {mae:.2f} percentage points")

# Eyeball a few individual predictions
comparison = pd.DataFrame({
    'true_category': y_test.values,
    'true_damage_pct': true_damage.values,
    'predicted_damage_pct': expected_damage.round(1)
})
print(comparison.sample(10, random_state=1))

comparison['abs_error'] = (comparison['predicted_damage_pct'] - comparison['true_damage_pct']).abs()
error_by_category = comparison.groupby('true_category')['abs_error'].mean()
print(error_by_category)


#Switches to gradient bosting model
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import pandas as pd

sample_weights = compute_sample_weight(class_weight='balanced', y=y_train)

gb_model = HistGradientBoostingClassifier(
    max_iter=200, random_state=42
)
gb_model.fit(X_train, y_train, sample_weight=sample_weights)

y_pred_gb = gb_model.predict(X_test)
print(classification_report(y_test, y_pred_gb))

labels = ['No Damage', 'Affected (>0-10%)', 'Minor (10-25%)', 'Major (25-50%)', 'Destroyed (>50%)']
cm_gb = confusion_matrix(y_test, y_pred_gb, labels=labels)
print(pd.DataFrame(cm_gb, index=labels, columns=labels))

# Expected-value scoring, same as before
probs_gb = gb_model.predict_proba(X_test)
class_order_gb = gb_model.classes_
midpoints = np.array([damage_map[c] for c in class_order_gb])
expected_damage_gb = probs_gb @ midpoints
true_damage = y_test.map(damage_map)
mae_gb = np.mean(np.abs(expected_damage_gb - true_damage))
print(f"Gradient Boosting MAE: {mae_gb:.2f} percentage points")


# runs gradient boosting model with no class balancing (08/14 best model)
gb_model_plain = HistGradientBoostingClassifier(max_iter=200, random_state=42)
gb_model_plain.fit(X_train, y_train)  # no sample_weight this time

probs_plain = gb_model_plain.predict_proba(X_test)
class_order_plain = gb_model_plain.classes_
midpoints = np.array([damage_map[c] for c in class_order_plain])
expected_damage_plain = probs_plain @ midpoints
mae_plain = np.mean(np.abs(expected_damage_plain - true_damage))
print(f"Unweighted Gradient Boosting MAE: {mae_plain:.2f} percentage points")

#Hyperparameter based model
from sklearn.model_selection import RandomizedSearchCV
import numpy as np

def expected_damage_mae_scorer(estimator, X, y_true):
    probs = estimator.predict_proba(X)
    class_order = estimator.classes_
    midpoints = np.array([damage_map[c] for c in class_order])
    expected = probs @ midpoints
    true_vals = y_true.map(damage_map)
    mae = np.mean(np.abs(expected - true_vals))
    return -mae   # negative: sklearn always maximizes a score, so "less error" must mean "higher score"

param_dist = {
    'max_iter': [100, 200, 300],
    'learning_rate': [0.05, 0.1, 0.2],
    'max_depth': [None, 5, 10],
    'max_leaf_nodes': [15, 31, 63],
    'min_samples_leaf': [10, 20, 50],
}

search = RandomizedSearchCV(
    estimator=HistGradientBoostingClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=15,
    scoring=expected_damage_mae_scorer,
    cv=3,
    random_state=42,
    n_jobs=-1,
    verbose=2
)

search.fit(X_train, y_train)

print("Best params:", search.best_params_)
print("Best CV score (neg MAE):", search.best_score_)

best_model = search.best_estimator_
probs_best = best_model.predict_proba(X_test)
class_order_best = best_model.classes_
midpoints = np.array([damage_map[c] for c in class_order_best])
expected_damage_best = probs_best @ midpoints
mae_best = np.mean(np.abs(expected_damage_best - true_damage))
print(f"Tuned model test MAE: {mae_best:.2f} percentage points")