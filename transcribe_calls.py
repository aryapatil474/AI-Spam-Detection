import whisper
import pandas as pd
from pathlib import Path

# Load the Whisper model (base is a good trade‑off of speed/accuracy)
model = whisper.load_model("base")

# Read your labels CSV
labels_df = pd.read_csv("call_data/call_labels.csv")

records = []
for _, row in labels_df.iterrows():
    file = Path("call_data") / row["filename"]
    print(f"⏳ Transcribing {file.name}…")
    
    # Whisper transcription
    res = model.transcribe(str(file))
    text = res.get("text", "").strip()
    
    records.append({
        "filename": row["filename"],
        "label": row["label"],
        "transcript": text
    })

# Save everything to a new CSV
out_df = pd.DataFrame(records)
out_df.to_csv("call_data/call_transcripts.csv", index=False)
print("✅ Saved transcripts to call_data/call_transcripts.csv")
