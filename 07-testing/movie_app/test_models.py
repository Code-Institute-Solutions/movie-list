from django.test import TestCase
from .models import Movie

class TestModels(TestCase):

    def test_watched_defaults_to_false(self):
        movie = Movie.objects.create(title="The Living Daylights",
                                     director="John Glen",
                                     genre="Action",
                                     rating=4,
                                     imdb_link="https://www.imdb.com/title/tt0093428/")
        self.assertFalse(movie.watched)

    def test_movie_string_method_returns_title(self):
        movie = Movie.objects.create(title="The Living Daylights",
                                     director="John Glen",
                                     genre="Action",
                                     rating=4,
                                     imdb_link="https://www.imdb.com/title/tt0093428/")
        self.assertEqual(str(movie), "The Living Daylights")
