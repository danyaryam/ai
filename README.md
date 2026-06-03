# 🧠 Mental Health Screening System

## Late Fusion Deep Learning + NLP + Tabular Data

---

## 📌 Overview

Mental Health Screening System merupakan aplikasi berbasis Machine Learning dan Deep Learning yang bertujuan untuk melakukan **screening awal kondisi kesehatan mental** berdasarkan data survei dan teks pengguna.

Sistem menggunakan pendekatan **Late Fusion**, yaitu menggabungkan dua model berbeda:

1. **Tabular Deep Learning Model**
   - Mengolah data survei kesehatan mental.
   - Fokus output:
     - Treatment: Yes / No

2. **NLP Deep Learning Model**
   - Mengolah input berupa teks.
   - Fokus klasifikasi:
     - Anxiety
     - Depression
     - Normal
     - Suicidal


Output akhir berupa:
- Risk Score
- Severity Level
- Recommendation


> Sistem ini digunakan untuk screening awal dan bukan sebagai pengganti diagnosis profesional.


---

# 🚀 Features

- ✅ Tabular Neural Network
- ✅ NLP Text Classification
- ✅ Custom Neural Network Layer
- ✅ Late Fusion Dynamic Adjustment
- ✅ Risk Score Calculation
- ✅ Severity Classification
- ✅ Recommendation System
- ✅ Flask REST API
- ✅ Model Deployment Ready

---

# 🔥 Late Fusion Method


Karena kedua model memiliki output berbeda:


Tabular:

```
Treatment Probability

Yes / No
```


NLP:

```
Mental Health Class Probability

4 Classes
```


maka probabilitas tidak digabung secara langsung.


Pendekatan:

```
Tabular Model = Confidence Modifier

NLP Model = Main Risk Detector
```


Formula:


```
Final Risk =
(NLP Risk × NLP Weight)
+
(Tabular Confidence × Tabular Weight)
```


Contoh:

```
NLP predicts Depression

+
Survey menunjukkan treatment diperlukan

=
Risk Score meningkat
```


---

# 📂 Project Structure


```
Mental-Health-Screening/

│
├── data/
│   │
│   ├── survey.csv
│   └── mental_health.csv
│
├── models/
│   │
│   ├── tabular_model.keras
│   └── text_model.keras
│
├── notebook/
│   │
│   └── training.ipynb
│
├── api/
│   │
│   └── app.py
│
├── requirements.txt
│
└── README.md

```


---

# ⚙️ Installation


## Clone Repository


```bash
git clone <repository-url>

cd Mental-Health-Screening
```

---

# 📦 Install Dependencies


```bash
pip install -r requirements.txt
```


atau:


```bash
pip install tensorflow
pip install pandas
pip install numpy
pip install scikit-learn
pip install nltk
pip install matplotlib
pip install seaborn
pip install flask
pip install flask-cors
pip install joblib
pip install deep-translator
```


---

# 🧪 Training Model


Jalankan:


```bash
jupyter notebook
```


Buka:


```
late_fusion2.ipynb
```


Training akan menghasilkan:


```
models/

tabular_model.keras

text_model.keras
```

---

---

# 📊 Evaluation


Model evaluation menggunakan:


Classification Metrics:

```
Accuracy
Precision
Recall
F1 Score
Confusion Matrix
```


Target:


```
Accuracy >= 85%
```


---

# 🛠️ Technologies


| Technology | Usage |
|---|---|
| Python | Programming |
| TensorFlow | Deep Learning |
| Keras | Neural Network |
| Scikit-Learn | Data Processing |
| NLP | Text Processing |
| Flask | REST API |
| Pandas | Dataset Processing |
| NumPy | Numerical Processing |


---

# ⚠️ Disclaimer


Aplikasi ini hanya digunakan untuk:

```
Early Mental Health Screening
```


Hasil prediksi bukan merupakan diagnosis medis.

Jika pengguna mengalami kondisi serius, konsultasi dengan profesional kesehatan mental tetap diperlukan.

