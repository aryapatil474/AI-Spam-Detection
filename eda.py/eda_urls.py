import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load URL dataset
urls_df = pd.read_csv("datasets\spam_urls.csv", encoding='latin1')

# Handle missing values
print("Missing values in URL dataset:")
print(urls_df.isnull().sum())

# Class distribution
print("\nPhishing vs Legitimate:")
print(urls_df['Result'].value_counts())

# Plot: Class distribution
plt.figure(figsize=(6, 4))
sns.countplot(x=urls_df['Result'].map({1: "Legitimate", -1: "Phishing"}), palette='coolwarm')
plt.title("Phishing vs Legitimate URLs")
plt.xlabel("URL Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Correlation heatmap (first 10 features for readability)
plt.figure(figsize=(10, 8))
sns.heatmap(urls_df.iloc[:, 1:11].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation (First 10 Features)")
plt.tight_layout()
plt.show()
