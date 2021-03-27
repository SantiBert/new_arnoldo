from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Season, Episodies, Links


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
        fields = ['name', 'description', 'image', 'ordering', 'season']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),

        }
        labels = {
            'name': '', 'description': '', 'image': 'Imagen de referencia', 'ordering': '', 'season': ''
        }


class LinkForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['enlase', 'episodie', 'spanish']
