# AI Resume Matcher

AI Resume Matcher is a Streamlit web application that helps you optimize your resume for a specific job description using Google Gemini (Generative AI). It extracts text from your uploaded resume (PDF, DOCX, or image), compares it to a job description, and rewrites your resume to better fit the job. The results are saved to a Google Sheet for easy tracking.

---

## Features

- **Resume Parsing:** Supports PDF, DOCX, and image files (PNG, JPG, etc.).
- **Job Description Input:** Paste or type the job description.
- **AI-Powered Resume Rewriting:** Uses Gemini LLM to tailor your resume to the job.
- **Google Sheets Integration:** Saves job info, job link, job description, and the AI-modified resume.
- **Simple UI:** Built with Streamlit for easy use.


## Steps to Get Started

1. **Clone the repository** and navigate to the project directory.

2. **Set up the Gemini API key:**
   - Generate a Gemini API key from Google AI Studio.
   - Create a `.env` file in the project root and add your key:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

3. **Enable Google Sheets API:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Google Sheets API and Google Drive API for your project.
   - Create a Service Account and download the JSON credentials file.

4. **Add credentials to your project:**
   - Place the downloaded JSON key file in your project directory.
   - Make sure to add the filename to your `.gitignore` to keep it secret.

5. **Share your Google Sheet:**
   - Create a Google Sheet to store results.
   - Share the sheet with the service account email (ending with `.com`) found in your credentials file, giving it Editor access.

6. **Run the app:**
   - Use `app.py` to run the complete application:
     ```
     streamlit run app.py
     ```


