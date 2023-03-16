# app.py
from flask import Flask, request

app = Flask(__name__)
FLAG = "CTF{simple_web_exploit}"

@app.route("/")
def index():
    return "Welcome to the CTF web exploitation challenge!"

@app.route("/secret", methods=["GET"])
def secret():
    secret_key = request.args.get("key")
    if secret_key == "verysecretkey":
        return FLAG
    else:
        return "Access denied."

if __name__ == "__main__":
    app.run(debug=True)
