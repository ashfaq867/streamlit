import gradio as gr
import time
from google.cloud import speech

def transcribe(audio, state=""):
    client = speech.SpeechClient()
    with open(audio, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        state += result.alternatives[0].transcript + " "

    return state, state

gr.Interface(
    fn=transcribe,
    inputs=[
        gr.inputs.Audio(source="microphone", type="filepath"),
        'state'
    ],
    outputs=[
        "textbox",
        "state"
    ],
    live=True).launch()
