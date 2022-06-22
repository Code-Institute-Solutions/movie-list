from django.test import TestCase
from .forms import MovieForm


class TestMovieForm(TestCase):
    def test_movie_title_is_required(self):
        form = MovieForm({"title": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors.keys())
        self.assertEqual(form.errors["title"][0], "This field is required.")

    def test_description_field_is_not_required(self):
        form = MovieForm({"title": "The Living Daylights",
                          "director": "John Glen",
                          "genre": "Action",
                          "rating": 4,
                          "watched": True,
                          "imdb_link": "https://www.imdb.com/title/tt0093428/"})
        self.assertTrue(form.is_valid())

    def test_watched_field_is_not_required(self):
        form = MovieForm({"title": "The Living Daylights",
                          "director": "John Glen",
                          "description": "First Timothy Dalton",
                          "genre": "Action",
                          "rating": 4,
                          "imdb_link": "https://www.imdb.com/title/tt0093428/"})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = MovieForm()
        self.assertEqual(
            form.Meta.fields,
            [
                "title",
                "director",
                "genre",
                "description",
                "rating",
                "watched",
                "imdb_link",
            ],
        )
