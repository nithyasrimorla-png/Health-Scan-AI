
###🩺 Health Scan AI – Symptom Checker

Health Scan AI is a Flask-based web application that predicts possible diseases from user-entered symptoms using a hybrid approach of Rule-Based Logic + Machine Learning (Random Forest). It provides instant health insights, emergency risk detection, multilingual support, and basic care guidance.

⚠️ This project is for educational purposes only and is not a substitute for professional medical advice.


### Features

🤖 Hybrid AI System – Combines rule-based logic with ML (Random Forest Classifier)
🌍 Multilingual Input Support – English, Hindi, Kannada, Tamil, Telugu.
🧠 Smart Symptom Normalization – Handles real-world messy inputs and regional terms
⚠️ Emergency Detection System – Classifies risk as HIGH / MEDIUM / LOW
📊 Confidence Score Output – Shows prediction reliability percentage
🍎 Care & Diet Recommendations – Basic health guidance for predicted conditions
🏥 40+ Diseases Covered – Includes viral, chronic, and lifestyle-related conditions


### Tech Stack

Backend: Flask (Python)
Machine Learning: scikit-learn (RandomForestClassifier)
Data Handling: Pandas, NumPy
Frontend: HTML5, CSS3, JavaScript (Jinja2 templates)
Deployment: Railway


### AI Model Details

Algorithm: Random Forest Classifier
Training Data: data.csv

### Key Features:

Fever
Cough
Headache
Vomiting
Dizziness
Chest Pain
Fatigue..
And other symptom indicators

### Supported Languages
Users can enter symptoms in multiple languages:

English
Hindi (हिंदी)
Kannada (ಕನ್ನಡ)
Tamil (தமிழ்)
Telugu (తెలుగు)

# Example Mapping:
Headache = सिर दर्द = ತಲೆನೋವು = தலைவலி = తలనొప్పి

### System Workflow

1. User enters symptoms in natural language
2. Input is normalized into structured medical keywords
3. Emergency risk level is evaluated first
4. Rule-based system checks for known patterns
5. If no match → ML model predicts disease
6. Output includes disease, confidence score, risk level, and care advice

## Project Structure

Health-Scan-AI/
│
├── app.py / main.py        # Flask backend
├── data.csv               # Dataset
├── templates/
│   └── index.html         # Frontend UI
├── static/                # CSS / JS files
├── requirements.txt
├── procfile
└── runtime.txt

## Installation & Setup

1. Clone the repository
     git clone https://github.com/nithyasrimorla-png/Health-Scan-AI.git
     cd Health-Scan-AI
2. Install dependencies:
     pip install -r requirements.txt
3. Run the application:
     python main.py
4. Open in browser:
     http://127.0.0.1:5000/

## Sample Inputs

Try entering:
1.fever, cough, fatigue
2.chest pain
3.vomiting, stomach pain
4.headache, dizziness
5.high fever with chills
6.burning urination

## Output Example

🧠 Disease: Viral Fever
📊 Confidence: 92%
⚠️ Risk Level: MEDIUM

💡 Advice:
- Take rest
- Stay hydrated
- Follow basic medication guidance

## Future Improvements

💬 Chatbot-style medical assistant
🗣️ AI voice responses
🌐 Fully multilingual AI doctor expansion
🧾 Medical report generation


⚠️ Disclaimer

This application is built for educational purposes only. It does not provide medical diagnosis or treatment. Always consult a qualified healthcare professional for medical concerns.


👩‍💻 Author
Nithya Sri Morla
