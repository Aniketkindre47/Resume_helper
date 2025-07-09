# AI Resume Matcher

AI Resume Matcher is a Streamlit web application that helps you optimize your resume for a specific job description using Google Gemini (Generative AI). It extracts text from your uploaded resume (PDF, DOCX, or image), compares it to a job description, and rewrites your resume to better fit the job. The results are saved to a Google Sheet for easy tracking.

---

## Features

- **Resume Parsing:** Supports PDF, DOCX, and image files (PNG, JPG, etc.).
- **Job Description Input:** Paste or type the job description.
- **AI-Powered Resume Rewriting:** Uses Gemini LLM to tailor your resume to the job.
- **Google Sheets Integration:** Saves job info, job link, job description, and the AI-modified resume.
- **Simple UI:** Built with Streamlit for easy use.


## How to use

Use app.py if you want to use a code as whole code.
Generate a Gemini key and store it in a .env file.
Enable Google Sheets API in Google Cloud, create a Service Account, and download the JSON key file.
Place the JSON file in your project (keep it secret, add to `.gitignore`).
Share your Google Sheet with the service account email (Editor access) that you will find in the credentials with .com ending.


