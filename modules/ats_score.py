from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Calculate ATS Score
def calculate_ats_score(resume_text, job_description):

    documents = [resume_text, job_description]

    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    score = round(similarity[0][0] * 100, 2)

    return score