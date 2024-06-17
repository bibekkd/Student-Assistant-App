import streamlit as st
import openai
from pymongo import MongoClient
from PIL import Image
import pytesseract
from moviepy.editor import VideoFileClip
from pytube import YouTube
import whisper
import os

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Initialize OpenAI API
openai.api_key = 'your_openai_api_key'

# Initialize MongoDB Client
client = MongoClient('your_cosmos_db_connection_string')
db = client['study_materials_db']
collection = db['materials']

# Initialize Whisper model
model = whisper.load_model("base")

def summarize_text(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Summarize the following text:\n\n{text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def suggest_quizzes_and_questions(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Based on the following study material, suggest quizzes and questions:\n\n{text}",
        max_tokens=200
    )
    return response.choices[0].text.strip()

def transcribe_video(video_path):
    result = model.transcribe(video_path)
    return result['text']

def store_material(content, metadata):
    summary = summarize_text(content)
    metadata['summary'] = summary
    collection.insert_one(metadata)

def predict_future_questions(previous_questions):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Based on the following previous year questions, predict future questions:\n\n{previous_questions}",
        max_tokens=200
    )
    return response.choices[0].text.strip()

st.title("Study Material and Exam Preparation")
st.write('---')
# Section 1: Upload and Summarize Study Material
st.subheader("Upload and Summarize Study Material")
uploaded_file = st.file_uploader("Choose a file", type=["txt", "jpg", "jpeg", "png", "mp4", "avi", "mov"])
video_url = st.text_input("Or enter a YouTube video URL")

if uploaded_file is not None or video_url:
    if uploaded_file is not None:
        if uploaded_file.type in ["image/jpeg", "image/png", "image/jpg"]:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            text = pytesseract.image_to_string(image)
            st.write("Extracted Text:")
            st.write(text)
        elif uploaded_file.type in ["video/mp4", "video/avi", "video/mov"]:
            video_path = f"temp_video.{uploaded_file.type.split('/')[-1]}"
            with open(video_path, "wb") as f:
                f.write(uploaded_file.read())
            text = transcribe_video(video_path)
            os.remove(video_path)
            st.write("Transcribed Text:")
            st.write(text)
        else:
            content = uploaded_file.read().decode("utf-8")
            st.write("Uploaded Text File Content:")
            st.write(content)
            text = content
    elif video_url:
        yt = YouTube(video_url)
        video_stream = yt.streams.filter(only_audio=True).first()
        video_path = video_stream.download(filename="temp_video.mp4")
        text = transcribe_video(video_path)
        os.remove(video_path)
        st.write("Transcribed Text from YouTube Video:")
        st.write(text)

    metadata = {"filename": uploaded_file.name if uploaded_file else video_url}
    store_material(text, metadata)
    st.write("File uploaded and summarized successfully!")

    quizzes_and_questions = suggest_quizzes_and_questions(text)
    st.write("Suggested Quizzes and Questions:")
    st.write(quizzes_and_questions)

st.button("Generate")
st.write("----")

# Section 2: Predict Future Exam Questions
st.subheader("Predict Future Exam Questions")
uploaded_questions_file = st.file_uploader("Upload previous year questions", type=["txt", "jpg", "jpeg", "png"])

if uploaded_questions_file is not None:
    if uploaded_questions_file.type in ["image/jpeg", "image/png", "image/jpg"]:
        image = Image.open(uploaded_questions_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        previous_questions = pytesseract.image_to_string(image)
        st.write("Extracted Text:")
        st.write(previous_questions)
    else:
        previous_questions = uploaded_questions_file.read().decode("utf-8")
        st.write("Uploaded Text File Content:")
        st.write(previous_questions)

    if st.button("Predict"):
        future_questions = predict_future_questions(previous_questions)
        st.write("Predicted Future Questions:")
        st.write(future_questions)

st.button("Predict")
