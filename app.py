from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Jenkins Docker app is running\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# Auto deploy test Sat Jun 13 02:11:03 PM UTC 2026
