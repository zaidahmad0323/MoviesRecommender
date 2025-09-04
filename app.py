from flask import Flask, render_template, request
import joblib
import requests

app = Flask(__name__)

# Load data
movies = joblib.load('model/movies.pkl')  # DataFrame of movies
similarity = joblib.load('model/similarity.pkl')  # similarity matrix

TMDB_API_KEY = "261c45208c26c74897560d639a911877"  # Replace with your TMDB API key


# Fetch poster
def fetch_poster(movie_id):
    if not movie_id:
        return "https://via.placeholder.com/500x750?text=No+Image"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    try:
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=No+Image"


# Recommendation function
def recommend(movie_name):
    recommended_movies = []
    recommended_posters = []
    if movie_name not in movies['title'].values:
        return []

    idx = movies[movies['title'] == movie_name].index[0]
    sim_scores = sorted(
        list(enumerate(similarity[idx])), key=lambda x: x[1], reverse=True
    )[1:6]

    for i in sim_scores:
        movie_index = i[0]
        recommended_movies.append(movies.iloc[movie_index]['title'])
        recommended_posters.append(fetch_poster(movies.iloc[movie_index]['id']))

    return list(zip(recommended_posters, recommended_movies))


@app.route("/", methods=["GET", "POST"])
def home():
    selected_movie = None
    recommendations = []
    movie_list = movies['title'].values.tolist()

    if request.method == "POST":
        selected_movie = request.form.get("movie")
        recommendations = recommend(selected_movie)

    return render_template(
        "index.html",
        movie_list=movie_list,
        selected_movie=selected_movie,
        recommendations=recommendations,
    )


if __name__ == "__main__":
    app.run(debug=True)
