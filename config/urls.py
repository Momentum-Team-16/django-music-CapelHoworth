"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from music import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    # this gives us all the registration urls
    # we are particularly interested in 'accounts/login' and 'accounts/logout'
    path('', views.index, name="home"),
    # url pattern that user visits, view that's called, context (if you have it), name argument (a nickname/shortcut used to refer to this path in other places in the project)
    path('albums/new', views.create_album, name='create-album'),
    path('songs/new', views.create_song, name='create-song'),
    # path('artists/new', views.create_artist, name='create-artist'),
]

