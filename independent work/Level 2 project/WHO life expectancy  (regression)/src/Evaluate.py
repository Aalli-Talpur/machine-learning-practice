from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def evaluate_model(y_true, y_pred):
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = mse ** 0.5
    
    return r2, mae, mse, rmse