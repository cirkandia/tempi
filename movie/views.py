from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Create your views here.
def home(request):
    #return render(request, 'home.html')


    searchterm = request.GET.get('searchMovie')
    if searchterm:
        movies=Movie.objects.filter(title__icontains=searchterm)
    else:
        movies=Movie.objects.all()
    return render(request, 'home.html', {'searchterm':searchterm, 'movies':movies})

    return render(request, 'home.html', {'name': 'johan mesa'})

    


def About(request):
    return HttpResponse('<h1>about aqui???</h1>')

def About2(request):
    return render(request, 'about2.html')