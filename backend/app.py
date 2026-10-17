
from flask import Flask, jsonify
import os
from datetime import datetime, timezone

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "cloud-native-api")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/")
def home():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "message": "Cloud-native API is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


@app.route("/api/info")
def info():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": os.getenv("APP_ENV", "development")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

