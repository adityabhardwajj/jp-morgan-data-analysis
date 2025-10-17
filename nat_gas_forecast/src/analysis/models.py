def train_model(X_train, y_train):
    from sklearn.linear_model import RidgeCV
    
    model = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0])
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    import numpy as np
    
    y_pred = model.predict(X_test)
    mse = np.mean((y_test - y_pred) ** 2)
    rmse = np.sqrt(mse)
    mae = np.mean(np.abs(y_test - y_pred))
    
    return {
        'Root Mean Square Error': rmse,
        'Mean Absolute Error': mae
    }

def make_predictions(model, latest_data):
    return model.predict(latest_data)[0]