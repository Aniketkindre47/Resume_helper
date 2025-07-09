import google.generativeai as genai


# ---- CONFIG ----
GEMINI_API_KEY = "AIzaSyA3fw8r3859Ot7lXJM5zYe90GH0tdqJexg"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
