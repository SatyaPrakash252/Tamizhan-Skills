# 🌿 Plant Disease Detection Using CNN

![Plant Health Checker Banner](https://user-images.githubusercontent.com/your-image-url/banner.png) <!-- Optional image -->

A deep learning-based web application for detecting plant diseases from leaf images using a **Convolutional Neural Network (CNN)**, built and deployed with **Streamlit**.

---

## 📸 Demo

<img src="https://user-images.githubusercontent.com/your-image-url/demo.gif" alt="Demo" width="100%"/>
![image](https://github.com/user-attachments/assets/81bd882b-ba20-4a43-b400-ff807ac344c3)<!-- Optional demo GIF -->
![image](https://github.com/user-attachments/assets/1201c38c-14cf-45c9-a584-c0beefaa74aa)


---

## 🧪 Features

- 🌱 Detects diseases from plant leaf images (Tomato, Potato, Bell Pepper)
- ✅ Identifies over **15+ disease classes**
- 🖥️ Simple, elegant Streamlit-based UI
- 🧠 Powered by TensorFlow and CNN architecture
- 📂 Accepts `.jpg`, `.jpeg`, and `.png` images

---

## 🔍 Supported Classes

```text
Pepper__bell___Bacterial_spot
Pepper__bell___healthy
Potato___Early_blight
Potato___healthy
Potato___Late_blight
Tomato___Target_Spot
Tomato___Tomato_mosaic_virus
Tomato___Tomato_YellowLeaf_Curl_Virus
Tomato___Bacterial_spot
Tomato___Early_blight
Tomato___healthy
Tomato___Late_blight
Tomato___Leaf_Mold
Tomato___Septoria_leaf_spot
Tomato___Spider_mites_Two_spotted_spider_mite
🧠 How It Works
📦 Upload an image of a plant leaf.

🧼 Image is preprocessed and resized to 150x150 pixels.

🧠 CNN model analyzes and predicts the disease class.

✅ Result is displayed with confidence score.

📁 Project Structure
bash
Copy
Edit
📦 Plant Health Checker/
 ┣ 📜 app.py                  # Streamlit app
 ┣ 📜 plant_disease_multiclass_model.h5  # Trained CNN model
 ┣ 📜 README.md               # This file
 ┗ 📁 .venv/                  # Virtual environment (optional)
🛠️ Tech Stack
🐍 Python 3.x

🧠 TensorFlow / Keras

📊 NumPy

🖼️ TensorFlow Image Preprocessing

⚡ Streamlit (for UI)

🚀 Getting Started
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/your-username/plant-disease-detector.git
cd plant-disease-detector
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not available, manually install:

bash
Copy
Edit
pip install streamlit tensorflow pillow numpy
4. Run the App
bash
Copy
Edit
streamlit run app.py
📌 Example Output
Uploaded Image	Predicted Class
	Tomato___Leaf_Mold

📚 Dataset
This model is trained on the PlantVillage Dataset, which contains over 50,000 labeled images of diseased and healthy plant leaves.

🤝 Credits
Project by: Satya

Internship: Tamizhan Skills – Real-time Internship & Skill Enhancement Program

Mentor Support: ❤️

📬 Contact
Want to try the app, suggest improvements, or collaborate?

📧 satyaprakashrout435@gmail.com
🌐 LinkedIn:https://www.linkedin.com/in/satya-prakash-rout-923393289/

⭐ Give a Star
If you found this project useful, please consider giving it a ⭐ on GitHub. It motivates me to build more such AI-powered solutions!

