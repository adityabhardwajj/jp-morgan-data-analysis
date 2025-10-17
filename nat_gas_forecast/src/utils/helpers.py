def calculate_moving_average(data, window_size):
    """Calculate the moving average of a given data series."""
    return data.rolling(window=window_size).mean()

def calculate_daily_returns(data):
    """Calculate daily returns from a price series."""
    return data.pct_change()

def split_data(data, train_size=0.8):
    """Split the dataset into training and testing sets."""
    train_length = int(len(data) * train_size)
    return data[:train_length], data[train_length:]

def prepare_features(data, lookback=30):
    """Prepare features for model training."""
    features = pd.DataFrame()
    target = data['Close'].shift(-1)  # Next day's price

    for i in range(lookback):
        features[f'price_lag_{i+1}'] = data['Close'].shift(i)

    features['MA5'] = data['Close'].rolling(window=5).mean()
    features['MA20'] = data['Close'].rolling(window=20).mean()
    features['MA50'] = data['Close'].rolling(window=50).mean()

    features = features.dropna()
    target = target[features.index]

    return features, target