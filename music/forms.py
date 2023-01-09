from django import forms
from .models import Album, Artist, Song

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['name']

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ['name']

class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['artist', 'title', 'album', 'genre', 'language', 'release_date']