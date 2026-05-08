# Extract missing and matched skills

def analyze_skill_gap(resume_skills, required_skills):

    resume_skills = [skill.lower() for skill in resume_skills]

    required_skills = [skill.lower() for skill in required_skills]

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill in resume_skills:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills