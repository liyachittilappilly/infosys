import pyttsx3
import os

# output folder
os.makedirs("reference_audio", exist_ok=True)

engine = pyttsx3.init()
engine.setProperty("rate", 150)   # slow & clear
engine.setProperty("volume", 1.0)

sentences = [
    "cat",
    "bat",
    "rat",
    "she sells sea shells"
]

for i, text in enumerate(sentences):
    out_path = f"reference_audio/ref_{i}.wav"
    engine.save_to_file(text, out_path)
    print("Saved:", out_path)

engine.runAndWait()
