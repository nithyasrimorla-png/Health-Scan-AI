
# 🩺 Health Scan AI – Symptom Checker (Flask + Machine Learning)

An AI-powered **health symptom checker web application** built using **Flask, Machine Learning (Random Forest), and multilingual symptom support**.
It predicts possible diseases based on user-entered symptoms and provides basic health advice.

---

## 🚀 Features

* 🤖 AI-based disease prediction using Random Forest
* 🌍 Multilingual symptom input support (Hindi, Kannada, Tamil, Telugu, etc.)
* 🧠 Rule-based + ML hybrid prediction system
* ⚠️ Emergency detection (HIGH / MEDIUM / LOW)
* 🍎 Health advice (food + care suggestions)
* 🏥 Covers 40+ diseases
* 🔍 Smart symptom normalization system
* 💡 Handles real-world messy user inputs

---
🛠️ Tech Stack

This project is built using:

Flask 🐍 – Backend web framework
Scikit-learn 🤖 – Machine learning model (RandomForestClassifier)
Pandas 📊 – Data handling and preprocessing
HTML / CSS / JavaScript 🎨 – Frontend UI

## 🧠 AI Model

* Algorithm: **Random Forest Classifier**
* Library: `scikit-learn`
* Trained on: `data.csv`
* Features used:

  * fever
  * cough
  * headache
  * vomiting
  * dizziness
  * chest pain
  * fatigue
  * and more symptom indicators

---

## 🌐 Supported Languages

The system supports symptom input in:

* English
* Hindi (हिंदी)
* Kannada (ಕನ್ನಡ)
* Tamil (தமிழ்)
* Telugu (తెలుగు)

Example:

headache = ತಲೆನೋವು = सिर दर्द = தலைவலி = తలనొప్పి


## 🏥 Diseases Covered

Some major diseases detected:

* Flu
* Viral Fever
* COVID-19
* Dengue
* Malaria
* Typhoid
* Pneumonia
* Asthma
* Diabetes
* Hypertension
* Migraine
* Tuberculosis
* UTI
* Kidney Infection
* Arthritis
* Osteoporosis
* Allergy
* Depression
* Anxiety Disorders



## ⚠️ Safety System

* 🚨 Chest pain → HIGH emergency warning
* ⚠️ Dizziness / vomiting → MEDIUM warning
* ❗ Invalid or unsafe combinations are filtered
* ❌ Prevents incorrect mapping (e.g., headache → osteoporosis)


## 🏗️ Project Structure

```
health_scan_ai/
│
├── app.py                 # Main Flask backend
├── data.csv              # Training dataset
├── templates/
│     └── index.html      # Frontend UI
├── static/               # CSS/JS (optional)
└── README.md


## ⚙️ Installation & Setup

### 1. Clone project

bash:
git clone https://github.com/yourusername/health-scan-ai.git
cd health-scan-ai


### 2. Install dependencies

```bash
pip install flask pandas scikit-learn
```

### 3. Run the app

```bash
python app.py
```

### 4. Open browser

```
http://127.0.0.1:5000/
```


## 🧪 Sample Inputs

Try these in your app:

```
fever, cough, fatigue
chest pain
vomiting, stomach pain
headache, light sensitivity
high fever, chills
burning urination
weak, dizziness
```

---

## 📊 Output Example

```
🧠 Disease: Viral Fever
📊 Confidence: 92%

💡 Advice:
- Rest well
- Drink fluids
- Take proper medication
```

---

## 🔮 Future Improvements

* 🎤 Voice-based symptom input
* 🗣️ Voice AI responses
* 💬 Chatbot UI (WhatsApp style)
* 🌐 Fully multilingual AI doctor
* 📱 Mobile app version
* 🧾 Medical report generation

---

## ⚠️ Disclaimer

This application is for **educational purposes only**.
It is **NOT a replacement for professional medical diagnosis or treatment**.

Always consult a qualified doctor for medical concerns.

---

