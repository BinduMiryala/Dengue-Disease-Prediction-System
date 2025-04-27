import joblib
import numpy as np
from django.shortcuts import render
def home(request):
    return render(request,"home.html")
def predict(request):
    return render(request,"predict.html")
import os
# ✅ Load Pre-trained Model & Scaler
model_path = os.path.join(os.path.dirname(__file__), "../model.pkl")
model = joblib.load(model_path)  # Load trained model
scaler_path = os.path.join(os.path.dirname(__file__), "../scaler.pkl")
scaler = joblib.load(scaler_path)  # Load the trained scaler  # Load trained scaler

def result(request):
    if request.method == "POST":
        # Get User Inputs from the Form
        val1 = float(request.POST.get('n1', 0))
        val2 = float(request.POST.get('n2', 0))
        val3 = float(request.POST.get('n3', 0))
        val4 = float(request.POST.get('n4', 0))
        val5 = float(request.POST.get('n5', 0))
        val6 = float(request.POST.get('n6', 0))
        val7 = float(request.POST.get('n7', 0))
        val8 = float(request.POST.get('n8', 0))

        # Convert Inputs to NumPy Array
        user_input = np.array([[val1, val2, val3, val4, val5, val6, val7, val8]])

        # Scale Input Using Pre-trained Scaler
        user_input_scaled = scaler.transform(user_input)
        pred=model.predict(user_input_scaled)
        result1="Positive" if pred[0] == 1 else "Negative"
        return render(request,"predict.html",{"result2":result1})
    return render(request,"predict.html",{"result2":"No inputs received"})
