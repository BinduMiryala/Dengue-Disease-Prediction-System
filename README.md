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
| n1    | Age                    |
| n2    | Systolic BP            |
| n3    | Diastolic BP           |
| n4    | Blood sugar            |
| n5    | Body Temperature       |
| n6    | Heart Rate             |
| n7    | Platelet Count         |
| n8    | WBC Count              |

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/dengue-disease-predictor.git
cd dengue-disease-predictor
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run Django Server
bash
Copy
Edit
python manage.py runserver
5. Open the App
Visit http://127.0.0.1:8000 in your browser.
