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

📸 **Example - Dropdown Selection:**
![Dropdown Selection](<img width="1461" height="707" alt="image" src="https://github.com/user-attachments/assets/d6fd01f3-37b1-4504-8745-56830fba96d9" />
)

---

## 🧠 How it Works

- Uses a preprocessed dataset of movies with genre, overview, and keywords
- Generates **TF-IDF vectors** or **CountVectorizer vectors**
- Computes **cosine similarity** between movies
- Shows top 5 most similar titles

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt
streamlit run app.py
