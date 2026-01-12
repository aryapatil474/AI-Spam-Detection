import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import os
import pickle

# Load email dataset
df = pd.read_csv("datasets/spam_emails.csv", encoding='latin1')[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})
df.dropna(inplace=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# TF-IDF + Logistic Regression
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression(class_weight='balanced')
model.fit(X_train_tfidf, y_train)

# Evaluation
y_pred = model.predict(X_test_tfidf)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred))

# Save model and vectorizer
if not os.path.exists("models"):
    os.makedirs("models")

with open("models/email_spam_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/email_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
