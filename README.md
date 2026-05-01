 🎙️ VoxBridge
 Time-Constrained English Speech-to-Multilingual Translation System

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![Whisper](https://img.shields.io/badge/Whisper-faster--whisper-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

📌 Overview

VoxBridge is a real-time voice translation system that captures English speech through a microphone, transcribes it using OpenAI's Whisper AI model, and translates it into 39+ languages instantly — all through a clean, browser-based interface built with Streamlit.

This project demonstrates the integration of state-of-the-art speech recognition, neural machine translation, and interactive web UI development using pure Python.

---

## 🚀 Features

- 🎤 **Real-time voice recording** — configurable duration (3–30 seconds)
- 🧠 **AI-powered transcription** — using faster-whisper (small model, int8 optimized)
- 🌍 **39+ language translation** — powered by Google Translate API
- ✅ **Confidence scoring** — shows how accurately speech was detected
- 📊 **Word count** — tracks transcription length per session
- 📋 **One-click copy** — instantly copy translated text to clipboard
- 📜 **Translation history** — view all translations within the session
- 🗑️ **Clear history** — reset session translations with one click

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.11+ |
| Speech to Text | faster-whisper (OpenAI Whisper small model) |
| Translation | deep-translator (Google Translate) |
| Web UI | Streamlit |
| Audio Capture | sounddevice |
| Audio Processing | NumPy |

---

## 📂 Project Structure


```
VoxBridge/
├── voice_assistant/
│   ├── app.py            ← Main Streamlit web app
│   ├── transcribe.py     ← Speech to text module
│   ├── translator.py     ← Translation module
│   └── pipeline.py       ← Terminal pipeline
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation & Setup

**Step 1 — Clone the repository**
```bash
git clone https://github.com/lohithak6460/VoxBridge.git
cd VoxBridge
```

**Step 2 — Install all dependencies**
```bash
pip install -r requirements.txt
```

**Step 3 — Run the app**
```bash
streamlit run voice_assistant/app.py
```

**Step 4 — Open in browser**
> ⚠️ First run will automatically download the Whisper small model (~465MB). This is a one-time download.

---

## 🎯 How to Use

1. Open the app in your browser
2. Select your target language from the dropdown
3. Adjust recording duration using the slider (3–30 seconds)
4. Click **🎤 Start Recording**
5. Speak clearly in English
6. Wait for transcription and translation to complete
7. View original and translated text side by side
8. Copy translated text with one click
9. View all previous translations in Translation History

---

## 🌍 Supported Languages (39+)

| Region | Languages |
|---|---|
| Indian | Hindi, Tamil, Telugu, Kannada, Malayalam, Marathi, Bengali, Gujarati, Punjabi, Urdu |
| European | French, Spanish, German, Italian, Portuguese, Russian, Dutch, Swedish, Polish, Greek, Czech, Romanian, Hungarian, Finnish, Norwegian, Danish, Ukrainian |
| Asian | Japanese, Chinese, Korean, Vietnamese, Thai, Indonesian, Malay, Filipino, Hebrew, Arabic, Turkish |
| African | Swahili |

---

## 📊 System Architecture
```
Microphone Input
↓
sounddevice (Audio Capture at 16kHz)
↓
NumPy (Audio Array Processing)
↓
faster-whisper small model (Speech to Text)
↓
deep-translator Google API (Translation)
↓
Streamlit (Web UI Display)
```

## 💻 System Requirements

- Python 3.11 or higher
- Working microphone
- Internet connection (for translation)
- Minimum 4GB RAM recommended
- Windows / Mac / Linux

---

## ⚠️ Known Limitations

- Currently supports English as source language only
- Requires active internet connection for translation
- Processing time varies based on CPU speed and recording duration
- Indian language speech input support planned for future release

---

## 🔮 Future Improvements

- [ ] Add Indian language input using AI4Bharat IndicWhisper model
- [ ] Add text input option alongside voice recording
- [ ] Add Text-to-Speech playback of translated output
- [ ] Support real-time streaming transcription
- [ ] Export translations to PDF or Word document
- [ ] Add speaker diarization for multi-speaker conversations

---

## 👩‍💻 Author

**K Lohitha**
GitHub: [@lohithak6460](https://github.com/lohithak6460)

---

## 📄 License

This project is licensed under the MIT License — feel free to use and modify.

---

⭐ If you found this project helpful, please consider giving it a star on GitHub!
