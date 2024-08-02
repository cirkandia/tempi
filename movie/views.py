from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'johan mesa'})

def About(request):
    return HttpResponse('<h1>about aqui???</h1>')

def About2(request):
    return render(request, 'about2.html')