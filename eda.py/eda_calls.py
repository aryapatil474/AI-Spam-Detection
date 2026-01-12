import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

labels_df = pd.read_csv("call_data/call_labels.csv")
transcripts_df = pd.read_csv("call_data/call_transcripts.csv")

print(labels_df.info())
print(transcripts_df.info())

print(labels_df.head())
print(transcripts_df.head())

# Check for missing values
print(labels_df.isnull().sum())
print(transcripts_df.isnull().sum())

# Check class distribution in both datasets
print(labels_df['label'].value_counts())
print(transcripts_df['label'].value_counts())

# Text length distribution
transcripts_df['text_length'] = transcripts_df['transcript'].apply(len)
print(transcripts_df['text_length'].describe())


# Visualizing label distribution
sns.countplot(x='label', data=transcripts_df)
plt.title("Distribution of Spam vs Ham")
plt.show()

# Visualizing text length distribution
sns.histplot(transcripts_df['text_length'], bins=20, kde=True)
plt.title("Distribution of Text Length")
plt.show()

