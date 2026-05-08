# Generate interview questions based on skills

def generate_interview_questions(skills):

    skills = [skill.lower() for skill in skills]

    questions = []

    # Python Questions
    if "python" in skills:

        questions.extend([
            "Explain Python decorators.",
            "What is list comprehension in Python?",
            "Difference between list and tuple."
        ])

    # Machine Learning Questions
    if (
        "machine learning" in skills
        or "deep learning" in skills
    ):

        questions.extend([
            "Explain Random Forest Algorithm.",
            "What is overfitting in ML?",
            "Difference between supervised and unsupervised learning."
        ])

    # NLP Questions
    if "nlp" in skills:

        questions.extend([
            "What is tokenization in NLP?",
            "Explain Named Entity Recognition.",
            "Difference between stemming and lemmatization."
        ])

    # SQL Questions
    if "sql" in skills:

        questions.extend([
            "What is normalization?",
            "Difference between SQL and NoSQL.",
            "Explain JOIN operations."
        ])

    # HR Questions
    questions.extend([
        "Tell me about yourself.",
        "What are your strengths?",
        "Why should we hire you?"
    ])

    return questions