# 💡 Tamizhan Skills – AI/ML Internship Projects 🚀

Welcome to the official repository for my internship under **Tamizhan Skills**. This repository showcases the end-to-end development of real-world AI/ML projects, covering both **Computer Vision** and **Natural Language Processing**, built using Python, TensorFlow, Scikit-learn, Streamlit, and more.

---

## 📁 Projects Included

### 🌿 Project 6 – Plant Disease Detection (CNN + Streamlit)
Detects multiple plant leaf diseases using a custom-trained **Convolutional Neural Network** on the [PlantVillage Dataset].

**Tech Stack:**  
`TensorFlow` • `Keras` • `OpenCV` • `Streamlit`

🔹 Upload a leaf image  
🔹 Real-time prediction with confidence  
🔹 Clean and simple web interface

📂 Folder: `Project 6/`  
📁 Contents:  
- `plant_disease_detection.ipynb` – training notebook  
- `app.py` – Streamlit frontend  
- `model.h5` – trained CNN model

---

### 😊 Project 7 – Emotion Detection from Text (NLP)
Predicts human emotions like joy, sadness, anger, etc. from raw user input using classic NLP techniques.

**Tech Stack:**  
`Scikit-learn` • `Logistic Regression` • `TF-IDF` • `Streamlit`

🔹 Enter a sentence  
🔹 Get emotion prediction instantly  
🔹 Trained on custom-labeled emotion dataset

📂 Folder: `Project 7/`  
📁 Contents:  
- `train_model.ipynb`  
- `app.py`  
- `emotion_model.pkl`, `vectorizer.pkl`

---

### 📈 Project 8 – Stock Price Prediction (LSTM)
Uses **LSTM neural networks** to forecast stock prices based on historical data from Yahoo Finance.

**Tech Stack:**  
`TensorFlow` • `Keras` • `yfinance` • `MinMaxScaler`

🔹 Uses past 60 days to predict future price  
🔹 Graphs for comparison  
🔹 Optional Streamlit dashboard

📂 Folder: `Project 8/`  
📁 Contents:  
- `Stock_Price_Prediction.ipynb`  
- `model.h5`, `scaler.save`  
- `app.py` *(optional)*

---

## 🛠 Installation & Usage

```bash
# Clone the repo
git clone https://github.com/SatyaPrakash252/Tamizhan-Skills.git
cd Tamizhan-Skills

# Create a virtual environment
python -m venv .venv
.venv\\Scripts\\activate     # for Windows

# Install required packages
pip install -r requirements.txt

# To run Streamlit apps
streamlit run Project7/app.py
