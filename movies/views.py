from site import venv
from turtle import title
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render 
from .models import MovieNames, deletedMovie
from tmdbv3api import TMDb, Movie, Discover
import hashlib


tmdb = TMDb()
tmdb.language = 'en'
tmdb.debug = True
tmdb.api_key = '6b59c5d47eb2648c358ffa9b413ff9c1'

def movies(request):
    data = MovieNames.objects.all()
    discover = Discover()
    m = discover.discover_movies({
        'sort_by': 'popularity.desc'
    })
    for a in m:
        a['id'] = int(hashlib.sha1(a['title'].encode("utf-8")).hexdigest(), 16) % (10 ** 8)
    
    return render(request, 'movies/movies.html', {'movies':data, 'popular':m})

def homepage(request):
    return render(request, 'movies/homepage.html')

def details(request, id):
    data = MovieNames.objects.get(pk = id)
    mo = Movie() #from tmdbv3api
    search = mo.search(data.title)
    if len(search) == 0:
        delete(request, id)
        return render(request, 'movies/error.html')
    search[0]['id'] = data.id
    return render(request, 'movies/details.html', {'movie':search[0]})

def add(request):
    title = request.POST.get('title')
    if title:
        movie = MovieNames(title=title)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request, 'movies/add.html')

def delete(request, id):
    try:
        movie = MovieNames.objects.get(pk = id)
    except:
        raise Http404('Movie does not exist')
    movie = MovieNames.objects.get(pk = id)
    deleted = deletedMovie()
    deleted.title = movie.title
    deleted.save()
    movie.delete()
    return HttpResponseRedirect('/movies')

def update(request, id):
    title = request.POST.get('title')
    movie = MovieNames.objects.get(pk = id)
    if title:
        MovieNames.objects.get(pk = id).delete()
        movie = MovieNames(title = title, id = id)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request, 'movies/update.html', {'movie': movie})

def deleted(request):
    data = deletedMovie.objects.all()
    return render(request, 'movies/deleted.html', {'data': data})

def restore(request, id):
    try:
        deleted = deletedMovie.objects.get(pk = id)
    except:
        raise Http404('Movie does not exist')
    movie = MovieNames()
    movie.title = deleted.title
    deleted.delete()
    movie.save()
    return HttpResponseRedirect('/movies/deleted')

def popular(request, title):
    mo = Movie() #from tmdbv3api
    search = mo.search(title)
    search[0]['id'] = int(hashlib.sha1(title.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
    return render(request, 'movies/detailspopular.html', {'movie':search[0]})


def permanent(request):
    data = deletedMovie.objects.all()
    return render(request, 'movies/perdelete.html', {'data': data})

def delete_permanent(request, id):
    deletedMovie.objects.get(pk = id).delete()
    return HttpResponseRedirect('movies/deleted/permanent')

