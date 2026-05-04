# =========================================
# IMPORT
# =========================================
import joblib
import re
import pandas as pd

# =========================================
# LOAD MODEL & ENCODER
# =========================================
model = joblib.load("models/mental_health_model.pkl")
encoders = joblib.load("models/encoders.pkl")


# =========================================
# NLP: CLEAN TEXT
# =========================================
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# =========================================
# NLP: UNIVERSAL RISK SCORING
# =========================================
def calculate_risk_score(message):
    message = clean_text(message)

    categories = {
        "emotional": {
            "keywords": ["cemas", "gelisah", "takut", "panik", "sedih"],
            "weight": 2,
        },
        "cognitive": {
            "keywords": ["overthinking", "sulit fokus", "pikiran kacau"],
            "weight": 2,
        },
        "physical": {
            "keywords": ["pusing", "lelah", "capek", "tidak bertenaga"],
            "weight": 1,
        },
        "behavioral": {
            "keywords": ["menyendiri", "malas bertemu", "menarik diri"],
            "weight": 2,
        },
        "sleep": {
            "keywords": ["tidak bisa tidur", "insomnia", "tidur terganggu"],
            "weight": 2,
        },
        "severe": {
            "keywords": ["ingin menyerah", "hidup tidak berarti", "putus asa"],
            "weight": 4,
        },
    }

    score = 0

    for category in categories.values():
        for word in category["keywords"]:
            if word in message:
                score += category["weight"]
                break

    return score


# =========================================
# MAPPING CHAT → DATASET FEATURES
# =========================================
def map_chat_to_features(user_input):
    message = user_input["message"].lower()

    # NLP sederhana
    if "tidak bisa tidur" in message:
        stress = "Often"
    elif "cemas" in message or "stress" in message:
        stress = "Often"
    else:
        stress = "Rarely"

    return {
        "Age": user_input["age"],
        "Gender": user_input["gender"],
        "Country": "Indonesia",
        "self_employed": "No",
        "family_history": user_input["family_history"],
        "work_interfere": stress,
        "no_employees": "1-5",
        "remote_work": "No",
        "tech_company": "Yes",
        "benefits": "No",
        "care_options": "No",
        "wellness_program": "No",
        "seek_help": "No",
        "anonymity": "Yes",
        "leave": "Somewhat difficult",
        "mental_health_consequence": "Yes" if stress == "Often" else "No",
        "phys_health_consequence": "No",
        "coworkers": "Some of them",
        "supervisor": "Some of them",
        "mental_health_interview": "No",
        "phys_health_interview": "No",
        "mental_vs_physical": "Don't know",
        "obs_consequence": "No",
    }


# =========================================
# ENCODING
# =========================================
def encode_features(features, encoders):
    columns = list(encoders.keys())
    encoded = []

    for col in columns:
        val = features.get(col, "Unknown")

        try:
            val_encoded = encoders[col].transform([str(val)])[0]
        except:
            val_encoded = 0

        encoded.append(val_encoded)

    return pd.DataFrame([encoded], columns=columns)


# =========================================
# MAIN PREDICTION
# =========================================
def predict_from_chat(user_input, debug=False):
    features = map_chat_to_features(user_input)
    encoded = encode_features(features, encoders)

    result = model.predict(encoded)[0]

    # NLP scoring
    score = calculate_risk_score(user_input["message"])

    # final risk
    if score >= 5:
        risk = "High"
    elif score >= 3:
        risk = "Medium"
    else:
        risk = "Low"

    if debug:
        print("Features:", features)
        print("Score:", score)

    return {"prediction": result, "risk": risk, "score": score}


# =========================================
# CLI TEST
# =========================================
def run_cli():
    print("\n=== Mental Health Screening ===")

    age = int(input("Umur: "))
    gender = input("Gender (Male/Female): ")
    family_history = input("Family history (Yes/No): ")
    message = input("Ceritakan kondisi Anda: ")

    user_input = {
        "age": age,
        "gender": gender,
        "family_history": family_history,
        "message": message,
    }

    result = predict_from_chat(user_input)

    print("\n=== HASIL ===")
    print(f"Risk Level : {result['risk']}")
    print(f"Score      : {result['score']}")
    print(f"Prediction : {result['prediction']}")


# =========================================
# TEST CASE
# =========================================
def run_test():
    test_cases = [
        {
            "age": 25,
            "gender": "Female",
            "family_history": "No",
            "message": "Saya baik-baik saja dan tidur nyenyak",
        },
        {
            "age": 30,
            "gender": "Male",
            "family_history": "Yes",
            "message": "Saya sangat cemas, overthinking dan tidak bisa tidur",
        },
        {
            "age": 22,
            "gender": "Male",
            "family_history": "No",
            "message": "Saya pusing dan lelah",
        },
    ]

    for i, case in enumerate(test_cases):
        print(f"\n=== Test Case {i+1} ===")
        print(predict_from_chat(case))


# =========================================
# MAIN
# =========================================
if __name__ == "__main__":
    mode = input("Pilih mode (test / cli): ").lower()

    if mode == "test":
        run_test()
    elif mode == "cli":
        run_cli()
    else:
        print("Mode tidak dikenali.")
