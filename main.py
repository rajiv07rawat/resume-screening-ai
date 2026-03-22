from src.resume_parser import load_resumes
from src.text_preprocessing import clean_text
from src.vectorizer import build_vectorizer
from src.similarity_scoring import compute_similarity
from src.ranking import rank_candidates


def main():

    print("\nPaste Job Description (press Enter twice to submit):\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    job_description = " ".join(lines)

    resumes = load_resumes("data/resumes")

    resume_texts = [clean_text(r["text"]) for r in resumes]
    jd_clean = clean_text(job_description)

    # vectorizer = build_vectorizer()

    # vectors = vectorizer.fit_transform(resume_texts + [jd_clean])

    # resume_vectors = vectors[:-1]
    # jd_vector = vectors[-1]

    # scores = compute_similarity(jd_vector, resume_vectors)

    scores = compute_bert_similarity(job_description, resumes)

    ranking = rank_candidates(resumes, scores)

    print("\nCandidate Ranking:\n")
    print(ranking)

    print("\nTop 3 Candidates:\n")
    print(ranking.head(3))


if __name__ == "__main__":
    main()