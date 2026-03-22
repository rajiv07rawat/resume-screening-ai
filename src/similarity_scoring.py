from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(jd_vector, resume_vectors):

    scores = cosine_similarity(resume_vectors, jd_vector)

    return scores