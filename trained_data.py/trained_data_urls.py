import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Load your dataset
df = pd.read_csv("datasets/spam_urls.csv", encoding='latin1')
df.dropna(inplace=True)

X = df.drop(columns=['Result', 'index'], errors='ignore')
y = df['Result'].map({1: 0, -1: 1})  # 0 = safe, 1 = phishing

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForestClassifier model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model and the feature names
with open("models/url_phishing_model.pkl", "wb") as f:
    pickle.dump((model, X_train.columns), f)  # Save both the model and feature names
