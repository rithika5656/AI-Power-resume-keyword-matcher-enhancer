import pdfplumber
from docx import Document
import re
import streamlit as st

# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="Resume Keyword Matcher", page_icon="📄", layout="centered")
st.title("📄 Resume Keyword Matcher")
st.write("Upload a Resume and Job Description to see skill matches and a fit score.")

resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
job_file = st.file_uploader("Upload Job Description (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])

# ---------------- Helper Functions ----------------
def extract_text(file):
    if file.name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.lower()
    elif file.name.endswith(".docx"):
        doc = Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.lower()
    elif file.name.endswith(".txt"):
        text = file.read().decode("utf-8")
        return text.lower()
    else:
        return ""

def extract_skills(text, skills_list):
    skills_found = [skill for skill in skills_list if skill.lower() in text]
    return skills_found

# ---------------- Skill List ----------------
skills_list = [
    "python", "java", "c++", "sql", "machine learning", "data analysis",
    "deep learning", "tensorflow", "pytorch", "react", "nlp", "excel", "communication"
]

# ---------------- Processing ----------------
if resume_file and job_file:
    resume_text = extract_text(resume_file)
    job_text = extract_text(job_file)

    resume_skills = extract_skills(resume_text, skills_list)
    job_skills = extract_skills(job_text, skills_list)

    matched_skills = list(set(resume_skills) & set(job_skills))
    match_score = round(len(matched_skills) / len(job_skills) * 100, 2) if job_skills else 0

    # ---------------- Display ----------------
    st.subheader("✅ Resume Skills Found")
    st.write(resume_skills if resume_skills else "No predefined skills found in resume.")

    st.subheader("📋 Job Description Skills")
    st.write(job_skills if job_skills else "No predefined skills found in job description.")

    st.subheader("🔹 Matched Skills")
    st.write(matched_skills if matched_skills else "No matching skills found.")

    st.subheader("📊 Match Score")
    st.write(f"**{match_score}%** match based on skills.")
