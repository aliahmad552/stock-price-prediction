import numpy as np
import pandas as pd
import yfinance as yf
import joblib
from tensorflow.keras.models import load_model

# =========================================================
# 1️⃣ Load Model & Scaler
# =========================================================
def load_trained_model(model_path, scaler_path):
    """
    Loads the trained GRU/LSTM model and scaler safely.
    """
    # Use compile=False to avoid Keras metric deserialization issue
    model = load_model(model_path, compile=False)
    scaler = joblib.load(scaler_path)
    return model, scaler


# =========================================================
# 2️⃣ Fetch Stock Data
# =========================================================
def fetch_stock_data(ticker, start, end):
    """
    Downloads stock data from Yahoo Finance.
    Returns a cleaned DataFrame with numeric columns only.
    """
    try:
        df = yf.download(ticker, start=start, end=end)
        if df.empty:
            return pd.DataFrame()

        df = df[['Open', 'High', 'Low', 'Close', 'Volume']].copy()
        df = df.ffill().dropna()
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()


# =========================================================
# 3️⃣ Predict Next Day Price
# =========================================================
def predict_next_price(model, scaler, df, seq_len=60):
    """
    Predicts the next day's closing price using the trained GRU/LSTM model.
    """
    features = ['Open', 'High', 'Low', 'Close', 'Volume']

    # Ensure numeric data only
    df = df[features].apply(pd.to_numeric, errors='coerce').dropna()

    # Safety check for sequence length
    if len(df) < seq_len:
        raise ValueError("Not enough data to form prediction sequence (need 60+ days).")

    # Scale data
    df_scaled = scaler.transform(df.values)

    # Build the last sequence
    last_sequence = df_scaled[-seq_len:]
    X_input = np.expand_dims(last_sequence, axis=0)

    # Predict the next day's scaled close price
    predicted_scaled = model.predict(X_input, verbose=0)

    # Prepare padded array for inverse scaling
    padded_pred = np.zeros((1, df_scaled.shape[1]))
    padded_pred[0, features.index('Close')] = predicted_scaled[0, 0]

    # Inverse transform
    predicted_price = scaler.inverse_transform(padded_pred)[0, features.index('Close')]
    return float(predicted_price)
