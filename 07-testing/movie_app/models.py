from django.db import models

# Create your models here.
class Movie(models.Model):
    """
    Stores a single movie entry
    """
    title = models.CharField(max_length=50, null=False, blank=False)
    director = models.CharField(max_length=50, null=False, blank=False)
    genre = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=400, null=False, blank=True)
    rating = models.IntegerField(null=False, blank=False)
    watched = models.BooleanField(default=False, null=False, blank=False)
    imdb_link = models.URLField(null=False, blank=False)

    def __str__(self):
        """
        Returns the movie title
        """
        return self.title
