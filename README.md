# Language Translation Tool

An interactive Streamlit website for translating text between 100 popular languages.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open the app at `http://localhost:8502`.

## Notes

- Translation uses Google Translate through `googletrans`.
- Text-to-speech is generated with `gTTS` when the selected language is supported.
- An internet connection is required for translation and audio generation.
