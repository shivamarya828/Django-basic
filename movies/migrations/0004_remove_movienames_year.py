# Generated by Django 4.0.6 on 2022-07-18 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rename_movie_movienames'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movienames',
            name='year',
        ),
    ]
