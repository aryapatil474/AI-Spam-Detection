AI Spam Detection System

An AI-powered application that detects spam in text messages, URLs, and voice messages using Machine Learning and Speech Recognition.
This system helps identify scam calls, fake messages, and malicious links through a simple and interactive web interface.

🔍 Overview

Spam and fraud are becoming increasingly common across emails, messages, links, and phone calls.
This project leverages Machine Learning to analyze input data and classify it as spam or not.

For voice inputs, it uses OpenAI Whisper to convert speech to text before classification.
The web interface is built with Streamlit, making it easy to use for anyone without technical knowledge.

🚀 Features

Detect spam from text messages

Detect spam from URLs

Detect spam from voice/audio files

Powered by trained Machine Learning models

Real-time predictions through a web interface

🛠️ Technologies Used

Python – Main programming language

Streamlit – Web-based interface

OpenAI Whisper – Speech-to-text conversion

Scikit-learn – Machine Learning models

Pandas & NumPy – Data processing

📂 Project Structure
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

💻 Installation & Setup

Clone the repository

git clone https://github.com/aryapatil474/AI-Spam-Detection.git
cd AI-Spam-Detection


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py


Open the browser at http://localhost:8501 to start using the app.

📝 Usage

Text Spam Detection: Enter a message and check if it is spam.

URL Spam Detection: Paste a URL to verify its safety.

Voice Spam Detection: Upload an audio file; the system will transcribe it and detect spam content.

🔧 Future Improvements

Add real-time SMS or call monitoring

Expand dataset for better model accuracy

Integrate multi-language support

Deploy on cloud platforms like Heroku or AWS

🤝 Contributing

Feel free to contribute to this project!
Whether it's improving the models, adding new features, fixing bugs, or enhancing the UI – all contributions are welcome.

To contribute:

Fork the repository

Create a new branch (git checkout -b feature/YourFeature)

Make your changes and commit (git commit -m "Add your feature")

Push to your branch (git push origin feature/YourFeature)

Open a Pull Request

Let's make spam detection smarter together! 🚀

📜 License

This project is licensed under the MIT License – see the LICENSE file for details.
