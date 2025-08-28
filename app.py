from flask import Flask, render_template, request
import joblib
import requests

app = Flask(__name__)

# Load your data
movies = joblib.load('model/movies.pkl')  # your dataframe
similarity = joblib.load('model/similarity.pkl')  # similarity matrix

TMDB_API_KEY = "261c45208c26c74897560d639a911877"  # replace with your TMDB API key

def fetch_poster(movie_id):
    if not movie_id:
        return "https://via.placeholder.com/500x750?text=No+Image"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    try:
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500" + poster_path
            return full_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie_name):
    recommended_movies = []
    recommended_posters = []
    if movie_name not in movies['title'].values:
        return [], []
    idx = movies[movies['title'] == movie_name].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # top 5 recommendations
    for i in sim_scores:
        movie_index = i[0]
        recommended_movies.append(movies.iloc[movie_index]['title'])
        recommended_posters.append(fetch_poster(movies.iloc[movie_index]['id']))  # your column is 'id'
    return recommended_movies, recommended_posters

@app.route("/", methods=["GET", "POST"])
def home():
    selected_movie = None
    recommendations = []
    if request.method == "POST":
        selected_movie = request.form.get("movie")
        recommended_movies, recommended_posters = recommend(selected_movie)
        recommendations = list(zip(recommended_movies, recommended_posters))

    return render_template(
        "index.html",
        movies=movies['title'].values,  # for dropdown
        recommendations=recommendations,
        selected_movie=selected_movie
    )

if __name__ == "__main__":
    app.run(debug=True)