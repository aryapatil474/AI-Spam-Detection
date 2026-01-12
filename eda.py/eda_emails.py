import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean email dataset
emails_df = pd.read_csv("datasets\spam_emails.csv", encoding='latin1')[['v1', 'v2']]
emails_df.columns = ['label', 'message']

# Handle missing values
print("Missing values in email dataset:")
print(emails_df.isnull().sum())

# Basic stats
emails_df['text_length'] = emails_df['message'].apply(len)
print("\nText Length Statistics:")
print(emails_df['text_length'].describe())

# Class distribution
print("\nClass Distribution:")
print(emails_df['label'].value_counts())

# Plot: Class distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='label', data=emails_df, palette='Set2')
plt.title("Email Spam vs Ham Count")
plt.xlabel("Label")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Plot: Message length distribution
plt.figure(figsize=(6, 4))
sns.histplot(emails_df['text_length'], bins=50, kde=True, color='skyblue')
plt.title("Email Message Length Distribution")
plt.xlabel("Length of Message")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

