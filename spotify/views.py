from django.shortcuts import render
from .models import Music

def home(request):
    musics = Music.objects.all()
    music_list = list(Music.objects.all().values())
    context = {
        'musics': musics,
        'music_list':music_list
    }
    return render(request, 'home.html', context)