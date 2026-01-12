# 🛡️ AI Spam Detection System

An AI-powered web application that detects **spam messages, URLs, and voice calls** using **Machine Learning** and **Speech Recognition**.

Built with **Python, Streamlit, Whisper AI, and Scikit-learn**.

---

## 🚀 Features

- 🔍 Detect spam in **text messages**
- 🌐 Detect spam in **URLs**
- 🎤 Detect spam from **voice/audio files**
- 🧠 Uses Machine Learning models for prediction
- 🖥️ Simple and interactive **Streamlit web app**

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- OpenAI Whisper (Speech-to-Text)  
- Scikit-learn  
- Pandas, NumPy  

---

## 📂 Project Structure

AI-Spam-Detection/
│
├── app.py                  # Main Streamlit application
├── models/
│   ├── text_model.pkl      # Trained ML model for text spam detection
│   ├── url_model.pkl       # Trained ML model for URL spam detection
│
├── utils/
│   ├── preprocess.py       # Data preprocessing functions
│   ├── speech_to_text.py   # Converts audio to text using Whisper AI
│
├── assets/
│   ├── logo.png            # Project logo
│   └── example_audio.wav   # Sample audio files for testing
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
