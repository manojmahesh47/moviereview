from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField('Actor', related_name='movies', blank=True)
    release_date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    trailer_link = models.URLField(blank=True)
    image = models.URLField(default=None, null=True)
    averageRating= models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username