from config.settings import model

def compare_and_suggest(jd_text, resume_text, model):
    prompt = f"""You are an AI assistant that improves resumes.
Match this resume with the job description and rewrite it to better fit:

Job Description:
{jd_text}

Resume:
{resume_text}

Modified Resume:"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"LLM Error: {e}"
