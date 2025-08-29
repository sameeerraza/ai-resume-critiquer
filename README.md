# AI Resume Critiquer 📃

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Google AI](https://img.shields.io/badge/Google%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

> AI-powered resume analysis tool that provides professional feedback and optimization suggestions using Google Gemini API.

## 🚀 Features

- **Smart Document Processing**: Upload PDF or DOCX resumes with automatic text extraction
- **AI-Powered Analysis**: Leverages Google Gemini 1.5 Flash for intelligent resume critique
- **Job Role Targeting**: Tailored feedback based on specific job positions
- **Structured Feedback**: Organized analysis covering content clarity, skills presentation, and experience descriptions
- **Real-time Processing**: Instant analysis with user-friendly progress indicators

## 🎯 Live Demo

**[Try the live app here!]([https://ai-resume-critiquer-crbjhq8czhdwubu3kprfe7.streamlit.app/](https://ai-resume-critiquer-crbjhg8czhdwubu3kprfe7.streamlit.app/))**

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI/ML**: Google Gemini API
- **Document Processing**: PyPDF2, python-docx
- **Environment Management**: python-dotenv

## 📋 Installation

1. **Clone the repository**
```bash
git clone https://github.com/sameeerraza/ai-resume-critiquer.git
cd ai-resume-critiquer
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Create .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

5. **Run the application**
```bash
streamlit run app.py
```

## 🔑 Configuration

1. Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/)
2. Create a `.env` file in the project root
3. Add your API key: `GEMINI_API_KEY=your_actual_api_key`

## 💡 Usage

1. Launch the Streamlit app
2. Upload your resume (PDF or DOCX format)
3. Optionally specify the target job role
4. Click "Analyze Resume" for instant AI feedback
5. Review structured feedback covering:
   - Content clarity and impact
   - Skills presentation
   - Experience descriptions
   - Tailoring recommendations

## 🏗️ Project Structure

```
ai-resume-critiquer/
│
├── app.py                 # Main Streamlit application
├── file_handler.py        # Document processing utilities
├── prompt_builder.py      # AI prompt engineering
├── gemini_service.py      # Google Gemini API integration
├── requirements.txt       # Project dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Google Gemini API for powerful AI analysis
- Streamlit for the intuitive web framework
- PyPDF2 and python-docx for document processing

## 📧 Contact

**Sameer Raza** - [GitHub](https://github.com/sameeerraza)

Project Link: [https://github.com/sameeerraza/ai-resume-critiquer](https://github.com/sameeerraza/ai-resume-critiquer)
