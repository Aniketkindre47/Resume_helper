import streamlit as st


def job_input_section():
    job_title = st.text_input("Job Title")
    job_link = st.text_input("Job Link")
    job_desc = st.text_area("Paste Job Description")
    return job_title, job_link, job_desc
