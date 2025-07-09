import streamlit as st
import fitz  # PyMuPDF for PDF parsing
import docx
from PIL import Image
import pytesseract
import re
import google.generativeai as genai
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ---- CONFIG ----
GEMINI_API_KEY = "AIzaSyA3fw8r3859Ot7lXJM5zYe90GH0tdqJexg"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# ---- UTILS ----
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip().lower()


def extract_resume_text(file):
    file_type = file.type
    file_name = file.name.lower()

    if file_type == "application/pdf" or file_name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return clean_text(text)

    elif file_type in [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/msword"
    ] or file_name.endswith(".docx") or file_name.endswith(".doc"):
        doc = docx.Document(file)
        fullText = [para.text for para in doc.paragraphs]
        return clean_text(" ".join(fullText))

    elif file_type.startswith("image/") or file_name.endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):
        image = Image.open(file).convert("RGB")
        text = pytesseract.image_to_string(image)
        return clean_text(text)

    else:
        return "Unsupported file format"


def save_to_google_sheet(job_title, job_link, job_desc, modified_resume):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "aqueous-abbey-457910-u5-f74637f4e96e.json", scope
    )
    client = gspread.authorize(creds)

    # Open the spreadsheet
    sheet = client.open("Resume Matcher Data").sheet1  # or use .worksheet("Sheet1")

    # Add a new row
    sheet.append_row([
        datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        job_title,
        job_link,
        job_desc[:2000],         # truncate long JD
        modified_resume[:2000]   # truncate long LLM response
    ])


def compare_and_suggest(jd_text, resume_text):
    prompt = f"""You are an AI assistant that improves resumes.
Match this resume with the job description and rewrite it to better fit:

Job Description:
{jd_text}

Resume:
{resume_text}

Modified Resume:"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"LLM Error: {e}"


# ---- STREAMLIT UI ----
st.title("🧠 AI Resume Matcher")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx", "doc", "png", "jpg", "jpeg", "bmp", "tiff"]
)
text = st.text_area("Paste Job Description")
job_title = st.text_input("Job Title / Label")
job_link = st.text_input("Job Link")

if uploaded_file and st.button("Analyze"):
    resume_text = extract_resume_text(uploaded_file)
    new_resume = compare_and_suggest(text, resume_text)
    st.subheader("📋 Modified Resume")
    st.text_area("Suggested Resume", new_resume, height=300)

    save_to_google_sheet(job_title, job_link, text, new_resume)
    st.success("✅ Saved to Google Sheet!")


