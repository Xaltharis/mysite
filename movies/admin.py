from django.contrib import admin
from .models import Genre, Movie, Director, Watchlist

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_year', 'rating', 'is_published', 'director')
    list_filter = ('is_published', 'genres', 'release_year')
    search_fields = ('title', 'description')

    readonly_fields = ('time_create', 'time_update')

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'poster')
        }),
        ('Данные о релизе', {
            'fields': (('release_year', 'rating'),)
        }),
        ('Связи', {
            'fields': ('director', 'genres')
        }),
        ('Статус', {
            'classes': ('collapse',),
            'fields': ('is_published', 'time_create', 'time_update')
        }),
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description')
        }),
    )

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

    fieldsets = (
        ('Основная информация', {
            'fields': ('first_name', 'last_name', 'birth_date')
        }),
        ('Биография и фото', {
            'fields': ('biography', 'photo')
        }),
    )

    @admin.register(Watchlist)
    class WatchlistAdmin(admin.ModelAdmin):
        list_display = ('id', 'user', 'movie', 'watched_on')
        list_filter = ('user', 'movie')