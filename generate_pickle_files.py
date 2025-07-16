import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie dictionary
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Optional: fill missing values
movies.fillna('', inplace=True)

# Combine relevant features (adjust depending on your dataset)
# If you already have a 'tags' column, use that.
if 'tags' not in movies.columns:
    if 'overview' in movies.columns and 'genres' in movies.columns:
        movies['tags'] = movies['overview'] + ' ' + movies['genres']
    else:
        raise Exception("Your dataset must include 'tags' or both 'overview' and 'genres' columns.")

# Convert text to feature vectors
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Compute cosine similarity
similarity = cosine_similarity(vectors)

# Save the similarity matrix
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ similarity.pkl has been regenerated successfully.")
