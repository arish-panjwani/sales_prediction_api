from flask import Flask, request, jsonify
from flask_cors import CORS
from model import SalesPredictor
import os  # ✅ import os for environment variables

app = Flask(__name__)
CORS(app)

predictor = SalesPredictor("Preprocessed-v2.csv")

@app.route("/")
def home():
    return "Sales Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict_sales():
    data = request.get_json()
    try:
        temperature = float(data["temperature"])
        promotions = float(data["promotions"])
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "Please provide valid 'temperature' and 'promotions' values."}), 400

    sales_pred = predictor.predict(temperature, promotions)
    return jsonify({
        "predicted_sales": round(sales_pred, 2),
        "model_metrics": predictor.metrics
    })

if __name__ == "__main__":
    # ✅ Bind to 0.0.0.0 and dynamic PORT for Fly.io
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
