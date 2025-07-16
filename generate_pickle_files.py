import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset (you can replace this with full dataset)
data = {
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['The Matrix', 'John Wick', 'The Dark Knight', 'Batman Begins', 'Inception'],
    'tags': [
        'sci-fi action hacker',
        'assassin action revenge',
        'dc superhero joker batman',
        'batman origin dc action',
        'dream sci-fi action thriller'
    ]
}

df = pd.DataFrame(data)

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(df['tags']).toarray()

# Similarity calculation
similarity = cosine_similarity(vectors)

# Save files
pickle.dump(df, open('movies.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ Pickle files generated successfully!")
