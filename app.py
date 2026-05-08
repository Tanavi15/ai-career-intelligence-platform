import streamlit as st
import pandas as pd
import plotly.express as px

from modules.resume_parser import parse_resume
from modules.ats_score import calculate_ats_score
from modules.skill_gap import analyze_skill_gap
from modules.recommendation import recommend_careers
from modules.interview_generator import generate_interview_questions
from modules.salary_predictor import predict_salary
from modules.chatbot import chatbot_response

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Career Intelligence Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stApp {
    background-color: #0E1117;
}

section[data-testid="stSidebar"] {
    background-color: #161B22;
}

h1, h2, h3 {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

st.sidebar.title("🚀 AI Career Intelligence")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Resume Analyzer",
        "ATS Score",
        "Skill Gap Analysis",
        "Career Recommendation",
        "Interview Generator",
        "Salary Prediction",
        "AI Chatbot"
    ]
)

# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.title("🚀 AI Career Intelligence Platform")

    st.markdown("""
    ### Advanced AI-Powered Recruitment & Career Analysis System
    """)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Resumes Analyzed", "1250")
    col2.metric("Hiring Predictions", "89%")
    col3.metric("Skill Matches", "93%")
    col4.metric("AI Accuracy", "96%")

    st.markdown("---")

    st.subheader("📊 AI Job Market Analytics")

    data = pd.DataFrame({
        "Role": [
            "Data Scientist",
            "ML Engineer",
            "Backend Developer",
            "Data Analyst",
            "AI Researcher"
        ],
        "Demand": [95, 90, 80, 85, 70]
    })

    fig = px.bar(
        data,
        x="Role",
        y="Demand",
        color="Demand",
        title="Current AI Job Market Demand"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------- RESUME ANALYZER ----------------

elif page == "Resume Analyzer":

    st.title("📄 AI Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    if uploaded_file:

        parsed_data = parse_resume(uploaded_file)

        st.success("Resume Uploaded Successfully!")

        st.subheader("📌 Extracted Information")

        st.write(f"### 👤 Name: {parsed_data['name']}")
        st.write(f"### 📧 Email: {parsed_data['email']}")
        st.write(f"### 📱 Phone: {parsed_data['phone']}")

        st.subheader("🧠 Skills Detected")

        if parsed_data["skills"]:

            for skill in parsed_data["skills"]:
                st.success(skill)

        st.subheader("📄 Resume Preview")

        st.text_area(
            "Extracted Resume Text",
            parsed_data["text"],
            height=300
        )

# ---------------- ATS SCORE ----------------

elif page == "ATS Score":

    st.title("📈 ATS Score Analyzer")

    uploaded_resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"],
        key="ats_resume"
    )

    job_description = st.text_area(
        "Paste Job Description"
    )

    if uploaded_resume and job_description:

        parsed_data = parse_resume(uploaded_resume)

        resume_text = parsed_data["text"]

        score = calculate_ats_score(
            resume_text,
            job_description
        )

        st.subheader("🎯 ATS Compatibility Score")

        st.progress(int(score))

        st.metric(
            "ATS Match Score",
            f"{score}%"
        )

# ---------------- SKILL GAP ----------------

elif page == "Skill Gap Analysis":

    st.title("🧠 AI Skill Gap Analysis")

    uploaded_resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"],
        key="skill_gap_resume"
    )

    required_skills_input = st.text_area(
        "Enter Required Skills",
        placeholder="Python, SQL, TensorFlow"
    )

    if uploaded_resume and required_skills_input:

        parsed_data = parse_resume(uploaded_resume)

        resume_skills = parsed_data["skills"]

        required_skills = [
            skill.strip()
            for skill in required_skills_input.split(",")
        ]

        matched_skills, missing_skills = analyze_skill_gap(
            resume_skills,
            required_skills
        )

        st.subheader("✅ Matched Skills")

        for skill in matched_skills:
            st.success(skill)

        st.subheader("❌ Missing Skills")

        for skill in missing_skills:
            st.error(skill)

# ---------------- CAREER RECOMMENDATION ----------------

elif page == "Career Recommendation":

    st.title("🎯 AI Career Recommendation")

    uploaded_resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"],
        key="career_resume"
    )

    if uploaded_resume:

        parsed_data = parse_resume(uploaded_resume)

        skills = parsed_data["skills"]

        recommendations = recommend_careers(skills)

        st.subheader("🚀 Recommended Careers")

        for career in recommendations:
            st.info(career)

# ---------------- INTERVIEW GENERATOR ----------------

elif page == "Interview Generator":

    st.title("💼 AI Interview Question Generator")

    uploaded_resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"],
        key="interview_resume"
    )

    if uploaded_resume:

        parsed_data = parse_resume(uploaded_resume)

        skills = parsed_data["skills"]

        questions = generate_interview_questions(skills)

        st.subheader("🎯 Generated Questions")

        for index, question in enumerate(questions, start=1):

            st.info(f"{index}. {question}")

# ---------------- SALARY PREDICTION ----------------

elif page == "Salary Prediction":

    st.title("💰 AI Salary Prediction")

    uploaded_resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"],
        key="salary_resume"
    )

    if uploaded_resume:

        parsed_data = parse_resume(uploaded_resume)

        skills = parsed_data["skills"]

        salary = predict_salary(skills)

        st.metric(
            "Predicted Annual Salary",
            f"₹{salary}"
        )

# ---------------- AI CHATBOT ----------------

elif page == "AI Chatbot":

    st.title("🤖 AI Career Chatbot")

    user_question = st.text_input(
        "Ask Career Question"
    )

    if user_question:

        response = chatbot_response(user_question)

        st.info(response)