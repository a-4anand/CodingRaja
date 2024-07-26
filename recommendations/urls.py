from django.urls import path
from .views import home, search_movies, recommend_movies

urlpatterns = [
    path('', home, name='home'),
    path('search/', search_movies, name='search_movies'),
    path('recommend/<int:movie_id>/', recommend_movies, name='recommend_movies'),
]
