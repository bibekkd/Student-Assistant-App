import streamlit as st

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Welcome to Studius.ai 👋")


st.write(' ')
st.image('bgimg.png')
# st.video("video1.mp4", autoplay=True, loop=True)

st.write("  ")

# Define the CSS styles
css = """
<style>
body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f9;
    color: #333;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

.app-description {
    max-width: 1000px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 70px;
    box-shadow: 0 0 100px rgba(227, 335, 70, 0.2);
}

.app-description h2 {
    font-size: 2.5em;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 20px;
}

.app-description p {
    font-size: 1.2em;
    margin-bottom: 20px;
}

.app-description ul {
    list-style-type: disc;
    padding-left: 20px;
}

.app-description ul li {
    font-size: 1.1em;
    margin-bottom: 10px;
}

.app-description ul li::marker {
    color: #3498db;
}

.app-description p:last-of-type {
    font-weight: bold;
    text-align: center;
}
</style>
"""

# Define the HTML content
html = """
<div class="app-description">
    <h2>About This App</h2>
    <p>This Study Material Upload and Summarization app is designed to help students and educators manage and summarize study materials efficiently. With this app, you can:</p>
    <ul>
        <li>Upload study materials in various formats including text, images, and videos.</li>
        <li>Automatically generate summaries of the uploaded content using advanced AI algorithms.</li>
        <li>Transcribe videos from YouTube links or other video sources.</li>
        <li>Receive suggestions for quizzes and questions based on the study material.</li>
        <li>Predict future exam questions based on previous year questions.</li>
    </ul>
    <p>Our goal is to make studying more efficient and effective by leveraging the power of AI and modern technology. We hope you find this app useful and easy to use!</p>
</div>
"""

# Render the CSS and HTML in Streamlit
st.markdown(css, unsafe_allow_html=True)
st.markdown(html, unsafe_allow_html=True)



