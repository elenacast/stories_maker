# Story maker

This project is a web application designed to create short, creative stories based on user-uploaded images. The application uses several machine learning models and libraries to achieve this functionality. Here is a detailed description:

Objective

* The objective of this project is to allow users to upload an image and receive a short, creative story based on the content of the image. The application also provides an audio version of the generated story.

Models and Libraries Used:

* Streamlit: Used to create the web application interface.

* Transformers: Specifically, the AutoProcessor and AutoModelForVision2Seq from the transformers library are used for image captioning.

* Image-to-Text Model: Salesforce/blip-image-captioning-base is used to generate a textual description of the uploaded image.

* GPT-2: Used for text generation to create a story based on the image description.

* PIL (Python Imaging Library): Used to handle image processing.

* Pyttsx3: Used for text-to-speech conversion to generate audio from the text story.




Workflow

* Image Upload: Users upload an image through the Streamlit interface.

* Image Captioning: The uploaded image is processed using the Salesforce/blip-image-captioning-base model to generate a caption describing the image.

* Story Generation: The generated caption is used as a prompt for the GPT-2 model to create a short, creative story.

* Text-to-Speech: The generated story is converted to audio using the pyttsx3 library.

* Display and Audio: The caption, story, and audio are displayed on the Streamlit interface.




Example Usage

* User uploads an image.

* The application generates a caption like "A cat sitting on a windowsill."

* The application then generates a (happy) story based on the caption.

* The story is displayed and an audio version is provided.

