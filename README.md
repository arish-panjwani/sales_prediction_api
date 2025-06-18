# Sales Prediction API 🚀

This API uses linear regression to predict sales based on temperature and promotions.  
It is containerized with Docker and deployed on Fly.io for minimal-cost, global availability.

---

## 📌 Features
- Predict sales from temperature and promotion inputs  
- CORS enabled  
- Lightweight: 256MB RAM, shared CPU (Fly.io free-tier friendly)  
- Auto-scales down when idle  

---

## ⚙️ Tech Stack
- Python (Flask, scikit-learn, pandas)
- Docker
- Fly.io (deployment)

---

## 🛠 How to run

### 1️⃣ Clone repo
```bash
git clone https://github.com/your-username/sales_prediction_api.git
cd sales_prediction_api
```

### 2️⃣ Create virtual environment (for local use)
```python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Run locally
```
python app.py
```

### 5️⃣ 🚀 Deployment on Fly.io
```
flyctl deploy
```

### Live app
```
https://sales-prediction-api.fly.dev
```

### 📦 Project files
```
app.py — Flask app entry
model.py — Sales predictor logic
requirements.txt — Python dependencies
Dockerfile — Container config
fly.toml — Fly.io deployment config
```

### Example request
POST /predict
```
{
  "temperature": 25.0,
  "promotions": 5.0
}
```
Response:
```
{
  "predicted_sales": 750.45,
  "model_metrics": { ... }
}
```