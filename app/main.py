from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model and vectorizer
model = joblib.load("app/model.pkl")
vectorizer = joblib.load("app/vectorizer.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define input schema
class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(data: TextInput):
    # Vectorize input text
    X = vectorizer.transform([data.text])
    # Predict sentiment
    pred = model.predict(X)[0]
    label = "Positive" if pred == 0 else "Negative"
    return {"prediction": label}
