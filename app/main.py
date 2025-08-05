from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP"})
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Secure API"})

@app.route("/hello/<name>", methods=['GET'])
def hello(name):
    return jsonify({f"hello: {name}"})
if __name__ == '__main__':
    app.run(debug=True)
