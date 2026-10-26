"""Cloud-native demo service for the CI/CD practical."""
import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "dev")


@app.route("/")
def index():
    return jsonify(
        message="Hello from the CI/CD pipeline!",
        version=VERSION,
        pod=socket.gethostname(),
    )


@app.route("/health")
def health():
    return jsonify(status="ok")


def add(a, b):
    return a + b


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
