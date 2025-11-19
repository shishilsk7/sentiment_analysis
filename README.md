# 🚀 Sentiment Analysis API using FastAPI

This project provides a simple **REST API** for sentiment analysis using a machine learning model trained in Python.  
The API is built with **FastAPI**, and the trained ML model + vectorizer are loaded from `.pkl` files using **joblib**.

---

## 📌 Features
- ✔ Predict sentiment (Positive / Negative) from input text  
- ✔ Lightweight and fast inference  
- ✔ Uses FastAPI for high-performance APIs  
- ✔ Model and vectorizer loaded from `.pkl` files (no retraining)

---

## 🛠 Tech Stack
- **Python 3.8+**
- **FastAPI**
- **Uvicorn**
- **Scikit-Learn**
- **Joblib**

---

## 📁 Project Structure
project/
│── app/
│ ├── main.py
│ ├── model.pkl
│ └── vectorizer.pkl
│── requirements.txt
│── README.md

yaml
Copy code

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone <your-repo-link>
cd project
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
Make sure your requirements.txt contains:

nginx
Copy code
fastapi
uvicorn
scikit-learn
joblib
▶️ Running the API
Start the FastAPI server:

bash
Copy code
uvicorn app.main:app --reload
The server will start at:

cpp
Copy code
http://127.0.0.1:8000
