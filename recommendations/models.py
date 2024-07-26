

# Create your models here.
from django.db import models

class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    user_id = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()

    def __str__(self):
        return f"User {self.user_id} - {self.movie.name}: {self.rating}"
