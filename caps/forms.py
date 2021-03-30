from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Season, Episodies


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['name', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
        }
        labels = {
            'name': '', 'description': '', 'image': 'Imagen de referencia'
        }


class EpisodieForm(forms.ModelForm):
    class Meta:
        model = Episodies
        fields = ['name', 'description', 'image', 'ordering',
                  'season', 'link1', 'link2', 'english', 'spoty']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'link1': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link en español'}),
            'link2': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link en español 2'}),
            'english': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link en inglés '}),
            'spoty': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link de Spotify'}),
            'mediafire': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link de Mediafire'})
        }
        labels = {
            'name': '', 'description': '', 'image': 'Imagen de referencia', 'ordering': '', 'season': '', 'link1': 'Link en español', 'link2': 'Link en español 2', 'english': 'Link en inglés ', 'spoty': 'Link de Spotify', 'mediafire': 'Link de descarga a mediafire'
        }
