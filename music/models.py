from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # extends Django's built-in AbstractUser class
    # adding optional fields for additional user info
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def artists_from_songs(self):
        return [song.artist for song in self.songs.all()]


class Song(models.Model):
    ROCK = 'RK'
    JAZZ = 'JZ'
    METAL = 'MT'
    POP = 'PO'
    ALTERNATIVE = 'AL'
    HIP_HOP = 'HH'
    COUNTRY = 'CO'

    GENRE_CHOICES = [
        (ROCK, 'Rock'),
        (JAZZ, 'Jazz'),
        (METAL, 'Metal'),
        (POP, 'Pop'),
        (ALTERNATIVE, 'Alternative'),
        (HIP_HOP, 'Hip-Hop/Rap'),
        (COUNTRY, 'Country')
    ]

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True, related_name="songs")
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name="songs")
    genre = models.CharField(
        max_length=2,
        choices=GENRE_CHOICES
    )
    language = models.CharField(max_length=200, default='eng')
    release_date = models.CharField(max_length=50, blank=True, null=True)
    # fields are required unless we explicitly make them optional with blank=True, null=True
    date_added = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # this article is helpful for implementing image fields

    def __str__(self):
        return f'{self.title} by {self.artist} on {self.album}'