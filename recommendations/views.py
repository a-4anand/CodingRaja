from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
ratings = pd.read_parquet("data/Netflix_Dataset_Rating.parquet")
movies = pd.read_csv("data/Netflix_Dataset_Movie.csv")

# Create Term Frequency matrix using TF-IDF with original titles
vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
tfidf = vectorizer.fit_transform(movies["Name"])

def search(Name):
    query_vec = vectorizer.transform([Name])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argsort(similarity)[::-1][:5]  # Sort in descending order
    results = movies.iloc[indices]
    if results.empty:
        return pd.DataFrame(columns=["Movie_ID", "Year", "Name"])
    return results

def find_similar_movies(movie_id):
    similar_users = ratings[(ratings["Movie_ID"] == movie_id) & (ratings["Rating"] >= 4)]["User_ID"].unique()
    similar_users_recs = ratings[(ratings["User_ID"].isin(similar_users)) & (ratings["Rating"] >= 4)]["Movie_ID"]
    similar_users_recs = similar_users_recs.value_counts() / len(similar_users)
    similar_users_recs = similar_users_recs[similar_users_recs > 0.1]
    all_users = ratings[(ratings["Movie_ID"].isin(similar_users_recs.index)) & (ratings["Rating"] >= 4)]
    all_users_recs = all_users["Movie_ID"].value_counts() / len(all_users["User_ID"].unique())
    rec_percentages = pd.concat([similar_users_recs, all_users_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]
    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    return rec_percentages.head(10).merge(movies, left_on="Movie_ID", right_on="Movie_ID")[["Movie_ID", "Year", "Name"]]

def home(request):
    return render(request, 'recommendations/home.html')

def search_movies(request):
    if request.method == 'POST':
        title = request.POST.get('movie-title', '')
        results = search(title)
        return render(request, 'recommendations/search.html', {'results': results})
    return render(request, 'recommendations/search.html')

def recommend_movies(request, movie_id):
    recommendations = find_similar_movies(movie_id)
    movie = movies[movies["Movie_ID"] == movie_id].iloc[0]
    return render(request, 'recommendations/recommend.html', {'recommendations': recommendations, 'movie': movie})
