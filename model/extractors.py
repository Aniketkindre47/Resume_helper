import fitz
import docx
from PIL import Image
import pytesseract
import re


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

