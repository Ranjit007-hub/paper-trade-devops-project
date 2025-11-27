from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend (browser) to call backend

# Mock NSE/BSE stock data (in-memory)
stocks = [
    {"symbol": "RELIANCE", "name": "Reliance Industries", "price": 3000.50, "change": 15.25},
    {"symbol": "TCS", "name": "Tata Consultancy Services", "price": 4100.00, "change": -10.10},
    {"symbol": "HDFCBANK", "name": "HDFC Bank", "price": 1650.75, "change": 5.60},
]

@app.route("/")
def home():
    return "PaperTrade backend running"

@app.route("/api/stocks")
def get_stocks():
    return jsonify(stocks)

if __name__ == "__main__":
    app.run(debug=True)
