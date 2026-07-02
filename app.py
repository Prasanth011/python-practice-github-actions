from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to My Flask App!"

@app.route("/about")
def about():
    return "This is a sample Flask application."

@app.route("/api/user")
def user():
    return jsonify({
        "id": 1,
        "name": "Sai Prasanth",
        "role": "DevOps Engineer"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
