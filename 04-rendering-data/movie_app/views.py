from django.shortcuts import render
from .models import Movie


# Create your views here.
def get_movie(request):
    movies = Movie.objects.all()
    context = {
        "movies": movies,
    }
    return render(request, "movie_app/movie_app_home.html", context)
