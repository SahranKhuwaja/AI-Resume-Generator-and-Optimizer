from docx import Document
import fitz
from io import BytesIO
from base_models.data_basemodel import Data

def get_data_from_file_type(file) -> Data:
    file_bytes = file.read()
    raw_text = ""
    if file.filename.endswith('.txt'):
        raw_text = file_bytes.decode('utf-8', errors="ignore")
    elif file.filename.endswith('.pdf'):
        raw_text = extract_text_from_pdf(file_bytes)
    elif file.filename.endswith('docx'):
        raw_text = extract_text_from_doc(file_bytes)
    else:
        return Data(text="",error="File type not supported", success=False)
    
    return Data(text=raw_text, success=True)

def extract_text_from_pdf(file_bytes):
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def extract_text_from_doc(file_bytes):
    doc = Document(BytesIO(file_bytes))
    return "\n".join([para.text for para in doc.paragraphs])
