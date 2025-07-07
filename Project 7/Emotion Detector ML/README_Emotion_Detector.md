
# 🧠 Emotion Detection from Text App

A lightweight **NLP-based Emotion Classifier** that predicts emotions from user-entered text using **Machine Learning** and an interactive **Streamlit** UI.

This project was built as part of the **RISE Internship Program by Damizan Skills**, focusing on Natural Language Processing, real-time text inference, and user-friendly app design.

---

## 🚀 Features

- 🧾 Accepts user input through a simple text area
- 🧹 Cleans and preprocesses the text (removing stopwords, punctuation)
- 🧠 Uses a trained **TF-IDF + ML model** to detect the underlying emotion
- 🎯 Supports classification into emotions like **joy, anger, sadness, fear, love**, etc.
- 💡 Clear and instant feedback with Streamlit UI

---

## 📊 Technologies Used

- **Python**  
- **Scikit-learn / Joblib**  
- **TF-IDF Vectorization**  
- **NLTK (for text cleaning and stopwords)**  
- **Streamlit**  

---

## 📁 Project Structure

```
├── app.py                       # Main Streamlit UI code
├── emotion_model.pkl           # Trained ML model (Joblib serialized)
├── tfidf_vectorizer.pkl        # TF-IDF vectorizer (Joblib serialized)
├── TextFile_Emotion_Detector.ipynb   # Notebook for training and testing
├── README.md                   # Documentation
```

---

## ⚙️ How It Works

1. User enters a message or text into the app.
2. The text is cleaned using `nltk` stopwords and regex.
3. Text is vectorized using the saved **TF-IDF model**.
4. The vector is passed into the **trained ML model** for emotion prediction.
5. The app displays the predicted emotion.

---

## 🚀 Getting Started

### 🖥️ Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/emotion-detector-app.git
   cd emotion-detector-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

> Make sure `emotion_model.pkl` and `tfidf_vectorizer.pkl` are in the same directory as `app.py`.

---

## 🎓 What I Learned

- Text cleaning and stopword removal with **NLTK**
- TF-IDF vectorization for machine learning pipelines
- Emotion classification using ML models
- Frontend integration using **Streamlit**

---

## 🙏 Acknowledgment

Special thanks to **Damizan Skills** and the **RISE Internship** for enabling this hands-on NLP project experience.

---

## 📬 Contact

**Satya Prakash Rout**  
📧 [satyaprakashrout435@gmail.com]  
🔗 [LinkedIn](https://www.linkedin.com/in/satya-prakash-rout-923393289/)  
🔍 NLP | ML | AI Enthusiast | Open to Collaboration

---

## ⭐ Show Some Love

If you liked this project, feel free to ⭐ the repo and connect with me for future collaborations!

