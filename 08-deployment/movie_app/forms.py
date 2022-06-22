from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    """
    Form for entering data to Movie model
    """
    class Meta:
        model = Movie
        fields = ['title', 'director', 'genre', 'description', 'rating',
                  'watched', 'imdb_link']

