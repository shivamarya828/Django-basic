from turtle import title
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render 
from .models import Movie, deletedMovie

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies':data})

def homepage(request):
    return render(request, 'movies/homepage.html')

def details(request, id):
    data = Movie.objects.get(pk = id)
    return render(request, 'movies/details.html', {'movie':data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year = year)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request, 'movies/add.html')

def delete(request, id):
    try:
        movie = Movie.objects.get(pk = id)
    except:
        raise Http404('Movie does not exist')
    movie = Movie.objects.get(pk = id)
    deleted = deletedMovie()
    deleted.title = movie.title
    deleted.year = movie.year
    deleted.save()
    movie.delete()
    return HttpResponseRedirect('/movies')

def update(request, id):
    title = request.POST.get('title')
    year = request.POST.get('year')
    movie = Movie.objects.get(pk = id)
    if title and year:
        Movie.objects.get(pk = id).delete()
        movie = Movie(title = title, year = year, id = id)
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
    movie = Movie()
    movie.title = deleted.title
    movie.year = deleted.year
    deleted.delete()
    movie.save()
    return HttpResponseRedirect('/movies')
