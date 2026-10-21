from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    rating = models.CharField(max_length=20)  # e.g., PG-13, R, star rating

    def __str__(self):
        return f"{self.title} ({self.release_year})"