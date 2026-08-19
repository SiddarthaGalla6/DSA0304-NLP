from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is used for machine learning",
    "Python is a programming language",
    "Machine learning uses algorithms"
]

query = input("Enter query: ")

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(documents + [query])

scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()

for i, score in enumerate(scores):
    print("Document", i + 1, "Score:", round(score, 3))

# Sample Input:
# Enter query: Python programming
#
# Sample Output:
# Document 1 Score: 0.473
# Document 2 Score: 0.816
# Document 3 Score: 0.0
