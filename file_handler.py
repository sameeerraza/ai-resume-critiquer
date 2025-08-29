from PyPDF2 import PdfReader
from docx import Document
import io

def extract_text_from_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        raise ValueError(f"Could not read PDF file: {str(e)}")

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.getvalue()))
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(io.BytesIO(uploaded_file.getvalue()))
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        try:
            return uploaded_file.getvalue().decode("utf-8", errors="ignore")
        except:
            raise ValueError("Unsupported file type. Please upload PDF, DOCX, or TXT files.")