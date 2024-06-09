import streamlit as st
import openai
from pymongo import MongoClient
from PIL import Image
import pytesseract

# Initialize OpenAI API
openai.api_key = 'your_openai_api_key'

# Initialize MongoDB Client
client = MongoClient('your_cosmos_db_connection_string')
db = client['study_materials_db']
collection = db['report_cards']

def analyze_report_card(report_card):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Analyze the following report card and provide strengths, weaknesses, study tips, and course suggestions:\n\n{report_card}",
        max_tokens=300
    )
    return response.choices[0].text.strip()

def store_report_card(report_card, analysis):
    collection.insert_one({'report_card': report_card, 'analysis': analysis})

st.title("Report Card Analysis")

uploaded_file = st.file_uploader("Upload a report card", type=["txt", "jpg", "jpeg", "png"])
if uploaded_file is not None:
    if uploaded_file.type in ["image/jpeg", "image/png", "image/jpg"]:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        report_card = pytesseract.image_to_string(image)
        st.write("Extracted Text:")
        st.write(report_card)
    else:
        report_card = uploaded_file.read().decode("utf-8")
        st.write("Uploaded Text File Content:")
        st.write(report_card)

    if st.button("Analyze"):
        analysis = analyze_report_card(report_card)
        store_report_card(report_card, analysis)
        st.write("Analysis:")
        st.write(analysis)
        st.write("Report card analyzed and stored successfully!")