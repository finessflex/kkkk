from django import forms
from .models import Genre, Track

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name_ru', 'name_en', 'description']


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'duration', 'genres', 'audio_file']
