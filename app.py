import streamlit as st
import traceback
from datetime import date
from helpers.helper import load_trained_model, fetch_stock_data, predict_next_price

# ------------------------------
# Page config & CSS
# ------------------------------
st.set_page_config(page_title="📈 Stock Price Forecasting App", layout="wide")

st.markdown("""
    <style>
        body { background-color: #0e1117; color: #f5f5f5; }
        .main-title { font-size: 42px; font-weight: bold; color: #4db8ff; text-align: center; }
        .prediction-box { background-color: #1e2130; padding: 20px; border-radius: 15px; text-align: center;
                          box-shadow: 0px 0px 10px rgba(77,184,255,0.2); }
        .debug { background:#0b1220; padding:8px; border-radius:6px; color:#c9d6e3; font-family:monospace; }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
# Header
# ------------------------------
st.markdown("<h1 class='main-title'>💹 AI-Powered Stock Price Predictor</h1>", unsafe_allow_html=True)
st.write("Predict the **next day's closing price** of your favorite stock using Deep Learning models (GRU, LSTM, BiLSTM).")

# ------------------------------
# Sidebar Inputs
# ------------------------------
st.sidebar.header("⚙️ Settings")

stock_option = st.sidebar.selectbox(
    "Select Stock:",
    ["Google (GOOG)", "Apple (AAPL)", "Tesla (TSLA)"]
)

# Dynamically choose model & scaler based on selection
if "Google" in stock_option:
    MODEL_PATH = "model/best_model_gru.h5"
    SCALER_PATH = "model/multiple_input_scaler.gz"
    default_ticker = "GOOG"

elif "Apple" in stock_option:
    MODEL_PATH = "model/aaple_best_model_gru.h5"
    SCALER_PATH = "model/aaple_multiple_input_scaler.gz"
    default_ticker = "AAPL"

else:  # Tesla
    MODEL_PATH = "model/tsla_best_model_gru.h5"
    SCALER_PATH = "model/tsla_multiple_input_scaler.gz"
    default_ticker = "TSLA"

# Sidebar for custom ticker input (optional)
ticker = st.sidebar.text_input("Enter Stock Ticker:", default_ticker).upper()
start_date = st.sidebar.date_input("Start Date", date(2015, 1, 1))
end_date = st.sidebar.date_input("End Date", date.today())

SEQ_LEN = 60

# ------------------------------
# Load Model & Scaler
# ------------------------------
try:
    model, scaler = load_trained_model(MODEL_PATH, SCALER_PATH)
    st.sidebar.success(f"✅ Loaded {stock_option} model successfully!")
except Exception as e:
    st.error(f"❌ Error loading model or scaler: {e}")
    st.stop()

# ------------------------------
# Fetch Data
# ------------------------------
st.subheader("📊 Historical Stock Data")

df = fetch_stock_data(ticker, start=start_date, end=end_date)

if df.empty:
    st.warning("⚠️ No data found for this ticker or date range. Try another ticker or expand the date range.")
    st.stop()

st.dataframe(df.tail(10))

# ------------------------------
# Predict Next Day
# ------------------------------
st.subheader("🔮 Next Day Prediction")

if st.button("Predict Next Day Price"):
    with st.spinner("Predicting... Please wait ⏳"):
        try:
            predicted_price = predict_next_price(model, scaler, df, seq_len=SEQ_LEN)
            latest_close = float(df['Close'].iloc[-1])
            change = predicted_price - latest_close
            direction = "⬆️ Increase" if change > 0 else "⬇️ Decrease"

            # Display result
            st.markdown(f"""
                <div class='prediction-box'>
                    <h3>{stock_option} Predicted Next Close Price: 
                        <span style='color:#4db8ff;'>${predicted_price:.2f}</span></h3>
                    <h4>Current Close: ${latest_close:.2f}</h4>
                    <h4>Expected Change: {direction} ({change:.2f})</h4>
                </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Prediction failed: {e}")
            st.exception(traceback.format_exc())

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown("🧠 Built by **Ali Ahmad** | Powered by **LSTM / BiLSTM / GRU Deep Learning Models**")
