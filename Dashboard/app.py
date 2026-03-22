import streamlit as st
import sys
import os
import tempfile

# fix for src import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.text_preprocessing import clean_text
from src.vectorizer import build_vectorizer
from src.similarity_scoring import compute_similarity
from src.ranking import rank_candidates
from src.resume_parser import extract_text_from_pdf, extract_text_from_docx

from src.bert_similarity import compute_bert_similarity


# ---------------- UI ---------------- #

st.title("AI Resume Screening System")

st.write("Paste Job Description below:")

job_description = st.text_area("Job Description", height=200)

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF/DOCX)",
    type=["pdf", "docx"],
    accept_multiple_files=True
)


# ---------------- Logic ---------------- #

if st.button("Run Screening"):

    if job_description.strip() == "":
        st.warning("Please enter a job description.")
        st.stop()

    if not uploaded_files:
        st.warning("Please upload at least one resume.")
        st.stop()

    resumes = []

    for file in uploaded_files:

        # temp file create
        with tempfile.NamedTemporaryFile(delete=False, suffix=file.name) as tmp:
            tmp.write(file.read())
            temp_path = tmp.name

        # extract text
        if file.name.endswith(".pdf"):
            text = extract_text_from_pdf(temp_path)

        elif file.name.endswith(".docx"):
            text = extract_text_from_docx(temp_path)

        else:
            continue

        resumes.append({
            "file_name": file.name,
            "text": text
        })

    # preprocessing
    resume_texts = [clean_text(r["text"]) for r in resumes]
    jd_clean = clean_text(job_description)

    # vectorization
    vectorizer = build_vectorizer()
    vectors = vectorizer.fit_transform(resume_texts + [jd_clean])

    resume_vectors = vectors[:-1]
    jd_vector = vectors[-1]

    # similarity
    scores = compute_similarity(jd_vector, resume_vectors)

    # ranking
    ranking = rank_candidates(resumes, scores)

    # ---------------- Output ---------------- #

    st.subheader("Candidate Ranking")
    st.dataframe(ranking)

    st.subheader("Top 3 Candidates")
    st.dataframe(ranking.head(3))