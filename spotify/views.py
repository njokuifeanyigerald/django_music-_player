from django.shortcuts import redirect, render
from .models import Music, Album
from .forms import AddMusicForm

def home(request):
    musics = Music.objects.all().order_by('-date_created')
    music_list = list(Music.objects.all().values())
    context = {
        'musics': musics,
        'music_list':music_list
    }
    return render(request, 'home.html', context)


# def addMusic(request):
#     form =  AddMusicForm(request.POST, request.FILES or None)
#     if request.method == 'POST':
#         form =  AddMusicForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             # check if there is a data in the album field
#             album = form.cleaned_data.get('album')
#             print(album)
#             if album:
#                 album_data = Album.objects.get_or_create(name=album)
#                 print(album_data[0])
#                 instance.album = album_data[0]
#                 instance.save()
#                 return redirect('home')
#             else:
#                 instance.save()
#                 return redirect('home')
#     context = {
#         'form': form,
#     }
#     return render(request, 'addPage.html', context)



def addMusic(request):
    form=AddMusicForm()

    if request.method == 'POST':
        form=AddMusicForm(request.POST,request.FILES)
     
        if form.is_valid():
            form_data=form.save(commit=False)
            album=form.cleaned_data.get('album')
            if album:
                album_data=Album.objects.get_or_create(name=album)
                form_data.album=album_data[0]
                form_data.save()
                return redirect("home")
            else:
                form_data.save()
                return redirect("home")

        else:
            print("no",form.data)
    context = {
        'form':form
    }
    
    return render(request,'addPage.html', context)