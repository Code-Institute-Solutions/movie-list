from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm


# Create your views here.
def get_movie(request):
    movies = Movie.objects.all()
    context = {
        "movies": movies,
    }
    return render(request, "movie_app/movie_app_home.html", context)


def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_movie')
    form = MovieForm()
    context = {'form': form}
    return render(request, 'movie_app/add_movie.html', context)


def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('get_movie')
    form = MovieForm(instance=movie)
    context = {'form': form}
    return render(request, 'movie_app/edit_movie.html', context)


def toggle_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.watched = not movie.watched
    movie.save()
    return redirect('get_movie')


def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('get_movie')
