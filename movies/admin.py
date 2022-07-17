from .models import Movie, deletedMovie

from django.contrib import admin

admin.site.register(Movie)
admin.site.register(deletedMovie)
