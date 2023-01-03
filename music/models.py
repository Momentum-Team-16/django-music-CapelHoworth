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



class Album(models.Model):
    ROCK = 'RK'
    JAZZ = 'JZ'
    METAL = 'MT'
    POP = 'PO'

    GENRE_CHOICES = [
        (ROCK, 'Rock'),
        (JAZZ, 'Jazz'),
        (METAL, 'Metal'),
        (POP, 'Pop')
    ]

    artist = models.CharField(max_length=200)
    edtition = models.CharField(max_length=3)
    condition = models.CharField(
        max_length=2,
        choices=GENRE_CHOICES
    )
    language = models.CharField(max_length=200)
    release_date = models.DateField(blank=True, null=True)
    # fields are required unless we explicitly make them optional with blank=True, null=True
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    # this article is helpful for implementing image fields