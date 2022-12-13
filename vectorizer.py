from modules import *

# Script to vectorize the data

def tfidf_vectorize_data(data):
    tfidf = TfidfVectorizer()
    tfidfTransform = tfidf.fit_transform(data["source_original"])
    return tfidf, tfidfTransform
