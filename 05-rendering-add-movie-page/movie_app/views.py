from django.shortcuts import render, redirect
from .models import Movie


# Create your views here.
def get_movie(request):
    movies = Movie.objects.all()
    context = {
        "movies": movies,
    }
    return render(request, "movie_app/movie_app_home.html", context)

def add_movie(request):
    if request.method == "POST":
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        watched = 'watched' in request.POST
        imdb_link = request.POST.get('imdb_link')
        Movie.objects.create(title=title, director=director, genre=genre,
                             description=description, rating=rating,
                             watched=watched, imdb_link=imdb_link)
        return redirect('get_movie')

    return render(request, 'movie_app/add_movie.html')

