from django.http import HttpResponse
from django.shortcuts import render 

data = {
    'movies':[
        {
            'id': 5,
            'title': 'Jaws',
        },
        {
            'id': 2,
            'title': 'Inception'
        }
    ]
    }

def movies(request):
    return render(request, 'movies/movies.html', data)

def homepage(request):
    return HttpResponse("Home page")