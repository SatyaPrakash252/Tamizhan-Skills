## 🚀 Streamlit UI (Save as `app.py` in same folder)
import streamlit as st
import joblib
import numpy as np
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return " ".join([word for word in text.split() if word not in stop_words])

st.set_page_config(page_title="Emotion Detector", layout="centered")
st.title("🧠 Emotion Detection from Text Files")
st.write("Enter any message to detect the **emotion** behind it.")

user_input = st.text_area("💬 Your Message", placeholder="e.g., I feel amazing today!", height=150)

if st.button("🔍 Detect Emotion"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])
        pred = model.predict(vec)[0]
        st.success(f"🎭 **Predicted Emotion:** {pred}")