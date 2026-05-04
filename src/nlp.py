# =========================================
# NLP PIPELINE
# =========================================

import re
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# =========================================
# 1. TEXT CLEANING
# =========================================

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # hapus simbol
    text = re.sub(r"\s+", " ", text).strip()
    return text

# =========================================
# 2. KEYWORD-BASED FEATURE EXTRACTION
# =========================================

sleep_keywords = {
    "Poor": ["sulit tidur", "insomnia", "tidak bisa tidur"],
    "Good": ["tidur nyenyak", "tidur baik"],
    "Average": []
}

stress_keywords = {
    "Often": ["cemas", "stress", "tertekan", "overthinking"],
    "Rarely": ["tenang", "baik-baik saja"]
}

def detect_category(text, keyword_dict, default):
    for category, keywords in keyword_dict.items():
        for word in keywords:
            if word in text:
                return category
    return default

def extract_features(text):
    text = clean_text(text)

    sleep = detect_category(text, sleep_keywords, "Average")
    stress = detect_category(text, stress_keywords, "Rarely")

    return {
        "sleep_quality": sleep,
        "stress_level": stress
    }

# =========================================
# 3. TF-IDF VECTORIZER (OPTIONAL ADVANCED)
# =========================================

def train_tfidf(corpus):
    vectorizer = TfidfVectorizer(max_features=3000)
    X = vectorizer.fit_transform(corpus)

    joblib.dump(vectorizer, "model/tfidf.pkl")

    return X

def load_tfidf():
    return joblib.load("model/tfidf.pkl")

def transform_text(text, vectorizer):
    text = clean_text(text)
    return vectorizer.transform([text])