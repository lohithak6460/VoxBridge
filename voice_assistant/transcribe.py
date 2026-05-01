import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import time

print("Loading Whisper Model..")
model = WhisperModel("small", compute_type="int8")
print("Model ready")

DURATION=5
SAMPLE_RATE=16000

print("Recording in 3 seconds... get ready!")
time.sleep(3)
print("Speak now! Recording for 5 seconds...")
audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype=np.float32
)
sd.wait()
print("Recording done!")
print("Thinking...")
audio_data = audio.flatten()
segments, info = model.transcribe(audio_data, beam_size=5)

print("\n--- What you said ---")
for segment in segments:
    print(segment.text)
    