import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommender:
    def __init__(self, product_path):
        self.products = pd.read_csv(product_path)
        self.tfidf_matrix = None
        self.similarity_matrix = None
        self.vectorizer = TfidfVectorizer()

    def preprocess(self):
        self.products["features"] = self.products["category"] + " " + self.products["brand"]
        self.tfidf_matrix = self.vectorizer.fit_transform(self.products["features"])
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)

    def get_recommendations(self, product_id, top_n=3):
        if self.similarity_matrix is None:
            raise Exception("Run preprocess() first.")
        
        index = self.products[self.products["product_id"] == product_id].index[0]
        scores = list(enumerate(self.similarity_matrix[index]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        recommended_indices = [i[0] for i in scores[1:top_n+1]]

        return self.products.iloc[recommended_indices]
