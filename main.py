from model.extractors import extract_resume_text
from controller.logic import compare_and_suggest
from model.sheets import save_to_google_sheet
from view.ui import job_input_section
import streamlit as st
from config.settings import model

st.title("🧠 AI Resume Matcher")
job_title, job_link, job_desc = job_input_section()
uploaded_file = st.file_uploader("Upload Resume")

if uploaded_file and st.button("Analyze"):
    resume_text = extract_resume_text(uploaded_file)
    result = compare_and_suggest(job_desc, resume_text, model)
    st.text_area("Modified Resume", result)
    save_to_google_sheet(job_title, job_link, job_desc, result)
    st.success("✅ Saved to Google Sheet!")