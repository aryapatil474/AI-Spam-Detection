import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

# 1. Load transcripts (with labels)
df = pd.read_csv("datasets\call_data\call_transcripts.csv")
df.dropna(subset=["transcript", "label"], inplace=True)
df["y"] = df["label"].map({"ham": 0, "spam": 1})

X = df["transcript"]
y = df["y"]

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Vectorize and train
vectorizer = TfidfVectorizer(stop_words="english")
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf  = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# 4. Evaluate
y_pred = model.predict(X_test_tfidf)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred, target_names=["ham","spam"]))

# 5. Ensure models/ exists
os.makedirs("models", exist_ok=True)

# 6. Save both vectorizer and model
with open("models/call_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
with open("models/call_spam_model_simple.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Saved call_vectorizer.pkl and call_spam_model_simple.pkl in models/")  
