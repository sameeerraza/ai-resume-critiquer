import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Import existing modules
from file_handler import extract_text_from_file
from prompt_builder import build_prompt
from gemini_service import analyze_resume

# Import new UI modules
from ui.styles import load_custom_css, get_theme_config, initialize_theme, render_theme_toggle
from ui.components import (
    render_header, render_upload_section, render_job_role_input,
    render_analysis_button, render_loading_state, render_analysis_results,
    render_error_state, render_feature_preview, render_sidebar_info,
    render_footer
)

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer - Get Expert Feedback",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/yourusername/resume-analyzer',
        'Report a bug': 'https://github.com/yourusername/resume-analyzer/issues',
        'About': """
        # AI Resume Analyzer

        Get professional feedback on your resume using AI-powered analysis.
        Built with Streamlit and Google Gemini AI.

        **Features:**
        - Comprehensive resume analysis
        - Role-specific feedback
        - ATS optimization tips
        - Professional formatting advice
        """
    }
)

# Load custom styles
load_custom_css()


def initialize_session_state():
    """Initialize session state variables"""
    if 'analysis_complete' not in st.session_state:
        st.session_state.analysis_complete = False
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = None
    if 'uploaded_file_name' not in st.session_state:
        st.session_state.uploaded_file_name = None

    # Initialize theme
    initialize_theme()


def validate_api_key():
    """Validate and configure Gemini API key"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        render_error_state(
            "Gemini API key not found. Please set GEMINI_API_KEY in your .env file.",
            "error"
        )
        st.stop()

    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        render_error_state(
            f"Failed to configure Gemini API: {str(e)}",
            "error"
        )
        st.stop()


def process_resume_analysis(uploaded_file, job_role):
    """Process the resume analysis with proper error handling"""
    try:
        # Extract text from file
        with st.status("Extracting text from file...", expanded=False) as status:
            file_content = extract_text_from_file(uploaded_file)
            status.update(label="Text extraction completed!", state="complete")

        # Validate file content
        if not file_content.strip():
            render_error_state(
                "The uploaded file appears to be empty or contains no readable text. Please try a different file.",
                "warning"
            )
            return None

        # Build prompt
        with st.status("Building analysis prompt...", expanded=False) as status:
            prompt = build_prompt(file_content, job_role)
            status.update(label="Prompt preparation completed!", state="complete")

        # Perform AI analysis
        with st.status("Analyzing resume with AI...", expanded=False) as status:
            response = analyze_resume(prompt)
            status.update(label="Analysis completed successfully!", state="complete")

        return response

    except FileNotFoundError:
        render_error_state(
            "Could not process the uploaded file. The file may be corrupted or in an unsupported format.",
            "error"
        )
        return None
    except ValueError as e:
        render_error_state(str(e), "warning")
        return None
    except Exception as e:
        render_error_state(
            f"An unexpected error occurred during analysis: {str(e)}",
            "error"
        )
        return None


def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()

    # Validate API configuration
    validate_api_key()

    # Render sidebar with theme toggle
    render_sidebar_info()
    render_theme_toggle()

    # Main content area
    with st.container():
        # Header
        render_header()

        # Create two columns for better layout
        col1, col2 = st.columns([2, 1])

        with col1:
            # File upload section
            uploaded_file = render_upload_section()

            # Job role input
            job_role = render_job_role_input()

            # Analysis button and processing
            if render_analysis_button(uploaded_file):
                # Show loading state
                render_loading_state("Analyzing your resume with AI...")

                # Process the analysis
                response = process_resume_analysis(uploaded_file, job_role)

                if response:
                    # Store results in session state
                    st.session_state.analysis_complete = True
                    st.session_state.analysis_results = response.text
                    st.session_state.uploaded_file_name = uploaded_file.name

                    # Rerun to show results
                    st.rerun()

        with col2:
            # Show file status or tips
            if uploaded_file:
                st.markdown("""
                <div class="custom-card">
                    <h4 style="color: #28B463; margin-top: 0;">✅ Ready for Analysis</h4>
                    <p style="color: #7B8794; font-size: 0.9rem;">
                        Your resume has been uploaded successfully. 
                        Click "Analyze My Resume" to get detailed feedback.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="custom-card">
                    <h4 style="color: #F39C12; margin-top: 0;">💡 Quick Tips</h4>
                    <ul style="color: #7B8794; font-size: 0.9rem; line-height: 1.6;">
                        <li>Use a clean, professional format</li>
                        <li>Include quantified achievements</li>
                        <li>Tailor content to your target role</li>
                        <li>Keep it concise (1-2 pages)</li>
                        <li>Use action verbs and keywords</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

    # Display analysis results if available
    if st.session_state.analysis_complete and st.session_state.analysis_results:
        st.markdown("---")
        render_analysis_results(st.session_state.analysis_results)

        # Show success metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📄 File Analyzed", st.session_state.uploaded_file_name or "Resume")
        with col2:
            st.metric("🤖 AI Model", "Gemini 1.5 Flash")
        with col3:
            st.metric("⚡ Analysis Time", "< 30 seconds")
        with col4:
            st.metric("✅ Status", "Complete")

    # Feature preview section
    if not st.session_state.analysis_complete:
        render_feature_preview()

    # Footer
    render_footer()


if __name__ == "__main__":
    main()