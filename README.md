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

## 📷 Input and Output Screens
![input page](https://github.com/user-attachments/assets/77059932-2ec7-4281-b5f5-5692d0343627)
![output page](https://github.com/user-attachments/assets/7b244e56-3344-4479-b99a-f6448879b773)

---

## 🧑‍💻 Installation & Setup

### Prerequisites

Before running the system, ensure that you have the following installed:
- Python 3.x (You can download it from https://www.python.org/downloads/)
- Git (For cloning the repository)

### Steps to Install and Run:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/dengue-disease-prediction-system.git
    cd dengue-disease-prediction-system
    ```

2. **Set up a virtual environment (recommended)**:
    Create a virtual environment to isolate dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    Install all necessary libraries using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask web server** (optional, if you want to deploy it as a web app):
    ```bash
    python app.py
    ```
    After starting the server, open your browser and go to [http://localhost:5000](http://localhost:5000).

5. **Training the Model**:
    If you want to retrain the machine learning model with your own data:
    ```bash
    python train_model.py
    ```

6. **Making Predictions**:
    To predict dengue outbreaks using the trained model:
    ```bash
    python predict.py
    ```

---

## 🚀 Features & Highlights

- **Predictive Modeling**: The core of this project uses machine learning models to predict dengue outbreaks based on environmental conditions.
- **Real-time Predictions**: With the Flask app, users can input weather data and get real-time predictions for a potential dengue outbreak.
- **Visualizations**: Visualize the dataset, model performance, and important features using **Matplotlib** and **Seaborn**.
- **Customizable**: The system is built to easily integrate additional weather parameters or different models.

---
