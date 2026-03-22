import pandas as pd

def rank_candidates(resumes, scores):

    results = []

    for i, resume in enumerate(resumes):

        results.append({
            "candidate": resume["file_name"],
            "score": scores[i][0]
        })

    df = pd.DataFrame(results)

    df = df.sort_values(by="score", ascending=False)

    return df