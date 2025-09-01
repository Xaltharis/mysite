from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render, get_object_or_404

from .models import Movie, Director, Genre

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить фильм', 'url_name': 'add_movie'},
]

def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()

    param = {
        'menu': menu,
        'movies': movies,
        'genres': genres,
        'title': 'Главная страница'
    }
    return render(request, 'movies/index.html', context=param)

def about(request):
    movie_count = Movie.objects.filter(is_published=True).count()
    director_count = Director.objects.count()

    param = {
        'menu': menu,
        'title': 'О сайте',
        'movie_count': movie_count,
        'director_count': director_count,
    }

    return render(request, 'movies/about.html', context=param)

def add_movie(request):
    return HttpResponse('Добавление фильма')

def show_movie(request, post_id):
    movie = get_object_or_404(Movie, pk=post_id)
    param = {
        'menu': menu,
        'title': movie.title,
        'movie': movie,
    }

    return render(request, 'movies/movie_detail.html', context=param)

def show_director(request, director_id):
    return HttpResponse(f'Страница режиссёра с ID = {director_id}')

def movie_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    movies = Movie.objects.filter(genres=genre)

    param = {
        'menu': menu,
        'movies': movies,
        'title': f'Фильмы в жанре: {genre.name}'
    }
    return render(request, 'movies/movies_by_category.html', context=param)

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')