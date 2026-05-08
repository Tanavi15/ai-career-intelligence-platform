import pdfplumber
import spacy
import re

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined skills list
SKILLS = [
    "python",
    "machine learning",
    "data science",
    "sql",
    "tensorflow",
    "pandas",
    "numpy",
    "streamlit",
    "power bi",
    "excel",
    "deep learning",
    "nlp",
    "flask",
    "django",
    "java",
    "c++"
]

# Extract text from PDF
def extract_text_from_pdf(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted

    return text

# Extract skills
def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))

# Extract email
def extract_email(text):

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    matches = re.findall(pattern, text)

    return matches[0] if matches else "Not Found"

# Extract phone number
def extract_phone(text):

    pattern = r"\+?\d[\d -]{8,12}\d"

    matches = re.findall(pattern, text)

    return matches[0] if matches else "Not Found"

# Extract name using NLP
def extract_name(text):

    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return "Not Found"

# Main parser function
def parse_resume(pdf_file):

    text = extract_text_from_pdf(pdf_file)

    parsed_data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "text": text
    }

    return parsed_data