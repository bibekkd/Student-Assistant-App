import streamlit as st
import openai

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def suggest_roadmap(domain):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Suggest a study roadmap and courses for someone starting in the domain of {domain}.",
        max_tokens=200
    )
    return response.choices[0].text.strip()

st.title("Suggest Roadmaps and Courses")

domain = st.text_input("Enter the domain")
if st.button("Suggest"):
    roadmap = suggest_roadmap(domain)
    st.write("Suggested Roadmap and Courses:")
    st.write(roadmap)