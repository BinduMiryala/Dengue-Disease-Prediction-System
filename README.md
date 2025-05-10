# 🦟 Dengue Disease Prediction System

A Django-based web application that predicts the **likelihood of Dengue infection** based on clinical input values using a pre-trained machine learning model. It uses a scaler for preprocessing and displays real-time results as **Positive** or **Negative**.

## 🚀 Features

- 🧠 Machine Learning-powered dengue detection
- 📊 Takes 8 clinical input values from user
- ⚙️ Preprocesses input with a trained scaler
- ✅ Displays "Positive" or "Negative" result
- 🌐 Built with Python, Django, NumPy, Scikit-learn

## 🧪 Input Fields

| Field | Description            |
|-------|------------------------|
| n1    | WBC Count              |
| n2    | RBC Count              |
| n3    | Platelet Count         |
| n4    | Hemoglobin             |
| n5    | Temperature (°C)       |
| n6    | Blood Pressure         |
| n7    | Age (in years)         |
| n8    | Days of Fever          |

## 📁 Project Structure

\```
dengue-disease-predictor/
├── templates/
│   ├── home.html
│   └── predict.html
├── model.pkl
├── scaler.pkl
├── views.py
├── requirements.txt
└── README.md
\```

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/dengue-disease-predictor.git
cd dengue-disease-predictor
