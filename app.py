import streamlit as st
import pandas as pd
import pickle

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('🎬 Movie Recommendation System')

# Debug shapes
st.write("📊 Movies shape:", movies.shape)
st.write("🧠 Similarity matrix shape:", similarity.shape)


def recommend(movie):
    if movie not in movies['title'].values:
        st.error(f"❌ Movie '{movie}' not found in dataset.")
        return []

    movie_index = movies[movies['title'] == movie].index[0]

    if movie_index >= similarity.shape[0]:
        st.error("⚠️ Similarity matrix and movie list are out of sync. Please regenerate 'similarity.pkl'.")
        return []

    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


selected_movie_name = st.selectbox(
    "🎥 Select a movie to get recommendations:",
    movies['title'].values
)

if st.button('🎯 Recommend'):
    recommendations = recommend(selected_movie_name)

    if recommendations:
        st.subheader("✅ You might also like:")
        for i in recommendations:
            st.write(f"👉 {i}")

st.markdown("---")
st.write("📌 You selected:", selected_movie_name)
