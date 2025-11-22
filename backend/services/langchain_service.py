from langchain_ollama import ChatOllama

agent = ChatOllama(model='deepseek-llm:7b')
    

def optimize_resume(job_description: str, resume: str):
    messages = [
    (
        "system", get_system_prompt_for_optimization()
    ),
    (
        "human", get_user_prompt_for_optimization(job_description, resume)
    ),
    ]
    return agent.invoke(messages).content


def generate_resume(job_description: str, resume: str):
    return "Stay tuned"


def get_system_prompt_for_optimization() -> str:
    return system_prompt_for_optimization

def get_user_prompt_for_optimization(job_description: str, resume: str):
    return f"""
                Rewrite and optimize the following resume to closely match the job description.

                Resume:
                    {resume}

                Job Description:
                    {job_description}

                Your tasks:
                    - Insert missing keywords from the job description.
                    - Rewrite bullet points to match job responsibilities.
                    - Emphasize achievements and relevant skills.
                    - Preserve ALL original experience, dates, and job titles.
                    - Keep resume roughly one page, but DO NOT delete important content.
                    - Output only the optimized resume (no explanation).
            """

system_prompt_for_optimization = """
                    You are an ATS resume optimization expert trained to rewrite resumes using the
                    exact language, responsibilities, and keywords from the job description.

                    RULES:
                        - ALWAYS include exact keywords from the job description.
                        - ALWAYS preserve ALL dates (start–end).
                        - ALWAYS preserve all job titles, company names, and education.
                        - NEVER invent fake experience.
                        - NEVER remove relevant experience.
                        - ONLY rewrite or restructure what exists.
                        - Keep the resume concise but do NOT delete important content.
                        - Use strong action verbs.
                        - Make resume ATS-friendly.
                        - Keep formatting clean and consistent.
                        - Goal: achieve a 90–100% similarity score with the job description.
                """


