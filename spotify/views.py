from django.shortcuts import render
from .models import Music

def home(request):
    musics = Music.objects.all()
    context = {
        'musics': musics
    }
    return render(request, 'home.html', context)