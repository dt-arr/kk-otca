# quote_service/frontend/app.py (Python Flask frontend)

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BACKEND_URL = "http://localhost:8080"

@app.route("/quote", methods=["GET"])
def get_quote():
    # with tracer.start_as_current_span("get_quote"):
    response = requests.get(f"{BACKEND_URL}/quote")
    return jsonify(response.json())

@app.route("/quote", methods=["POST"])
def add_quote():
    new_quote = request.json.get("quote")
    # with tracer.start_as_current_span("add_quote"):
    response = requests.post(f"{BACKEND_URL}/quote", json={"quote": new_quote})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(port=5000, debug=True)
