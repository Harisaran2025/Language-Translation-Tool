import streamlit as st
from googletrans import Translator
from gtts import gTTS
import io

# Translator
translator = Translator()

# Languages
languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-cn",
    "Korean": "ko",
    "Arabic": "ar",
    "Russian": "ru",
    "Italian": "it",
    "Portuguese": "pt"
}

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translation Tool")

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

text = st.text_area(
    "Enter Text",
    height=180
)

if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter text.")

    else:
        try:

            translated = translator.translate(
                text,
                src=languages[source],
                dest=languages[target]
            )

            st.subheader("Translated Text")

            st.text_area(
                "",
                translated.text,
                height=180
            )

            st.code(translated.text)

            tts = gTTS(
                translated.text,
                lang=languages[target]
            )

            audio = io.BytesIO()
            tts.write_to_fp(audio)

            st.audio(audio.getvalue())

        except Exception as e:
            st.error(e)