# WHO Life Expectancy Regression

## Project Overview

This project predicts **Life Expectancy** using health, economic, demographic, and country-level features from the WHO Life Expectancy dataset.

The project was developed as a **Level 2 machine learning project**, moving beyond notebook-based experimentation into a structured workflow with reusable Python modules, proper validation, model comparison, feature selection, model persistence, and inference.

## Project Structure

```text
WHO life expectancy/
├── Data/
│   └── Data.csv
├── models/
│   └── life_expectancy_catboost.cbm
├── notebooks and experimentations/
│   ├── EDA.ipynb
│   └── Model Experimentation.ipynb
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── evaluate.py
├── main.py
├── predict.py
└── README.md
```

## Workflow

1. Load and clean the dataset
2. Remove rows with missing target values
3. Perform exploratory data analysis
4. Compare different validation strategies
5. Train and tune CatBoost and XGBoost
6. Select CatBoost as the final model
7. Analyse feature importance
8. Test low-importance feature removal
9. Remove selected weak features
10. Train and evaluate the reduced model
11. Save the trained model
12. Load the saved model and perform inference

## Validation Strategy

Several validation approaches were tested:

- Random train/test split
- Country-based group split
- Time-based split

The final workflow uses a **time-based split**:

- **Training data:** 2000–2010
- **Test data:** 2011–2015

This setup better represents the intended task of using historical observations to predict later observations.

## Final Model

The final model is a tuned `CatBoostRegressor`.

Main settings:

```python
iterations=200
learning_rate=0.1
depth=5
loss_function="RMSE"
random_seed=1
```

CatBoost was selected because it:

- handles categorical features natively
- handles numerical missing values natively
- avoids creating a large one-hot encoded feature set
- performed better overall than the tuned XGBoost model

## Final Performance

The reduced CatBoost model achieved approximately:

| Metric | Value |
|--------|-------|
| R²     | 0.926 |
| MAE    | 1.56 years |
| MSE    | 5.35  |

The reduced model performed very close to the full-feature model while using fewer features.

## Feature Selection

Feature importance analysis and removal experiments were used to simplify the final model.

The following features were removed:

- Population
- Hepatitis B
- Diphtheria

Their combined removal caused only a small reduction in predictive performance.

## Reusable Modules

### `preprocessing.py`

Handles:

- loading the dataset
- cleaning column names
- removing missing target rows
- removing selected features
- preprocessing the dataset
- separating features and target

### `train.py`

Handles:

- building the CatBoost model
- training the model
- saving the trained model
- loading the saved model

### `evaluate.py`

Calculates:

- R²
- MAE
- MSE
- RMSE

## Training Workflow

Run:

```bash
python main.py
```

This will:

- load and preprocess the dataset
- create the time-based split
- train the final CatBoost model
- generate predictions
- evaluate model performance
- save the trained model

## Prediction Workflow

Run:

```bash
python predict.py
```

This loads the saved CatBoost model and demonstrates inference by comparing predicted and actual Life Expectancy values on sample observations.

## Key Learning Outcomes

This project demonstrates:

- structured exploratory data analysis
- realistic missing data handling
- categorical feature handling
- multiple validation strategies
- model comparison
- hyperparameter tuning
- feature importance analysis
- feature removal experiments
- reusable Python modules
- model saving and loading
- inference using a persisted model

## Conclusion

The project progressed from exploratory notebook-based analysis to a reusable machine learning workflow.

CatBoost provided the strongest overall performance and allowed categorical features and numerical missing values to be handled without separate encoding or imputation pipelines.

Feature importance and removal experiments were used to simplify the model by removing Population, Hepatitis B, and Diphtheria while maintaining similar predictive performance.

The final result is a structured Level 2 regression project with reusable preprocessing, training, evaluation, model persistence, and inference workflows.