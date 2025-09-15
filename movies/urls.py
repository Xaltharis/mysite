from django.urls import path, re_path
from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    path('', index, name='home' ),
    path('about/', about, name='about'),
    path('addmovie/', add_movie, name='add_movie'),
    path('post/<int:post_id>/', show_movie, name='post'),
    path('director/<int:director_id>/', show_director, name='director'),
    path('director/<int:director_id>/movies/', movie_by_director, name='movies_by_director'),
    path('genre/<int:genre_id>/', movie_by_genre, name='genre'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_to_watchlist/<int:movie_id>/', add_to_watchlist, name='add_to_watchlist'),
    path('profile/', profile, name='profile'),
]