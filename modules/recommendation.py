# Career recommendation logic

def recommend_careers(skills):

    skills = [skill.lower() for skill in skills]

    recommendations = []

    # AI / ML Roles
    if (
        "machine learning" in skills
        or "deep learning" in skills
        or "tensorflow" in skills
        or "nlp" in skills
    ):

        recommendations.extend([
            "Machine Learning Engineer",
            "AI Engineer",
            "Data Scientist"
        ])

    # Data Roles
    if (
        "sql" in skills
        or "pandas" in skills
        or "numpy" in skills
        or "power bi" in skills
    ):

        recommendations.extend([
            "Data Analyst",
            "Business Intelligence Analyst",
            "Data Engineer"
        ])

    # Web Roles
    if (
        "flask" in skills
        or "django" in skills
    ):

        recommendations.extend([
            "Backend Developer",
            "Python Developer"
        ])

    # Programming Roles
    if (
        "python" in skills
        or "java" in skills
        or "c++" in skills
    ):

        recommendations.extend([
            "Software Engineer",
            "Application Developer"
        ])

    # Remove duplicates
    recommendations = list(set(recommendations))

    return recommendations