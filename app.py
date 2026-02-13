import streamlit as st
import os
from analyze_call import analyze_with_ollama
from transcribe import transcribe_audio


st.set_page_config(page_title="AI Call Analyzer", page_icon="🎧")

st.title("🎧 AI Call Analyzer")
st.write("Upload a call recording and get AI-powered insights.")


uploaded_file = st.file_uploader(
    "Upload Audio File",
    type=["wav", "mp3", "m4a"]
)


if uploaded_file is not None:

    # Save uploaded file temporarily
    temp_path = os.path.join(os.getcwd(), uploaded_file.name)

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ File uploaded successfully!")

    if st.button("Analyze Call"):

        with st.spinner("🔊 Transcribing audio..."):
            transcript = transcribe_audio(temp_path)

        st.subheader("📄 Transcript")
        st.write(transcript)

        with st.spinner("🧠 Analyzing with AI..."):
            analysis = analyze_with_ollama(transcript)

        st.subheader("🤖 AI Call Insights")
        st.write(analysis)
