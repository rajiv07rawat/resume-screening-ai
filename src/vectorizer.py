from sklearn.feature_extraction.text import TfidfVectorizer


def build_vectorizer():

    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1,2)
    )

    return vectorizer