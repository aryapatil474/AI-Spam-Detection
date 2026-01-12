import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load your full phishing dataset here
df = pd.read_csv("datasets/spam_urls.csv")  # Make sure this CSV has correct feature names

X = df.drop("Result", axis=1)
y = df["Result"]

model = RandomForestClassifier()
model.fit(X, y)

# Save model with feature names
with open("models/url_phishing_model.pkl", "wb") as f:
    pickle.dump((model, X.columns.tolist()), f)
