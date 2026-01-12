import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
duration = 5  # seconds

print("🎙️ Recording...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished

write("test_voice.wav", fs, recording)
print("✅ Recording saved as test_voice.wav")
