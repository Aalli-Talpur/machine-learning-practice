# Import reusable project functions
from src.preprocessing import load_data, clean_col_names, drop_missing_target, drop_selected_features, preprocess_data, split_features_target
from src.train import build_model, train_model, save_model, load_model 
from src.evaluate import evaluate_model


# Load and preprocess dataset
data = load_data(r"independent work\Level 2 project\WHO life expectancy  (regression)\Data\Data.csv")
data = preprocess_data(data)


# Create time based training and test sets
train_data = data[data["Year"] <= 2010]
test_data = data[data["Year"] > 2010]


# Separate features and target
x_train, y_train = split_features_target(train_data)
x_test, y_test = split_features_target(test_data)


# Build and train final CatBoost model
model = build_model()
model = train_model(model, x_train, y_train)


# Generate predictions
y_pred = model.predict(x_test)


# Evaluate model performance
r2, mae, mse, rmse = evaluate_model(y_test, y_pred)


# Save trained model
save_model(model, r".\independent work\Level 2 project\WHO life expectancy  (regression)\models\life_expectancy_catboost.cbm")
