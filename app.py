import streamlit as st
from resume_parser import extract_text_from_pdf
from ats_scoring import calculate_ats_score
from keyword_matcher import extract_keywords, compare_keywords

st.set_page_config(page_title="ATS Resume Analyzer", layout="wide")

st.title("📄 ATS Resume Analyzer")
st.write("Upload your Resume PDF and paste the Job Description to get ATS Score and Improvement Suggestions.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description Here", height=250)

if st.button("Analyze Resume"):
    if resume_file is None or job_desc.strip() == "":
        st.warning("Please upload a resume PDF and enter job description.")
    else:
        resume_text = extract_text_from_pdf(resume_file)

        ats_score, similarity = calculate_ats_score(resume_text, job_desc)

        resume_keywords = extract_keywords(resume_text)
        jd_keywords = extract_keywords(job_desc)

        matched, missing = compare_keywords(resume_keywords, jd_keywords)

        st.subheader("📊 ATS Score Result")
        st.metric("ATS Score", f"{ats_score}/100")
        st.write(f"📌 Similarity Score: **{round(similarity*100, 2)}%**")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matched Keywords")
            st.write(", ".join(matched) if matched else "No matched keywords found.")

        with col2:
            st.subheader("❌ Missing Keywords")
            st.write(", ".join(missing) if missing else "No missing keywords found.")

        st.subheader("💡 Suggestions to Improve Resume")
        if missing:
            st.write("Add these important skills/keywords to improve ATS score:")
            for word in missing[:15]:
                st.write(f"- {word}")
        else:
            st.success("Your resume matches the job description well!")
