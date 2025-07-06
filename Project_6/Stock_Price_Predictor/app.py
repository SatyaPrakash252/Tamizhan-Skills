# Save this as app.py and run with: streamlit run app.py

import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

st.set_page_config(page_title="📈 Stock Price Predictor (LSTM)", layout="centered")

st.title("📊 Stock Price Prediction with LSTM")
ticker = st.text_input("Enter stock ticker (e.g., AAPL, GOOGL, TCS.NS):", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime("2015-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2023-12-31"))

if st.button("Run Prediction"):
    df = yf.download(ticker, start=start_date, end=end_date)
    if df.empty:
        st.error("No data found for this ticker.")
    else:
        data = df[['Close']].values
        scaler = MinMaxScaler()
        scaled = scaler.fit_transform(data)

        def create_dataset(dataset, time_step=60):
            X, y = [], []
            for i in range(len(dataset) - time_step):
                X.append(dataset[i:i+time_step, 0])
                y.append(dataset[i+time_step, 0])
            return np.array(X), np.array(y)

        X, y = create_dataset(scaled)
        X = X.reshape(X.shape[0], X.shape[1], 1)

        model = Sequential([
            LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)),
            LSTM(50),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        with st.spinner("Training LSTM model..."):
            model.fit(X, y, epochs=10, batch_size=32, verbose=0)

        pred = model.predict(X)
        pred_inv = scaler.inverse_transform(pred)
        actual_inv = scaler.inverse_transform(y.reshape(-1, 1))

        st.subheader("📉 Predicted vs Actual Prices")
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(actual_inv, label='Actual Price')
        ax.plot(pred_inv, label='Predicted Price')
        ax.set_title(f"{ticker} Stock Price Prediction")
        ax.set_xlabel("Time Steps")
        ax.set_ylabel("Price")
        ax.legend()
        st.pyplot(fig)
