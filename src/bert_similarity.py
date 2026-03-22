from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# model load (once)
model = SentenceTransformer('all-MiniLM-L6-v2')


def compute_bert_similarity(job_description, resumes):

    # embeddings create
    jd_embedding = model.encode([job_description])

    resume_texts = [r["text"] for r in resumes]
    resume_embeddings = model.encode(resume_texts)

    # similarity
    scores = cosine_similarity(resume_embeddings, jd_embedding)

    return scores