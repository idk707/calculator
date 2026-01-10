from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])

def calculate():
    return