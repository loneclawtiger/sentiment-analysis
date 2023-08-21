from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

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
    # nltk.download('popular')
    # nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    compound_score = sentiment_scores["compound"]

    if compound_score > 0.05:
        return "Positive"
    elif compound_score < -0.05:
        return "Negative"
    else:
        return "Neutral"


if __name__ == "__main__":
    app.run()
