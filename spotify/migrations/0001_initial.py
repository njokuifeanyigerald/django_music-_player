# Generated by Django 4.0.3 on 2022-04-27 15:59

from django.db import migrations, models
import spotify.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('artist', models.CharField(max_length=300)),
                ('album', models.CharField(blank=True, max_length=300, null=True)),
                ('time_length', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('audio_file', models.FileField(upload_to='musics', validators=[spotify.validators.validate_audio])),
                ('cover_image', models.ImageField(upload_to='music_image/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
