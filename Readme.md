# AI Resume Screening System

This project is an AI-based resume screening tool that helps recruiters match resumes with job descriptions and rank candidates based on relevance.

## Features
- Resume parsing from PDF and DOCX
- NLP-based text preprocessing
- TF-IDF based similarity scoring
- BERT-based semantic matching
- Candidate ranking system
- Streamlit dashboard for recruiter interaction
- Resume upload functionality

## Tech Stack
- Python
- Scikit-learn
- Sentence Transformers (BERT)
- Streamlit
- NLTK

## Workflow
1. Upload resumes (PDF/DOCX)
2. Enter job description
3. System processes resumes
4. Computes similarity scores
5. Ranks candidates

## How to Run

Install dependencies:

pip install -r requirements.txt


Run the dashboard:
streamlit run dashboard/app.py


## Project Structure

resume_screening_ai
│
├── data

├── src

├── dashboard

├── main.py

├── requirements.txt

└── README.md



## Key Highlights
- Built a recruiter-facing dashboard
- Implemented semantic matching using BERT
- Designed an end-to-end NLP pipeline
