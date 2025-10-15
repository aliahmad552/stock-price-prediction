# 📈 Stock Price Prediction with LSTM, BiLSTM, and GRU  

This project predicts the **future stock prices** of major companies such as **Google (GOOG)**, **Apple (AAPL)**, and **Tesla (TSLA)** using **deep learning models** like **LSTM**, **BiLSTM**, and **GRU**.  
It provides an interactive **Streamlit web app** where users can select a stock, set a date range, and visualize predicted prices on beautiful graphs.  

---

## 🧠 Project Overview

Stock markets are highly volatile and influenced by multiple factors like economy, company performance, and global events.  
In this project, we use **time-series forecasting** techniques with **Recurrent Neural Networks (RNNs)** such as:

- **LSTM (Long Short-Term Memory)**  
- **BiLSTM (Bidirectional LSTM)**  
- **GRU (Gated Recurrent Unit)**  

These models are excellent for sequence data because they can remember patterns over time — making them ideal for stock price prediction.

---

## 🚀 Features

✅ Predict **future stock prices** for Google, Apple, or Tesla  
✅ **Interactive Streamlit UI** with dynamic dropdowns  
✅ Displays **real stock price vs predicted price graph**  
✅ Supports **custom ticker input** (you can enter any stock symbol)  
✅ Works with **Docker** (ready for containerized deployment)  
✅ Clean, modular, and easy-to-understand code  

---

## 🧩 Tech Stack

| Category | Technology |
|-----------|-------------|
| Programming Language | Python 3.10.11 |
| Web Framework | Streamlit |
| Deep Learning | TensorFlow / Keras |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Plotly |
| Deployment | Docker |

---

## 🧾 Installation Guide

Follow these steps to run the project locally:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/stock-price-prediction.git
cd stock-price-prediction
```

### 2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run Streamlit app
```bash
streamlit run app.py
```


Now open the URL shown in the terminal (usually http://localhost:8501)
## 🧠 Model Explanation
| Model      | Description                                       |
| ---------- | ------------------------------------------------- |
| **LSTM**   | Captures long-term dependencies in stock prices   |
| **BiLSTM** | Reads data in both directions, improving learning |
| **GRU**    | Similar to LSTM but faster and less complex       |
.

Each model was trained on **historical stock data (from 2015 onward)** and evaluated using metrics such as **MAE, RMSE, and R² Score.**
## 📅 Supported Stocks
| Company | Ticker |
| ------- | ------ |
| Google  | GOOG   |
| Apple   | AAPL   |
| Tesla   | TSLA   |

## 💡 Author

### Ali Ahmad
🎓 Data Scientist & AI Engineer
💻 Specializing in Deep Learning and Time Series Forecasting
📍 The Islamia University of Bahawalpur
