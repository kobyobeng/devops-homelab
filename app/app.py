from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

VERSION = "1.0.0"

@app.route("/")
def home():
    return f"""
    <h1>DevOps Homelab</h1>
    <p>Flask application running successfully!</p>
    <p>Hostname: {socket.gethostname()}</p>
    <p>Version: {VERSION}</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/version")
def version():
    return jsonify({
        "version": VERSION
    })

@app.route("/hostname")
def hostname():
    return jsonify({
        "hostname": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
