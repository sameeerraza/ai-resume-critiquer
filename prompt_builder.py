def build_prompt(file_content: str, job_role: str = None) -> str:
    job_context = job_role if job_role else 'general job applications'
    return f"""
    You are a professional career coach and resume reviewer with 10+ years of experience.  
    Analyze the following resume and provide detailed, constructive feedback in 800-1200 words.  

    Focus on these areas:  
    1. **Content clarity & overall impact** – Is the information easy to understand and compelling?  
    2. **Skills presentation** – Are skills highlighted effectively and aligned with {job_context}?  
    3. **Experience descriptions** – Do the work experiences demonstrate achievements, quantify results, and match the expectations for {job_context}?  
    4. **Tailoring & improvements** – What specific changes would strengthen the resume for {job_context}?  

    Resume content:  
    {file_content}  

    Please provide your feedback in a **clear, structured format** with:  
    - Strengths (what is working well)
    - Weaknesses (what needs improvement)  
    - Actionable recommendations (specific edits, rewording suggestions, or additions)
    """