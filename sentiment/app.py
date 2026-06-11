from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/analyze/<text>", methods=["POST", "GET"])
def analyze(text):
    t = text.lower()
    if "fantastic" in t or "great" in t or "good" in t:
        sentiment = "positive"
    elif "bad" in t or "poor" in t:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return jsonify({"text": text, "sentiment": sentiment})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
