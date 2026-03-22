import os
import PyPDF2
import docx


def extract_text_from_pdf(file_path):

    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text


def extract_text_from_docx(file_path):

    doc = docx.Document(file_path)

    text = ""

    for para in doc.paragraphs:
        text += para.text

    return text


def load_resumes(folder_path):

    resumes = []

    for file in os.listdir(folder_path):

        path = os.path.join(folder_path, file)

        if file.endswith(".pdf"):
            text = extract_text_from_pdf(path)

        elif file.endswith(".docx"):
            text = extract_text_from_docx(path)

        else:
            continue

        resumes.append({
            "file_name": file,
            "text": text
        })

    return resumes