# AI chatbot responses

def chatbot_response(user_input):

    user_input = user_input.lower()

    if "machine learning" in user_input:
        return """
Focus on:
- Python
- Scikit-learn
- Deep Learning
- Real-world projects
- Deployment
"""

    elif "resume" in user_input:
        return """
A strong resume should include:
- Projects
- Skills
- Achievements
- Certifications
- GitHub links
"""

    elif "interview" in user_input:
        return """
Prepare:
- DSA fundamentals
- Core ML concepts
- SQL
- Python coding
- Project explanations
"""

    elif "salary" in user_input:
        return """
AI/ML salaries depend on:
- Skills
- Experience
- Projects
- Deployment knowledge
"""

    else:
        return """
Keep improving your:
- Technical skills
- Real-world projects
- Problem solving
- Communication skills
"""