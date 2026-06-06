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
        "food": "Warm soups, fruits, ginger tea.",
        "care": "Rest and drink plenty of fluids."
    },

    "cold": {
        "food": "Warm milk, soup, herbal tea.",
        "care": "Steam inhalation and rest."
    },

    "covid": {
        "food": "Protein-rich foods and fluids.",
        "care": "Rest and monitor symptoms."
    },

    "viral_fever": {
        "food": "Coconut water and fruits.",
        "care": "Hydration and rest."
    },

    "dengue": {
        "food": "ORS, fruits, papaya leaf juice.",
        "care": "Medical monitoring recommended."
    },

    "malaria": {
        "food": "Light meals and fluids.",
        "care": "Complete medication course."
    },

    "typhoid": {
        "food": "Soft boiled food and soups.",
        "care": "Complete rest and medication."
    },

    "pneumonia": {
        "food": "Warm soup and fluids.",
        "care": "Doctor consultation needed."
    },

    "bronchitis": {
        "food": "Honey tea and warm liquids.",
        "care": "Avoid smoke and dust."
    },

    "asthma": {
        "food": "Healthy balanced diet.",
        "care": "Avoid allergens and dust."
    },

    "tuberculosis": {
        "food": "High-protein nutritious foods.",
        "care": "Seek medical treatment."
    },

    "migraine": {
        "food": "Light food and water.",
        "care": "Rest in a dark room."
    },

    "sinusitis": {
        "food": "Warm fluids and soups.",
        "care": "Steam inhalation."
    },

    "throat_infection": {
        "food": "Warm water and honey.",
        "care": "Salt-water gargles."
    },

    "ear_infection": {
        "food": "Healthy food and fluids.",
        "care": "Consult doctor if pain persists."
    },

    "conjunctivitis": {
        "food": "Hydration and fruits.",
        "care": "Keep eyes clean."
    },

    "gastritis": {
        "food": "Rice, curd and banana.",
        "care": "Avoid spicy foods."
    },

    "food_poisoning": {
        "food": "ORS and bland foods.",
        "care": "Stay hydrated."
    },

    "stomach_infection": {
        "food": "Rice, banana, toast.",
        "care": "Drink fluids and rest."
    },

    "uti": {
        "food": "Drink plenty of water.",
        "care": "Medical evaluation recommended."
    },

    "kidney_infection": {
        "food": "Adequate fluids.",
        "care": "Doctor consultation required."
    },

    "hepatitis": {
        "food": "Low-fat healthy diet.",
        "care": "Avoid alcohol."
    },

    "appendicitis": {
        "food": "Seek medical attention.",
        "care": "Urgent evaluation required."
    },

    "arthritis": {
        "food": "Anti-inflammatory foods.",
        "care": "Regular exercise."
    },

    "osteoporosis": {
        "food": "Calcium-rich foods.",
        "care": "Weight-bearing exercise."
    },

    "anemia": {
        "food": "Spinach, dates, iron-rich foods.",
        "care": "Iron supplementation."
    },

    "diabetes": {
        "food": "Low sugar diet.",
        "care": "Monitor blood sugar."
    },

    "hypertension": {
        "food": "Low salt foods.",
        "care": "Exercise and stress reduction."
    },

    "heart_problem": {
        "food": "Heart-healthy foods.",
        "care": "Consult doctor immediately."
    },

    "allergy": {
        "food": "Avoid trigger foods.",
        "care": "Stay away from allergens."
    },

    "skin_infection": {
        "food": "Healthy balanced diet.",
        "care": "Keep skin clean."
    },

    "eczema": {
        "food": "Hydrating foods.",
        "care": "Moisturize skin regularly."
    },

    "psoriasis": {
        "food": "Balanced diet.",
        "care": "Follow treatment plan."
    },

    "stress_related": {
        "food": "Fruits and nuts.",
        "care": "Relaxation and sleep."
    },

    "anxiety_disorder": {
        "food": "Nutritious foods.",
        "care": "Stress management."
    },

    "depression": {
        "food": "Balanced meals.",
        "care": "Professional support may help."
    },

    "insomnia": {
        "food": "Avoid caffeine at night.",
        "care": "Maintain sleep routine."
    },

    "dehydration": {
        "food": "Water, ORS, coconut water.",
        "care": "Increase fluid intake."
    },

    "obesity": {
        "food": "Balanced calorie-controlled diet.",
        "care": "Regular physical activity."
    },

    "hypothyroidism": {
        "food": "Balanced nutritious diet.",
        "care": "Follow prescribed treatment."
    },

    "hyperthyroidism": {
        "food": "Balanced meals.",
        "care": "Regular medical follow-up."
    }
}

return info.get(
    disease,
    {
        "food": "Eat healthy home food and stay hydrated.",
        "care": "Consult doctor if symptoms continue."
    }
)




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
    # Additional disease rules

if "loss of smell" in symptoms or "loss of taste" in symptoms:
return "covid", 94

if "joint pain" in symptoms and "rash" in symptoms:
return "dengue", 92

if "frequent urination" in symptoms and "thirst" in symptoms:
return "diabetes", 93

if "burning urination" in symptoms:
return "uti", 92

if "yellow skin" in symptoms or "yellow eyes" in symptoms:
return "hepatitis", 94

if "joint pain" in symptoms and "swelling" in symptoms:
return "arthritis", 90

if "night sweats" in symptoms and "cough" in symptoms:
return "tuberculosis", 93

if "red eyes" in symptoms:
return "conjunctivitis", 90

if "ear pain" in symptoms:
return "ear_infection", 88

if "itching" in symptoms and "rash" in symptoms:
return "allergy", 89

if "anxiety" in symptoms and "stress" in symptoms:
return "anxiety_disorder", 88

if "cannot sleep" in symptoms or "insomnia" in symptoms:
return "insomnia", 88

if "weight loss" in symptoms and "thirst" in symptoms:
return "diabetes", 92

if "back pain" in symptoms and "burning urination" in symptoms:
return "kidney_infection", 91

if "dry cough" in symptoms and "breathless" in symptoms:
return "asthma", 90





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
