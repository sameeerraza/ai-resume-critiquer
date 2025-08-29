import google.generativeai as genai
from google.api_core import exceptions as google_exceptions

def analyze_resume(prompt: str):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 2000,
                "top_p": 0.8,
                "top_k": 40
        }
    )
        if not response.text:
            raise ValueError("Received empty response from Gemini")

        return response

    except google_exceptions.ResourceExhausted:
        raise Exception("API quota exceeded. Please try again later.")
    except google_exceptions.InvalidArgument:
        raise Exception("Invalid request. Please check your resume content.")
    except Exception as e:
        raise Exception(f"Failed to analyze resume: {str(e)}")