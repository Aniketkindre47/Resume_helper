import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime



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
