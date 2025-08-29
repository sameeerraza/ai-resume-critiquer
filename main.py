# import streamlit as st
# from PyPDF2 import PdfReader
# from docx import Document
# import io
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()

# st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")
#
# st.title("AI Resume Critiquer")
# st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#
# uploaded_file = st.file_uploader("Upload your resume (PDF or Word)", type=["pdf", "docx"])
# job_role = st.text_input("Enter the job role you're targeting (optional)")
#
# analyze = st.button("Analyze Resume")

# def extract_text_from_pdf(pdf_file):
#     reader = PdfReader(pdf_file)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text() or ""
#     return text
#
# def extract_text_from_file(uploaded_file):
#     if uploaded_file.type == "application/pdf":
#         return extract_text_from_pdf(io.BytesIO(uploaded_file.getvalue()))
#     elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
#         doc = Document(io.BytesIO(uploaded_file.getvalue()))
#         return "\n".join([p.text for p in doc.paragraphs])
#     else:
#         return uploaded_file.getvalue().decode("utf-8", errors="ignore")

# if analyze and uploaded_file:
#     try:
#         file_content = extract_text_from_file(uploaded_file)
#
#         if not file_content.strip():
#             st.error("File does not have any content")
#             st.stop()

        # prompt = f"""
        # You are a professional career coach and resume reviewer.
        # Analyze the following resume and provide detailed, constructive feedback.
        #
        # Focus on these areas:
        # 1. **Content clarity & overall impact** – Is the information easy to understand and compelling?
        # 2. **Skills presentation** – Are skills highlighted effectively and aligned with {job_role if job_role else 'general job applications'}?
        # 3. **Experience descriptions** – Do the work experiences demonstrate achievements, quantify results, and match the expectations for {job_role if job_role else 'target roles'}?
        # 4. **Tailoring & improvements** – What specific changes would strengthen the resume for {job_role if job_role else 'general job applications'}?
        #
        # Resume content:
        # {file_content}
        #
        # Please provide your feedback in a **clear, structured format** with:
        # - Strengths (what is working well)
        # - Weaknesses (what needs improvement)
        # - Actionable recommendations (specific edits, rewording suggestions, or additions)
        # """

        # genai.configure(api_key=GEMINI_API_KEY)
        # model = genai.GenerativeModel("gemini-1.5-flash")

        # with st.spinner("Analyzing resume..."):
        #     response = model.generate_content(prompt,generation_config={"temperature": 0.7,"max_output_tokens": 1000})

        # st.markdown("### Analysis Results")
        # st.write(response.text)

    # except Exception as e:
    #     st.error(f"An error occurred: {str(e)}")