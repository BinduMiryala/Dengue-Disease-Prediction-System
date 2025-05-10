
# 🚨 Dengue Disease Prediction System 🚨

## 🔍 Project Overview

The **Dengue Disease Prediction System** is a machine learning-based tool designed to predict the likelihood of dengue outbreaks using key environmental factors. By analyzing weather data such as temperature, humidity, and rainfall, the system helps forecast dengue outbreaks in a given region. This early warning allows health authorities to take timely action, reducing the impact of dengue and saving lives.

---

## ⚙️ Technologies & Tools

| **Category**            | **Tools & Libraries**                                      |
|-------------------------|------------------------------------------------------------|
| **Programming Language** | Python 🐍                                                   |
| **Machine Learning**     | - Scikit-learn (for machine learning algorithms)          |
| **Data Analysis**        | - Pandas (data manipulation)                               |
|                         | - NumPy (numerical computations)                           |
| **Visualization**        | - Matplotlib (data visualization)                          |
|                         | - Seaborn (advanced visualizations)                        |
| **Web Framework**        | - Flask (for web app deployment)                          |
| **Model Serialization**  | - Joblib (to save/load models)                             |
| **Database**             | - SQLite/MySQL (optional for storing data)                |
| **Version Control**      | - Git (source code management)                             |

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

## 📊 Data Preprocessing

The system requires historical weather data to make accurate predictions. This data typically includes:
- **Temperature** (°C)
- **Humidity** (%)
- **Rainfall** (mm)
- **Dengue Outbreak Status** (0 = No outbreak, 1 = Outbreak)

The `data_preprocessing.py` script handles:
- Data cleaning (removing missing values).
- Feature engineering (e.g., encoding categorical variables if needed).
- Feature scaling (normalizing data for better model performance).

You can replace the data in the `data` folder with your own CSV file that contains the weather data.

---

## 🚀 Features & Highlights

- **Predictive Modeling**: The core of this project uses machine learning models to predict dengue outbreaks based on environmental conditions.
- **Real-time Predictions**: With the Flask app, users can input weather data and get real-time predictions for a potential dengue outbreak.
- **Visualizations**: Visualize the dataset, model performance, and important features using **Matplotlib** and **Seaborn**.
- **Customizable**: The system is built to easily integrate additional weather parameters or different models.

---

## 📁 Project Structure

