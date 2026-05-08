# Salary prediction logic

def predict_salary(skills):

    skills = [skill.lower() for skill in skills]

    salary = 300000

    # AI/ML Skills
    if (
        "machine learning" in skills
        or "deep learning" in skills
    ):
        salary += 400000

    if "nlp" in skills:
        salary += 200000

    if "tensorflow" in skills:
        salary += 250000

    # Data Skills
    if "sql" in skills:
        salary += 150000

    if "power bi" in skills:
        salary += 100000

    # Programming
    if "python" in skills:
        salary += 200000

    if "java" in skills:
        salary += 150000

    return salary