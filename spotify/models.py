from django.db import models

from .validators import validate_audio
from .helpers import get_audio_length

class Music(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True, blank=True)
    time_length = models.DecimalField(blank=True, max_digits=6, decimal_places=2)
    audio_file = models.FileField(upload_to='musics', validators=[validate_audio])
    cover_image = models.ImageField(upload_to='music_image/')

    def save(self, *args, **kwargs):
        if not self.time_length:
            # logic forgetting the music length
            audio_length = get_audio_length(self.audio_file)
            self.time_length = audio_length
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Album(models.Model):
    name = models.CharField(max_length=300)


    def __str__(self):
        return self.name



