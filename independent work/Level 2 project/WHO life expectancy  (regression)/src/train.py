from catboost import CatBoostRegressor

def build_model():
    model = CatBoostRegressor(iterations=200, learning_rate=0.1, depth=5, loss_function='RMSE', random_seed=1, verbose=0, cat_features=["Country", "Status"], allow_writing_files=False)
    return model

def train_model(model, x_train, y_train):
    model.fit(x_train, y_train)
    return model

def save_model(model, path):
    model.save_model(path)

def load_model(path):
    model = CatBoostRegressor()
    model.load_model(path)
    return model