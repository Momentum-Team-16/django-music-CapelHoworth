# Generated by Django 4.1.5 on 2023-01-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_alter_song_album_alter_song_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='language',
            field=models.CharField(default='eng', max_length=200),
        ),
    ]