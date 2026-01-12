# generate_calls.py

from gtts import gTTS
from pydub import AudioSegment
import os
import pandas as pd

# 1) Create output directory
output_dir = "call_data"
os.makedirs(output_dir, exist_ok=True)

# 2) Define your texts
spam_texts = [
    "Congratulations! You have won a free vacation to the Bahamas. Press 1 to claim.",
    "This is a limited-time offer for a personal loan with zero interest.",
    "Act now to get your free iPhone. Supplies are limited.",
    "Urgent: Your credit card has been suspended. Call us immediately.",
    "You have been selected for a cash prize. Respond now.",
    "Your loan is approved. Contact us to receive your money.",
    "This is a special offer just for you. Don’t miss it.",
    "Click the link now to claim your reward.",
    "Your account has been compromised. Verify now.",
    "Get a new car with zero down payment. Call today.",
    "Exclusive deal: credit score boost available for a short time.",
    "Claim your free gift card by signing up now.",
    "You're the lucky winner of our monthly jackpot."
]

ham_texts = [
    "Hey, just checking in to see how you’re doing.",
    "Don’t forget to take your medicine after lunch.",
    "Mom is calling, she wants to talk to you.",
    "Your appointment is confirmed for 10 AM tomorrow.",
    "The meeting has been moved to 4 PM.",
    "Dinner is ready, come downstairs.",
    "How was your day at work?",
    "Let’s go for a walk in the evening.",
    "Don’t stay up too late, get some rest.",
    "Reminder: Yoga session starts in 30 minutes.",
    "Good morning! Have a great day ahead.",
    "Don’t forget to water the plants."
]

# 3) Generate audio files and labels
records = []
for i, txt in enumerate(spam_texts):
    mp3 = os.path.join(output_dir, f"spam_{i+1}.mp3")
    wav = os.path.join(output_dir, f"spam_{i+1}.wav")
    tts = gTTS(txt)
    tts.save(mp3)
    AudioSegment.from_mp3(mp3).export(wav, format="wav")
    os.remove(mp3)
    records.append({"filename": f"spam_{i+1}.wav", "label": "spam"})

for i, txt in enumerate(ham_texts):
    mp3 = os.path.join(output_dir, f"ham_{i+1}.mp3")
    wav = os.path.join(output_dir, f"ham_{i+1}.wav")
    tts = gTTS(txt)
    tts.save(mp3)
    AudioSegment.from_mp3(mp3).export(wav, format="wav")
    os.remove(mp3)
    records.append({"filename": f"ham_{i+1}.wav", "label": "ham"})

# 4) Save labels CSV
df = pd.DataFrame(records)
df.to_csv(os.path.join(output_dir, "call_labels.csv"), index=False)

print(f"✅ Generated {len(records)} files in '{output_dir}/' and created call_labels.csv")
