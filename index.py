from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])

def calculate():
    data = request.get_json()

    a = int(data["a"])
    b = int(data["b"])
    op = data["op"]

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        result = a / b
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)