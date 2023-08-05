# !pip install transformers -q

# !pip install gradio -q

from transformers import pipeline

p = pipeline("automatic-speech-recognition")

import gradio as gr
import time

def transcribe(audio, state=""):
    time.sleep(3)
    text = p(audio)["text"]
    state += text + " "
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
