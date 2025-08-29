# 🎬 Movies Recommender System

A simple **Movie Recommendation System** built with Python and Machine Learning.  
This project recommends movies based on similarity scores calculated from a dataset of movies.  

---

## 🚀 Features
- 📊 Uses **content-based filtering** to recommend movies  
- 🔍 Search any movie and get **top similar movies**  
- 🧠 Machine learning model built with **scikit-learn**  
- 📦 Simple Python script for inference  
- 🔗 Easy to integrate into other apps (Flask/Django frontend)

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Pandas** for data manipulation
- **scikit-learn** for machine learning
- **Pickle** for model saving/loading
- (Optional) **Flask** for serving the model

---

## 📂 Project Structure
MoviesRecommender/
│
├── app.py                          # Main Flask app
├──README
├──Procfile
├──requirements.txt                 # List of dependencies
│                       
├── model
│   ├── similarity.pkl               # Pickled similarity or ML model
│   ├── movies.pkl                   # Pickled DataFrame of movies with IDs
├── static/                          # Static assets (CSS, images, JS)
│   ├── style.css
│   └── script.js
│
└── templates/                       # HTML templates for Flask
│    └── index.html

---

## ⚙️ Installation
```bash
# Clone the repository
git clone https://github.com/zaidahmad0323/MoviesRecommender.git
cd MoviesRecommender

# Install dependencies
pip install -r requirements.txt

# Run the recommender script
python recommend.py

# If using Flask
python app.py

Enter a movie name: Avatar
Top 5 recommended movies:
1. Guardians of the Galaxy
2. Avengers: Endgame
3. Thor: Ragnarok
4. Iron Man
5. Doctor Strange

🔮 Future Improvements

✅ Add collaborative filtering
✅ Deploy as a web app
✅ Build a front-end with React
🤝 Contributing

Pull requests are welcome!
If you’d like to contribute, please fork the repo and submit a PR.

📜 License
This project is licensed under the MIT License.

🙋‍♂️ About Me
Zaid Ahmad
Aspiring AI Engineer | Python & ML Enthusiast
📧 zaidahmad0323@gmail.com
🌐 LinkedIn

