from deep_translator import GoogleTranslator

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
    "polish": "pl"
}
target_name = input("Enter target language name (e.g. Hindi, Tamil, French): ")
target_lang = LANGUAGES.get(target_name.lower())

if target_lang is None:
    print(f"'{target_name}' not found in list.")
    print("You can enter the language code directly.")
    print("Find codes at: https://cloud.google.com/translate/docs/languages")
    target_lang = input("Enter language code manually (e.g. 'af' for Afrikaans): ")

translator = GoogleTranslator(source='auto', target=target_lang)
print(f"Translating to: {target_name}")

text=input("\n Enter the text to translate:")
translated = translator.translate(text)
print(f"\nOriginal  : {text}")
print(f"Translated: {translated}")