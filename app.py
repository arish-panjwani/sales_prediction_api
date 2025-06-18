from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ import CORS properly
from model import SalesPredictor

app = Flask(__name__)
CORS(app)  # ✅ enable CORS for all routes

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
    app.run(debug=True)
