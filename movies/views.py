from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render, get_object_or_404

from .models import Movie

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить фильм', 'url_name': 'add_movie'},
]

def index(request):
    movies = Movie.objects.all()
    param = {
        'menu': menu,
        'movies': movies,
        'title': 'Главная страница'
    }
    return render(request, 'movies/index.html', context=param)

def about(request):
    return render(request, 'movies/about.html', {'menu': menu, 'title': 'О сайте'})

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

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')