from distutils.command.build_scripts import first_line_re
from email.mime import audio
import imp
import os
from django.core.exceptions import ValidationError

from mutagen.mp3 import MP3

def validate_audio(file):
    try:
        audio = MP3(file)
        if not audio:
            raise TypeError()
        first_file_check = True
        # return first_file_check
    except Exception as error:
        first_file_check = False
    if not first_file_check:
        raise ValidationError('unsupported audio Type')
    valid_file_extension = ['.mp3']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extension:
        raise ValidationError('unsupported Audio type')
