from django import forms
from .models import Music


class AddMusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = [
            'title', 'artist',  'audio_file', 'cover_image', 'album'
        ]