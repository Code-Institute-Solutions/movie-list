from django.shortcuts import render

# Create your views here.
def get_movie(request):
    return render(request, "movie_app/movie_app_home.html")
