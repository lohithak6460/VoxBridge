import streamlit as st
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
from deep_translator import GoogleTranslator

# Page config
st.set_page_config(
    page_title="VoxBridge",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ VoxBridge")
st.markdown("Time-Constrained English Speech-to-Multilingual Translation System")
st.divider()

# Language dictionary
LANGUAGES = {
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Urdu": "ur",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Chinese": "zh",
    "Korean": "ko",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Swedish": "sv",
    "Polish": "pl",
    "Swahili": "sw",
    "Vietnamese": "vi",
    "Thai": "th",
    "Greek": "el",
    "Hebrew": "he",
    "Indonesian": "id",
    "Malay": "ms",
    "Filipino": "tl",
    "Ukrainian": "uk",
    "Czech": "cs",
    "Romanian": "ro",
    "Hungarian": "hu",
    "Finnish": "fi",
    "Norwegian": "no",
    "Danish": "da"
}

# Source language locked to English
source_lang = "en"

# Target language dropdown
target_name = st.selectbox("🌍 Translate To", list(LANGUAGES.keys()))
target_lang = LANGUAGES[target_name]

st.divider()

# Load Whisper model once
@st.cache_resource
def load_model():
    return WhisperModel("small", compute_type="int8", cpu_threads=4)

model = load_model()

# Recording settings
SAMPLE_RATE = 16000
DURATION = st.slider("⏱️ Recording Duration (seconds)", 3, 30, 5)

# Start recording button
if st.button("🎤 Start Recording", use_container_width=True):

    with st.spinner(f"🔴 Recording for {DURATION} seconds... Speak now!"):
        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype=np.float32
        )
        sd.wait()

    with st.spinner("💭 Transcribing your speech..."):
        audio_data = audio.flatten()
        segments, info = model.transcribe(
            audio_data,
            beam_size=3,
            language=source_lang,
            vad_filter=True,
            condition_on_previous_text=False
        )

        original_text = ""
        for segment in segments:
            original_text += segment.text

    with st.spinner("🌍 Translating..."):
        try:
            translated_text = GoogleTranslator(
                source=source_lang,
                target=target_lang
            ).translate(original_text)
        except Exception as e:
            st.error(f"Translation failed: {e}")
            translated_text = ""

    if original_text.strip() != "":
        st.divider()

        confidence = round(info.language_probability * 100, 1)
        word_count = len(original_text.strip().split())

        st.caption(f"✅ Confidence: {confidence}% | Words: {word_count}")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🗣️ Original")
            st.write(original_text)
        with col2:
            st.subheader(f"🌍 {target_name}")
            st.write(translated_text)
            st.code(translated_text, language=None)

        if "history" not in st.session_state:
            st.session_state.history = []

        st.session_state.history.append({
            "original": original_text,
            "translated": translated_text,
            "language": target_name
        })

    else:
        st.warning("⚠️ No speech detected! Please try again.")

# Translation history
if "history" in st.session_state and len(st.session_state.history) > 0:
    st.divider()
    st.subheader("📜 Translation History")

    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.rerun()

    for item in reversed(st.session_state.history):
        with st.expander(f"🌍 {item['language']} — {item['original'][:30]}..."):
            col1, col2 = st.columns(2)
            with col1:
                st.caption("🗣️ Original")
                st.write(item["original"])
            with col2:
                st.caption("🌍 Translated")
                st.write(item["translated"])
                st.code(item["translated"], language=None)