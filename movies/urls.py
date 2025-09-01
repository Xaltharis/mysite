from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home' ),
    path('about/', about, name='about'),
    path('addmovie/', add_movie, name='add_movie'),
    path('post/<int:post_id>/', show_movie, name='post'),
    path('director/<int:director_id>/', show_director, name='director'),
    path('genre/<int:genre_id>/', movie_by_genre, name='genre'),
]