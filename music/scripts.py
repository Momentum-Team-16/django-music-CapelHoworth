import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '../config.settings')


from django.conf import settings
import json
import models

with open('test.json') as f:
    data = json.load(f)
    print(type(data), data)


song = models.Song.objects.create(
    title=data.get('trackName'))
