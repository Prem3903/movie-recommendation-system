import streamlit as st
import pandas as pd
import pickle

# Load movie data and similarity matrix
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movies

# Streamlit UI
st.title('🎥 Movie Recommendation System')

selected_movie_name = st.selectbox('Select a movie to get recommendations:', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.subheader("You might also like:")
    for i in recommendations:
        st.write(f"👉 {i}")
