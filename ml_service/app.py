from flask import Flask, request, jsonify
import joblib 

app = Flask(__name__)
model = None
@app.route("/")
def home():
    return "CMEO API running"

def load_model():
    global model
    model = joblib.load("trained_models/RegressionModel.pkl")


@app.route("/predict", methods=[ "POST"])
def predict():

    data = request.get_json()
    print(data)
    if data is None: 
        return jsonify({'Error': "invalid or missing json body"}), 400
    feature = data.get('features')
    if not feature:
        return jsonify({"error": " features field required"}), 422
    if model is None:
        return jsonify({"error": "model not loaded"}), 500
    try:
        prediction = model.predict([feature])
        return jsonify({
        "prediction": prediction[0]
        }), 200
    except Exception as e: 
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    load_model()
    app.run(debug=True)

