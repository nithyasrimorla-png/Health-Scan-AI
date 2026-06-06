from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# -----------------------------
# LOAD DATA
# -----------------------------
data = pd.read_csv("data.csv")

X = data.drop("disease", axis=1)
y = data["disease"]

# -----------------------------
# TRAIN MODEL
# -----------------------------
model = RandomForestClassifier(
    n_estimators=500,
    max_depth=20,
    random_state=42,
    class_weight="balanced"
)

model.fit(X, y)

print("AI Model trained successfully!")

# -----------------------------
# EMERGENCY CHECK
# -----------------------------
def emergency_check(symptoms):
    symptoms = symptoms.lower()

    if any(x in symptoms for x in ["chest pain", "cannot breathe", "unconscious"]):
        return "HIGH"

    if any(x in symptoms for x in ["high fever", "dizziness", "vomiting"]):
        return "MEDIUM"

    return "LOW"

# -----------------------------
# ADVICE SYSTEM
# -----------------------------
def advice(disease):
    info = {
        "flu": { 
            "food": "Warm soups, fruits, ginger tea, honey water.",
            "care": "Rest, drink fluids, stay warm." }, 
        "cold": {
            "food": "Soup, warm milk, fruits, herbal tea.", 
            "care": "Steam inhalation, rest." }, 
        "covid": { 
            "food": "Protein foods, fruits, fluids.",
            "care": "Isolation, monitor oxygen, rest." }, 
        "migraine": {
            "food": "Light food, bananas, lots of water.", 
            "care": "Rest in dark room, avoid noise." },
        "gastritis": { 
            "food": "Rice, curd, banana, soft foods.",
            "care": "Avoid spicy/oily food." },
        "dengue": { 
            "food": "Papaya leaf juice, fruits, fluids.", 
            "care": "Rest, medical monitoring needed." },
        "food_poisoning": { 
            "food": "ORS, rice porridge, toast, banana.", 
            "care": "Hydration, rest, avoid outside food." }, 
        "pneumonia": { 
            "food": "Light soups, fluids.",
            "care": "Immediate doctor consultation." },
        "typhoid": { 
            "food": "Boiled food, soups, soft diet.", 
            "care": "Complete rest and medication." }, 
        "throat_infection": { 
            "food": "Warm water, honey, soups.", 
            "care": "Salt water gargle." }, 
        "heart_problem": {
            "food": "Low salt diet, fruits, vegetables.",
            "care": "Avoid stress, consult doctor immediately." }, 
        "viral_fever": { 
            "food": "Fruits, fluids, coconut water.", 
            "care": "Rest and hydration." }, 
        "malaria": { 
            "food": "Fruits, coconut water, light meals.", 
            "care": "Complete rest, avoid mosquito exposure." }, 
        "anemia": { 
            "food": "Spinach, dates, iron-rich foods.", 
            "care": "Take iron supplements, proper diet." },
        "sinusitis": { 
            "food": "Warm fluids, soups.", 
            "care": "Steam inhalation, avoid cold." },
        "asthma": {
            "food": "Healthy diet, avoid cold foods.", 
            "care": "Avoid dust, use inhaler if needed." }, 
        "diabetes": { 
            "food": "Low sugar diet, vegetables.",
            "care": "Monitor sugar, exercise regularly." }, 
        "hypertension": { 
            "food": "Low salt diet, fruits.",
            "care": "Reduce stress, regular exercise." }
    }
    

    return info.get(disease, {
        "food": "Eat healthy home food and stay hydrated.",
        "care": "Consult doctor if symptoms continue." })
# -----------------------------
# FIXED PREDICTION FUNCTION
# -----------------------------
def predict_disease(symptoms):
    symptoms = symptoms.lower()

    
    if "fever" in symptoms and "cough" in symptoms and "fatigue" in symptoms:
        return "flu", 95

    if "fever" in symptoms and "cough" in symptoms:
        return "viral_fever", 92

    if "fever" in symptoms and "body pain" in symptoms:
        return "flu", 90

    if "chest pain" in symptoms:
        return "heart_problem", 95

    if "vomiting" in symptoms and "stomach" in symptoms:
        return "food_poisoning", 93

    if "high fever" in symptoms and "chills" in symptoms:
        return "malaria", 94
    if "chest pain" in symptoms or "breathless" in symptoms:
        return "heart_problem", 95
    if "stomach" in symptoms and "vomiting" in symptoms and "fever" in symptoms:
        return "stomach_infection", 93
    if "stomach" in symptoms and "vomiting" in symptoms:
        return "food_poisoning", 90
    if "fever" in symptoms and "cough" in symptoms and "breath" in symptoms:
        return "covid", 92 
    if "fever" in symptoms and "body pain" in symptoms and "chills" in symptoms: 
        return "dengue", 91 
    if "headache" in symptoms and "light" in symptoms:
        return "migraine", 88
    if "sore throat" in symptoms and "cough" in symptoms:
        return "cold", 85
    if "high fever" in symptoms and "chills" in symptoms: 
        return "malaria", 94 
    
    if "weak" in symptoms and "dizziness" in symptoms: 
        return "anemia", 90 
    if "headache" in symptoms and "runny nose" in symptoms: 
        return "sinusitis", 88
    if "breathing" in symptoms and "chest" in symptoms:
        return "asthma", 91
    if "frequent urination" in symptoms or "thirst" in symptoms: 
        return "diabetes", 89
    if "headache" in symptoms and "stress" in symptoms:
        return "hypertension", 90 
    if "fever" in symptoms and ("chills" in symptoms or "sweating" in symptoms):
        return "malaria", 90




    # -------------------------
    # ML INPUT (IMPROVED)
    # -------------------------
    input_data = pd.DataFrame([{
        "fever": int("fever" in symptoms),
        "cough": int("cough" in symptoms),
        "headache": int("headache" in symptoms),
        "stomach_pain": int("stomach" in symptoms or "nausea" in symptoms),
        "fatigue": int("fatigue" in symptoms or "weak" in symptoms),
        "sore_throat": int("throat" in symptoms),
        "heart_pain": int("chest pain" in symptoms),
        "vomiting": int("vomiting" in symptoms),
        "dizziness": int("dizziness" in symptoms),
        "body_pain": int("body pain" in symptoms),
        "runny_nose": int("runny nose" in symptoms),
        "chills": int("chills" in symptoms),
        "sweating": int("sweating" in symptoms)
    }])

    prediction = model.predict(input_data)[0]
    confidence = round(max(model.predict_proba(input_data)[0]) * 100, 2)

    return prediction, confidence

# -----------------------------
# ROUTE
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    disease = None
    care = ""
    food = ""
    prediction = 0
    emergency_level = "LOW"
    submitted = False

    if request.method == "POST":
        submitted = True
        user_input = request.form["symptoms"]

        emergency_level = emergency_check(user_input)
        disease, prediction = predict_disease(user_input)

        info = advice(disease)
        care = info["care"]
        food = info["food"]

    return render_template(
        "index.html",
        disease=disease,
        care=care,
        food=food,
        prediction=prediction,
        emergency_level=emergency_level,
        submitted=submitted
    )

# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)