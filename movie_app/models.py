from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Director(models.Model):
    name = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(default=1, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])

