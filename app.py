from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/time")
def get_time():
    # Return current server time
    now = datetime.now().strftime("%H:%M:%S")
    return jsonify({"time": now})

if __name__ == "__main__":
    app.run(debug=False)
