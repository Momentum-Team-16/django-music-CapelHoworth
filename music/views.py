from django.shortcuts import render

# Create your views here.
# This is where actions happen. They are triggered by the user (or an AJAX request w/ JS) visiting a url.


def index(request):
    context = {}
    # context will be data from the db
    return render(request, 'music/index.html', context)
