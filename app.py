import streamlit as st

from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.missing_skills import find_missing_skills
from utils.suggestions import get_suggestions

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF only)",
    type=["pdf"]
)

if uploaded_file is not None:

    # Extract Resume Text
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.text_area("Resume Content", text, height=300)

    # Detect Skills
    skills = extract_skills(text)

    st.subheader("Detected Skills")

    if skills:
        st.success(", ".join(skills))
    else:
        st.warning("No skills detected.")

    # ATS Score
    ats_score = calculate_ats_score(skills)

    st.subheader("ATS Score")
    st.progress(int(ats_score))
    st.success(f"Your ATS Score: {ats_score}%")

    # Missing Skills
    missing_skills = find_missing_skills(skills)

    st.subheader("Missing Skills")

    if missing_skills:
        st.warning(", ".join(missing_skills))
    else:
        st.success("Great! No important skills are missing.")

    # Resume Suggestions
    suggestions = get_suggestions(skills)

    st.subheader("Resume Improvement Suggestions")

    if suggestions:
        for suggestion in suggestions:
            st.info(suggestion)
    else:
        st.success("Your resume looks strong!")