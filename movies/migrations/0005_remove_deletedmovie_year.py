# Generated by Django 4.0.6 on 2022-07-18 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_remove_movienames_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deletedmovie',
            name='year',
        ),
    ]
