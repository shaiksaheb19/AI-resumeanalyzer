import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if token.is_alpha and not token.is_stop])

def get_similarity(resume_text, job_desc):
    texts = [preprocess(resume_text), preprocess(job_desc)]
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(texts)
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)
