### Import libraries
import streamlit as st
import os
import pandas as pd
import requests
import re

from transformers import AutoProcessor, AutoModelForVision2Seq, pipeline
from PIL import Image
import torch
import pyttsx3


### Load image-to-text model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = AutoModelForVision2Seq.from_pretrained("Salesforce/blip-image-captioning-base")

### Load story maker model

generator = pipeline("text-generation", model="gpt2")

def generate_story(description):
    prompt = f"Complete the following idea with a creative and happy very short story based on this description: {description}. Once upon a time..."""
    response = generator(prompt, max_length=200, num_return_sequences=1)
    story = response[0]['generated_text']
    modified_story = re.sub(f"Complete the following idea with a creative and happy very short story based on this description: {description}. Once upon a time...",'', story)
    return modified_story


### Load text-to-speech library
def generate_audio(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


### Start app
st.title('Stories maker✨')
st.subheader('Create your own stories based on your image!!')


upload_image = st.file_uploader('Upload your image here', type=['jpg', 'png', 'jpeg'])

if upload_image is not None:
    image = Image.open(upload_image).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    generated_ids = model.generate(
        **inputs,
        max_length=100,
        num_beams=5,        
        repetition_penalty=2.0,  
        length_penalty=1.5, 
        temperature=1,     
        top_p=0.5           
    )
    caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    st.text(f'Your image is about: {caption}')

    modified_story = generate_story(caption)
    st.text("Once upon time...:")
    st.write(modified_story)

    st.audio(generate_audio(modified_story), format='audio/mp3')



