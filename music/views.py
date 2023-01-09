from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Album, Song, Artist
from .forms import AlbumForm, SongForm


# Create your views here.
# This is where actions happen. They are triggered by the user (or an AJAX request w/ JS) visiting a url.


def index(request):
    albums = Album.objects.all()
    form = AlbumForm()
    context = {
        'form': form,
        'albums': albums
    }
    # context will be data from the db
    return render(request, 'music/index.html', context)


def create_album(request):
    if request.method == 'POST':
        # if the form was submitted
        form = AlbumForm(request.POST)
        # this form is 'bound', meaning it is populated with data that the user entered
        if form.is_valid():
            # breakpoint()
            # checks if the data from the form can actually be saved in the db without error
            album = form.save(commit=False)
            # commit is false to hold on saving in db until additional info added
            album.owner = request.user
            album.save()
            # saves new instance of Album in the db
            return redirect('home')
    # builds a blank card form to render on the page
    data = {
        'created': 'yes'
    }
    return JsonResponse(data)


def create_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.owner = request.user
            song.save()
            return redirect('home')

    data = {
        'created': 'yes'
    }
    return JsonResponse(data)