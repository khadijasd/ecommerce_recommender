import sys
import os

# Add the parent directory to sys.path so ecommerce_recommender is found
sys.path.append(os.path.abspath(".."))

from ecommerce_recommender.recommender import ContentBasedRecommender

def test_recommender():
    rec = ContentBasedRecommender("data/products.csv")
    rec.preprocess()
    recommendations = rec.get_recommendations(1)
    assert not recommendations.empty
    print("✅ Test passed: Recommendations generated successfully.")

if __name__ == "__main__":
    test_recommender()
