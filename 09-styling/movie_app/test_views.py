from django.test import TestCase
from .models import Movie

# Create your tests here.
class TestViews(TestCase):

    def test_get_movie_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_app/movie_app_home.html')

    def test_movie_app_add_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_app/add_movie.html')

    def test_movie_app_edit_page(self):
        movie = Movie.objects.create(title="The Living Daylights",
                                     director="John Glen",
                                     genre="Action",
                                     rating=4,
                                     imdb_link="https://www.imdb.com/title/tt0093428/")
        response = self.client.get(f'/edit/{movie.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_app/edit_movie.html')

    def test_can_add_movie(self):
        response = self.client.post('/add', {"title": "The Living Daylights",
                                             "director": "John Glen",
                                             "genre": "Action",
                                             "rating": 4,
                                             "imdb_link": "https://www.imdb.com/title/tt0093428/"})
        self.assertRedirects(response, '/')

    def test_can_delete_movie(self):
        movie = Movie.objects.create(title="The Living Daylights",
                                     director="John Glen",
                                     genre="Action",
                                     rating=4,
                                     imdb_link="https://www.imdb.com/title/tt0093428/")
        response = self.client.get(f'/delete/{movie.id}')
        self.assertRedirects(response, '/')
        existing_movies = Movie.objects.filter(id=movie.id)
        self.assertFalse(len(existing_movies), 0)

    def test_can_toggle_movie(self):
        movie = Movie.objects.create(title="The Living Daylights",
                                     director="John Glen",
                                     genre="Action",
                                     rating=4,
                                     watched=True,
                                     imdb_link="https://www.imdb.com/title/tt0093428/")
        response = self.client.get(f'/toggle/{movie.id}')
        self.assertRedirects(response, '/')
        updated_movie = Movie.objects.get(id=movie.id)
        self.assertFalse(updated_movie.watched)

    def test_can_edit_movie(self):
        movie = Movie.objects.create(title="The Living Daylights",
                                     director="John Glen",
                                     genre="Action",
                                     rating=4,
                                     watched=True,
                                     imdb_link="https://www.imdb.com/title/tt0093428/")
        response = self.client.post(f'/edit/{movie.id}',
                                    {"title": "The Living Daylights",
                                     "director": "John Glen",
                                     "genre": "Action",
                                     "rating": 5,
                                     "imdb_link": "https://www.imdb.com/title/tt0093428/"},
                                    )
        self.assertRedirects(response, "/")
        updated_movie = Movie.objects.get(id=movie.id)
        self.assertEqual(updated_movie.rating, 5)