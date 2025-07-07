
# 📈 Stock Price Prediction Web App using LSTM

A real-time **Stock Price Forecasting Web Application** built with **LSTM Neural Networks** using **TensorFlow/Keras**, and deployed through **Streamlit**.

This project was developed as part of the **RISE Internship Program by Damizan Skills**, combining Machine Learning, Time Series Forecasting, and Interactive Web App deployment.

---

## 🚀 Features

- 🔍 Input any stock ticker symbol (e.g., `AAPL`, `GOOGL`, `TCS.NS`)
- 📅 Choose custom date range for historical data
- 🧠 Live training of an **LSTM model** in the browser
- 📉 Visualize predicted vs actual stock prices
- 🖥️ Clean and responsive UI built with Streamlit

---

## 📊 Technologies Used

- **Python**  
- **TensorFlow / Keras**  
- **yFinance API**  
- **NumPy / Pandas**  
- **Matplotlib**  
- **Streamlit**  
- **MinMaxScaler (from Scikit-learn)**

---

## 📁 Project Structure

```
├── app.py                         # Main Streamlit application
├── Stock_Price_Prediction_LSTM.ipynb   # Jupyter notebook for experimentation
├── README.md                     # Project documentation
```

---

## ⚙️ How It Works

1. **User inputs a stock ticker** (e.g., `AAPL`)
2. The app uses **Yahoo Finance API** to fetch historical data
3. Data is preprocessed using **MinMaxScaler** and formatted with a sliding window technique
4. A **2-layer LSTM model** is trained on the data
5. Predictions are made and plotted against actual values using Matplotlib

---

## 🚀 Getting Started

### 🖥️ Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/SatyaPrakash252/stock-price-lstm.git
   cd stock-price-lstm
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

> You’ll need Python 3.7+ and a stable internet connection for fetching live stock data.

---


## 🎓 What I Learned

- Handling real-world financial data with `yfinance`
- Time Series Forecasting using **LSTM**
- Model evaluation and live visualization
- Deploying ML models using **Streamlit**

---

## 🙏 Acknowledgment

Big thanks to **Damizan Skills** and the **RISE Internship Program** for the guidance and support throughout the project.

---

## 📬 Contact

**Satya Prakash Rout**
📧 [satyaprakashrout435@gmail.com]  
🔗 [LinkedIn](https://www.linkedin.com/in/satya-prakash-rout-923393289/)  
🐍 Passionate about AI | Open to opportunities

---

## ⭐ Show Some Love!

If you found this useful, please ⭐ the repo and share it! Contributions and suggestions are welcome. 👇
