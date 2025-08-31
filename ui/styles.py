import streamlit as st


def initialize_theme():
    """Initialize theme in session state if not exists"""
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False


def render_theme_toggle():
    """Render simple theme toggle in sidebar"""
    with st.sidebar:
        st.markdown("---")

        col1, col2 = st.columns([3, 1])

        with col1:
            if st.session_state.dark_mode:
                st.markdown("**🌙 Dark Mode**")
            else:
                st.markdown("**☀️ Light Mode**")

        with col2:
            if st.button("🔄", help="Toggle theme", key="theme_toggle"):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()


def load_custom_css():
    """Load custom CSS with simple theme support"""

    # Initialize theme
    initialize_theme()

    # Get theme colors
    if st.session_state.dark_mode:
        # Dark mode colors
        bg_color = "#1E1E1E"
        secondary_bg = "#2D2D2D"
        card_bg = "#2D2D2D"
        text_color = "#FFFFFF"
        text_secondary = "#CCCCCC"
        border_color = "#404040"
        shadow = "0 2px 4px rgba(0,0,0,0.3)"
        shadow_hover = "0 4px 12px rgba(0,0,0,0.4)"
    else:
        # Light mode colors
        bg_color = "#FFFFFF"
        secondary_bg = "#F8F9FA"
        card_bg = "#FFFFFF"
        text_color = "#2C3E50"
        text_secondary = "#7B8794"
        border_color = "#E1E8ED"
        shadow = "0 2px 4px rgba(0,0,0,0.1)"
        shadow_hover = "0 4px 12px rgba(0,0,0,0.15)"

    st.markdown(f"""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap');

    /* Apply theme to main app */
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}

    /* Main content area */
    .main .block-container {{
        background-color: {bg_color};
        color: {text_color};
        padding-top: 2rem;
        padding-bottom: 2rem;
    }}

    /* Top Header/Toolbar */
    [data-testid="stHeader"] {{
        background-color: {secondary_bg} !important;
    }}

    .css-18e3th9, .css-1d391kg {{
        background-color: {secondary_bg} !important;
    }}

    /* Streamlit header elements */
    header[data-testid="stHeader"] {{
        background-color: {secondary_bg} !important;
    }}

    /* Top toolbar buttons and elements */
    [data-testid="stHeader"] button {{
        color: {text_color} !important;
    }}

    [data-testid="stHeader"] svg {{
        fill: {text_color} !important;
    }}

    /* Sidebar - Updated selectors for proper dark mode support */
    .css-1d391kg, [data-testid="stSidebar"] {{
        background-color: {secondary_bg} !important;
    }}

    .css-1d391kg > div, [data-testid="stSidebar"] > div {{
        background-color: {secondary_bg} !important;
    }}

    /* Sidebar content */
    [data-testid="stSidebar"] .stMarkdown {{
        color: {text_color} !important;
    }}

    [data-testid="stSidebar"] .stMarkdown h1,
    [data-testid="stSidebar"] .stMarkdown h2,
    [data-testid="stSidebar"] .stMarkdown h3,
    [data-testid="stSidebar"] .stMarkdown h4,
    [data-testid="stSidebar"] .stMarkdown h5,
    [data-testid="stSidebar"] .stMarkdown h6 {{
        color: {text_color} !important;
    }}

    [data-testid="stSidebar"] .stMarkdown p {{
        color: {text_color} !important;
    }}

    [data-testid="stSidebar"] .stMarkdown ul {{
        color: {text_color} !important;
    }}

    [data-testid="stSidebar"] .stMarkdown li {{
        color: {text_color} !important;
    }}

    [data-testid="stSidebar"] .stMarkdown strong {{
        color: {text_color} !important;
    }}

    /* Sidebar buttons */
    [data-testid="stSidebar"] .stButton > button {{
        background-color: {card_bg} !important;
        color: {text_color} !important;
        border: 1px solid {border_color} !important;
    }}

    [data-testid="stSidebar"] .stButton > button:hover {{
        background-color: {bg_color} !important;
        border-color: {text_color} !important;
    }}

    /* All text elements */
    .stMarkdown, .stText, .stWrite, p, h1, h2, h3, h4, h5, h6, div {{
        color: {text_color} !important;
    }}

    /* Typography */
    html, body, [class*="css"] {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: {text_color};
    }}

    /* Header Styles */
    .main-header {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: {shadow_hover};
        animation: fadeInUp 0.6s ease-out;
    }}

    .main-header h1 {{
        color: white !important;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }}

    .main-header p {{
        color: rgba(255,255,255,0.9) !important;
        font-size: 1.2rem;
        font-weight: 400;
        margin: 0;
        max-width: 600px;
        margin: 0 auto;
    }}

    /* Card Components */
    .custom-card {{
        background: {card_bg};
        border-radius: 12px;
        padding: 2rem;
        box-shadow: {shadow};
        border: 1px solid {border_color};
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }}

    .custom-card:hover {{
        box-shadow: {shadow_hover};
        transform: translateY(-2px);
    }}

    .custom-card h3, .custom-card h4, .custom-card p {{
        color: {text_color} !important;
    }}

    /* Feature cards */
    .feature-card {{
        text-align: center;
        padding: 1rem;
        background: {secondary_bg};
        border-radius: 8px;
        border: 1px solid {border_color};
    }}

    .feature-card h4 {{
        color: {text_color} !important;
        margin: 0.5rem 0;
    }}

    .feature-card p {{
        font-size: 0.9rem;
        color: {text_secondary} !important;
        margin: 0;
    }}

    .upload-card {{
        background: {card_bg};
        border: 2px dashed #2E86C1;
        border-radius: 16px;
        padding: 2.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }}

    .upload-card:hover {{
        border-color: #28B463;
    }}

    /* Status Components */
    .status-success {{
        background: {card_bg};
        border: 1px solid #58D68D;
        border-left: 4px solid #58D68D;
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
    }}

    .status-success * {{
        color: {text_color} !important;
    }}

    .status-error {{
        background: {card_bg};
        border: 1px solid #E74C3C;
        border-left: 4px solid #E74C3C;
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
    }}

    .status-error * {{
        color: {text_color} !important;
    }}

    .status-warning {{
        background: {card_bg};
        border: 1px solid #F39C12;
        border-left: 4px solid #F39C12;
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
    }}

    .status-warning * {{
        color: {text_color} !important;
    }}

    /* Button Enhancements */
    .stButton > button {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: {shadow} !important;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: {shadow_hover} !important;
        opacity: 0.9 !important;
    }}

    .stButton > button:disabled {{
        background: #BDC3C7 !important;
        transform: none !important;
        box-shadow: none !important;
    }}

    /* File Uploader */
    .uploadedFile {{
        border: 1px solid #58D68D !important;
        border-radius: 10px !important;
        background: {card_bg} !important;
    }}

    /* File uploader drag and drop area */
    [data-testid="stFileUploader"] {{
        background-color: {card_bg} !important;
    }}

    [data-testid="stFileUploader"] > div {{
        background-color: {card_bg} !important;
        border-color: {border_color} !important;
    }}

    [data-testid="stFileUploader"] > div > div {{
        background-color: {card_bg} !important;
        color: {text_color} !important;
    }}

    [data-testid="stFileUploader"] label {{
        color: {text_color} !important;
    }}

    /* File uploader drop zone - more specific targeting */
    [data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"] {{
        background-color: {card_bg} !important;
        border: 2px dashed {border_color} !important;
        color: {text_color} !important;
    }}

    [data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"]:hover {{
        border-color: #2E86C1 !important;
        background-color: {secondary_bg} !important;
    }}

    /* File uploader inner content */
    [data-testid="stFileUploaderDropzone"] div {{
        background-color: transparent !important;
        color: {text_color} !important;
    }}

    [data-testid="stFileUploaderDropzone"] span {{
        color: {text_color} !important;
    }}

    [data-testid="stFileUploaderDropzone"] svg {{
        fill: {text_color} !important;
    }}

    /* File uploader drop zone */
    .css-1cpxqw2, .css-1erivf3 {{
        background-color: {card_bg} !important;
        border-color: {border_color} !important;
        color: {text_color} !important;
    }}

    /* File uploader text */
    [data-testid="stFileUploader"] span {{
        color: {text_color} !important;
    }}

    [data-testid="stFileUploader"] small {{
        color: {text_secondary} !important;
    }}

    /* File uploader browse button */
    [data-testid="stFileUploader"] button {{
        background-color: {secondary_bg} !important;
        color: {text_color} !important;
        border: 1px solid {border_color} !important;
    }}

    [data-testid="stFileUploader"] button:hover {{
        background-color: {bg_color} !important;
        border-color: #2E86C1 !important;
    }}

    /* Alternative file uploader selectors */
    .stFileUploader div[data-baseweb="file-uploader"] {{
        background-color: {card_bg} !important;
        border-color: {border_color} !important;
    }}

    .stFileUploader div[data-baseweb="file-uploader"] * {{
        color: {text_color} !important;
    }}

    /* Text Input */
    .stTextInput > div > div > input {{
        border-radius: 10px !important;
        border: 2px solid {border_color} !important;
        padding: 0.75rem !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        background-color: {card_bg} !important;
        color: {text_color} !important;
    }}

    .stTextInput > div > div > input::placeholder {{
        color: {text_secondary} !important;
        opacity: 0.7 !important;
    }}

    .stTextInput > div > div > input:focus {{
        border-color: #2E86C1 !important;
        box-shadow: 0 0 0 3px rgba(46, 134, 193, 0.1) !important;
    }}

    .stTextInput label {{
        color: {text_color} !important;
    }}

    /* File uploader label */
    .stFileUploader label {{
        color: {text_color} !important;
    }}

    /* Results Section */
    .results-container {{
        background: {card_bg};
        border-radius: 16px;
        padding: 2rem;
        box-shadow: {shadow_hover};
        margin-top: 2rem;
        border-left: 5px solid #2E86C1;
    }}

    .results-header {{
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid {border_color};
    }}

    .results-content {{
        line-height: 1.7;
        font-size: 1rem;
        color: {text_color};
    }}

    .results-content * {{
        color: {text_color} !important;
    }}

    /* Loading Spinner */
    .stSpinner > div {{
        border-top-color: #2E86C1 !important;
    }}

    /* Metrics */
    [data-testid="metric-container"] {{
        background: {card_bg} !important;
        border: 1px solid {border_color} !important;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: {shadow};
        color: {text_color} !important;
    }}

    [data-testid="metric-container"] * {{
        color: {text_color} !important;
    }}

    /* Animations */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    @keyframes pulse {{
        0%, 100% {{
            opacity: 1;
        }}
        50% {{
            opacity: 0.7;
        }}
    }}

    /* Responsive Design */
    @media (max-width: 768px) {{
        .main-header h1 {{
            font-size: 2rem;
        }}

        .main-header p {{
            font-size: 1rem;
        }}

        .custom-card {{
            padding: 1.5rem;
        }}

        .upload-card {{
            padding: 1.5rem;
        }}
    }}

    /* Code Blocks */
    .stMarkdown code {{
        background-color: {secondary_bg} !important;
        padding: 0.25rem 0.5rem !important;
        border-radius: 6px !important;
        font-family: 'Fira Code', monospace !important;
        color: {text_color} !important;
    }}
    </style>
    """, unsafe_allow_html=True)


def get_theme_config():
    """Return theme configuration for consistent styling"""
    return {
        'primaryColor': '#2E86C1',
        'backgroundColor': '#F8F9FA',
        'secondaryBackgroundColor': '#FFFFFF',
        'textColor': '#2C3E50',
        'font': 'Inter'
    }