import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from features import get_features

data = {
    "url": [
        "https://google.com",
        "https://amazon.in",
        "https://github.com",
        "http://login-bank-verify.tk",
        "http://paypal-secure-login.xyz",
        "http://192.168.1.1/admin",
        "http://freegift-winner.ru"
    ],
    "label": [0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = [get_features(url) for url in df["url"]]
y = df["label"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

with open("phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained successfully!")