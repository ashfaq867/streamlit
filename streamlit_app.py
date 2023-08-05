import streamlit as st
import time
from transformers import pipeline

p = pipeline("automatic-speech-recognition")

def transcribe(audio, state=""):
    time.sleep(3)
    text = p(audio)["text"]
    state += text + " "
    return state, state

def main():
    st.title("Speech-to-Text App")
    st.write("Click the 'Start Recording' button to start transcribing speech.")

    state = ""
    audio_file = st.file_uploader("Upload audio file (in WAV format)", type=["wav"])

    if audio_file:
        with st.spinner("Transcribing..."):
            state, _ = transcribe(audio_file)
        
        st.subheader("Transcription:")
        st.text(state)

    st.write("NOTE: The transcription may take some time, depending on the length of the audio.")

if __name__ == "__main__":
    main()
