from src.preprocessing import load_data, preprocess_data, split_features_target
from src.train import load_model
import pandas as pd


data = load_data(r"independent work\Level 2 project\WHO life expectancy  (regression)\Data\Data.csv")
data = preprocess_data(data)
sample_data = data.sample(5,random_state=1)

x_sample, y_sample = split_features_target(sample_data)

model = load_model(r".\independent work\Level 2 project\WHO life expectancy  (regression)\models\life_expectancy_catboost.cbm")

y_hat = model.predict(x_sample)

results = pd.DataFrame({
    "Actual Life Expectancy": y_sample.values,
    "Predicted Life Expectancy": y_hat
})

results["Error"] = (
    results["Actual Life Expectancy"]
    - results["Predicted Life Expectancy"]
).abs()

print(results)

