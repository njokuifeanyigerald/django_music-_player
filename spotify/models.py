from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True, blank=True)
    time_length = models.DecimalField(blank=True, max_digits=6, decimal_places=2)
    audio_file = models.FileField(upload_to='musics')
    cover_image = models.ImageField(upload_to='music_image/')

    def save(self, *args, **kwargs):
        if not self.time_length:
            # logic forgetting the music length
            pass
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Album(models.Model):
    name = models.CharField(max_length=300)



