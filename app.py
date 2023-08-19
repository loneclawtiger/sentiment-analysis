from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import subprocess

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/analyze_sentiment", methods=["POST"])
@cross_origin()
def analyze_sentiment():
    text = request.json.get("text")
    result = analyze_sentiment_with_python_script(text)
    return jsonify({"result": result})


def analyze_sentiment_with_python_script(text):
    # Call your Python sentiment analysis script here
    # For demonstration purposes, I'm using a simple echo command
    cmd = f'echo "{text}"'
    result = subprocess.check_output(cmd, shell=True, text=True)
    return result.strip()


if __name__ == "__main__":
    app.run()
