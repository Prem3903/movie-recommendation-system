# 🎬 Movie Recommendation System

A content-based movie recommendation system built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**. Users can select a movie from a dropdown and instantly get visually rich recommendations based on similarity scores.

---

## 🚀 Features

- Clean and modern UI with Streamlit
- Dropdown to select any movie title
- "Recommend" button to generate 5 similar movie suggestions
- Each suggestion includes:
  - Movie poster
  - Movie title
- Light and dark mode compatible

📸 **Some Visuals Of Movie Recommender System**

📸 **Example 1 - Home Page:**
<img width="1461" height="707" alt="image" src="https://github.com/user-attachments/assets/795ea4cd-6d7a-4e7c-bfe1-21e50ce2f982" />



📸 **Example 2 - Dropdown Selection:**

<img width="1325" height="783" alt="image" src="https://github.com/user-attachments/assets/e88ff5e1-042e-45ec-84e4-239591901d7a" />


📸 **Example 3 - Result With Movie Posters:**

<img width="1357" height="810" alt="image" src="https://github.com/user-attachments/assets/78f6b01c-559b-4a81-b477-7f6558319f99" />



---

## 🧠 How it Works

- Uses a preprocessed dataset of movies with genre, overview, and keywords
- Generates **TF-IDF vectors** or **CountVectorizer vectors**
- Computes **cosine similarity** between movies
- Shows top 5 most similar titles

---


## 🛠️ Technologies Used
- Python 🐍
- Pandas
- Numpy
- Scikit-learn
- Streamlit
- TMDB API (for fetching posters)



## 📦 Installation

```bash
git clone https://github.com/Prem3903/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt
streamlit run app.py
