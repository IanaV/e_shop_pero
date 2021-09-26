from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'home/index.html', data)


def about(request):
    return render(request, 'home/about.html')