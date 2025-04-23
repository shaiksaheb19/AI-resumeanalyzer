import streamlit as st
from resume_analyzer import get_similarity

st.title("📄 AI Resume Analyzer")

resume = st.text_area("Paste your resume text:")
job_desc = st.text_area("Paste job description:")

if st.button("Analyze"):
    if resume and job_desc:
        score = get_similarity(resume, job_desc)
        st.success(f"✅ Match Score: {score}%")
    else:
        st.warning("Please enter both resume and job description.")
