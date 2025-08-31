import streamlit as st
from typing import Optional, Dict, Any
import time


def render_header():
    """Render the main application header"""
    st.markdown("""
    <div class="main-header">
        <h1>🎯 AI-Powered Resume Analyzer</h1>
        <p>Get expert feedback on your resume with AI-driven insights tailored to your target role. 
        Upload your resume and receive detailed analysis to boost your job application success.</p>
    </div>
    """, unsafe_allow_html=True)


def render_upload_section():
    """Render the file upload section with enhanced UI"""
    with st.container():
        st.markdown("""
        <div class="custom-card">
            <h3 style="margin-top: 0; color: #2E86C1;">📄 Upload Your Resume</h3>
            <p style="color: #7B8794; margin-bottom: 1.5rem;">
                Supported formats: PDF, Word Document (.docx), or plain text files
            </p>
        </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Choose your resume file",
            type=["pdf", "docx", "txt"],
            help="Upload your most recent resume for AI analysis. File size limit: 10MB"
        )

        if uploaded_file:
            render_file_info(uploaded_file)

        return uploaded_file


def render_file_info(uploaded_file):
    """Display information about the uploaded file"""
    file_size = len(uploaded_file.getvalue()) / (1024 * 1024)  # Convert to MB

    st.markdown(f"""
    <div class="status-success">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 1.5rem;">✅</span>
            <div>
                <strong>File uploaded successfully!</strong><br>
                <small style="color: #7B8794;">
                    📁 {uploaded_file.name} • 📊 {file_size:.2f} MB • 📅 Ready for analysis
                </small>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_job_role_input():
    """Render the job role input section"""
    with st.container():
        st.markdown("""
        <div class="custom-card">
            <h3 style="margin-top: 0; color: #28B463;">🎯 Target Job Role (Optional)</h3>
            <p style="color: #7B8794; margin-bottom: 1rem;">
                Specify your target role to receive tailored feedback and industry-specific recommendations
            </p>
        </div>
        """, unsafe_allow_html=True)

        job_role = st.text_input(
            "Enter the job role you're targeting",
            placeholder="e.g., Senior Software Engineer, Data Scientist, Product Manager...",
            help="This helps our AI provide more relevant and specific feedback"
        )

        if job_role:
            st.markdown(f"""
            <div class="status-success">
                <span style="font-size: 1.2rem;">🎯</span>
                <strong>Targeting:</strong> {job_role}
            </div>
            """, unsafe_allow_html=True)

        return job_role


def render_analysis_button(uploaded_file):
    """Render the analysis button with proper states"""
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if uploaded_file:
            if st.button("🚀 Analyze My Resume", key="analyze_btn", use_container_width=True):
                return True
        else:
            st.button(
                "📄 Upload Resume First",
                disabled=True,
                use_container_width=True,
                help="Please upload your resume before analysis"
            )
    return False


def render_loading_state(message: str = "Analyzing your resume..."):
    """Render an enhanced loading state"""
    with st.container():
        st.markdown(f"""
        <div class="custom-card" style="text-align: center;">
            <h3 style="color: #2E86C1;">🤖 AI Analysis in Progress</h3>
            <p style="color: #7B8794; font-size: 1.1rem;">{message}</p>
            <div style="margin: 2rem 0;">
                <div style="display: inline-block; animation: pulse 2s infinite;">
                    <span style="font-size: 3rem;">🧠</span>
                </div>
            </div>
            <p style="color: #7B8794; font-size: 0.9rem;">
                Our AI is carefully reviewing your resume content, structure, and alignment with best practices...
            </p>
        </div>
        """, unsafe_allow_html=True)


def render_results_header():
    """Render the results section header"""
    st.markdown("""
    <div class="results-header">
        <span style="font-size: 2rem; margin-right: 1rem;">📊</span>
        <div>
            <h2 style="margin: 0; color: #2E86C1;">Analysis Results</h2>
            <p style="margin: 0; color: #7B8794;">Comprehensive AI-powered resume feedback</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_analysis_results(response_text: str):
    """Render the analysis results with enhanced formatting"""
    with st.container():
        st.markdown('<div class="results-container">', unsafe_allow_html=True)

        render_results_header()

        # Add download button for results
        col1, col2 = st.columns([3, 1])
        with col2:
            st.download_button(
                label="💾 Download Report",
                data=response_text,
                file_name=f"resume_analysis_{int(time.time())}.txt",
                mime="text/plain",
                help="Save this analysis for future reference"
            )

        # Display the analysis content
        st.markdown(f'<div class="results-content">{response_text}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # Add action buttons
        render_post_analysis_actions()


def render_post_analysis_actions():
    """Render action buttons after analysis"""
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔄 Analyze Another Resume", use_container_width=True):
            st.rerun()

    with col2:
        if st.button("💡 Get Interview Tips", use_container_width=True):
            st.info("🚀 Interview preparation feature coming soon!")

    with col3:
        if st.button("✍️ Cover Letter Help", use_container_width=True):
            st.info("📝 Cover letter analysis feature coming soon!")


def render_error_state(error_message: str, error_type: str = "error"):
    """Render error states with appropriate styling"""
    icons = {
        "error": "❌",
        "warning": "⚠️",
        "info": "ℹ️"
    }

    css_class = f"status-{error_type}"
    icon = icons.get(error_type, "❌")

    st.markdown(f"""
    <div class="{css_class}">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 1.5rem;">{icon}</span>
            <div>
                <strong>Oops! Something went wrong</strong><br>
                <span style="color: #7B8794;">{error_message}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_feature_preview():
    """Render upcoming features preview"""
    st.markdown("---")

    st.markdown("""
    <div class="custom-card">
        <h3 style="color: #F39C12; margin-top: 0;">🚀 Coming Soon</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            <div class="feature-card">
                <span style="font-size: 2rem;">📝</span>
                <h4>Cover Letter Generator</h4>
                <p>AI-powered cover letters tailored to job postings</p>
            </div>
            <div class="feature-card">
                <span style="font-size: 2rem;">💼</span>
                <h4>Interview Prep</h4>
                <p>Practice questions based on your resume</p>
            </div>
            <div class="feature-card">
                <span style="font-size: 2rem;">📊</span>
                <h4>ATS Score</h4>
                <p>Applicant Tracking System compatibility check</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_sidebar_info():
    """Render helpful information in the sidebar"""
    with st.sidebar:
        st.markdown("""
        ### 📚 How It Works

        1. **Upload** your resume (PDF, DOCX, or TXT)
        2. **Specify** your target job role (optional)
        3. **Get** detailed AI-powered feedback
        4. **Improve** your resume with actionable insights

        ---

        ### 💡 Tips for Best Results

        - Upload your most recent resume
        - Be specific about your target role
        - Include quantified achievements
        - Keep formatting clean and simple

        ---

        ### 🛠️ Supported Formats

        - **PDF** - Most common format
        - **Word (.docx)** - Microsoft Word
        - **Text (.txt)** - Plain text files

        **File size limit:** 10MB
        """)


def render_footer():
    """Render application footer"""
    st.markdown("---")

    st.markdown("""
    <div style="text-align: center; color: #7B8794; padding: 2rem 0;">
        <p>🤖 Powered by <strong>Google Gemini AI</strong> • Built with ❤️ using <strong>Streamlit</strong></p>
        <p style="font-size: 0.9rem;">
            Get professional resume feedback in seconds • Improve your job application success rate
        </p>
    </div>
    """, unsafe_allow_html=True)