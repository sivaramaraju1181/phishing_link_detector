import os
import pickle
from flask import Flask, render_template, request
from features import get_features

app = Flask(__name__)

with open("phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        url = request.form.get("url")

        try:
            features = [get_features(url)]
            prediction = model.predict(features)[0]

            if prediction == 1:
                result = "⚠️ Phishing Website (Unsafe)"
            else:
                result = "✅ Legitimate Website (Safe)"

        except:
            result = "❌ Invalid URL"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)