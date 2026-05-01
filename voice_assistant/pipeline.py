import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
from deep_translator import GoogleTranslator
import time

print("Loading Whisper Model..")
model = WhisperModel("small", compute_type="int8",cpu_threads=4)
print("Model ready")

LANGUAGES = {
    "english": "en",
    "hindi": "hi",
    "tamil": "ta",
    "telugu": "te",
    "kannada": "kn",
    "malayalam": "ml",
    "marathi": "mr",
    "bengali": "bn",
    "gujarati": "gu",
    "punjabi": "pa",
    "urdu": "ur",
    "french": "fr",
    "spanish": "es",
    "german": "de",
    "italian": "it",
    "portuguese": "pt",
    "russian": "ru",
    "japanese": "ja",
    "chinese": "zh",
    "korean": "ko",
    "arabic": "ar",
    "turkish": "tr",
    "dutch": "nl",
    "swedish": "sv",
    "polish": "pl",
    "swahili": "sw",
    "vietnamese": "vi",
    "thai": "th",
    "greek": "el",
    "hebrew": "he",
    "indonesian": "id",
    "malay": "ms",
    "filipino": "tl",
    "ukrainian": "uk",
    "czech": "cs",
    "romanian": "ro",
    "hungarian": "hu",
    "finnish": "fi",
    "norwegian": "no",
    "danish": "da"
}
source_name = input("Enter your speaking language (e.g. English, Hindi, Tamil): ")
source_lang = LANGUAGES.get(source_name.lower())

if source_lang is None:
    print(f"'{source_name}' not found in list.")
    print("Find codes at: https://cloud.google.com/translate/docs/languages")
    source_lang = input("Enter language code manually: ")

target_name = input("Enter target language (e.g. Hindi, Tamil, French): ")
target_lang = LANGUAGES.get(target_name.lower())

if target_lang is None:
    print(f"'{target_name}' not found in list.")
    print("Find codes at: https://cloud.google.com/translate/docs/languages")
    target_lang = input("Enter language code manually: ")

translator = GoogleTranslator(source=source_lang, target=target_lang)
print(f"Translating to: {target_name}")

DURATION=3
SAMPLE_RATE=16000

print("\nStarting continuous listening... Press Ctrl+C to stop anytime!")


try:
    while True:
        input("\nPress Enter to start recording... (Ctrl+C to quit)")
        
        print("Recording... Speak now! Press Enter when done.")
        
        recording = []
        
        def callback(indata, frames, time, status):
            recording.append(indata.copy())
        
        stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype=np.float32,
            callback=callback
        )
        
        stream.start()
        input()
        stream.stop()
        stream.close()
        
        print("Processing...")
        
        audio_data = np.concatenate(recording, axis=0).flatten()
        segments, info = model.transcribe(audio_data, beam_size=3, language=source_lang,vad_filter=True, condition_on_previous_text=False)
        original_text = ""
        for segment in segments:
            original_text += segment.text

        
        if original_text.strip() == "":
            print("No speech detected, try again!")
            continue

        word_count = len(original_text.strip().split())
        detected_lang = info.language
        detected_confidence = round(info.language_probability * 100, 1)

        try:
            translated_text = translator.translate(original_text)
        except Exception as e:
            print(f"Translation failed: {e}")
            print("Check your internet connection and try again!")
            continue

        print(f"\nDetected language : {detected_lang} ({detected_confidence}% confident)")
        print(f"Word count        : {word_count} words")
        print(f"Original          : {original_text}")
        print(f"Translated        : {translated_text}")
        print("-" * 40)

except KeyboardInterrupt:
    print("\n\nStopped! Goodbye!")