from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    albums = models.ManyToManyField('Album')

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    genres = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
