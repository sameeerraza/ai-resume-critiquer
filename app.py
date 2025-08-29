import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

from file_handler import extract_text_from_file
from prompt_builder import build_prompt
from gemini_service import analyze_resume

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")
st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("Gemini API key not found. Please set GEMINI_API_KEY in your .env file.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)

uploaded_file = st.file_uploader("Upload your resume (PDF or Word)", type=["pdf", "docx"])
job_role = st.text_input("Enter the job role you're targeting (optional)")
analyze = st.button("Analyze Resume")

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content")
            st.stop()

        prompt = build_prompt(file_content, job_role)

        with st.spinner("Analyzing resume..."):
            response = analyze_resume(prompt)

        st.markdown("### Analysis Results")
        st.write(response.text)

    except FileNotFoundError:
        st.error("Could not process the uploaded file. Please try a different file.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")