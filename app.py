import streamlit as st
from googletrans import Translator
from gtts import gTTS
import io

languages = {
    "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar",
    "Armenian": "hy", "Azerbaijani": "az", "Basque": "eu", "Belarusian": "be",
    "Bengali": "bn", "Bosnian": "bs", "Bulgarian": "bg", "Catalan": "ca",
    "Cebuano": "ceb", "Chinese (Simplified)": "zh-cn", "Chinese (Traditional)": "zh-tw",
    "Croatian": "hr", "Czech": "cs", "Danish": "da",
    "Dutch": "nl", "English": "en", "Esperanto": "eo", "Estonian": "et",
    "Filipino": "tl", "Finnish": "fi", "French": "fr",
    "Galician": "gl", "Georgian": "ka", "German": "de", "Greek": "el",
    "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha", "Hawaiian": "haw",
    "Hebrew": "he", "Hindi": "hi", "Hungarian": "hu",
    "Icelandic": "is", "Igbo": "ig", "Indonesian": "id", "Irish": "ga",
    "Italian": "it", "Japanese": "ja", "Javanese": "jw", "Kannada": "kn",
    "Kazakh": "kk", "Khmer": "km", "Kinyarwanda": "rw", "Korean": "ko",
    "Kurdish (Kurmanji)": "ku", "Kyrgyz": "ky", "Lao": "lo",
    "Latvian": "lv", "Lithuanian": "lt", "Luxembourgish": "lb", "Macedonian": "mk",
    "Malay": "ms", "Malayalam": "ml", "Maltese": "mt",
    "Maori": "mi", "Marathi": "mr", "Mongolian": "mn", "Myanmar": "my",
    "Nepali": "ne", "Norwegian": "no", "Odia": "or",
    "Pashto": "ps", "Persian": "fa", "Polish": "pl", "Portuguese": "pt",
    "Punjabi": "pa", "Romanian": "ro", "Russian": "ru",
    "Serbian": "sr", "Sesotho": "st", "Shona": "sn",
    "Sindhi": "sd", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl",
    "Somali": "so", "Spanish": "es", "Sundanese": "su", "Swahili": "sw",
    "Swedish": "sv", "Tajik": "tg", "Tamil": "ta",
    "Telugu": "te", "Thai": "th", "Turkish": "tr", "Turkmen": "tk",
    "Ukrainian": "uk", "Urdu": "ur", "Uyghur": "ug", "Uzbek": "uz",
    "Vietnamese": "vi", "Welsh": "cy", "Xhosa": "xh", "Yiddish": "yi",
    "Yoruba": "yo", "Zulu": "zu"
}

source_languages = {"Auto Detect": "auto", **languages}

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="wide"
)

st.title("Language Translation Tool")
st.caption(f"Translate text between {len(languages)} popular languages.")

col1, swap_col, col2 = st.columns([5, 1, 5])

with col1:
    source = st.selectbox(
        "Source Language",
        list(source_languages.keys())
    )

with swap_col:
    st.write("")
    if st.button("Swap", use_container_width=True):
        if source != "Auto Detect":
            st.session_state.source = target
            st.session_state.target = source
            st.rerun()

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=list(languages.keys()).index("English")
    )

text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type or paste text here..."
)
st.caption(f"{len(text)} characters")

if st.button("Translate", type="primary", use_container_width=True):

    if text.strip() == "":
        st.warning("Please enter text.")
    elif source != "Auto Detect" and source == target:
        st.info("Choose two different languages to translate.")

    else:
        try:
            translated = Translator().translate(
                text, src=source_languages[source], dest=languages[target]
            )

            st.subheader("Translated Text")
            st.text_area("Result", translated.text, height=180)
            st.download_button(
                "Download translation", translated.text,
                file_name="translation.txt", mime="text/plain"
            )

            try:
                tts = gTTS(translated.text, lang=languages[target])
                audio = io.BytesIO()
                tts.write_to_fp(audio)
                st.audio(audio.getvalue())
            except Exception:
                st.caption("Audio is unavailable for this language.")

        except Exception as e:
            st.error(f"Translation failed: {e}")