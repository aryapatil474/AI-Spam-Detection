import streamlit as st
import pickle, tempfile, os
import whisper 
import pandas as pd

from utils.emails_features import extract_email_features
from utils.url_features import enhanced_extract_url_features

# ─── Page Config ─────────────────────────────────────
st.set_page_config(page_title="Spam Detection System", layout="wide")

# ─── Load Models ─────────────────────────────────────
@st.cache_resource
def load_resources():
    whisper_model = whisper.load_model("base")

    with open("models/email_vectorizer.pkl", "rb") as f:
        email_vectorizer = pickle.load(f)
    with open("models/email_spam_model.pkl", "rb") as f:
        email_model = pickle.load(f)

    with open("models/call_vectorizer.pkl", "rb") as f:
        call_vectorizer = pickle.load(f)
    with open("models/call_spam_model_simple.pkl", "rb") as f:
        call_model = pickle.load(f)

    with open("models/url_phishing_model.pkl", "rb") as f:
        url_model , url_feature_names = pickle.load(f)

    return whisper_model, email_vectorizer, email_model, call_vectorizer, call_model, url_model, url_feature_names

whisper_model, email_vec, email_mod, call_vec, call_mod, url_mod, url_feature_names = load_resources()

# ─── App Title ───────────────────────────────────────
st.title("🛡️ AI-Based Spam Detection & Prevention System")
tab1, tab2, tab3 = st.tabs(["📩 Email", "📞 Call", "🔗 URL"])

# ─── Email Tab ───────────────────────────────────────
with tab1:
    st.subheader("📩 Email Spam Detection")
    email_text = st.text_area("Paste your email text here:")

    if st.button("📤 Detect Email Spam") and email_text.strip():
        # Step 1: Vectorize
        X = email_vec.transform([email_text])

        # 🔍 Debug Info
        # st.write("Sample email input:", email_text)
        # st.write("Vectorized shape:", X.shape)
        # st.write("Model expects:", email_mod.n_features_in_)

        # Step 2: Predict
        pred = email_mod.predict(X)[0]
        label = "Spam" if pred == 1 else "Not Spam"

        # Step 3: Display result
        if label == "Spam":
            st.error(f"🚨 Prediction: **{label}**")
        else:
            st.success(f"✅ Prediction: **{label}**")


# ─── Call Tab ────────────────────────────────────────
with tab2:
    st.subheader("📞 Call Spam Detection (Audio Upload Only)")
    audio_file = st.file_uploader("Upload an audio file (.mp3 or .wav)", type=["mp3", "wav"])

    if st.button("🔍 Detect Call Spam"):
        if audio_file:
            ext = ".mp3" if audio_file.type == "audio/mpeg" else ".wav"
            with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
                tmp.write(audio_file.read())
                tmp_path = tmp.name

            st.info("🎙️ Transcribing the uploaded audio...")
            transcript = whisper_model.transcribe(tmp_path)["text"].strip()

            st.subheader("📝 Transcription:")
            st.write(transcript)

            X = call_vec.transform([transcript])
            pred = call_mod.predict(X)[0]
            label = "Spam" if pred == 1 else "Not Spam"

            if label == "Spam":
                st.error(f"🚨 Prediction: **{label}**")
            else:
                st.success(f"✅ Prediction: **{label}**")

            os.remove(tmp_path)
        else:
            st.warning("⚠️ Please upload an audio file first.")

# ─── URL Tab ─────────────────────────────────────────
with tab3:
     st.subheader("🔗 URL Phishing Detection")
     url_input = st.text_input("Enter a URL:")

     if st.button("🔍 Detect URL Phishing"):
        features = enhanced_extract_url_features(url_input.lower())

        # Adjust features to match model input
        n = len(url_feature_names)
        if len(features) < n:
            features += [0] * (n - len(features))
        elif len(features) > n:
            features = features[:n]

        features_df = pd.DataFrame([features], columns=url_feature_names)
        pred = url_mod.predict(features_df)[0]
        label = "Phishing" if pred == 1 else "Safe"

        if label == "Phishing":
            st.error(f"🚨 Prediction: **{label}**")
        else:
            st.success(f"✅ Prediction: **{label}**")